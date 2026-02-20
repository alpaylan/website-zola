+++
title = "Database Integrated Random Testing"
description = "Developing database integrated random testing tools"
weight = 2

[extra]
link_to = "/research/random_testing_databases"
+++

Database management systems are notoriously complex, and that complexity leads to bugs. The state-of-the-art for finding them is off-the-shelf random testing tools like SQLancer, which have been remarkably successful at finding logic bugs in *mature* databases -- PostgreSQL, MySQL, SQLite. But when applied to databases that are still *under active development*, these tools struggle. The input space of SQL is larger than what the database actually implements, causing most generated tests to hit unimplemented features and register as false positives. For a database where many features are still missing, the signal-to-noise ratio becomes unworkable.

D4 is a paradigm for *database-integrated testing*: instead of running an external tool against the database, the testing framework is embedded directly within the DBMS itself. This lets the generators evolve alongside the database, avoiding false positives by construction. D4 provides developers with a domain-specific language for writing correctness properties, a stateful query generation algorithm, and a novel human-in-the-loop approach to counterexample minimization.

D4 was evaluated on [Turso](https://turso.tech), an actively developed SQLite-compatible OLTP engine. It found 23 unique, confirmed bugs -- with 19 of them already fixed -- significantly outperforming off-the-shelf alternatives in terms of true positive rate and usefulness of bug reports.

**Paper:** D4: Debugging Databases During Development (under submission) | [PDF](/documents/d4.pdf)

## The Core Problem

Traditional database testing tools like SQLancer are designed for mature, feature-complete databases. SQLancer generates random SQL queries, executes them, and checks the results against sophisticated correctness oracles (Pivoted Query Synthesis, Non-Optimizing Reference Engine Construction, Ternary Logic Partitioning, etc.). This works well when the database implements the full SQL dialect the tool generates.

But for a database under active development, the situation is different. Many SQL features are simply not implemented yet. When SQLancer generates a query using an unimplemented feature, the database returns an error, and the tool reports a false positive. Running SQLancer against Turso with its default SQLite3 integration (with pragmas disabled, since most were unimplemented) resulted in a false positive rate of over 96%. Even a custom SomeDB-specific SQLancer integration, developed by a contributor, still had a 58% false positive rate.

The fundamental issue is that an external tool cannot know which features the database supports at any given moment. D4 solves this by embedding the testing infrastructure within the database itself, so the generators naturally stay in sync with the implemented feature set.

## Generation Actions: A DSL for Correctness Properties

Rather than expecting database developers to modify SQLancer to suit their particular needs, D4 provides flexible abstractions so that they can test their database throughout its development. The central abstraction is a *generation action* (GA): an imperative formulation of properties that describes not just *what* to test, but *how* to generate the test.

For example, consider the commutativity of `AND`. For any database and any two predicates `p` and `q` that range over variables in the database, `SELECT (p AND q)` and `SELECT (q AND p)` should return equivalent results. As a generation action:

```
gen property db =
  t  <- pick db.tables
  c  <- pick t.columns
  v  <- genOf expression c.type

  p  := t.c = v
  q  <- gen expression (t, c)

  ! r1 := SELECT (p AND q)
  ! r2 := SELECT (q AND p)
  ! assert(r1 == r2)
```

The `<-` operator binds the result of a generation step, `:=` binds a regular let expression, and `!` marks interactions with the database -- queries or assertions. The generation action `pick`s from the current database state, meaning it can only reference tables and columns that actually exist. This is what prevents false positives by construction: the generated queries are always valid for the current state of the database.

D4 reimplements several SQLancer oracles as generation actions and also expresses properties that are not present in SQLancer. Here are a few examples:

**Non-Optimizing Reference Engine Construction (NoREC):**

```
gen property db:
  t <- pick db.tables
  r <- pick t.rows
  p <- gen expression (t, r)

  ! RS1 = SELECT * FROM t WHERE p
  ! RS2 = SELECT p FROM t
  ! assert(RS1.length() == RS2.count(1))
```

**Deleted rows should not be in the table:**

```
gen property db:
  t <- pick db.tables
  r <- pick t.rows
  p <- gen expression (t, r)

  ! DELETE * FROM t WHERE P
  ! RS = SELECT * FROM t WHERE p
  ! assert(r not in RS)
```

**The same table cannot be created twice (a regression property):**

```
gen property:
  t1  <- gen id
  c1  <- gen id
  ct1 <- gen columntype

  ! CREATE TABLE t1 (c1 ct1)]
  ! error := CREATE TABLE t1 (c1 ct1)]
  ! assert(error == "Parse error: Table {t1} already exists")
```

This last example illustrates that generation actions can express *microproperties*: targeted tests for specific regression scenarios that previously caused bugs.

## Shrinking Stateful Sequences

Counterexample minimization for databases is harder than for typical property-based testing. The "input" is a sequence of SQL statements, and the statements have complex dependencies between them: an `INSERT` affects later `SELECT` results, a `CREATE TABLE` must precede any reference to that table, and so on. Standard shrinking assumes independence between parts of the input, which breaks down in this stateful setting.

Consider this sequence:

```sql
(1) CREATE TABLE t0 (c0);
(2) CREATE TABLE t1 (c1);
(3) SELECT * FROM t1;
(4) INSERT INTO t0 VALUES (NULL);
```

If the bug is triggered by statement (4), a naive shrinker that tries removing (1) first will get a *different* failure (table `t0` does not exist), conclude (1) is needed, and produce the overly large counterexample (1)-(2)-(4) instead of the minimal (1)-(4).

D4 addresses this with *human-in-the-loop shrinking*. After automatic shrinking produces an initial minimized sequence, database developers can inspect the interaction plan, remove interactions they believe are irrelevant based on their domain knowledge, and feed the result back into the automatic shrinker. This iterative process consistently produces counterexamples that are both smaller than what automatic methods achieve alone and obtained faster than a human could manage unaided.

For example, for bug ID 924 (a crash in B-tree balancing), interactive shrinking reduced the counterexample from 1000 interactions to just 5. For bug ID 1975, automated shrinking reduced 1000 interactions to 40, and developers further reduced it to 12 via interactive shrinking.

## Bug Case Studies

D4 found 23 confirmed bugs in Turso over the course of its development, ranging from simple parser-level issues to severe logic bugs deep in the storage engine. A few notable cases:

**DELETE not emitting WHERE terms (Bug #1734).** The bytecode compiler had a bug where constant expressions in the `WHERE` clause of `DELETE` statements were not emitted, causing `DELETE FROM t WHERE 5-5` to incorrectly execute. D4's PQS implementation with validity-preserving queries between `INSERT` and `SELECT` statements caught this automatically.

**B-tree balancing self-reference (Bug #2106).** When the B-tree depth exceeded 2, interior node replacement during post-delete balancing caused a self-reference. D4 triggered this by gradually extending generation to include `DELETE`, `UPDATE`, database indexes, and larger tables -- naturally following the database's development trajectory.

**Database header initialization (Bug #1818).** SQLite uses write-ahead logs (WAL) for non-blocking reads, which means metadata like database size and schema can be out-of-date. D4 found this through fault injection in its generation actions: a `ReopenDatabase` primitive that closes and reopens connections, enabling detection of persistent state errors that would otherwise be invisible.