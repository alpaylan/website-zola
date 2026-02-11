+++
title = "The Year of Autonomous Translations, and Where to Go From Here"
date = "2026-02-11"
[taxonomies]
tags = ['software engineering', 'ai', 'testing']
language = ["en"]
+++

2026 started with a boom of AI-assisted autonomous translations, on 14th of January,
Cursor published their post on [Scaling long-running autonomous coding](https://cursor.com/blog/scaling-agents)
in which they created translations of a browser, Java LSP, Windows emulator and Excel. This was
followed by an Anthropic post on [Building a C compiler with a team of parallel Claudes](https://www.anthropic.com/engineering/building-c-compiler), which has only further fan the flames of the hype. Both of these posts have garnered lots of positive
attention but have failed to stand to the expectations of the demos, Cursor browser got lots of well-deserved critique, and people had
their good laughs when the C compiler that could compile the Linux kernel failed on a Hello World example. I view both of these as
fundamentally broken PR attempts at translating production grade software products using a toy translation engine, and getting
broken toy results. It seems from a speculative point of view that the models are capable enough to do this translation, so my
position is that the translation harnesses themselves aren't good enough, or the total budget required is much higher. I'll go
into the economics of translation in the [translation as a function of money](#translation-as-a-function-of-money) section.

To make my position clear, I think we'll get better and better demos of these autonomous translations throughout 2026,
and maybe even have some decent autonomous translation products by the end of the year. This article starts with a technical
dive into how these translations even work in [How does AI translate software?](#how-does-ai-translate-software), followed
by my personal analysis of the question of "is translation capability really useful, and if yes, how so?" in
[How can we derive value out of translations?](#how-can-we-derive-value-out-of-translations). In [the next frontier](#the-next-frontier-optimization) I'll start making some more predictions,
and finish with a discussion of a world where ubiquitous translation of software is possible.

## How does AI translate software?

I should start this section with a disclaimer to its title, **AI does not translate software**. If AI translated software,
it would be like waving a magic wand, we would say "give me a Rust version of Doom", and voila, we would get one. What instead
happens right now is, people use LLMs as neural seach engines, *AI proposes translations*, which are then rejected
by a translation harness that is designed by a human, in these cases experts that understand the mistakes LLMs make,
and know how to create a robust testing loop with continuous improvements. This may change in the future where
the harnesses themselves good enough for translation are written by the models, which is I think the point where the terminology
should shift, not at this point in the history. The fundamental current change is that these translations are now economically
viable because of the model capabilities. I feel the need to say this because whenever one of these translations drop to the
timeline, the vendors hype it up to suggest this indicates a larger ability in the context of software engineering, which I
fully disagree.

As such, let's build a very dumb translation loop without LLMs:

```python
def translate(source_code):

    while True:
        # Randomly generate some strings
        target_code = "".join(random.choices(string.ascii_letters + string.digits, k=random.randint(1, 1000000)))

        equivalent = True
        for i in range(1000):
            # Randomly generate some bytes
            test_case = random.randbytes(random.randint(1, 1000000))
            if run(source_code, test_case) != run(target_code, test_case):
                equivalent = False
                break
        if equivalent:
            return target_code
```

There's a very cool mathematical theorem in combinatorics that is called the [infinite monkey theorem](https://en.wikipedia.org/wiki/Infinite_monkey_theorem), which states that a monkey hitting keys at random on a typewriter keyboard for an infinite amount of time will almost surely type any given text, such as the complete works of William Shakespeare. We don't really care about
Shakespeare's complete works right now, but we might care about translating an old COBOL software into Java without changing
its semantics, so it would be immensely useful if we had these infinite monkeys with some infinite time at hour hands to produce
modern Java equivalents of some old COBOL programs.

### Translation as a function of money

While we don't have infinite randomized labor coupled with infinite time, we have something that comes close to it, we have
AI models that can generate code that are astonishingly good at following instructions. These models unsurprisingly
cost a decent amount of money to run, but they make it so that we can now sample from a much better distribution of
possible translations than was previously possible. We can even guide this sampling by augmenting our instructions
with feedback from the testing harness, so the suggestions of the model is self-improving within this translation loop.
We can modularize the software into multiple units or modules, each of which is separately validated, which once
means we the model now doesn't even have to generate the whole thing, it can generate each smaller unit and compose
the whole thing together.

There's an economic balance here:

> `translation cost ≈ (cost per iteration) × (expected iterations until “good enough”) + (harness engineering + oversight)`

As models and harnesses get better, the expected number of iterations to reach equivalence do and will get lower,
and assuming that the cost to generation itself doens't increase too much, we should expect the cost of translation
to drop significantly, expecting to see many more of these results. There are two significant developments from the model
side here, one is that they are getting better at following specifications, the two is that they are getting better at
being in the control plane. In addition to doing the translations themselves, we can trust the model to make better
judgements within the harness such as invoking subagents to translate a logical module and producing a smaller random test for
it, essentially letting the model dicdate how much of the translation is successfully completed. I'm not aware of any current
demos that is doing this, but I would also expect this to happen.

### Verifying Translations

The loop we saw at the beginning of the section is a *differential test*, where two systems must be observable equivalent.
It's the most popular form of Property-Based Testing in software engineering, because it is the simplest property of software.
Traditionally it's used for validating ports across languages (translations), refactors, optimizations, and there's an even
interesting method of software development where when implementing a new system, you first build a *model*, a naive, simpler
version that defines the observable correct behavior of the system is, and use that to test your production grade system that
can be much more complex. Testing researchers have been using differential tests to find bugs in compilers, databases,
browsers and many other types of software for many years, and now differential testing is becoming mainstream thanks to
its ability to produce shiny demos for new AI models.

There's a larger technical debate here, which is what does it mean for a translation to be correct, because observable
equivalence is my definition is doing a heavy lifting. What do we observe to make it equivalent? Test cases! So the strength
of the test case generation directly affects the strength of the equivalence we can ensure. There are some important
ramifications of this, one is namely that our translations are laser focused on functional equivalence because that's the
easiest to test for, and fails to account for equivalence in performance, equivalence in security, equivalence in any scenario
we cannot test our systems for. For any sufficiently complex language, be it C, Rust, SQL or Brainfuck, it's impossible
to produce all possible inputs to the system, so we must do the next best thing and try to reach as many states of the
underlying system as possible. I suspect a large part of the bottleneck today is how we generate the test cases, how much
of the system we are able to test quickly enough, and how much information are we able to give back to the model as feedback
when there's an equivalence failure, how easy it is to localize failures, how much time is spent on tracing the root
cause of each failure, how much of the token budget are we spending that we could just solve with other, much faster techniques.

There is another large debate, which is that is this really useful? Let's say the model is able generate a browser from scratch,
a GCC equivalent, or rather it really just replicates any software with the same exact input output structure across language
ecosystems, how much value do we produce here? What good is it to produce translations across languages?

## How can we derive value out of translations?

The answer here isn't really obvious. Let's say we have a perfect translator from Javascript to Rust, and we give it
the following Javascript program:

```js
function add(a, b) {
    return a + b;
}
```

Here's a potential Rust translation of it:

```rust
fn add(a: i32, b: i32) -> i32 {
    a + b
}
```

Of course this is completely wrong, because we are translating a Javascript function, which can take any JS object, so the correct translation would be something like:

```rust
enum JsValue {
    Number(f64),
    String(String),
    Object(HashMap<String, JsValue>),
    // and so on for all JS types
}
fn add(a: JsValue, b: JsValue) -> JsValue {
    match (a, b) {
        (JsValue::Number(x), JsValue::Number(y)) => JsValue::Number(x + y),
        (JsValue::String(x), JsValue::String(y)) => JsValue::String(x + &y),
        (JsValue::Number(x), JsValue::String(y)) => if let Ok(y_num) = y.parse::<f64>() {
            JsValue::Number(x + y_num)
        } else {
            JsValue::String(x.to_string() + &y)
        },
        // handle other cases and type coercions
        _ => panic!("TypeError: Invalid types for addition"),
    }
}
```

There's immensely less value in this translation compared to the previous one, because staying true to the semantics without
any type of restriction on the existing types hardly produces readable, maintainable, or faster code. This is more true
for translation of libraries where input types are necessarily host language objects, so making a strictly equivalent translation
gives us very little wiggle room. On the other hand, if we are translating an application, we have much more freedom to change
the underlying types as long as the public interface, which is usually a simpler object model we can easily serialize and
deserialize, is preserved. Therefore, it is in my opinion more possible to make an application more readable, maintainable, or
faster via translation as opposed to libraries.

Another point we can derive value is platform dependence. For instance, on web, we could only run Javascript as a scripting
language for a while, although nowadays WASM is changing this, but if it had not, we could use translation to run arbitrary
languages on the web, as older symbolic translation methods such as ghcjs, emscripten had done. This type of platform
dependence also exists in other ecosystems such as smaller embedded devices, where we might want to run a Rust application
in a language that Rust compilation isn't yet possible; or moving out of a dying ecosystem such as COBOL, where it's very
hard to find developers, or the language doesn't evolve with modern hardware to take advantage, so moving to a modern language
with an active ecosystem can be a huge win.

## The next frontier, optimization

Translation has emerged as a powerful use case for LLMs due to its convenience in testability, so it's natural to
ask what's next? If we master translation, what would be the next emerging capability? I view optimization as a natural
next step after translation because (1) it already includes a valid translation as its requirement, so it isn't surprising
we haven't seen much advances on it without mastering translation first; (2) there are forms of optimization that are
as easily tested as translation even though optimization is much more nuanced.

The simplest form of optimization is a dominant one, where the new program is strictly better than the old one across all dimensions, for all possible inputs. This type of optimization is typically possible by doing less, meaning we remove
allocations, extra pointer chasing via indirections, push ifs up and loops down to make our programs do less work. Given a
program where it's possible to have such optimizations, we can once again treat the model as a neural search engine that proposes possibly optimized programs we can reject via benchmarks with little changes to the testing harness we had
for translations.

There are other forms of optimization that aren't necessarily dominant, these might be optimizing for specific types of
known input distributions or focusing on absolute wins where making a small input run on 2x is deemed less important
than making a very large input run on 0.9x time. I think for these types of optimizations it's harder to automate the harnesses
as it requires subjective judgement on the acceptable bounds on different input types and distributions.

## Can we copy behind closed windows?

A futuristic application going forward in this technology is not just translating open source applications we have unlimited
access to with the ability to run hundreds of millions of side by side equivalence tests, but rather reconstruct existing closed
source software, perhaps even behind servers we have limited access to. This would be possible by essentially building a mirror model of the state machine implemented by the server that is refined across time as assumptions of the mirror model is broken.
I wonder what this would do to the existing SaaS ecosystem, what does on choose to build when it's possible to build
autonomous copies of simpler architectures, how do businesses defend their competitive advantage...

## Future of programming languages

I wrote a bit earlier that translation between languages themselves isn't straightforward because faithful
translations can be hardly useful. There's a bit of intellectual dishonesty here, because such as translation
also gives us the ability to specify types of the software too. We can take programs that are initially
too liberal with their types and progressively cut down those overly permissive types into simpler forms,
just as how the V8 JIT compiler dynamically computes when Javascript function types can be pruned and simplified
based on existing input profiles. Our translation units also don't have to be aligned at functions, which might
again force us to use patterns that are at a disadvantage in one language but useful in the other, such as memory
management patterns in C that isn't expressible in safe Rust, but could have been avoided if we draw the translation
unit at a higher point in the code.

In an environment we are able to do such translations, what would we do? Which types of languages would become
more likely translation sources, which would become more likely translation targets? What kind of properties
of existing programming languages would shine in this ecosystem, which would become obsolete?

I would like to think that, in such a scenario, we would look for more declarative, but precisely specified
paradigms as opposed to natural language that I outlined the problems in [my last post](https://alperenkeles.com/posts/llms-could-be-but-shouldnt-be-compilers/)
where I talk about the topic of LLMs as compilers. Instead of picking
a specific implementation of a map, we could define an abstract map object that upholds certain properties; similar
for sets, lists, queues, heaps... Given the ability to translate at will, we could conjure programs that conform
to these declarative specs which we can refine in time, taking back the control we relinquish whenever necessary.
