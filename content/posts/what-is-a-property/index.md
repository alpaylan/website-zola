+++
title = "What is a property?"
date = "2026-04-05"
[taxonomies]
tags = ['testing']
language = ["en"]
+++

When talking about Property-Based Testing, we typically talk in very abstract terms.
There are properties, which define the correctness; there are generators, which define
the domain; the PBT framework gives us APIs for writing property-based tests that
combine the properties with the generators to find bugs. It's all very nice and simple.

A (surprisingly) large chunk of my time goes into exploring different PBT frameworks,
many times porting an existing PBT workload to use a new one instead of the other. This
requires me to build abstractions on what a PBT framework is, which should have been
very easy if the simple definition I gave in the first paragraph captured what PBT is.
Unfortunately it doesn't, so let's see what the issue is. A property is a universally
quantified computation that must hold for all possible inputs. The simplest model of a
property in a programming language is a function that returns a boolean, such as the one
below:

```haskell
property :: a -> Bool
```

For instance, `\l -> reverse (reverse l) == l` is a property, it asserts double
reversion leads to the original list. This gets slightly complicated with
_preconditions_, which are rules that state if an input is valid or not. So we can write
things like:

```haskell
data Database = ...

execute :: Database -> Query -> Database
query :: Database -> Query -> [[Value]]

(==>) :: Bool -> Bool -> Maybe Bool
(==>) precondition property =
    if precondition then Just property else Nothing

prop_insert_select :: Database -> String -> [Value] -> Maybe Bool
prop_insert_select db table values =
    let insert = Insert table values
        select = Select table "*"
    in
        hasTable db table ==> (values `elem` query (execute db insert) select)
```

Where `==>` is the implication operator, which states that if the precondition (the
left-hand side) is not satisfied, then the property cannot be tested. In our case, the
precondition is `hasTable db table`, which checks if the database has the specified
table. If it doesn't, then we don't care about the result, we just discard it. If the
database has the table, then we execute the insert and check if the select query returns
the values we inserted.

Now that we have a property at hand, we need some random generators for it. We can write
`Arbitrary` instances for all the input types and let QuickCheck handle the rest.

```haskell
data Value = Number Int | String String | ...

instance Arbitrary Value where
    arbitrary = oneof [Number <$> arbitrary, String <$> arbitrary, ...]

instance Arbitrary Database where
    arbitrary = ...
```

Well, not really. When we write these instances, what do you think QuickCheck does? It
generates a random database, a random string, a list of random `Value`s, and then runs
the `prop_insert_select` function. In what percent of cases do you think a random string
is a valid table name that exists in the database?

What we want is a dependent generator, where some values can depend on the others:

```haskell
-- Randomly generate a table
genTable :: Gen Table
genTable = ...

tableName :: Table -> String
tableName = ...

genValuesFor :: Database -> String -> Gen [Value]
genValuesFor db table = ...

gen :: Gen (Database, String, [Value])
gen = do
    -- Decide how many tables we want to create
    numTables <- choose (1, 10)
    -- Randomly generate the tables
    tables <- vectorOf numTables genTable
    -- Create an empty database
    let db0 = emptyDatabase
    -- Populate the database with the generated tables
    let db = foldl createTable db0 tables
    -- Now we can generate a valid table name and values
    let tableNames = map tableName tables
    table <- elements tableNames
    values <- genValuesFor db table
    return (db, table, values)
```

Now we don't need to worry about the precondition failure because the inputs are valid
by construction. The table is selected from the already existing list of tables in the
database, so it will never fail. How do we run the tests? Here's a conceptual API for
it:

```haskell
quickCheck :: Gen t -> (t -> Maybe Bool) -> Int -> Gen (Maybe t)
quickCheck gen property n =
    if n == 0 then pure Nothing
    else do
        -- Generate a random input using the provided generator
        input <- gen
        -- Check the property with the generated input
        case property input of
            -- Test passed, generate another input
            Just True -> quickCheck gen property (n - 1)
            -- Test failed, return the failing input
            Just False -> pure (Just input)
            -- Precondition not satisfied, generate another input
            Nothing -> quickCheck gen property (n - 1)
```

This is **not** how QuickCheck actually works (for instance, it ignores shrinking and
the actual test runner machinery), but the details of that are probably left best to
another post, because I want to focus on something different. The fact that the
generator is _not_ independent from the property. To be fair, that is a common
requirement, you cannot just randomly sample data in the hopes of running into
interesting inputs, you need to be aware of the system under test. But we have a more
pressing situation here, the generator runs computations that are seemingly not related
to the random generation itself. The `foldl createTable ...` call runs with the database
to add the generated tables to it. This is in contrast to our usual mental model of a
random generator which makes some random decisions to construct some datatype.

Instead here, the `Database` is too complex to generate from scratch, so we generate a
really simple version and use its own API for constructing it. While we're at it, we
could go even further. The generator already returns the `(db, table)` pair, which then
the property checks if `hasTable db table` to detect validity. We know that for this
specific generator, the `db` always has the `table`, so we can just remove it. For other
generators, we could just add it as a check within the generator and make the generator
partial instead of total, make the property total instead of partial. In the example
below, the generator returns `Gen (Maybe ...)` instead of plain `Gen`, and the property
returns `Bool` instead of `Maybe Bool` because the `hasTable` check has moved into the
generator.

