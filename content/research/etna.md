+++
title = "ETNA"
description = "An Evaluation Platform for Property-Based Testing"
weight = 4

[extra]
link_to = "/research/etna"
+++

Property-based testing (PBT) has an abundance of tools. Haskell alone has QuickCheck, SmallCheck, LeanCheck, and Hedgehog; Rocq has QuickChick with multiple generation strategies; OCaml offers QCheck, Crowbar, and Base_quickcheck. Each tool makes different design choices about how to generate test inputs, how to shrink counterexamples, and how to guide the search. But the literature is short on rigorous comparisons that help users and tool designers understand the tradeoffs between all these choices. How is a tool designer supposed to measure success? How can we turn PBT from an art to a science?

ETNA is a CLI tool and platform for empirical evaluation and comparison of PBT techniques. It is designed to answer questions like: *Is a hand-written bespoke generator always better than a naive type-driven one? Do larger inputs always find more bugs? How sensitive are enumerative frameworks to the order of their constructors?*

**Papers:**
- [ETNA: An Evaluation Platform for Property-Based Testing (ICFP 2023)](https://doi.org/10.1145/3607860) | [PDF](/documents/etna.pdf)
- ETNA: An Evaluation Platform for Property-Based Testing (JFP, extended version) | [PDF](/documents/etna-jfp.pdf)

## Installation and Quick Start

ETNA is distributed as a Rust CLI tool. You can install it with a single command:

```bash
curl --proto '=https' --tlsv1.2 -LsSf \
  https://github.com/alpaylan/etna-cli/releases/latest/download/etna-installer.sh | sh
```

A typical workflow looks like this:

```bash
# Initialize ETNA
etna setup

# Create a new experiment
etna experiment new my-experiment --local-store

# Add workloads for the languages and data structures you want to test
etna workload add Haskell BST --experiment my-experiment
etna workload add Racket BST --experiment my-experiment

# Run the experiment
etna experiment run --name my-experiment --tests bst-haskell
etna experiment run --name my-experiment --tests bst-racket

# Visualize and compare the results
etna experiment visualize --name my-experiment --figure bst --tests bst-haskell
```

Each experiment lives in its own directory and contains a `tests/` folder with JSON configuration files that specify which workloads, mutations, strategies, and properties to test. For example, a test file specifies tasks as combinations of a strategy and a property, run against a set of mutations with a given number of trials and a timeout:

```json
[
    {
        "language": "Haskell",
        "workload": "BST",
        "mutations": ["insert_1"],
        "trials": 10,
        "timeout": 60,
        "tasks": [
            { "strategy": "Correct", "property": "InsertPost" },
            { "strategy": "Correct", "property": "InsertModel" },
            { "strategy": "Correct", "property": "DeleteInsert" }
        ]
    }
]
```

## Platform Architecture

ETNA is built around four concepts:

- **Workloads** are collections of programs with injected bugs (mutants). Each workload includes data type definitions, function implementations, property specifications, and manually sourced mutants. ETNA ships with workloads for binary search trees, red-black trees, the simply-typed lambda calculus, System F, information flow control, and a Lua-based parser.

- **Frameworks** are PBT libraries: QuickCheck, SmallCheck, LeanCheck in Haskell; QuickChick in Rocq; QCheck, Crowbar, Base_quickcheck in OCaml; RackCheck in Racket; and quickcheck in Rust.

- **Strategies** describe how a framework generates test inputs. Examples include type-based random generation, manually written bespoke generators, specification-derived generators, and coverage-guided fuzzing.

- **Tasks** are mutant-property pairs. ETNA measures the effectiveness of a strategy by how quickly it can *solve* each task, that is, detect the injected bug across all trials within a timeout.

ETNA uses mutation testing rather than code coverage to evaluate generators. Code coverage is popular but problematic: higher coverage does not always translate to better bug finding. Mutation testing directly measures whether testing can detect known bugs, providing ground truth.

Mutants are embedded directly in the source code using a terse comment syntax. For example, a correct Haskell implementation of BST `insert` with an embedded mutant:

```haskell
insert k v E = T E k v E
insert k v (T l k' v' r)
    {-! -}
    | k < k' = T (insert k v l) k' v' r
    | k > k' = T l k' v' (insert k v r)
    | otherwise = T l k' v r
    {-!! insert_becomes_singleton -}
    {-!
    = T E k v E
    -}
```

The uncommented code is the correct implementation. The `insert_becomes_singleton` block defines a mutant that, when activated, replaces the body with a version that always creates a singleton tree. ETNA's `mutation` commands toggle between these variants.

## Current Coverage

| Language | Testing Tools                              | Workloads                            |
| :------- | :----------------------------------------- | :----------------------------------- |
| Haskell  | QuickCheck, LeanCheck, SmallCheck          | BST, RBT, STLC, System F<:, LuParser |
| Rocq     | QuickChick                                 | BST, RBT, STLC, IFC                  |
| Racket   | RackCheck                                  | BST, RBT, STLC, System F             |
| Rust     | QuickCheck (fork)                          | BST, RBT, STLC                       |
| OCaml    | QCheck, Base_quickcheck, Crowbar           | BST, RBT, STLC                       |

Adding a new language requires implementing an adapter that describes the directory structure, compilation commands, and result-capturing infrastructure. Adding a new framework or strategy to an existing language requires providing the standard combinators and connecting them to ETNA's JSON result schema. ETNA also supports cross-language experiments, enabling the first precise comparisons of PBT tool performance across languages.

## Key Findings

### Bespoke Generators Outperform Naive Ones Along Multiple Axes

Comparing strategies on Haskell workloads, the bespoke strategy (hand-crafted generators) solved all tasks while naive QuickCheck failed on 43. Among tasks both solved, bespoke generation was statistically significantly faster in 83 out of 124 tasks and required fewer valid inputs in 89 out of 124 tasks. The bespoke strategy found more bugs, more quickly, and with better quality tests.

Between the enumerative frameworks, LeanCheck substantially outperformed SmallCheck, achieving an 82% solve rate compared to SmallCheck's 35%, and producing over a hundred times more tests per second.

### Larger Inputs Can Hurt Bug-Finding

Conventional wisdom holds that larger inputs exercise more program behaviors. ETNA's size exploration experiment on BSTs challenged this assumption.

For properties whose inputs have dependencies between them, larger trees made bug-finding *worse*. Consider a mutant where the delete function fails unless the key happens to be the root. As the tree size increases, the probability of satisfying the necessary conditions decreases, so larger trees require exponentially more inputs to solve the task.

The takeaway: PBT users should not naively expect that larger inputs are better, especially for properties with multiple inputs. Frameworks should not treat property inputs as independent, and testers should think carefully about interactions between their property's inputs.

<style>
    .row {
        display: flex;
        gap: 16px;
        justify-content: space-between;
        flex-wrap: wrap;
    }

    .column {
        flex: 1;
        padding: 8px;
    }
</style>

<div class="row">
    <div class="column">
        {{ github(repo="alpaylan/etna-cli") }}
    </div>
    <div class="column">
        {{ github(repo="jwshii/etna") }}
    </div>
</div>

