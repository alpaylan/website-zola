+++
title = "On The Simplicity of Humanness"
date = "2026-04-13"
[taxonomies]
tags = ['software engineering', 'ai']
language = ["en"]
+++

Just yesterday, Bryan Cantrill published a short piece that touches something that I
think most of us fundamentally understand, but don't have the words. The article is very
short, titled
["The peril of laziness lost"](https://bcantrill.dtrace.org/2026/04/12/the-peril-of-laziness-lost/).
I recommend you all read it. I plucked out one sentence for you:

> The problem is that LLMs inherently **lack the virtue of laziness.**

The essence is, our laziness is the reason we engineer simple systems. LLMs lack this
laziness, which results in the fact that they don't have the incentive or the process to
simplify, given that we don't externally create such mechanisms. That is why Anthropic
had to introduce a separate command (`/simplify`) to enable such post hoc simplification
process.

The thing that touches me the most about this idea is that I have been frequently amazed
by the simplicity of human-engineered artifacts. All the algorithms I've ever read
seemed simple, perhaps _too simple_ in hindsight. All the codebases, even the gigantic
ones, can be broken into simpler modules, sections, abstractions, hierarchies that allow
us to understand the system. A great deal of modern advances in computing are due to
simplification, malloc made memory allocation simpler, structured programming made
control flow simpler, Rust made memory management simpler, typically via removal of our
mental burdens.

It's not just computer science, all human-engineered systems are _simple_, for a very
specific meaning of the word; as opposed to emerging structures such as social
relationships or physical world that just _is_, or evolution that just _happens_. One
may object that a plane, or Linux kernel, or the lithography machine of ASML is very
complex, and they would be right. But all of those systems can be broken into smaller
modules, subsystems, abstractions that allow for understanding them. I can say this
confidently without having a concrete idea of what those systems are and how they work,
because I believe in a fundamental principle of engineering, **we must be able to
maintain the systems we build**.

When something goes wrong in a system, we must be able to locate where it is, understand
the root cause of the problem, make changes in a way that are isolated without
regressing on other parts of the system, and validate that the change correctly fixed
our problem. Nature has the luxury to simply _not care_, things break, systems fail,
earthquakes happen, it's all part of the plan.

There are escape hatches to this simplicity, complexities that we do not need to
understand, when there's an asymmetric relationship between the process and the
verification of the result. This has been long known and applied in the field of
automated theorem proving, the
[de Bruijn Criterion](https://lawrencecpaulson.github.io/2022/01/05/LCF.html) separates
the proof object, the proof checker, and the proof producer from each other. We must
only understand and trust the proof checker, the proof objects themselves are irrelevant
for the purposes of understanding the system. Although the generated proofs are
irrelevant, I argue that the same engineering principles still apply to the proof
producing programs, just not their results. A SAT solver possesses _humanness_, but the
proofs it produces will not. A genetic algorithm possesses the humanness, but its
artifact, such as AlphaZero, is akin to a biological organism that we must try to
understand and model. We still care about understanding such results, because they allow
us to improve on the engineering artifacts that produce them, as well as the outputs
themselves, but we can **bear** not to.

LLMs do not possess the humanness right now, they probably will never do, just as
AlphaZero doesn't. This doesn't make their outputs useless, but rather a new challenge
we must overcome. In highly
[verifiable domains](https://alperenkeles.com/posts/verifiable-abstractions/), such as
[translation](https://alperenkeles.com/posts/autonomous-translations/) or
[optimization](https://alperenkeles.com/posts/self-optimizing-system/), we will continue
to see them in high, sometimes autonomous capacities. In other domains, we will find a
way to push [their limits](https://alperenkeles.com/posts/verifiability-is-the-limit/).
We will build more and more tools for analyzing and understanding programs that we
previously did not need to, not because we couldn't, but because such understanding now
gives us a great deal of
[leverage](https://alperenkeles.com/posts/specifiability-is-the-leverage/).

I didn't really know what I wanted to say when starting to write this one, I do that
sometimes. Now that I'm concluding, I am searching for a conclusion, here it is; we are
driven to understand the systems we build and maintain, and we find ways to do so. We
were able to analyze the world, figure out the rules of the universe, model the human
genome to its molecules that we didn't even know existed. I don't think that was
primarily due to laziness, but rather the drive to build better, larger, greater
systems; and I think we'll find a way to mold the LLM outputs into forms that we can
understand too.

Thanks Bryan for lighting a spark that led me to write this, I hope you have enjoyed
reading this as much as I did writing.
