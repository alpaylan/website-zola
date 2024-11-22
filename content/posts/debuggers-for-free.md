+++
title = "Printf Debuggers for Free"
date = "2024-11-23"
[taxonomies]
tags = ["project", "programming"]
language = ["en"]
+++

Software engineering has many ancient debates. OOP vs FP, dynamic types vs static types,
printf debugging vs visual debuggers... I personally always found the last one very intriguing,
because it feels like we shouldn't have to choose at all. Why isn't there a best-of-both-worlds
solution that allows us to get the level of convenience and integration printf does, with
the level of inspectability we get from the visual debuggers?

The answer is probably around (1) it exists, but people don't use it, (2) language tooling is
hard, so we don't have a good version of it yet, and (3) we haven't figured out the exact
user experience for it yet. Well, this article introduces one such approach, which I call
`trace debugging`, that allows for constructing custom stack traces of only the functions the user
cares about, and a post-hoc visual interface for playing with it.

## Trace debugging

The title is carefully worded as `printf debuggers`, instead of `printf debugging`, because
I think `trace debugging` is exactly a `printf debugger`, it's a debugger made out of printfs.
In trace debugging, we mark functions to be traced. When a function is traced, two things happen.

1. It gets added to a global map tracking function calls.
2. The function itself gets instrumented to (1) increment the corresponding counter when it's called,
    (2) decrement the counter when it finishes execution, (3) two print statements get injected before
    and after the function call.

Let's consider a simple addition function in Rust.

```rust
#[trace]
fn add(left: u64, right: u64) -> u64 {
    left + right
}
```

Calling this function with `3` and `5` now prints:

```text
> [add] (left: 3) (right: 5)
< [add] 8
```

Most of this is pretty easy and expected, with the small addition of `>` and `<` at the beginning. `>` marks the entry point of a function,
and `<` marks the result. The usefulness of the approach comes when recursion is involved.

Consider the following `fib` function.

```rust
#[trace]
pub fn fib(n: i64) -> i64 {
    if n <= 1 {
        n
    } else {
        fib(n - 1) + fib(n - 2)
    }
}
```

The resulting trace for `fib` is as follows;

```text
> [fib] (n: 4)
> > [fib] (n: 3)
> > > [fib] (n: 2)
> > > > [fib] (n: 1)
< < < < [fib] 1
> > > > [fib] (n: 0)
< < < < [fib] 0
< < < [fib] 1
> > > [fib] (n: 1)
< < < [fib] 1
< < [fib] 2
> > [fib] (n: 2)
> > > [fib] (n: 1)
< < < [fib] 1
> > > [fib] (n: 0)
< < < [fib] 0
< < [fib] 1
< [fib] 3
```

Now, we can track the function calls easily through the nesting at each level, which we couldn't have done with naive printf debugging.

When you consider mutual recursion through a series of nested function calls, the approach becomes even more useful.

```text
> [even] (n: 5)
> [odd] (n: 4)
> > [even] (n: 3)
> > [odd] (n: 2)
> > > [even] (n: 1)
> > > [odd] (n: 0)
< < < [odd] false
< < < [even] false
< < [odd] false
< < [even] false
< [odd] false
< [even] false
```

Of course, as programs get longer, the inspection of these traces will get too long to read. That's where the visual
debugger aspect comes from. So far, all we've done is to create a nice printing macro that tracks call depth and
prints it in a standardized format.

Good thing for us is that, those things enable many applications on top of them. Because we have the inputs to each function call, we can
jump to any pure function call that doesn't access any globals and execute it. We have essentially created small snapshots of the program
for the subset we're interested in. Well, unfortunately I haven't implemented such advanced debugging capabilities yet; but I have
a proof of concept.

The thing is, I haven't invented the idea of tracing, I saw it in [Racket](https://racket-lang.org). Racket has a [trace function](https://docs.racket-lang.org/reference/debugging.html)
that you can use to hook functions, and it does exactly what I've described so far. The Rust macro I implemented uses the same printing
interface, which is essentially a serialization protocol, that Racket uses. So, any tool that is designed to consume the Racket trace output
would be able to read and navigate Rust traces now, and vice versa. That's where the `free` part of the title comes from, in any language
you implement the tracer, you get access to the same debugging tools.

I've created a prototype tool to read the Racket output, and the demo is at [https://alperenkeles.com/pages/debugger.html](/pages/debugger.html).

Below is an iframe of the tool, but you can also visit the link to see it in full screen. When you hit `Parse Trace`, it will parse the trace
on the left, and construct a visual representation of the function calls on the right. You can collapse a function call to hide the details
and just check its result, and I've also plans for adding tree-based navigation to the trace too.

So this is it. My next plans are making the Rust macro more robust, adding more features to the visual debugger, implementing the tracer in more
languages such as Javascript or Python, and maybe even creating a language server protocol for it so I can hook it inside an IDE. I really think
this might be a viable middle ground between printf debugging and visual debuggers, and I'm excited to see where it goes. **Let me know what you think!**

<iframe src="/pages/debugger.html" width="100%" height="500px"></iframe>