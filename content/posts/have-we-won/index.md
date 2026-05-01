+++
title = "Have we won, what now?"
date = "2026-05-01"
[taxonomies]
tags = ['software engineering']
language = ["en"]
+++

Will Wilson of Antithesis is a terrific public speaker, his latest keynote "We won, what
now?" at the flagship Antithesis conference, BugBash 2026, was another great hit. There
are some other nice accounts of the conference and Will's keynote from
[Alex Weisberg](https://concerningquality.com/bug-bash-two/) and
[Murat Demirbaş](https://muratbuffalo.blogspot.com/2026/04/bugbash26-keynote.html), so I
won't go into a detailed description of all the talk, but rather take the key idea and
mash it together with some of my own.

The idea is simple and powerful:

> Software correctness people have spent decades trying to convince people to take
> correctness, and methods that lead to correctness seriously. This was, for a variety
> of reasons, not a very successful endeavour. Now, with the emergence of neural program
> synthesis, there's an emerging inflow of money and attention to software correctness,
> random testing, formal methods; which means software correctness people won, people
> now _care_ about software correctness. However, this previously niche community will
> now will resentful towards the newcomers; they are the rushing into the gold, they are
> sitting on top of hundreds of thousands of prior work, with little acknowledgement or
> gratitude, they are here to collect the rewards. How will we as a community react to
> this, are we going to be able to survive winning?

The "fight" is already upon us. The
[blanket LLM ban proposal for Agda](https://github.com/agda/agda/pull/8456),
[the bullshit (excuse my language) proofs](https://x.com/prz_chojecki/status/2038941194126790716),
[my blog post on the critique of the promises of AI-assisted proofs](https://alperenkeles.com/posts/test-dont-verify/),
[r/ProgrammingLanguages fighting slop](https://lobste.rs/s/ifcyr1/contributor_poker_zig_s_ai_ban#c_zbbl7j),
many, many blog posts that argue for and against a complicated variety of points...

It is important to note that formal verification has always had a high-tension
relationship with pragmatics. The academic field of formal verification is a noble one;
spending years proving code correct is a rewardless endeavour, a majority of what you
prove is trivial in hindsight. You prove, not because proving those small lemmas,
individual theorems about some modules give you reliability; but because proving a
system end-to-end gives you unmatched correctness guarantees. (on a very personal and
subjective account) I believe this results in a reality where the people doing proofs
have long been very passionate about the proofs themselves, the understanding one
extracts in the process of doing the proof, the aesthetics of the underlying
mathematics, rather than the pragmatics of correct software alone.

Now that generative proof tactics are here, there's an influx of pragmatists flowing
into the field. At BugBash, Ron Minsky mentioned that JaneStreet is considering
investing into formal methods as a long term skeptic of the potential ROI because of the
changing landscape, on the formal methods roundtable (no names because we had the
Chatham House Rule), several people presented new provable domains due to the lower cost
of proofs.

There's an entirely separate question of "are they right", of which my personal response
is "to a degree", but regardless, the investments are pouring in, the billion dollar
startup landscape of Axiom, Harmonic, Math Inc... are tackling Erdös problems alongside
mathematics competitions, mathematicians are increasingly using these tools for
mechanized proofs, and we should expect these changes to spill into formal verification
of software too.

To be perfectly fair, pragmatists aren't new. For the last 10 years, perhaps the most
popular option for a formal methods grad student after graduation was proving
cryptocurrency code correct, followed by proving planetary scale systems at AWS ARG. The
change is (1) the volume of the influx, and (2) the fact that the researchers are
expected to change the way they work too. That is perhaps one of the largest differences
of AI from other technologies in my lifetime, the proponents tell you that you _have to_
use it, otherwise you're left behind; most folks rightfully hate this rethoric, even if
it might be correct to some degree.

There's another side of the pragmatist influx; which is that they want results "now",
even if it means cutting corners. like the infamous autoformalization. Autoformalization
is the process of taking an informal specification, which could be a textual theorem
taken from a textbook or literally two sentences of verbal explanation of the theorem;
and synthesizing a formal, mechanized theorem in a proof assistant such as Rocq or Lean.
This process is fundamentally unsound as natural language has no constrained semantics,
so the meaning is ultimately dependent on the intent of the author; which has actually
led to some interesting discussions in the formalization of Erdös theorems, because some
interpretations of a theorem are trivial to prove, while others may take significant
effort. So the mathematics community must decide on an interpretation they find
valuable, while mechanized mathematics (as far as I know) admits a single interpretation
at a given point. There's some effort in detecting autoformalization faults by
roundtripping but I think all of these still fall outside the traditional expected bar
of the formal verification community because it expands the trusted base of the system
and one no longer has the total guarantees that historically comes with the "formally
verified" stamp.

I do not think that corner cutting is going to end with autoformalization, because
formal verification is fundamentally a very hard problem. It is not just the effort
required to prove things, but rather the fact that you cannot just prove arbitrary
programs and arbitrary facts. The way to state the theorem is part of the proving
process, further so, the way to write the program as well as the language you write
program are all parts of the process. **Verification does not work in isolation.** A
simple example here is Rust; in order to get the correctness guarantees you are
forbidden from writing some supposedly valid programs, using patterns that might have
better cache locality. With this limitation, I presume we will see more cases where
formal verification is a "rubber stamp", and the meaning of the word is lost if we're
not careful.

Of course it's not all bad; theorem provers has long leveraged the
[de Bruijn Criterion](https://lawrencecpaulson.github.io/2022/01/05/LCF.html), when we
can separate the proof producer from the proof checker, we can focus on a sound checker
and a complete producer instead of trying to have a sound producer too, the _tactics_ in
theorem provers leverage this exact idea; and I posit proof object synthesis will work
very well. We are not limited to the scope of tactics, we can enlarge the untrusted
envelope as long as we build a trusted interface around it; something
[I've been articulating](https://alperenkeles.com/posts/verifiability-is-the-limit/) for
some time now.

So, what now? I expect the different fractions of people I mentioned in the article to
actually go on building different subcommunities instead of trying to reconcile them all
under a common "we", because they have different mental models of the world, different
motivations in doing formal verification and different incentive structures. So it feels
to me that we might not have actually won, because I don't know if alignment within the
broad community is really possible.
