+++
title = "Closing the verification loop: Observability-driven harnesses for building with agents"
date = "2026-03-09"

[taxonomies]
tags = ["software engineering", "ai", "testing"]
language = ["en"]

[extra]
mirror_url = "https://www.datadoghq.com/blog/ai/harness-first-agents/"
mirror_publisher = "Datadog AI"
mirror_redirect = true
mirror_redirect_delay = 5
mirror_stay_param = "stay"
canonical_url = "https://www.datadoghq.com/blog/ai/harness-first-agents/"
+++

This is a mirror entry of an article I co-authored published in [Datadog AI Blog](https://www.datadoghq.com/blog/ai/harness-first-agents/).

AI systems can now produce software faster than teams can verify it. Rather than manually inspecting every line of agent-generated code, we propose harness-first engineering: invest in automated verification mechanisms—deterministic simulation testing, formal specifications, shadow evaluation, observability-driven feedback loops—capable of determining correctness with high confidence within seconds.

We demonstrate this methodology through two projects: redis-rust, a Redis-compatible server built by a single agent with layered verification (shadow-state oracles, DST, TLA+ specs, Kani proofs, Maelstrom testing), and Helix, a Kafka-compatible streaming engine that served ~10,000 messages/second in staging with p50 produce latency of 22.2ms vs Kafka's 116ms. Both projects maintained human involvement in harness design, target-setting, and architectural approval, while agents handled implementation, bug-fixing, and optimization against established constraints.
