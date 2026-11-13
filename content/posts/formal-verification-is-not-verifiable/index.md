+++
title = "Formal Verification is Not Verifiable"
date = "2026-10-07"
[taxonomies]
tags = ['software engineering', 'ai', 'formal methods', 'software testing']
language = ["en"]
[extra]
draft = true
+++

> AI *is* making formal verification go mainstream...

...I wrote on December 2025, well, after the last 12 months I believe it has hard to argue otherwise. AI *has* made formal verification go mainstream.

Not only did the number of formal verification startups skyrocket, Lean surpassed a billion lines of code, everyone from the creator of Claude Code to Vercel CEO, lead Codex/Cursor developers is talking about formal verification. The early startups have started to show econimical value in software on top of simply producing math proofs: Theorem's binary verification work with Anthropic, Harmonic verifying C programs and ASICs... With the cybersecurity risk going through the roof, formal verification is not just easier, it is also getting more economically valuable.

The questions people ask now are not "how can we prove X", but rather "what can we prove about X"; or "is fuzzing obsolete", "what is left that we can't prove"? These are good questions to ask, I am writing this post in part to answer them; an in part as a follow up to last year's post "Test, Don't (just) Verify". To tease the ending, I am very optimistic about formal verification, but I think people mean lots of different things when they say something is "formally verified", which I will try to break down into the parts I'm optimistic and pessimistic about.

Let's start from the title, I'm what an SF person would call a "verifiability-pilled" person, I've argued for long (well, 2 years) that verifiability was the limit of how much leverage AI can give us; my rough long term view is that we will build our technology stack around these spikes of verifiable components in our systems. Nowadays, when verifiability is mentioned formal verification very quickly jumps into the discussion. However, somehow, formally verified systems can still have bugs, and when I hear someone formally verify their systems I am genuinely not filled with a flow of confidence in the correctness of their system. On the other hand, when someone says they found a bug in a system, I am fairly confident that they did so. I argue that this is because testing is verifiable, it produces a well-defined, reviewable, understandable object, a good old bug report. Testing is verifiable (by a HUMAN) as in UI components are verifiable, that's why they're both very easy to use AI with.

Formal verification on the other is has "verified" components that require no external review, the proofs; and hard to verify components, the definitions themselves, the underlying models of the object we are proving facts about, the provers that are doing the verification. Because the underlying claim is much stronger--formal verification is a *forall* claim, testing is an *exists* claim--any mistake in any of these hard to verify components lead to the downfall of the proofs.

I argue that the future of formal verification is reduction of these "trusted" components; of course I am hardly the first person to do this, formal methods people have long argued for smaller TCBs, but it seems we are somewhat forgetting these hard-earned lessons?

First of all, let's picture 


https://x.com/julianor/status/2120878929145741430

