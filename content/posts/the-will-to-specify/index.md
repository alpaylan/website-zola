+++
title = "The Will to Specify"
date = "2026-02-02"
[taxonomies]
tags = ['software engineering', 'ai']
language = ["en"]
+++

I have been going round and round in my mind about a particular discussion
about LLMs, are they really similar to compilers? Are we going to a world
where people really don't look at the underlying code for their programs?

People have been making this argument since Andrej Karpathy announced English
to be the hottest new programming language, computer science has
been advancing language design by building higher and higher level
languages, and this is the latest iteration, we no longer need a separate
language to express ourselves to the machine, we can just use our native
tongues, let alone English.

My stance has been pretty rigid for some time, LLMs hallucinate, so they
aren't reliable building blocks, which means you cannot use them as a new
layer of abstraction because they provide no guarantees about the underlying
systems.

As models get better and better, the hallucinations have been less and less
of a concern, even though the models still make lots of mistakes, I've started
to realize a new aspect of the discussion. Let's say that LLMs stop hallucinating,
they do exactly what we want them to do, would they be the next generation of compilers,
what would that mean for programming, and software engineering in general?

This post is my stab at this question. The core of my argument is as follows:

> Specifying systems is *hard*; and we.are.*lazy*.

Before going into what this contextually means, let's follow up with another question,
what does a higher level language mean?

Programming is, at a fundamental level, the act of making a computer do something. Computers
are very dumb from the point of view of a human. You need to tell the computer exactly what to do,
there's no inference. A computer fundamentally doesn't even have the notion of a value, type, concept; everything
is a series of bits, which are processed to generate other bits, we bring meaning to this whole ordeal.
Very early on, people have started by building arithmetic and logical instructions into computers,
you would have 2 different bit sequences each denoting a number, you could add, subtract, multiply them.
In order to make a computer do something, you could denote your data in terms of a bunch of numbers, map
your logical operations onto those ALU instructions, and interpret the result in your domain at the end.
Then, you can define a bunch of operations on your domain, which will be compiled down to those smaller ALU
instructions, and *voila*, you have a compiler at hand.

This compiler is, admittedly, kind of redundant. It doesn't do anything you would be able to do because you
essentially have a direct mapping between your two *languages*, your higher level language desugars into a
bunch of lower level ALU instructions, so anyone would be able to implement the same mapping very easily,
and even go further, perhaps just write the ALU instructions themselves.

What *real* higher level languages do is they give you an entirely new language that is eventually mapped
to the underlying instruction set in non-trivial mechanisms in order to reduce the mental complexity
on the side of the programmer. For instance, instruction sets do not have the concept of variables,
nor loops, nor data structures. You can definitely build a sequence of instructions that amount to a binary
search tree, but the mental burden of the process is orders of magnitude higher than any classic programming
language. Structs, Enums, Classes, Loops, Conditionals, Exceptions, Variables, Functions are all properties
that exist in higher level languages that are compiled away when going down the stack.

There's a crucial aspect of compilation, which is that the programmer gives away some control, that's essentially
what removes the mental burden. If a programming language doesn't give away any control, it arguably isn't a very
useful abstraction layer, because it did not absolve you of any responsibility that comes with that control. One
of the first examples of this type of control we gave away is code layout. If you are writing handwritten assembly, you control where the code lives in the program memory. When you go into a language with structured control flow with callable procedures,
you now don't have exact control over when the instructions for a particular piece of code is fetched, how basic
blocks are arranged in the memory. Other examples are more common, the *runtime* of a language works in the background
to absolve you of other responsibilities such as manual memory management, which itself was an abstraction
for automatically managing how your data is organized in memory in the first place.

This loss of control gives rise to another question, how do we know that the abstraction is implemented correctly? More
importantly, **what does it mean for the abstraction to be correct?**

