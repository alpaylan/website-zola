+++
title = "Next Chapter!"
date = "2026-07-01"
[taxonomies]
tags = ["life, testing, ai"]
language = ["en"]
[extra]
draft = true
+++

Yesterday, I've defended my 5 year, 5 chapter Ph.D. thesis. Today, I write about what's
next, a spiritual 6th chapter!

My dissertation, titled "Designing Effective Property-Based Testing Frameworks",
comprises of the results of four research papers and projects I've worked on during my
Ph.D. Two of these papers are about PBT libraries I have worked on, and two are about
PBT libraries I have measured. In the next chapter, I would like to not just develop
testing tools, but also leverage them, build applications upon them beyond bug finding.

## Tests are experiments

If we want to go beyond using random testing for bug finding, we must start with
changing our view of what a test is. The common way to view a test is a specification;
we write a test, we write a program (in different orders depending on how much you like
TDD), and the program must adhere to the specified behavior. This is however, isn't
really complete. For instance in
[expect testing](https://blog.janestreet.com/the-joy-of-expect-tests/), we define the
input, run the program, see the result, and finally decide if the behavior is what we
expect it is to be. One could perhaps argue this is once again specifying a program,
which is true, but it is something more; it is defining the behavior of the program via
measuring its current behavior, and deciding if that is the correct behavior or not.

As such, each program execution is a singular point in the large space of possible
inputs to the program. Once we have an input, we can observe the execution to decide how
long it takes, what path in the program it follows, what instructions it executes, what
side effects it produces, and what results it returns. The purpose of a random testing
campaign is to maximize the information we can extract from this program, traditionally
in order to discover bugs that invalidate expectations of the programmer.

Random testing tools both _randomize_, to extract information from all possible parts of
the input space, and _systematize_, to tame the infinite space of possible inputs
produced by the randomization. For instance, uniform sampling of lists of elements is
practically impossible, because the mean length of a uniformly sampled list would also
be infinite, so we bias randomness in ways that are empirically useful.

Random testing tools are also _learners_. It is undeniable that a fuzzer "learns" the
validity conditions of the underlying system, how else would we explain its ability to
[pull JPEGs out of thin air](https://lcamtuf.blogspot.com/2014/11/pulling-jpegs-out-of-thin-air.html)
only through random mutations, starting from a completely benign string of 'hello'. This
is possible because the fuzzer is maximizing branch coverage via a genetic algorithm
that reuses existing seeds when they are "interesting", so each step towards a more
valid JPEG is recorded as progress; that is why once the JPEG validness is satisfied,
the fuzzer then goes on to creating interesting JPEGs.

If fuzzing is learning, can we use random tests for other types of _learning_ too?
Apparently yes! I was very excited to see
[CWM (Code World Models)](https://ai.meta.com/research/publications/cwm-an-open-weights-llm-for-research-on-code-generation-with-world-models/)
last year, a paper out of Meta FAIR using fuzzing to obtain input-output pairs and the
accompanying program traces for training a model that can reason about program behavior.

I believe we are still scratching the surface here. Programs have an endless amount of
interesting properties: termination, information flow, performance, memory allocation,
security... that we could observe program executions for learning the underlying
semantics and representations, and use them for _something_. The big question is, what
is **something**?

The obvious answer is bug finding. We could look for termination bugs, discover unwanted
flows of information, detect performance regressions, unwanted allocations...
Researchers have done all of these and much more. I think perhaps we can go forward; we
can start building software with random instead of well, testing it.

## Elephant in the room

There's an obviously novel element to the discussion that did not exist 5 years ago, the
introduction of LLMs into software engineering processes. We are now in possession of
neural program synthesis engines that can turn arbitrary natural language instructions
into programs. These are very powerful tools, and they can produce immense leverage from
the gap between the specification and implementation of a program. This gap can be
**huge**, such as the simple instruction to translate a million line software
_faithfully_ to another language. What follows can be separated into two conceptual
phases, although the implementation can be arbitrarily complex and interleaving. The
first phase is the autoformalization of this request, i.e. building a sort of acceptance
criteria for the result; this could be simply checking if the result typechecks or fully
fledged differential testing. The second phase is akin to a search process over the
acceptable criteria, finding a solution that can pass the formalized acceptance criteria
for the request.

At the limit, I view this as smart finite monkeys problem; a proud coercion of the
classic combinatorial infinite monkeys theorem where given enough time and randomness,
you will produce a string conforming to any predefined acceptance criteria. The smarter
the search process, the shorter the time, the cheaper the cost.

## "When a measure becomes a target, it ceases to be a good measure"

The cautionary tale of the
[deadly cobras in Delhi](https://en.wikipedia.org/wiki/Perverse_incentive) tells us we
might not be able to eat our cake and have it. Again and again, from health to economics
to reinforcement learning, we have learned that simply setting a reward to reach a goal
does not let you reach that goal. You need a much more abstract notion, "alignment", to
go towards the goal. For instance, when translating a software from Go to Rust, we could
in theory build an Go to Rust transpiler, run it, and we'll have _a_ Rust version of our
program, probably not _the_ Rust version that we wanted. The hidden criteria is that we
want the code to be readable, idiomatic; we want it to be somewhat human, which is very
hard to codify in our acceptance criteria, alignment is necessary.

However, alignment is necessary, but not sufficient. Today's models are fairly aligned
to not be literal evil genies; they can follow verbal guidelines quite well. There are
two other problems we need to think about: The first is underspecification, a great
danger of unrestricted autoformalization of natural language is that the gap between the
informal and formal specification can be gigantic. The second is incompetence; in my
writings I typically write "as-if" the models are perfect instruction followers, however
anyone who's used one knows they are not. A combination of alignment mismatch and
incompetence exaggerates the underspecification problem; the inferred additional
constraints can be unaligned or misformalized.

We have already seen these problems play out in practice, Anthropic's C compiler failing
to compile Hello World with a specific configuration while being able to compile the
whole Linux kernel; Rust version of Bun failing to pass basic MIRI checks; Cursor's
browser experiment failing to compile... Underspecification and misformalization is a
major, long tail problem.

## "Quantity has a quality all its own"

(Sorry to quote Stalin) It's important to note the primary discussion here. There was a
time, perhaps 2 years ago, the narrative was that an unstoppable force of economic
disruption was on its way to replace software engineers. The narrative today has shifted
into one that centers verification. You might hear "What you can verify, you can
automate", or "the bottleneck is the code review" pretty frequently.

There's a consistent, and in my view successful, effort in solving many of these
problems by building good user interfaces and tools for AI-assisted development,
augmenting people instead of trying to automate them, that will be, or perhaps already
is, transformational to our profession. Underspecification, for instance, can even be
fought against via `/grill-me`, a technique of getting the model to ask you questions
about potential aspects of design instead of inferring them.

The question I find more interesting is this; what are parts of software engineering
that could qualitatively change with a quantitative change in attention boosted by the
machines? I'm sure in time we'll come up with many more of these instance; but one that
catches my attention at the moment is _performance_.

## Performance engineering at scale

A particular meta-property of software is; all else equal, we would prefer it to be
faster (almost always, barring security). Faster software is cheaper to run on hardware,
but even more importantly, time to run a piece of code actually changes how much we can
run it. Think of the contemporary type checkers, running every second as we type. If
they were 10x more expensive to run, we would start running them at every compilation,
just as people did 15 years ago. The speed at which we run software qualitatively
affects the user interface we build around it.

Well, could we just tell a model _make faster_ and watch the software get better.
Apparently yes, the latest boom with "loops" allow people to just give the agent a vague
goal, let it autoformalize and run incrementally towards a given target. This sounds
good, until you realize you cannot remove the human from the loop. There is no guarantee
that the model-authored performance measurement is sound; there is no guarantee that the
behavior did not change; there is not guarantee that the improvement is actually
reflected in production traffic.

The lack of these guarantees mean you did not actually remove the human from the loop,
code review, especially the review of the acceptance criteria, is still the bottleneck.
Ideally, we can build primitives for building these measurement criterias; instead of
letting the model author the target, we can separate the judge from the proposer; build
fully autonomous optimization pipelines that do not require review.

Wait a second, we already have these things; they are called compiler optimizations! A
compiler optimization takes a piece of code and produces a semantically equivalent but
optimized version. A JIT compiler goes further; it compiles code based on online
measurements of the existing inputs. These existing "optimization passes" are separately
verified **for all possible programs**, we prove that they do not break the semantics of
the code before incorporating them in our compilers. The corollary is; we cannot use any
pass that we do not have the ability to verify. If a compiler pass has 50% change of
breaking the semantics of a piece of code, I highly doubt Clang is going to accept it.

But, if we had a verifier that could tell us if a pass is valid **for the given
program**, then we could use that. The practicality of such a method would of course
depend on how costly the construction of the pass is, how much performance improvement
it brings, and more importantly the soundness of the verifier that reports if the
semantics are preserved, and if the program is optimized.

## Building an optimization verifier

Is it even possible to build such a sound verifier? I believe it is. And the starting
point is tracing. A few months ago; I fixed a small bug in Ty, a new Python typechecker.
The CI ran my bugfix across PyPi to detect any behavioral changes in their index and
report it to me. Of course, my PR changed the semantics because it fixed them. But a
mere performance optimization should have simply kept it constant. _If_ we have access
to all possible production data (that is small enough to enumerate), then we can have
our verifier.

That is of course not really possible for any practical software. The first thing is,
even if programs are simple, the software is not; and programs are not really simple.
The complexity arises from the sheer amount of discrete behaviors encoded by each
program; the programmer's model of what a program does is necessarily incomplete,
evidenced by even seemingly simple programs such as `std::midpoint` that computes the
midpoint of two numbers (hint: `a+b/2` may not actually work). Even so, having a
significant amount of production traffic to test the optimization is a very solid ground
to stand on.

Ideally, we would simply "prove" the equivalence of the programs, or even perhaps the
optimization against a formal cost model, to increase reliability of such a pipeline.
Practically, however, at least today, we are yet to reach any indication of this
reality. This is because very few languages have formalized semantics that allow us to
do such proofs; and there are no guarantees that automated proofs of equivalence is
possible within those formalizations.

Instead, good old random testing is here to help us. Fuzzing has historically been a
tool for finding edge cases in programs to discover the cognitive limits of the
programmer that lead to bugs. Many of these bugs were crashes in the program, but
researchers have looked into performance bugs as well. A fuzzer, fully autonomously, can
discover edge cases that take disproportionately longer time for a human to discover.
Equivalence testing, or differential testing, has already been used to build software.
Amazon researchers have written Cedar, a permission engine they built, in Lean, proving
many properties about the language from first principles. Then they built a Rust version
for production use; using random testing to bridge the gap between the two versions and
prove (to them informally, not formally) that the implementations are equivalent.

We can use random testing in conjunction with tracing, maybe random testing augmented by
tracing, to prove such equivalences. We can also use random testing to discover worst
case bounds to detect performance regressions from the hypothetically optimized code
according to benchmarks constructed from the traces.

## Software optimization as buoyancy compensation

We can go further in our optimizations by, similar to how balloons drop _ballast_ to
increase its height by reducing its weight. Many programs we write today have
unnecessary loads that we could shed, let me elaborate. It is possible to write the same
exact program in Python and Rust, getting exactly the same outputs in both cases, one
100 times slower than the other. This isn't because the people developing Python don't
know what makes software fast, this is because Python, as a programming language, has a
very different interface than Rust, and that interface requires Python to carry around
much more data than Rust does, and Python allows you to create objects that would be
impossible (or rather _very_ impractical) to write in Rust. So, if we were to naively
translate _any_ Python code to Rust, it is more than likely that we would have many
programs that are slower, because we are doing the same work, but we do not have the
benefit of the engineering Python's developers have been doing. Of course, this is very
different from being able to translate some software which does not require those Python
features or cases where patterns in Python have straightforward but more efficient
alternatives in Rust.

The proposal here is not just translating software from one language to another; it's
more so that using random testing to discover scenarios where the software is
underspecified, a dynamic analysis of understanding which parts of the input space of
the program that are supposedly safe lead to panics or runtime failures, and propagate
that information back to the program to statically define the constraints. Equipped with
these constraints, we can actually benefit from program translation because now we do
not have to carry out bloated Python objects in the translation, but rather objects that
the program can actually use at some point. This is something JIT compilers essentially
do while the program is running, I think we can use random testing to do it as a
pre-compilation optimization pass.

## Where is this next chapter?

I hope to work on the types of projects I mentioned, among many others, as I start at
Datadog as a research scientist in 2 months! I find random testing to be immensely
valuable for discovering edge cases and bounds of a system, but I view understanding the
production traffic as crucial for any type of guaranteed and sound automation; and
Datadog is _the_ place for working with production traffic. I believe the team is still
hiring, so if working on these types of projects seem exciting to you, please reach out
to Sesh Nalla.

## Related articles

Last, but not least, almost none of the ideas I mention here are new, they are a
combination of ideas from my old writings, I'm leaving those here in case you would be
interested to read.

### On AI in software engineering

- [Verifiability is the Limit](@/posts/verifiability-is-the-limit/index.md) — a theory
  of how we can never get rid of verification entirely, we can only push it up to a
  different layer.
- [Breaking Verifiable Abstractions](@/posts/verifiable-abstractions/index.md) — where
  autonomous AI can win, and how abstractions only ever preserve the properties we
  measure.
- [Verification is Not the Silver Bullet](@/posts/verification-is-not-the-silver-bullet/index.md)
  — why computational verification alone is insufficient, and what more we need.
- [LLMs could be, but shouldn't be compilers](@/posts/llms-could-be-but-shouldnt-be-compilers/index.md)
  — the specification gap and the dangers of using LLMs as compilers.
- [Specifiability is the Leverage](@/posts/specifiability-is-the-leverage/index.md) —
  specifiability, not raw capability, is the real lever of AI-assisted programming.
- [Representation-Free Editing](@/posts/representation-free-editing/index.md) —
  representation, lossiness, and the roundtrips that make backpropagation possible.
- [The Mechanics of Autonomous Software Translation](@/posts/autonomous-translations/index.md)
  — the autoformalization-and-search machinery behind the 2026 wave of autonomous
  translations.
- [From Hand-Tuned Go to Self-Optimizing Code: Building BitsEvolve](@/posts/self-optimizing-system/index.md)
  — turning expert performance optimizations into an agentic self-optimizing system, the
  backdrop to the performance-engineering section above.
- [Closing the verification loop: Harness-First Agents](@/posts/harness-first-agents/index.md)
  — observability-driven harnesses for building trustworthy software with agents.

### On testing

- [A Better Vocabulary for Testing](@/posts/vocab-for-testing/index.md) — an
  alternative.
- [Test, don't (just) verify](@/posts/test-dont-verify/index.md) — why testing still
  matters as AI pushes formal verification into the mainstream.
- [Time Budget as a Software Constraint](@/posts/budget/index.md) — how performance
  budgets shape testing strategy, from PBT's milliseconds to fuzzing's hours.
