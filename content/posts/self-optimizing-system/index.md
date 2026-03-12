+++
title = "From Hand-Tuned Go to Self-Optimizing Code: Building BitsEvolve"
date = "2025-09-18"

[taxonomies]
tags = ["software engineering", "ai", "optimization", "datadog"]
language = ["en"]

[extra]
mirror_url = "https://www.datadoghq.com/blog/engineering/self-optimizing-system/"
mirror_publisher = "Datadog Engineering"
mirror_redirect = true
mirror_redirect_delay = 5
mirror_stay_param = "stay"
canonical_url = "https://www.datadoghq.com/blog/engineering/self-optimizing-system/"
+++

This is a mirror entry of an article I co-authored published in [Datadog Engineering Blog](https://www.datadoghq.com/blog/engineering/self-optimizing-system/).

> At Datadog, cost-aware engineering is more than a principle; it’s a performance challenge at scale. We’ve published how we saved $17 million by rethinking our infrastructure, and we’ve built Cloud Cost Management to help customers do the same. But scaling deep, expert-level code optimization across a fast-moving engineering organization presents its own challenge.

> Our journey didn’t start with a grand AI design. It began as a mission to trim CPU usage in several critical hot-path functions in our most expensive services. For the hands-on performance engineer, we’ll dig into the gritty work of optimizing Go code: eliminating compiler bounds checks, restructuring loops, and rewriting functions for maximum efficiency. For those building agentic systems with LLMs, we’ll share how those human-driven optimizations seeded the heuristics behind BitsEvolve, our internal agentic system for self-optimizing code.

> Whether you’re here for the nanoseconds saved in Go or for a way to scale deep optimization work beyond a handful of experts, we’ll share what worked, what surprised us, and how the art of manual optimization provided the blueprint for an automated system.
