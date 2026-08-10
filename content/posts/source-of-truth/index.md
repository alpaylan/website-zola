+++
title = "Source of truth is all you need"
date = "2026-08-10"
[taxonomies]
tags = ['software engineering', 'ai']
language = ["en"]
+++

Coding agents are, well, _surprisingly good_. Maybe I'm telling on myself by this, but I
sometimes learn by inspecting the way the agent leverages an API, or the way it solves a
problem that I couldn't wrap my head around in the first place. As agents are able to do
more things, do them reliably and tirelessly, the position of a software engineer is
ever-increasingly questioned, **what is left for the engineer to do?**

A simplest answer is: let's separate software engineering into 3 phases, (1) design, (2)
implementation, (3) verification. Using a coding agent shrinks (2); helps raise the bar
on (1); sometimes helps, but mostly actually moves lots of work to (3) because the
previous coupling of these three helped verification itself.

Lots of people are in agreement of this formula right now, "verification is the only
bottleneck" is a usual saying at this point. However, as the models get better, it is
tempting to ask if, and how, we can remove this verification bottleneck. The holy grail
of every automation is the final step of removing the human from the loop, so I presume
we will keep revisiting this discussion. I further presume that many of those
revisitations will lead us to discover junctions, points where the answer to the posed
question depends on the problem at hand, so the nuances in our understanding of the
topic will evolve.

A junction we have today is, **do we still need to read the code?** On one hand, the
answer is obviously no, because lots of people don't read lots of code they write and
even deploy, so the statement isn't universally true. On the other hand, the answer is
obviously yes, because nobody wants to use a vibecoded plane. So I get to do my favorite
thing, try to find where the line is, and guess where it could shift with better models
in the coming years.

To discover the dividing line, let's start by looking at programming languages and their
compilers. The programming language specifies a set of behaviors, the compiler
implements them in a best-effort manner. To me, the interesting part of this discussion
is not miscompilation that leads to semantic failures; the compiler implements so much
more than the specification of the programming language, it implements the specification
in a "good" way. This goodness is highly contextual, the compiler balances performance,
security, portability, binary size, compilation speed, correctness, and this act of
juggling always leaves for improvement on some axis, which a sufficiently good engineer
with the right requirements can search for and exploit.

The LLMs pose two new challenges, the first is that the there is a new axis to the
"goodness", how good is the intent formalization? In contrast to a classic programming
language where each operation has its own semantics at a particular, preset level;
natural language offers us a whole range of granularities, any missing detail is
inferred by the model. The "accuracy" of the model in inferring the correct intent,
whatever that is, is crucial in our ability to use it. Note that this is different from
the model capability in following instructions, which is a discussion I tend not to go
into, but rather the result of the tension of specification granularity,
[is a sufficiently detailed spec code](https://haskellforall.com/2026/03/a-sufficiently-detailed-spec-is-code)
or
[not?](https://buttondown.com/hillelwayne/archive/a-sufficiently-comprehensive-spec-is-not/)

I think Gabriella and Hillel are both right, many times a sufficiently detailed spec is
code, but it need not be. Why is this sufficiently detailed spec written in Rust or
Haskell rather than the underlying assembly, not because the initial compilers were
great at genenerating better code than the early programmers, but rather because it
allowed them to do more, it allowed more people to write code, organize, scale, build,
understand. Anyway, I have some longer thoughts on a previous post
([LLMs could be, but shouldn't be compilers](https://alperenkeles.com/posts/llms-could-be-but-shouldnt-be-compilers/)),
but I should get to my point, the second challenge.

Let's say that we stopped reading code, the question now is, _what do we read instead of
code?_

Software engineering is the process of creating and maintaining software systems. In the
existing paradigm, every line of code is read and audited, the software engineer builds
an understanding of the underlying system through this process. This allows the engineer
to propose and validate changes to the system. Even further so, code _is_ the source of
truth. When a fault emerges in a system, confusions are cleared up by reading the code,
stepping on the debugger, checking out the logs; incidentally the more complex and
disorganized the source of truth for a system is, the harder it is to resolve such
issues. A side effect of the fact that every line of code is read is that
[code is simple](https://alperenkeles.com/posts/on-the-simplicity-of-humanness/). Built
by engineering practices for engineers, programs are built on hierarchical, manageable
pieces; and at many times every single piece is deceptively simple. A machine-built
codebase, much like the proof we get from a SAT solver, will not be simple, it will be
chaotic, its limits will be directed by how "machine-readable" it is, which means we
will need a new source of truth, because we won't be able to reason simply by looking at
the code, very much like how we aren't able to reason about the whole program by going
through its assembly today.

Well, in that case, what is the equivalent of a high level programming language in this
paradigm, what do we read if we want to understand what the system does, why/how it does
it, what a particular change means? (no, it's not markdown, please not)

Today's answer to this question is that the model is the source of truth. You want to
onboard to a codebase? Ask the model where to start, what to check, what each behavior
surfaces from... This can work fairly well in guiding you a codebase of today, optimized
for human readability. However, with a paradigm change towards machine readability, I do
not feel as confident that will be the case, and I think that will be the step in trying
to figure out higher levels of abstractions and programming languages, formal
reflections of our high level informal specifications, which would constitute a
compiler-like revolution within the natural language programming paradigm, as opposed to
the current form where code is still the source of truth but it is ever increasingly
harder to understand and interpret.

So, going back, if we don't need to read the code, what do we need to read? Well,
whatever the source of truth is, I think that will be all we need.
