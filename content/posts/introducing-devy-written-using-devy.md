+++
title = "Introducing Devy, written using Devy!"
date = "2024-04-11"
[taxonomies]
tags = ['devy', 'static site generator']
language = ["en"]
+++

<h1 id="introducing-devy-written-using-devy">
 Introducing Devy, written
using Devy!
</h1>
<p>
 <img alt="Devy Logo" src="https://github.com/alpaylan/devy/blob/630d2519cc3e62458f30e689470d2b6c34403a03/devy-logo.png?raw=true" style="display: block; margin-right: 20; float: left; width: 250px; "/>
</p>
<p>
 This blog post introduces
 <a href="https://github.com/alpaylan/devy">
  Devy
 </a>
 , the interactive blog
engine I’ve been working on. Devy is a static site generator that allows
you to write interactive blog posts using a combination of markdown and
a custom DSL. This post is written using Devy, so you can see how it
works in action!
</p>
<p>
 I like to write a lot of small code snippets in my code, and I want
my readers to be able to try them out. Using DCL(Declarative Component
Language), I can define components and their interactions in a simple
way. For example, the following code block defines a function for
turning a given string into uppercase:
</p>
<p>
 <strong>
  If you would like to see what this post looks like without
any CSS, check out the
  <a href="https://alperenkeles.com/devy.html">
   raw HTML
  </a>
  .
 </strong>
</p>
<input id="toUpperCase" type="hidden" value="const toUpperCase = (str) =&gt; str.toUpperCase();"/>
<script>
 const toUpperCase = (str) => str.toUpperCase();
</script>
<pre><code class="language-js" name="toUpperCase">const toUpperCase = (str) =&gt; str.toUpperCase();</code></pre>
<p>
 A simple feature, which probably should be the default behavior in
the future, is the ability to copy the code block to the clipboard. The
next code block is a simple example of a function that adds two numbers
together:
</p>
<input id="add" type="hidden" value='const add = (a, b) =&gt; "Answer is " + (parseInt(a) + parseInt(b));'/>
<button onclick="navigator.clipboard.writeText(document.getElementById('add').value);">
 Copy
</button>
<script>
 const add = (a, b) => "Answer is " + (parseInt(a) + parseInt(b));
</script>
<pre><code class="language-js" name="add">const add = (a, b) =&gt; "Answer is " + (parseInt(a) + parseInt(b));</code></pre>
<p>
 Line numbers are also an important feature(you need a little bit of
css to make them look good). Of course, we are not always limited to
Javascript, so here’s a Rust version of the
 <code>
  add
 </code>
 function.
</p>
<style>
 .line-numbers {
        display: inline-block;
        margin-right: 10;
        padding: 0;
    }
</style>
<input id="add-rs" type="hidden" value="fn add(a: i32, b: i32) -&gt; i32 {
    a + b
}"/>
<div style="display: flex; flex-direction: row;">
 <pre class="line-numbers"><code><span>1</span>
<span>2</span>
<span>3</span></code></pre>
 <pre style="flex:1"><code class="language-rust" name="add-rs">fn add(a: i32, b: i32) -&gt; i32 {
    a + b
}</code></pre>
</div>
<p>
 That’s all pretty cool, but nothing impressive. The fun starts when
you can run code snippets and use their results. That’s where DCL comes
into play. Below is a short DCL snippet that uses the
 <code>
  add
 </code>
 function to add two numbers together. The first two lines define the
