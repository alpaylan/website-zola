+++
title = "Specifiability is the Leverage"
date = "2026-02-24"
[taxonomies]
tags = ['software engineering', 'ai']
language = ["en"]
+++

Almost a year ago, I wrote my first ever blog post on AI-assisted programming, [Verifiability is the Limit](https://alperenkeles.com/posts/verifiability-is-the-limit/).
The core idea was a push against the school of thought that AI-assisted programming would scale to an infinite productivity level, because someone had to verify
that the outputs conform to the given specification, the prompt. I predicted that this had, and would, give rise to uneven levels of productivity in different domains,
in UI development, it would make human-in-the-loop development much faster, because UIs are very easy to verify via looking, checking, inspecting the changes. If
we could construct a perfect oracle, a computational verifier that has the ability to reject or accept any artifact produced by the model, we could get autonomous
improvements comparable to those we got in games such as Chess or Go, which I've further explored in [Breaking Verifiable Abstractions](https://alperenkeles.com/posts/verifiable-abstractions/),
[Test, don't (just) verify](https://alperenkeles.com/posts/test-dont-verify/) and [The Mechanics of Autonomous Software Translation](https://alperenkeles.com/posts/autonomous-translations/).
This time, I've come back to reframe these ideas from a new lens, I don't know how useful these lenses are, perhaps both of them separate don't lend any
usefulness to anyone, but if they are of interest to you, here's the thesis.

**The gap between the specification and the task is the leverage.**

There's an important component here, which is that this new thesis isn't really that different from how verifiability is the limit. Rather it recognizes that the computational
perfect oracle is the specification. So, it gives us a tool to answer the question, how much productivity gain can we get from using an LLM, which is that the difference in
time to specify the task versus executing it. This is an upper limit to the productivity gain that we're far away from because these systems are far from perfect, they make mistakes,
and we also make mistakes on how we think about specifying systems, so we've a lot to improve on.

The rest of this post is talking about different domains, different ways to specify, how to gain leverage, how people have been gaining leverage, what are we still missing.

The simplest form of specification is a reference. Imagine you take a screenshot of a webpage, and you ask the model to keep generating code until it recreates it. You gain
immense leverage from this interaction, because you have left much of the specification of the details to your reference with a minimal requirement, the page must look the same.
There are, however, millions of different ways to fulfill this request. For instance, nothing prevents the model from literally making the page a canvas and putting the picture
there, objective achieved! That is probably not you want, you want a reasonable approximation of the screenshot in a usable manner. So something that looks like a button should
probably be a button, something that resembles a textbox should be a text area, etc. You also want reasonable behavior on scrolling, resizing, reloading... You see how this is
somehow damaging on the leverage, we started with a simple reference as the specification of what to generate, but we see that's not really enough, the specification is much
more nuanced in practice. This isn't really a groundbreaking discovery, we started from a static 2D reference image, which captures (maybe) a moment in the life of a webpage,
so the model has to infer, or guess, or ask, every decision beyond the reference.

This isn't really so bad, because models are not blind followers of instructions, they generalize them in the context of training data. So when we ask the model to generate
a webpage based on a screenshot, I am (99.99%) certain that it will not just print it on a canvas, it will infer that you want DOM elements organized in such a way that it
resembles the screenshot, and that's a very nice behavior we certainly want when using the models, because if we wanted to be *that* precise, we lose the leverage we get by using
a generative model of programming, at the limit without contextual inference, the specification can be equivalent to the implementation.

In practice, we are advantageous in two ways. The first is, lots of times people don't have very specific requests. A simple book club app might be fine the way the model infers
what it should be. The second is, we don't need have a precise specification in mind, we're using the model interactions as a way to iteratively refine the specification, as we would
when developing without model assistance. We can even use the model to help us with the refinement,
you can get the model to *quiz* you, ask you questions to refine the specification you gave, in order to produce software that is a better fit to your intent. You can, as is the typical
development workflow, check the output to refine the specification by correcting a piece of it.

You might've realized in the screenshot example that references themselves are not the specifications, they are anchors, targets to adhere to. We have to also specify the gadgets,
the tools, the platform to produce the artifact to conform to the reference, which would be a standalone HTML page or a React application in the screenshot instance. In other
instances we might specify using specific programming languages, testing strategies, implementation tricks, dependencies... The highest leverage, however, comes with the ability
to remove the human from the loop. If we could only produce a computational verifier that completely specifies our program, we could just let the model evolve the program in an
autonomous loop, I've outlined a rough economic function of the cost for such an autonomous
loop in my latest post, [The Mechanics of Autonomous Software Translation](https://alperenkeles.com/posts/autonomous-translations/):

> `total cost ≈ (inference cost per iteration) × (expected iterations until “good enough”) + (harness engineering + oversight)`

Here, the leverage is the effort we spend on `(harness engineering + oversight)` subtracted from the total engineering effort we would have spent if we didn't have the
computational verifier. What does the computational verifier looks like? It's a random testing loop! Produce random inputs, pass them in the new and the old implementation,
assert that their results are the same, or at least equivalent. We once again rely on the generalization capacities of the model here, trusting that it won't keep
adding new `if` statements for every single input it gets wrong until the testing loop is exhausted. Within this framework, we get increasingly higher leverage as models
get better and harnesses are better engineered, we should get increasingly better results in translation. The current demos with the [C Compiler](https://www.anthropic.com/engineering/building-c-compiler),
[the browser](https://cursor.com/blog/scaling-agents), [SimCity](https://x.com/ccccjjjjeeee/status/2021160492039811300), [Javascript Compiler](https://ladybird.org/posts/adopting-rust/),
or the recent news of [COBOL modernization](https://claude.com/blog/how-ai-helps-break-cost-barrier-cobol-modernization) are the footsteps of what's to come, they mark
what we can achieve with high leverage using these computational verifiers.

Well then, we get to the gist of the important question. **Where else do we have this type of leverage?**

The core idea of Property-Based Testing is, users write executable specifications using first order logic. Properties are universally quantified predicates that must hold true
for any given input, and they are implemented as predicate functions from such inputs to booleans, letting the testing harness decide on how the inputs are produced. For instance,
we can write and test the following properties in Python:

Program translation:

```python
def translation_preserves_semantics(python_program: PythonProgram, input: Input):
    translated_program = translate_to_rust(python_program)
    return execute_python(python_program, input) == execute_rust(translated_program, input)
```

Program optimization:

```python
def optimization_preserves_semantics(program: Program, input: Input):
    optimized_program = optimize(program)
    return execute(program, input) == execute(optimized_program, input)
```

Preservation of momentum in physics simulations:

```python
def momentum_preservation(mass1: float, velocity1: float, mass2: float, velocity2: float):
    initial_momentum = mass1 * velocity1 + mass2 * velocity2
    final_velocity1, final_velocity2 = simulate_collision(mass1, velocity1, mass2, velocity2)
    final_momentum = mass1 * final_velocity1 + mass2 * final_velocity2
    return initial_momentum == final_momentum
```

Serialization and deserialization consistency:

```python
def serialization_consistency(protobuf_message: ProtobufMessage):
    serialized = serialize(protobuf_message)
    deserialized = deserialize(serialized)
    return protobuf_message == deserialized
```

All of these examples denote universal truths. A program optimizer must not change the output of any program for any input. A physics simulation
must preserve the momentum for all possible physical worlds, a serialize/deserialize pair must not lose information for any type of message.
Once we have such universal expectations about the implementations, it is possible that we no longer need to worry about the implementation.
Write the specification, run sufficiently long random testing campaigns, keep feeding counterexamples back to the model until there are none.
That would be hell of a way to develop software, but unfortunately real life is messier.

**None of the examples I gave are complete.** Program optimization must not just preserve the semantics, it must also optimize the program.
We tested momentum preservation with only two rigid bodies, but the simulation might have more. We made sure serializing and deserializing
any protobuf message leads to the same message, but not that broken serialized messages could not be deserialized, or parsed, into
the wrong messsage. We checked that the translations are functionally equivalent, but not that of compatible in memory usage or runtime performance;
we also did not account for nondeterminism or concurrency that might not be well suited for random testing to test for. We have another
way to check specifications, namely formal verification, but I will just name drop a previous blog post of mine,
[Test, don't (just) verify](https://alperenkeles.com/posts/test-dont-verify/), if anyone is interested in how and when
LLM-assisted formal verification can and can't provide similar or even better leverage to random testing.

So are we back to the beginning? Do we not get any leverage from the random tests, of course not! We must merely be very careful. As we move away
from the implementation to the specification, we start to use the [LLM as some kind of compiler](https://alperenkeles.com/posts/llms-could-be-but-shouldnt-be-compilers/),
we relinquish control of every detail we choose not to specify, or not to test for. This means the model has free reign to do as it pleases as long
as the tests pass.

Universally quantified properties aren't the only way to specify software at scale. Temporal logic formulas as in TLA+, or the newly announced
[Bombadil](https://wickstrom.tech/2026-01-28-there-and-back-again-from-quickstrom-to-bombadil.html) allow users to specify behavior of a program
temporally, as formulas over time reasoning if a property always holds for a program, or that all paths in the program eventually lead to
some supposed destination such as a cleanup routine. These types of specifications are especially crucial in distributed settings because many
distributed algorithms as expressed as temporal logic formulas and proven in model checkers like TLA+. These formulas, unsurprisingly, have to be
combined with finer level details we expect from the implementations too, after all, many concepts in theoretical computing such as eventuality
have to be bounded by certain limits to be practical in real life settings.

Let's talk about what I see we're still missing.

For starters, we lack the expressivity in our specification languages to specify many useful aspects of the software. All of the harnesses people
use in [OpenEvolve](https://github.com/algorithmicsuperintelligence/openevolve) style systems are still programs, programs that are written as bespoke,
potentially buggy specifications for evolving code for some metric. We talk about faster software without talking about the distribution of inputs,
we talk about software security without talking about properly defining the threat model. We're also missing proper harnesses for autonomous
programming. There are a multitude of impressive products such as Codex, Claude Code, Cursor, Open Code for programming via prompting, they
take care of context management, tool calling, model selection, prompt caching, sandboxing, checkpointing and many other useful feature for AI-assisted programming,
but I don't know of any such polished product for building fully autonomous loops. Last but not least, we are missing the mindset to look for
the leverage. I don't see us identifying potential gaps to open up between the specification and the implementation and focusing on exploiting
those gaps. It's not that there aren't people working on these problems, I mentioned in my previous posts, BitsEvolve, ShinkaEvolve, ADRS, Glia,
Algotune, there are many people working on finding opportunities to produce autonomous tasks, but the leverage is still in the niche.

(I think this will be the last one of these posts, because I feel like I told all I wanted to say in this topic, wish me luck
on getting back to writing about testing databases and type systems!)
