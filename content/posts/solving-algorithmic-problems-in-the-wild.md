+++
title = "Solving Algorithmic Problems in The Wild"
date = "2024-03-06"
[taxonomies]
tags = ['algorithms']
language = ["en"]
+++

<article class="h-entry">
 <section class="e-content" data-field="body">
  <section class="section section--body section--first section--last" name="e446">
   <div class="section-content">
    <div class="section-inner sectionLayout--insetColumn">
     <h3 class="graf graf--h3 graf--leading graf--title" id="373a" name="373a">
      Solving Algorithmic Problems in The Wild
     </h3>
     <p class="graf graf--p graf-after--h3" id="a381" name="a381">
      For most software engineers, algorithmic problems are this bizarre type of problems that they only have to know in order to succeed in their interviews and get a job. Perhaps most readers will concede that they are sometimes useful, but I would imagine only a handful few studied solving algorithms outside of LeetCode or their college classes.
     </p>
     <p class="graf graf--p graf-after--p" id="516e" name="516e">
      The premise of this article is that the methods for solving your Algorithms homework or LeetCode mediums are ill-equipped to handle the algorithmic problems you will face as a software engineer, and I hope to provide you with a fresh technique I myself employ. To be fair to the reader, the two examples I talk about in the article are far from any reasonable definition of
      <strong class="markup--strong markup--p-strong">
       the Wild,
      </strong>
      but let’s bear with me for now!
     </p>
     <h3 class="graf graf--h3 graf-after--p" id="d0ee" name="d0ee">
      What is the problem with solving LeetCode?
     </h3>
     <p class="graf graf--p graf-after--h3" id="4be1" name="4be1">
      The problem is not that solving LeetCode problems is bad, per se, but how the platform is designed in getting you to solve questions.
     </p>
     <ol class="postList">
      <li class="graf graf--li graf-after--p" id="0868" name="0868">
       The set of inputs is fixed and limited. Our instincts urge us to submit the least good enough code that passes all the existing inputs without considering the problem in more depth.
      </li>
      <li class="graf graf--li graf-after--li" id="074f" name="074f">
       The feedback from the platform is imminent, the number of tests passing, leading to the fact that we tend to ignore any other forms of possible feedback in terms of correctness and performance.
      </li>
     </ol>
     <p class="graf graf--p graf-after--li" id="a64d" name="a64d">
      You might have realized that the two points have nearly identical indications, we need to understand what the problem is asking and the algorithm we design in more detail than LeetCode forces or sets us to do.
     </p>
     <p class="graf graf--p graf-after--p" id="d411" name="d411">
      Why? Because we don’t have such nice input-output examples in reality. The ones we have are called unit tests, which are impossible to write for any sufficiently complex algorithmic problem. Imagine you are implementing a new shortest path algorithm for graphs that has certain types of properties, how many graphs and input-output examples would you need to see to have a sufficiently solid belief on the correctness of your algorithm?
     </p>
     <p class="graf graf--p graf-after--p" id="64e7" name="64e7">
      If unit tests are insufficient, what can we do then? Well, there is the classic computer science approach of picking a pen and paper, writing down the invariants of the algorithms and an inductive proof; or you could just find
      <a class="markup--anchor markup--p-anchor" data-href="https://twitter.com/Keleesssss" href="https://twitter.com/Keleesssss" rel="noopener" target="_blank">
       a friend doing a Ph.D. in formal verification
      </a>
      to write your proofs for you. For the rest of this article, I’ll work on convincing you that coming up with some properties for your problem and writing random tests in the style of
      <a class="markup--anchor markup--p-anchor" data-href="https://en.wikipedia.org/wiki/QuickCheck" href="https://en.wikipedia.org/wiki/QuickCheck" rel="noopener" target="_blank">
       QuickCheck
      </a>
      is a better option.
     </p>
     <h3 class="graf graf--h3 graf-after--p" id="5753" name="5753">
      What the heck is a property?
     </h3>
     <p class="graf graf--p graf-after--h3" id="7113" name="7113">
      A property is a weird thing. In tutorials for property-based testing, you usually see properties like this.
     </p>
     <pre class="graf graf--pre graf-after--p graf--preV2" data-code-block-lang="cpp" data-code-block-mode="1" id="f2de" name="f2de" spellcheck="false"><span class="pre--content">list.<span class="hljs-built_in">reverse</span>().<span class="hljs-built_in">reverse</span>() == list<br/><span class="hljs-comment">// Reversing a list twice gives you the same list</span></span></pre>
     <pre class="graf graf--pre graf-after--pre graf--preV2" data-code-block-lang="go" data-code-block-mode="1" id="2b25" name="2b25" spellcheck="false"><span class="pre--content">list.<span class="hljs-built_in">append</span>(x).<span class="hljs-built_in">len</span>() == list.<span class="hljs-built_in">len</span>() + <span class="hljs-number">1</span><br/><span class="hljs-comment">// Adding an item to a list increases its length by one</span></span></pre>
     <pre class="graf graf--pre graf-after--pre graf--preV2" data-code-block-lang="scss" data-code-block-mode="1" id="5224" name="5224" spellcheck="false"><span class="pre--content"><span class="hljs-built_in">sorted</span>(list.sort())<br/><span class="hljs-comment">// Sorting a list means it's sorted.</span></span></pre>
     <p class="graf graf--p graf-after--pre" id="4a6d" name="4a6d">
      I’m sure these seem like no brainers to you,
      <em class="markup--em markup--p-em">
       what do you mean sorting a list means it’s sorted, what the hell was it gonna be?
      </em>
     </p>
     <p class="graf graf--p graf-after--p" id="dce2" name="dce2">
      The reality is different though. The
      <em class="markup--em markup--p-em">
       meaning
      </em>
      of the sorting function is that the output respects to some ordering
      <code class="markup--code markup--p-code">
       (sorted(list) == true)
      </code>
      . We have deeply embodied that meaning, so such examples are obvious, and might feel like a child’s toy. For algorithms, data structures, or code that is less studied, less familiar, it is possible that we never thought about the meaning of them.
     </p>
     <p class="graf graf--p graf-after--p" id="9ed8" name="9ed8">
      What are other types of properties?(there are perhaps more formal/correct names for these, please notify me if so)
     </p>
     <ul class="postList">
      <li class="graf graf--li graf-after--p" id="db46" name="db46">
       <strong class="markup--strong markup--li-strong">
        Modeling Property:
       </strong>
       The property that the results of our function is the same as another function. Perhaps we are writing a blazingly fast sorting function, and we want the result to be the same as the result of bubble sort.
      </li>
      <li class="graf graf--li graf-after--li" id="f088" name="f088">
       <strong class="markup--strong markup--li-strong">
        RoundTrip Property:
       </strong>
       Roundtrip properties are usually found in programs such as parsers or encoders. One example I previously used is
       <code class="markup--code markup--li-code">
        JSON.parse(JSON.stringify(object)) === object
       </code>
       . You can imagine we actually rely a lot on this property a lot while sending data over the wire.
      </li>
      <li class="graf graf--li graf-after--li" id="d7e4" name="d7e4">
       <strong class="markup--strong markup--li-strong">
        Effect Properties:
       </strong>
       Effect properties build the expectation that the result of some computation is a (simple)function of the input. When we don’t care about the way a computation is performed, but rather the effect of the computation on some state/variable, we use effect properties. All 3 examples I gave in the beginning are effect properties.
      </li>
     </ul>
     <h3 class="graf graf--h3 graf-after--li" id="ff68" name="ff68">
      Where does properties and algorithmic problems come together?
     </h3>
     <p class="graf graf--p graf-after--h3" id="d3fa" name="d3fa">
      As I said, LeetCode is all nice and good, but in reality, we have to define the correctness of our programs. Property-based tests with well-crafted properties provide more confidence in such correctness than unit tests. In the rest of the article, I will provide two examples of properties I came up with for my own problems.
     </p>
     <p class="graf graf--p graf-after--p" id="83b6" name="83b6">
      The first problem I will talk about is a familiar one, it’s actually a LeetCode medium in addition to being an elementary school problem,
      <code class="markup--code markup--p-code">
       pow(x, n)
      </code>
      .
     </p>
     <p class="graf graf--p graf-after--p" id="3bba" name="3bba">
      The problem, as you might have guessed, asks us to write a function that will give us the n’th power of x.
     </p>
     <p class="graf graf--p graf-after--p" id="efe9" name="efe9">
      A simple and intuitive solution might look like the one right below.
     </p>
     <pre class="graf graf--pre graf-after--p graf--preV2" data-code-block-lang="java" data-code-block-mode="2" id="e1ee" name="e1ee" spellcheck="false"><span class="pre--content"><span class="hljs-type">double</span> <span class="hljs-variable">result</span> <span class="hljs-operator">=</span> <span class="hljs-number">1</span>;<br/><span class="hljs-keyword">for</span> (<span class="hljs-type">int</span> <span class="hljs-variable">i</span> <span class="hljs-operator">=</span> <span class="hljs-number">0</span>; i &lt; n; i++) {<br/>    result *= x;<br/>}<br/><span class="hljs-keyword">return</span> result;</span></pre>
     <p class="graf graf--p graf-after--pre" id="bc21" name="bc21">
      The problem here, for the careless reader, is that for
      <code class="markup--code markup--p-code">
       n &lt; 0
      </code>
      , this code just returns 1. We can solve this problem by leveraging an algebraic identity,
      <code class="markup--code markup--p-code">
       x^-n = (1/x)^n
      </code>
      .
     </p>
     <pre class="graf graf--pre graf-after--p graf--preV2" data-code-block-lang="cpp" data-code-block-mode="1" id="f9e8" name="f9e8" spellcheck="false"><span class="pre--content"><span class="hljs-keyword">if</span> (n &lt; <span class="hljs-number">0</span>) {<br/>    x = <span class="hljs-number">1</span> / x;<br/>    n = -n;<br/>}<br/><span class="hljs-comment">// x^-n = (1/x)^n</span><br/><span class="hljs-type">double</span> result = <span class="hljs-number">1</span>;<br/><span class="hljs-keyword">for</span> (<span class="hljs-type">int</span> i = <span class="hljs-number">0</span>; i &lt; n; i++) {<br/>    result *= x;<br/>}<br/><span class="hljs-keyword">return</span> result;</span></pre>
     <p class="graf graf--p graf-after--pre" id="4917" name="4917">
      This code is indeed a bit slow. It is linear with n, meaning that it takes roughly n multiplications to get to the result. We can get better by using two more algebraic identities,
      <code class="markup--code markup--p-code">
       x^2n = (x^2)^n, x^2n+1 = x * x^2n
      </code>
      . As you might have realized, we just cut our work in half at each step, resulting in an exponential speed-up.
     </p>
     <pre class="graf graf--pre graf-after--p graf--preV2" data-code-block-lang="cpp" data-code-block-mode="1" id="a6a8" name="a6a8" spellcheck="false"><span class="pre--content"><span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-type">double</span> <span class="hljs-title">pow</span><span class="hljs-params">(<span class="hljs-type">double</span> x, <span class="hljs-type">int</span> n)</span> </span>{<br/>  <span class="hljs-keyword">if</span> (n == <span class="hljs-number">0</span>) {<br/>      <span class="hljs-keyword">return</span> <span class="hljs-number">1</span>;<br/>  }<br/>  <br/>  <span class="hljs-keyword">if</span> (n &lt; <span class="hljs-number">0</span>) {<br/>      x = <span class="hljs-number">1</span> / x;<br/>      n = -n;<br/>  }<br/>  <span class="hljs-keyword">if</span> (n % <span class="hljs-number">2</span> == <span class="hljs-number">0</span>) {<br/>      <span class="hljs-keyword">return</span> <span class="hljs-built_in">pow</span>(x * x, n / <span class="hljs-number">2</span>);<br/>  } <span class="hljs-keyword">else</span> {<br/>      <span class="hljs-keyword">return</span> x * <span class="hljs-built_in">pow</span>(x * x, n / <span class="hljs-number">2</span>);<br/>  }<br/>}</span></pre>
     <p class="graf graf--p graf-after--pre" id="0250" name="0250">
      How do we make sure that our code is correct, though? The first option is to use a
      <strong class="markup--strong markup--p-strong">
       Modeling Property.
      </strong>
      We can just compare our results with
      <code class="markup--code markup--p-code">
       Math.pow
      </code>
      from the Java standart library.
     </p>
     <pre class="graf graf--pre graf-after--p graf--preV2" data-code-block-lang="cpp" data-code-block-mode="1" id="c19a" name="c19a" spellcheck="false"><span class="pre--content"><span class="hljs-built_in">pow</span>(x, n) == Math.<span class="hljs-built_in">pow</span>(x, n)</span></pre>
     <p class="graf graf--p graf-after--pre" id="ce16" name="ce16">
      The second option is a less hacky one that actually relies on the
      <strong class="markup--strong markup--p-strong">
       meaning
      </strong>
      of the pow function.
     </p>
     <pre class="graf graf--pre graf-after--p graf--preV2" data-code-block-lang="cpp" data-code-block-mode="1" id="8108" name="8108" spellcheck="false"><span class="pre--content"><span class="hljs-built_in">pow</span>(x, n) * x = <span class="hljs-built_in">pow</span>(x, n + <span class="hljs-number">1</span>)</span></pre>
     <p class="graf graf--p graf-after--pre" id="4343" name="4343">
      We can just generate many (x, n) pairs, run our pow function for
      <code class="markup--code markup--p-code">
       pow(x,n)
      </code>
      and
      <code class="markup--code markup--p-code">
       pow(x, n+1)
      </code>
      separately, and check the results.
     </p>
     <p class="graf graf--p graf-after--p" id="2d75" name="2d75">
      One nice feature of using Randomized Property-Based Testing is that it allows for benchmarking our code pretty easily. So, in addition to getting correctness, we get to measure performance. As the inputs are sampled from a large space, timing the results allows for comparing different algorithms easily. Below is the
      <strong class="markup--strong markup--p-strong">
       Time vs N graph
      </strong>
      obtained by running 4 versions of the
      <code class="markup--code markup--p-code">
       pow
      </code>
      function I implemented, measured over randomized inputs. The purple line that looks like it’s completely flat is the logarithmic implementation.
     </p>
     <figure class="graf graf--figure graf-after--p" id="db35" name="db35">
      <img class="graf-image" data-height="1520" data-image-id="1*eUlw8qRLDOFf2mkw4sO2RQ.png" data-width="2876" src="https://cdn-images-1.medium.com/max/800/1*eUlw8qRLDOFf2mkw4sO2RQ.png"/>
     </figure>
     <h3 class="graf graf--h3 graf-after--figure" id="492c" name="492c">
      A More Realistic Example
     </h3>
     <p class="graf graf--p graf-after--h3" id="84cf" name="84cf">
      I can hear you saying, come oon, who writes pow these days??? So I come bearing good news, I have a better example.
     </p>
     <p class="graf graf--p graf-after--p" id="7913" name="7913">
      There is a board game called
      <a class="markup--anchor markup--p-anchor" data-href="https://en.wikipedia.org/wiki/Quoridor" href="https://en.wikipedia.org/wiki/Quoridor" rel="noopener" target="_blank">
       Quoridor
      </a>
      that I started playing recently, and I decided to implement a mobile version of it to play with some friends overseas. Creating a mobile application has many hassles, but the first thing you need to do is to create a model of the game. The game has 81 squares, 144 tile locations, 10 1x2 tiles per player, and 2 pawns. There are several rules governing how tiles can be placed and how pawns can move, but one specific rule is pretty interesting.
      <strong class="markup--strong markup--p-strong">
       When placing tiles, opposing player must have at least one path toward their target open, you cannot shut them out.
      </strong>
     </p>
     <p class="graf graf--p graf-after--p" id="fb68" name="fb68">
      This can be easily modeled as a
      <strong class="markup--strong markup--p-strong">
       Undirected Graph Reachability Problem
      </strong>
      . We can model the board as a 9x9 grid, where all adjacent squares have an undirected edge between them if there is no tile. If the pawn can reach any square in the first line of the opposing player after putting a new tile, then the move it valid. Below is a rough picture of the board, showing a path from the mid-top for the white pawn towards the left-bottom.
     </p>
     <figure class="graf graf--figure graf-after--p" id="5e64" name="5e64">
      <img class="graf-image" data-height="3280" data-image-id="1*H4Aq_Uz9WKwepWazxnHLYA.png" data-is-featured="true" data-width="3942" src="https://cdn-images-1.medium.com/max/800/1*H4Aq_Uz9WKwepWazxnHLYA.png"/>
     </figure>
     <p class="graf graf--p graf-after--figure" id="2c8e" name="2c8e">
      There are two ways of solving this problem. The first is constructing a graph out of the board and running an off the shelf reachability algorithm, the second is to implement a reachability algorithm on top of your own board, which is of course more fun(try to guess which one I decided to do).
     </p>
     <p class="graf graf--p graf-after--p" id="ac7a" name="ac7a">
      After implementing a DFS(Depth First Search), I was met with the question of how to verify the correctness of my algorithm, how do I know I’m not too permissive or too restrictive?
     </p>
     <p class="graf graf--p graf-after--p" id="32ba" name="32ba">
      I found two such properties.
     </p>
     <ol class="postList">
      <li class="graf graf--li graf-after--p" id="e542" name="e542">
       In the case of a permission, I ask for a witness(a path from the pawn to the target line). I follow through the line to make sure there are not tiles on the way.
      </li>
      <li class="graf graf--li graf-after--li" id="0b10" name="0b10">
       In the case of a restriction, things are more complicated. How can you guarantee there are no actual ways? I came up with an interesting solution to this one. I pick a point in the target line, I generate a random non-overlapping walk to the point, and I crush(remove) any tiles on the way, effectively generating at least one path. Running the algorithm again must give me a witness. This is of course a weak property, perhaps my random walks are not uncovering interesting paths that my code is not able to find. I am open to suggestions here!
      </li>
     </ol>
     <p class="graf graf--p graf-after--li" id="0697" name="0697">
      I like this because (1) it was directly useful to me in a personal project, (2) it was a case where testing the algorithm was actually pretty hard by hand, (3) the property I came up with was fun to think of.
     </p>
     <p class="graf graf--p graf-after--p" id="7bf2" name="7bf2">
      With this, I conclude my examples, and the article. As I said, I believe algorithms come up in many places around software projects, and they are hard to test and verify, especially if you’re not ready for it. I think Randomized Property Based Testing has a pretty good potential for both correctness and performance measurements, and it’s also really fun. If you like property based testing, you can check out my previous article.
     </p>
     <div class="graf graf--mixtapeEmbed graf-after--p graf--trailing" id="0846" name="0846">
      <a class="markup--anchor markup--mixtapeEmbed-anchor" data-href="https://medium.com/learning-from-learners/learners-guide-to-property-based-testing-1-ce979c1a58a1" href="https://medium.com/learning-from-learners/learners-guide-to-property-based-testing-1-ce979c1a58a1" title="https://medium.com/learning-from-learners/learners-guide-to-property-based-testing-1-ce979c1a58a1">
       <strong class="markup--strong markup--mixtapeEmbed-strong">
        Learner’s Guide to Property Based Testing#1
       </strong>
       <br/>
       <em class="markup--em markup--mixtapeEmbed-em">
        Property Based Random Testing is a flavor of testing that aims to use higher level specifications for testing instead…
       </em>
       medium.com
      </a>
      <a class="js-mixtapeImage mixtapeImage u-ignoreBlock" data-media-id="19a1af58cac5358feef1ed754df15c73" data-thumbnail-img-id="1*92Av2ZbXV98Ryo1C0cxpFw.png" href="https://medium.com/learning-from-learners/learners-guide-to-property-based-testing-1-ce979c1a58a1" style="background-image: url(https://cdn-images-1.medium.com/fit/c/160/160/1*92Av2ZbXV98Ryo1C0cxpFw.png);">
      </a>
     </div>
    </div>
   </div>
  </section>
 </section>
 <footer>
  <p>
   By
   <a class="p-author h-card" href="https://medium.com/@alpkeles99">
    Alperen Keleş
   </a>
   on
   <a href="https://medium.com/p/edf47daf3f88">
    <time class="dt-published" datetime="2024-03-07T04:20:18.356Z">
     March 7, 2024
    </time>
   </a>
   .
  </p>
  <p>
   <a class="p-canonical" href="https://medium.com/@alpkeles99/solving-algorithmic-problems-in-the-wild-edf47daf3f88">
    Canonical link
   </a>
  </p>
  <p>
   Exported from
   <a href="https://medium.com">
    Medium
   </a>
   on March 27, 2024.
  </p>
 </footer>
</article>
