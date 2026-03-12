+++
title = "From Hand-Tuned Go to Self-Optimizing Code: Building BitsEvolve"
date = "2025-09-18"

[taxonomies]
tags = ["software engineering", "ai", "optimization"]
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

Performance optimization at scale requires strategic focus. At Datadog, we started with manual optimizations of hot functions in the tag-processing pipeline—achieving a 25% speedup on `NormalizeTag` and a 90% speedup on `NormalizeTagArbTagValue` through loop unrolling and fast-path optimizations informed by observability data.

But hand-tuned optimization doesn't scale. Inspired by Google DeepMind's AlphaEvolve, we built BitsEvolve, an agentic optimizer that uses evolutionary algorithms with automated evaluation to evolve code variants. Early results were striking: BitsEvolve rediscovered our manual optimizations bit-for-bit, improved Murmur3 hashing by ~20%, and converged on CRC32 optimizations in about 50 iterations.

Combined with Simba (our SIMD Binary Accelerator for Go-to-Rust interop) and production observability, we achieved a 97% compute reduction on a critical ingestion path. The vision: optimization as infrastructure—persistent, production-aware agents continuously watching, learning, and improving.