inputs and their initial values, and the third line defines the output
as a function of the result of adding the two inputs together.
</p>
<input id="" type="hidden" value="```dcl {#add-example}
input1 : text-input := 5
input2 : text-input := 10
output : text-area := input1, input2 =&gt; add(input1, input2)
```"/>
<pre><code class="language-" name="">```dcl {#add-example}
input1 : text-input := 5
input2 : text-input := 10
output : text-area := input1, input2 =&gt; add(input1, input2)
```</code></pre>
<p>
 Devy compiles this DCL snippet into HTML and Javascript code that
updates the output whenever the inputs change as you can see below:
</p>
<input id="add-example" type="hidden" value="input1 : text-input := 5
input2 : text-input := 10
output : text-area := input1, input2 =&gt; add(input1, input2)"/>
<input id="input1" type="text" value="5"/>
<input id="input2" type="text" value="10"/>
<script>
 document.getElementById("input1").addEventListener('input', function(event) {
    document.getElementById("output").value = add(document.getElementById("input1").value, document.getElementById("input2").value)
});
</script>
<script>
 document.getElementById("input2").addEventListener('input', function(event) {
    document.getElementById("output").value = add(document.getElementById("input1").value, document.getElementById("input2").value)
});
</script>
<textarea id="output"></textarea>
<p>
 Text inputs are not the only components available. Here’s an example
of a radio button that asks a question and provides feedback based on
the answer:
</p>
<p>
 <strong>
  Do you think Devy is a cool project?
 </strong>
</p>
<input id="radio-example" type="hidden" value='option : radio := yes, no, of course
feedback : paragraph := option =&gt; option === "of course" ? "Great job!" : "Incorrect! Try Again!"'/>
<input id="option" type="hidden"/>
<input id="option_yes" name="option" type="radio" value="yes"/>
<script>
 document.getElementById("option_yes").addEventListener('input', function(event) {
    document.getElementById("option").value = "yes";
    document.getElementById("option").dispatchEvent(new Event('input'));
});
</script>
<label for="option_yes">
 yes
</label>
<input id="option_no" name="option" type="radio" value="no"/>
<script>
 document.getElementById("option_no").addEventListener('input', function(event) {
    document.getElementById("option").value = "no";
    document.getElementById("option").dispatchEvent(new Event('input'));
});
</script>
<label for="option_no">
 no
</label>
<input id="option_of course" name="option" type="radio" value="of course"/>
<script>
 document.getElementById("option_of course").addEventListener('input', function(event) {
    document.getElementById("option").value = "of course";
    document.getElementById("option").dispatchEvent(new Event('input'));
});
</script>
<label for="option_of course">
 of course
</label>
<script>
 document.getElementById("option").addEventListener('input', function(event) {
    document.getElementById("feedback").innerHTML = document.getElementById("option").value === "of course" ? "Great job!" : "Incorrect! Try Again!"
});
</script>
<p id="feedback">
</p>
<details>
 <summary>
  Click to see the CDL code for the question!
 </summary>
 <input id="" type="hidden" value='```dcl {#radio-example}
option : radio := yes, no, of course
feedback : paragraph := option =&gt; option === "of course" ? "Great job!" : "Incorrect! Try Again!"
```'/>
 <pre><code class="language-" name="">```dcl {#radio-example}
option : radio := yes, no, of course
feedback : paragraph := option =&gt; option === "of course" ? "Great job!" : "Incorrect! Try Again!"
```</code></pre>
</details>
<p>
 Aside from interactivity, I also want to focus on easily creating
diagrams and other visualizations. For now, I started with the
 <a href="https://mermaid.js.org">
  Mermaid
 </a>
 diagrams, which are simple to
write and look great. Here’s an example of a simple flowchart:
</p>
<input id="mermaid-0" type="hidden" value="graph LR
A[Second diagram] --&gt; B[Something]
B --&gt; C[Something]
C --&gt; D[Something]
A --&gt; D[Something]"/>
<script src="https://cdn.jsdelivr.net/npm/mermaid@8/dist/mermaid.min.js">
</script>
<script>
 setTimeout(() => {
                                            mermaid.render(
                                                "mermaid-0-renderer",
                                                document.getElementById("mermaid-0").value,
                                                (code) => {document.getElementById("mermaid-0-rendered").innerHTML = code}
                                            ), 100});
</script>
<div id="mermaid-0-rendered">
</div>
<p>
 One cool thing I added(which doesn’t exist natively in Mermaid) is
animating the diagrams. Users can easily add a
 <code>
  rate
 </code>
 attribute to the mermaid code block to control the animation speed. For
example, the following diagram animates at a rate of 1000ms:
</p>
<input id="mermaid-1" type="hidden" value="graph LR
A[Second diagram]
A[Second diagram] --&gt; B[Something]
B --&gt; C[Something]
C --&gt; D[Something]
A --&gt; D[Something]"/>
<script src="https://cdn.jsdelivr.net/npm/mermaid@8/dist/mermaid.min.js">
</script>
<script>
 setInterval(() => {
                                            let value = document.getElementById("mermaid-1").value;
                                            let frames = value.split("\n");
                                            let numberOfFrames = frames.length - 1;
                                            let currentSecond = Math.floor(Date.now() / 1000);
                                            let currentFrame = (currentSecond % numberOfFrames) + 1;
                                            let frameContent = frames.slice(0, currentFrame + 1).join("\n");
                                            mermaid.render(
                                                "mermaid-1-renderer",
                                                frameContent,
                                                (code) => {document.getElementById("mermaid-1-rendered").innerHTML = code}
                                            )
                                        }, 1000);
</script>
<div id="mermaid-1-rendered">
</div>
<p>
 The current animation system is pretty simple, but I plan to add (1)
phase-based animations where user can define the frame each element
should appear, (2) control mechanisms for animations such as dynamic
speed control, and (3) layout preserving animation where all elements do
not destructively move around.
</p>
<p>
 That concludes the current state of Devy. It’s a brand new project,
and there are lots of features I want to add. If you have any ideas,
please let me know by opening an issue on the
 <a href="https://github.com/alpaylan/devy">
  GitHub repository
 </a>
 . I’m
excited to see where this project goes, and I hope you are too! Also,
please leave a star on the repository if you like the project!
</p>
<p>
 <strong>
  Repository Link:
 </strong>
 <a href="https://github.com/alpaylan/devy">
  https://github.com/alpaylan/devy
 </a>
</p>
<h2 id="appendix">
 Appendix
</h2>
<p>
 Below is the Markdown code for all of this article.
</p>
<input id="" type="hidden" value="# Introducing Devy, written using Devy!

&lt;img src=&quot;https://github.com/alpaylan/devy/blob/630d2519cc3e62458f30e689470d2b6c34403a03/devy-logo.png?raw=true&quot; 
alt=&quot;Devy Logo&quot; 
style=&quot;display: block; margin-right: 20; float: left; width: 250px; &quot; /&gt;

This blog post introduces [Devy](https://github.com/alpaylan/devy), the interactive 
blog engine I've been working on. Devy is a static site generator that allows you 
to write interactive blog posts using a combination of markdown and a custom DSL.
This post is written using Devy, so you can see how it works in action!

I like to write a lot of small code snippets in my code, and I want my readers to be
able to try them out. Using DCL(Declarative Component Language), I can define components
and their interactions in a simple way. For example, the following code block defines
a function for turning a given string into uppercase:

**If you would like to see what this post looks like without any CSS, check out the [raw HTML](devy.html).**

```js  {#toUpperCase .script .show}
const toUpperCase = (str) =&gt; str.toUpperCase();
```

A simple feature, which probably should be the default behavior in the future, is the
ability to copy the code block to the clipboard. The next code block is a simple example
of a function that adds two numbers together:

```js  {#add .script .show .copy}
const add = (a, b) =&gt; &quot;Answer is &quot; + (parseInt(a) + parseInt(b));
```

Line numbers are also an important feature(you need a little bit of css to make them look
good). Of course, we are not always limited to Javascript, so here's a Rust version of
the `add` function.

&lt;style&gt;
    .line-numbers {
        display: inline-block;
        margin-right: 10;
        padding: 0;
    }
&lt;/style&gt;

```rust  {#add-rs .show .linenumbers}
fn add(a: i32, b: i32) -&gt; i32 {
    a + b
}
```

That's all pretty cool, but nothing impressive. The fun starts when you can run
code snippets and use their results. That's where DCL comes into play. Below is
a short DCL snippet that uses the `add` function to add two numbers together.
The first two lines define the inputs and their initial values, and the third
line defines the output as a function of the result of adding the two inputs together.

````
```dcl {#add-example}
input1 : text-input := 5
input2 : text-input := 10
output : text-area := input1, input2 =&gt; add(input1, input2)
```
````

Devy compiles this DCL snippet into HTML and Javascript code that updates
the output whenever the inputs change as you can see below:

```dcl {#add-example}
input1 : text-input := 5
input2 : text-input := 10
output : text-area := input1, input2 =&gt; add(input1, input2)
```

Text inputs are not the only components available. Here's an example of a
radio button that asks a question and provides feedback based on the answer:


**Do you think Devy is a cool project?**

```dcl {#radio-example}
option : radio := yes, no, of course
feedback : paragraph := option =&gt; option === &quot;of course&quot; ? &quot;Great job!&quot; : &quot;Incorrect! Try Again!&quot;
```

&lt;details&gt;
  &lt;summary&gt;Click to see the CDL code for the question!&lt;/summary&gt;

````
```dcl {#radio-example}
option : radio := yes, no, of course
feedback : paragraph := option =&gt; option === &quot;of course&quot; ? &quot;Great job!&quot; : &quot;Incorrect! Try Again!&quot;
```
````

&lt;/details&gt;

Aside from interactivity, I also want to focus on easily creating diagrams
and other visualizations. For now, I started with 
the [Mermaid](https://mermaid.js.org) diagrams, which are simple to write
 and look great. Here's an example of a simple flowchart:


```mermaid {#mermaid-0}
graph LR
A[Second diagram] --&gt; B[Something]
B --&gt; C[Something]
C --&gt; D[Something]
A --&gt; D[Something]
```

One cool thing I added(which doesn't exist natively in Mermaid) is
animating the diagrams. Users can easily add a `rate` attribute to
the mermaid code block to control the animation speed. For example,
the following diagram animates at a rate of 1000ms:

```mermaid {#mermaid-1 rate=1000}
graph LR
A[Second diagram]
A[Second diagram] --&gt; B[Something]
B --&gt; C[Something]
C --&gt; D[Something]
A --&gt; D[Something]
```

The current animation system is pretty simple, but I plan to add (1) phase-based
animations where user can define the frame each element should appear, (2) control
mechanisms for animations such as dynamic speed control, and (3) layout preserving
animation where all elements do not destructively move around.

That concludes the current state of Devy. It's a brand new project, and there are
lots of features I want to add. If you have any ideas, please let me know by opening
an issue on the [GitHub repository](https://github.com/alpaylan/devy). I'm excited
to see where this project goes, and I hope you are too! Also, please leave a star
on the repository if you like the project!

**Repository Link:** [https://github.com/alpaylan/devy](https://github.com/alpaylan/devy)"/>
<pre><code class="language-" name=""># Introducing Devy, written using Devy!

&lt;img src="https://github.com/alpaylan/devy/blob/630d2519cc3e62458f30e689470d2b6c34403a03/devy-logo.png?raw=true" 
alt="Devy Logo" 
style="display: block; margin-right: 20; float: left; width: 250px; " /&gt;

This blog post introduces [Devy](https://github.com/alpaylan/devy), the interactive 
blog engine I've been working on. Devy is a static site generator that allows you 
to write interactive blog posts using a combination of markdown and a custom DSL.
This post is written using Devy, so you can see how it works in action!

I like to write a lot of small code snippets in my code, and I want my readers to be
able to try them out. Using DCL(Declarative Component Language), I can define components
and their interactions in a simple way. For example, the following code block defines
a function for turning a given string into uppercase:

**If you would like to see what this post looks like without any CSS, check out the [raw HTML](devy.html).**

```js  {#toUpperCase .script .show}
const toUpperCase = (str) =&gt; str.toUpperCase();
```

A simple feature, which probably should be the default behavior in the future, is the
ability to copy the code block to the clipboard. The next code block is a simple example
of a function that adds two numbers together:

```js  {#add .script .show .copy}
const add = (a, b) =&gt; "Answer is " + (parseInt(a) + parseInt(b));
```

Line numbers are also an important feature(you need a little bit of css to make them look
good). Of course, we are not always limited to Javascript, so here's a Rust version of
the `add` function.

&lt;style&gt;
    .line-numbers {
        display: inline-block;
        margin-right: 10;
        padding: 0;
    }
&lt;/style&gt;

```rust  {#add-rs .show .linenumbers}
fn add(a: i32, b: i32) -&gt; i32 {
    a + b
}
```

That's all pretty cool, but nothing impressive. The fun starts when you can run
code snippets and use their results. That's where DCL comes into play. Below is
a short DCL snippet that uses the `add` function to add two numbers together.
The first two lines define the inputs and their initial values, and the third
line defines the output as a function of the result of adding the two inputs together.

````
```dcl {#add-example}
input1 : text-input := 5
input2 : text-input := 10
output : text-area := input1, input2 =&gt; add(input1, input2)
```
````

Devy compiles this DCL snippet into HTML and Javascript code that updates
the output whenever the inputs change as you can see below:

```dcl {#add-example}
input1 : text-input := 5
input2 : text-input := 10
output : text-area := input1, input2 =&gt; add(input1, input2)
```

Text inputs are not the only components available. Here's an example of a
radio button that asks a question and provides feedback based on the answer:


**Do you think Devy is a cool project?**

```dcl {#radio-example}
option : radio := yes, no, of course
feedback : paragraph := option =&gt; option === "of course" ? "Great job!" : "Incorrect! Try Again!"
```

&lt;details&gt;
  &lt;summary&gt;Click to see the CDL code for the question!&lt;/summary&gt;

````
```dcl {#radio-example}
option : radio := yes, no, of course
feedback : paragraph := option =&gt; option === "of course" ? "Great job!" : "Incorrect! Try Again!"
```
````

&lt;/details&gt;

Aside from interactivity, I also want to focus on easily creating diagrams
and other visualizations. For now, I started with 
the [Mermaid](https://mermaid.js.org) diagrams, which are simple to write
 and look great. Here's an example of a simple flowchart:


```mermaid {#mermaid-0}
graph LR
A[Second diagram] --&gt; B[Something]
B --&gt; C[Something]
C --&gt; D[Something]
A --&gt; D[Something]
```

One cool thing I added(which doesn't exist natively in Mermaid) is
animating the diagrams. Users can easily add a `rate` attribute to
the mermaid code block to control the animation speed. For example,
the following diagram animates at a rate of 1000ms:

```mermaid {#mermaid-1 rate=1000}
graph LR
A[Second diagram]
A[Second diagram] --&gt; B[Something]
B --&gt; C[Something]
C --&gt; D[Something]
A --&gt; D[Something]
```

The current animation system is pretty simple, but I plan to add (1) phase-based
animations where user can define the frame each element should appear, (2) control
mechanisms for animations such as dynamic speed control, and (3) layout preserving
animation where all elements do not destructively move around.

That concludes the current state of Devy. It's a brand new project, and there are
lots of features I want to add. If you have any ideas, please let me know by opening
an issue on the [GitHub repository](https://github.com/alpaylan/devy). I'm excited
to see where this project goes, and I hope you are too! Also, please leave a star
on the repository if you like the project!

**Repository Link:** [https://github.com/alpaylan/devy](https://github.com/alpaylan/devy)</code></pre>
