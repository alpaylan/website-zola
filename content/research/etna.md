+++
title = "etna"
description = "An Evaluation Platform for Property-Based Testing"
weight = 1

[extra]
link_to = "/research/etna"
+++

ETNA is an evaluation and analysis platform for Property-Based
Testing Tools. It provides **(1)** a modular interface for adding new
languages and new testing frameworks, **(2)** several testing workloads
replicated in different languages, **(3)** experimentation primitives for
running tests and collecting results, and **(4)** visualization tools for
comparing the results of different tools.


<style>
    .row {
        display: flex;
        gap: 16px;
        justify-content: space-between;
        flex-wrap: wrap;
    }

    .column {
        flex: 1;
        /* min-width: 150px; */
        padding: 8px;
    }
    
    .noted {
    position: relative;
    display: flex;
    gap: 16px;
    
    }

    .main {
    position: relative;
    max-width: 70%;
    }
    .note {
    max-width: 30%;
}
</style>


<div class="row">
    <div class="column">
        {{ github(repo="jwshii/etna") }}
    </div>
    <div class="column">
        {{ github(repo="alpaylan/etna-cli") }}
    </div>
</div>

