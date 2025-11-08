+++
title = "Ruggle"
description = "A structural search engine for Rust"
weight = 1

[extra]
github_link = "http://github.com/alpaylan/ruggle"
+++

Ruggle is a fork of [Roogle](https://github.com/roogle-rs/roogle), a Rust API search engine that allow for searching functions using type signatures over Rust codebases.

The idea of API search for programming languages isn't novel, [Hoogle](https://wiki.haskell.org/index.php?title=Hoogle) has been around for more than 2 decades, Roogle itself is 4 years old,
OCaml has [Sherlodoc](https://github.com/art-w/sherlodoc), Lean recently announced [Loogle!](https://loogle.lean-lang.org)...

Yet, none of these tools are mainstream in the languages they reside in. **I would like to change that.**

I am building Ruggle with the vision of becoming the default mode of search when working on a Rust project, making structural search a first class citizen developer tooling. When searching in a codebase, it is rare that we are without context; however text search forces us to build a textual context when we already have access to much more structural information. The objective of Ruggle is to build this graph of structured information, and allow the user to query it as a better search engine.

This starts with a local first interface with minimal friction, that's why I started by building a [VSCode Extension for Ruggle](https://marketplace.visualstudio.com/items?itemName=AlperenKeles.ruggle). The users can automatically download the latest Ruggle server
and start searching. Let's also give some bit of context.

## How does Ruggle work under the hood?

Rust already has a decent amount of tooling for building overviews of projects (crates), [docs.rs](https://docs.rs). docs.rs
project hosts a detailed documentation of every published Rust crate, built using `rustdoc`, a part of the Rust compiler
toolchain, which also has a `json` backend that allows for creating alternative frontends to docs.rs. In some sense,
that is exactly what we're doing, we are building an alternative to docs.rs, a local, realtime search engine instead of a
hosted service.

Once the dependencies are indexed, the users can start searching by writing queries in the form:

```rust
fn(String) -> &str
fn append<T>(&mut Vec<T>, T)

```




