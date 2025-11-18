+++
title = "Verification is Not the Silver Bullet"
date = "2025-11-18"
[taxonomies]
tags = ['software engineering', 'ai']
language = ["en"]
+++

This post is a sequel to my thoughts on "What are the limits of LLMs" ([Verifiability is the Limit](/posts/verifiability-is-the-limit)) and "What are the domains I believe LLMs will shine at autonomously" ([Breaking Verifiable Abstractions](/posts/verifiable-abstractions)). As I see verifiability as part of the mainstream discussions more and more, I decided to break down on the limits of verifiability, focusing on how verification as a general principle isn't sufficient, and what more do we need.

In my original post, I posed verification as a human endeavour, as opposed to the mainstream usage of the term that usually means
computational verification. Computational verification is a procedural activity, it is the act of asserting facts about programs
by stating the facts in the form of tests that can be run, or factual statements that can be mechanically checked. Humans use
computational verification as part of their workflows, but they typically go beyond, because the facts checked by the machine are
subjective to the human verifier. If you would think about contesting this statement, think about any system you previously worked on,
would two people come up with the same exact tests for the same system in any of those cases? Unfortunately for us, correctness
is ultimately subjective, so we must be bothered with defining it.

This reveals a crucial limitation of the autoformalization approaches like Harmonic AI's Aristotle, Math Inc's Gauss, and a number
of similar efforts throughout the industry. The fact that you have perfect prover does not mean you have perfectly good theorems
about your systems. The fact that you have perfectly good theorems also doesn't mean your autoformalization procedure, which takes
your perfectly good theorems expressed in natural language, will translate them by preserving their semantics. At any point
where the semantics of your specification is not precise, the systems need to "guess" your intent, which is prone to failures
on both sides, you might have ill-defined, or the system might have ill-guessed the specification. This is exactly the point I
touch in [Breaking Verifiable Abstractions](../verifiable-abstractions/index.md), we can go above a traditional programming
language but still have precise semantics, or we can break the traditional flows of compilation by leveraging the perfect verifiers
without relying on imprecise specifications.

Nothing I wrote so far has been in contrast to anything I wrote prior to this, so let's get to the new rather interesting bit I've
been thinking about. There's an opinion that gets more mainstream by the day, the more verifiable a task is, the better the models
will get at it, we see this fact in games, mathematics, programming. When taken to the limit, this statement implies that any perfectly
verifiable task should be completely solvable my the models. The point of this post is to falsify this implication, and put a framework
for the limits of verifiability, what are the properties of verifiability of a domain that helps models get better in solving problems
in it?

The example I'll use is prime factorization, the mathematical definition is very straightforward.

```r
n = p_1 * p_2 * ... * p_k
```

Where `n` is a natural number, and `p_1, p_2, ..., p_k` are prime numbers. The solution to the problem is the list of prime numbers that
multiply to `n`. The verification of the solution is also very straightforward, you multiply the list of prime numbers, and check if the result is `n`. Prime factorization is one of the foundations of today's cryptographic systems as scientist haven't been able to find
any patterns for reducing the problem space into something that's essentially asymptotically better than brute force trials.

If we were to accept the original overly generalized statement that anything verifiable can be solved, we would reach to the conclusion
that one could train a model to the point it can automatically decide the prime factorization of any given number. A possible critique
of this position is that an LLM could indeed do that by learning to do arithmetic. There's nothing that prevents the model from learning
to perfectly divide numbers, do this in a loop that simulates the algorithm we currently run on the CPU. My response to the critique would
be that this isn't what we mean when we say that the model gets better at X. A model getting better at chess doesn't necessarily learn
Alpha-beta pruning, it learns patterns at higher levels than the low level mathematically descriptive operations we traditionally have.

So we differentiated chess from prime factorization using "something", which we haven't really defined. What I would like to propose here
is "progress" as an augmentation to "Verifiability is the Limit", I would like to revise myself to say "Verifiable Progress is the Limit".
The problem with prime factorization is that there aren't "to the best of our knowledge" patterns to discover and exploit. There's no
information about "how wrong" the result is. In games and in programming, it is possible to compare two solutions to the same problem
and produce information based on their comparison; therefore repeated play produces more and more information by providing a compare
and contrast style of learning based on how different actions affect the outcomes.

What are the implications of this fact, if it is indeed a fact? The first is that it would mean you cannot target AI at an NP problem for 
repeatedly running a verifier on the problem and hoping that the model will become better in time, assuming that the model doesn't
capture new patterns that we previously haven't been able to uncover or realize. The second is that, building verifiers isn't sufficient,
because we now have a measure of how useful a verifier is for a model based on the amount of information it produces. We must discuss
what types of feedback can be incorporated in the result of the verifier, and how that affects the process of learning.

That was it! As I think more on this issue, it becomes harder to differentiate between sound claims and personal bias, so it is
entirely possible that I'm missing some crucial points of the discussion. If you find such missing links, please let me know
at [akeles@umd.edu](akeles@umd.edu), I would love to know about the deficiencies of these arguments.