```haskell
gen :: Gen (Maybe (Database, String, [Value]))
gen = do
    db <- arbitrary :: Gen Database
    table <- arbitrary :: Gen String
    if hasTable db table then do
        values <- arbitrary :: Gen [Value]
        return $ Just (db, table, values)
    else
        return Nothing

prop_insert_select :: (Database, String, [Value]) -> Bool
prop_insert_select (db, table, values) =
    let insert = Insert table values
        select = Select table "*"
    in
        values `elem` query (execute db insert) select
```

If we can move some part of the property into the generator, can't we do that with the
rest?

```haskell
gen :: Gen (Maybe Bool)
gen = do
    db <- arbitrary :: Gen Database
    table <- arbitrary :: Gen String
    if hasTable db table then do
        values <- arbitrary :: Gen [Value]
        let insert = Insert table values
            select = Select table "*"
        in
            return $ Just (values `elem` query (execute db insert) select)
    else
        return Nothing
```

Voila, we're now back to the original property-only version of the code, only now we're
in the generator land, so we can actually change the generation inline without
separating it into two parts and rewriting something from scratch. QuickCheck already
has support for this style of property-based test writing without making you write your
property under `Gen`:

```haskell
prop_insert_select :: Property
prop_insert_select =
    forAll arbitrary $ \db ->
    forAll arbitrary $ \table ->
    hasTable db table ==>
    forAll arbitrary $ \values ->
        let insert = Insert table values
            select = Select table "*"
        in
            values `elem` query (execute db insert) select
```

In this style, every `forAll` combinator takes a generator and produces a context with
access to the generated value, which while hiding the fact that you're working with
generators, allow you to write dependent generators without hassle. Here, the property
is not a function that returns a boolean, it's the test that captures the generation as
well as the assertion. To be fair, nothing I wrote here is revolutionary, `forAll` has
been a part of QuickCheck for the past 26 years, every person writing PBTs is aware of
the fact that property-based tests aren't properties and generators completely separated
from each other, but rather a combination of the two. The
[Hypothesis intro](https://hypothesis.readthedocs.io/en/latest/) puts it especially well
from a practical perspective:

> you write tests which should pass for all inputs in whatever range you describe, and
> let Hypothesis randomly choose which of those inputs to check

Essentially, Property-Based Tests leverage properties as universally quantified
statements about the program under test, but many times, they cannot use them without
breaking the abstraction boundaries. Thinking about this is especially important as we
implement libraries, for instance, the Rust port of Haskell's QuickCheck,
[quickcheck](https://github.com/BurntSushi/quickcheck) gets the abstraction boundary
wrong.

Its `quicktest` expects a `Testable` instance, which has a function
`fn result(&self, _: &mut Gen) -> TestResult`. This instance is implemented for tuples
of up to 8 elements as follows:

```rust
impl<T: Testable,
     $($name: Arbitrary + Debug),*> Testable for fn($($name),*) -> T {
    #[allow(non_snake_case)]
    fn result(&self, g: &mut Gen) -> TestResult {
        let self_ = *self;
        let a: ($($name,)*) = Arbitrary::arbitrary(g);
        let ( $($name,)* ) = a.clone();
        let mut r = safe(move || {self_($($name),*)}).result(g);

        if r.is_failure() {
            let mut a = a.shrink();
            while let Some(t) = a.next() {
                let ($($name,)*) = t.clone();
                let mut r_new = safe(move || {self_($($name),*)}).result(g);
                if r_new.is_failure() {
                    {
                        let ($(ref $name,)*) : ($($name,)*) = t;
                        r_new.arguments = Some(debug_reprs(&[$($name),*]));
                    }

                    // The shrunk value *does* witness a failure, so remember
                    // it for now
                    r = r_new;

                    // ... and switch over to that value, i.e. try to shrink
                    // it further.
                    a = t.shrink()
                }
            }
        }

        r
    }
```

Where the line `let a: ($($name,)*) = Arbitrary::arbitrary(g);` calls the arbitrary for
the input tuple and passes it to the property that computes the result in
`let mut r = safe(move || {self_($($name),*)}).result(g);`. The design here assumes the
exact boundary we just said was inadequate because computations might need to be
interleaved with the generation. Proptest, as far as I can tell, makes the same
decision. The
[comparison against QuickCheck](https://altsysrq.github.io/proptest-book/proptest/vs-quickcheck.html)
mentions differences that I personally do not find that much impactful, while not
mentioning the capability that this blog post focuses on. The newly introduced
[Hegel](https://github.com/hegeldev/hegel-rust) keeps the `tc: TestCase` argument that
allows for mixing generation with the test case that allows the original functionality
in Haskell via a different mechanism that Hypothesis has been using for some time.

The article wasn't really meant to lead to a particular result, but rather to explore
what we need expressible in a PBT library in general. I hope it's been fun to read and
insightful, if you have any objections, I would love to discuss them over at
[akeles@umd.edu](mailto:akeles@umd.edu).

My related work on the topic:

- {{ newtab(href="https://arxiv.org/abs/2602.18545", label="Programmable Property-Based Testing") }}
- {{ newtab(href="https://alperenkeles.com/documents/dirt.pdf", label="Database-Integrated Random Testing") }}