There are 3 answers here. The first is, these abstractions are typically formally defined with respect to the semantics
of the higher level language. A `malloc` call in C gives us (not really) the guarantee that the returned pointer
will be an exclusively owned piece of memory of our requested size. This is a functional guarantee, there are other
types of guarantees such as bounds of time complexity, security related safety and privacy properties, and possibly
quite many others I wouldn't know about. These formally defined guarantees are testable, and they are extensively tested,
that's how we trust the underlying implementation of the abstraction. There's another part to the story, which is that
we don't really care. Of course we care about the functional guarantee, a piece of memory we own shouldn't just vanish
into thin air, but most programs in the wild don't really care about the performance of their malloc implementation. The
ones that do look beneath the abstraction, that's why you see many performance critical programs switching their allocation
algorithm.

This highlights a cricial point, the guarantees of the underlying abstractions aren't uniform, abstractions are contextual.
For the majority of programming, this contextuality has been modulo functional correctness. The progress of programming
languages have had a unique focus on functional correctness, we built our abstractions with provable and testable guarantees
that a list in Python the same push/pop semantics as a vector in Java, even thought they are nothing alike in how they work under
the hood. LLMs alleviate this focus, specifically because they don't expose formal, precise semantics that allow us to define
functional correctness of our code.

With that, we get to the core argument at hand, what changes with LLMs isn't that their results are non-deterministic, or
that they are unpredictable at times, or that they hallucinate; but rather the language of programming with them is functionally
imprecise. Just as a programmer using a garbage collected language instead of a manual memory managed one relinquishes control
over how, when, which memory gets acquired and released in a program, a programmer using English to program relinquishes control
over how, when, which program runs to get fulfill their requirements. The functional imprecision necessitates that the LLM *guess*
details of the program, similar to how the allocation algorithm decides on a particular allocation strategy, the LLM decides on
all the missing details of the English-written specification.

**This creates quite a novel danger in how we write programs.**

We get to be lazy about the functional precision of the code we are running for the first time in the history of programming,
like we did become lazy about memory layouts or memory management, now we can just leave functional details of our programs
to our new generation of compilers (LLMs). We say, give me a note taking app, and the LLM will spit one of a billion different
possibilities in which the request is satisfied, this means we could technically get back Notion, Evernote, or Apple Notes, or
perhaps we could be met with a novelty that no note taking app already possess.

This puts us into an iterative refinement mode of development. Create an imprecise specification, get one of the possible results,
inspect the result and refine the specification, repeat step 3 until satisfied. We just became the consumer of our program instead
of its producer. We lose all the possibilities we would have otherwise explored if we didn't have a magic genie that gave us
exactly what we wished for.

I think this isn't a widely accepted point, hallicunations aren't the only problem, in an hallicunation-free world, the fact that we
can take the easy way out on defining the software we write plays into a dangerously lazy part of our mind, evidenced by all the
semi-concious slips (I'm also guilty of this phenomenon) into accept-all-edits and one-more-prompt-and-all-is-going-to-be-fine loops
we put ourselves.

That's why I think the will to specify is going to become increasingly important as we go forward. We already see great advances when
LLMs are given concrete specifications, they can optimize programs, people are testing them on translations and migrations that would previously
take so much time that we would have laughed if someone said they were going to do. This is possible because those problems are very well specified and they have concrete and robust test suites for validation of their results. I think it has been long true that specifying a piece of software has been
harder than building it, but right now it's possible that we are going to a world that if you can specify, you can build it. This will
make the ability to specify and verify much more important than they have ever been.

It's not been one of my best polished posts, but I still want to get this out. I now think that it's possible to think of LLMs as a sort of compiler,
but the relinquished control from the user to the compiler is greater than it has ever been in the history. Just like previous compilers have reduced
the need to look into those lower level layers in our stack in many contexts, LLMs will and are reducing our need to look into source code in many contexts.
However, the fact that the control we lose with LLMs isn't formally defined and tested as in the compilers case, the fact that we can lose control to the degree
that we become consumers of the software we had set out to produce, and the fact that we are predisposed to lose such control to the degree that we don't
understand what we created, I think we must not accept the anology and look for ways to produce the will to specify.
