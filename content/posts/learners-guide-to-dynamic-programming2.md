+++
title = "Learner’s Guide to Dynamic Programming#2"
date = "2023-06-10"
[taxonomies]
tags = ['software engineering', 'algorithms']
language = ["en"]
+++

<article class="h-entry">
 <section class="e-content" data-field="body">
  <section class="section section--body section--first section--last" name="28ef">
   <div class="section-content">
    <div class="section-inner sectionLayout--insetColumn">
     <h3 class="graf graf--h3 graf--leading graf--title" id="a989" name="a989">
      Learner’s Guide to Dynamic Programming#2
     </h3>
     <p class="graf graf--p graf-after--h3" id="d7d3" name="d7d3">
      Dynamic programming is an algorithmic problem solving paradigm focused on recognization and elimination of repetitive computation. Earlier this week, I had another article introducing dynamic programming and a perspective I found useful. I’m leaving a link for that below.
     </p>
     <div class="graf graf--mixtapeEmbed graf-after--p" id="b3c0" name="b3c0">
      <a class="markup--anchor markup--mixtapeEmbed-anchor" data-href="https://medium.com/learning-from-learners/learners-guide-to-dynamic-programming-1-f520a5b2ba4b" href="https://medium.com/learning-from-learners/learners-guide-to-dynamic-programming-1-f520a5b2ba4b" title="https://medium.com/learning-from-learners/learners-guide-to-dynamic-programming-1-f520a5b2ba4b">
       <strong class="markup--strong markup--mixtapeEmbed-strong">
        Learner’s Guide to Dynamic Programming#1
       </strong>
       <br/>
       <em class="markup--em markup--mixtapeEmbed-em">
        Dynamic programming is an algorithmic problem solving paradigm focused on recognization and elimination of repetitive…
       </em>
       medium.com
      </a>
      <a class="js-mixtapeImage mixtapeImage u-ignoreBlock" data-media-id="55d6be621f25383557007b51a7b44998" data-thumbnail-img-id="1*uPxMi97vZ0vYqjGNHOTcFw.png" href="https://medium.com/learning-from-learners/learners-guide-to-dynamic-programming-1-f520a5b2ba4b" style="background-image: url(https://cdn-images-1.medium.com/fit/c/160/160/1*uPxMi97vZ0vYqjGNHOTcFw.png);">
      </a>
     </div>
     <p class="graf graf--p graf-after--mixtapeEmbed" id="0cd6" name="0cd6">
      In this second article, I will focus on a different example, Wildcard Matching.
     </p>
     <h3 class="graf graf--h3 graf-after--p" id="f2af" name="f2af">
      Problem Statement
     </h3>
     <p class="graf graf--p graf-after--h3" id="bedd" name="bedd">
      Given an input string (
      <code class="markup--code markup--p-code">
       s
      </code>
      ) and a pattern (
      <code class="markup--code markup--p-code">
       p
      </code>
      ), implement wildcard pattern matching with support for
      <code class="markup--code markup--p-code">
       '?'
      </code>
      and
      <code class="markup--code markup--p-code">
       '*'
      </code>
      where:
     </p>
     <ul class="postList">
      <li class="graf graf--li graf-after--p" id="634e" name="634e">
       <code class="markup--code markup--li-code">
        '?'
       </code>
       Matches any single character.
      </li>
      <li class="graf graf--li graf-after--li" id="fa43" name="fa43">
       <code class="markup--code markup--li-code">
        '*'
       </code>
       Matches any sequence of characters (including the empty sequence).
      </li>
     </ul>
     <p class="graf graf--p graf-after--li" id="f63a" name="f63a">
      The matching should cover the
      <strong class="markup--strong markup--p-strong">
       entire
      </strong>
      input string (not partial).
     </p>
     <h3 class="graf graf--h3 graf-after--p" id="918f" name="918f">
      Solution
     </h3>
     <p class="graf graf--p graf-after--h3" id="ee37" name="ee37">
      Again, we should start with small examples.
     </p>
     <p class="graf graf--p graf-after--p" id="f09a" name="f09a">
      <strong class="markup--strong markup--p-strong">
       isMatch(“”, “”)
      </strong>
      = True =&gt; Empty pattern matches empty string.
     </p>
     <p class="graf graf--p graf-after--p" id="5326" name="5326">
      <strong class="markup--strong markup--p-strong">
       isMatch(“”, “a”)
      </strong>
      = False =&gt; A letter pattern cannot match empty string.
     </p>
     <p class="graf graf--p graf-after--p" id="034b" name="034b">
      <strong class="markup--strong markup--p-strong">
       isMatch(“”, “?”)
      </strong>
      = False =&gt; A single matcher pattern cannot match empty string.
     </p>
     <p class="graf graf--p graf-after--p" id="11c9" name="11c9">
      <strong class="markup--strong markup--p-strong">
       isMatch(“”, “*”)
      </strong>
      = True =&gt; A wildcard matcher pattern can match empty string.
     </p>
     <p class="graf graf--p graf-after--p" id="12f3" name="12f3">
      <strong class="markup--strong markup--p-strong">
       isMatch(“a”, “”)
      </strong>
      = False =&gt; Empty pattern cannot match a non-empty string.
     </p>
     <p class="graf graf--p graf-after--p" id="f51c" name="f51c">
      So, we are actually finished with small examples. As I will show you in a minute, we can reduce any pattern to these patterns by recognizing a set of simple relations.
     </p>
     <p class="graf graf--p graf-after--p" id="084e" name="084e">
      <strong class="markup--strong markup--p-strong">
       isMatch(“a__”, “a__”) or isMatch(“a__”, “?__”)
      </strong>
      = isMatch(“__”, “__”) =&gt; When a letter pattern or a single matcher matches the first character of the string, we can consume both characters and control the rest of S and P.
     </p>
     <p class="graf graf--p graf-after--p" id="5fe1" name="5fe1">
      This last one is the real deal. What happens when we meet a wildcard pattern?
     </p>
     <p class="graf graf--p graf-after--p" id="205f" name="205f">
      <strong class="markup--strong markup--p-strong">
       isMatch(“a__”, “*__”)
      </strong>
      has 3 possibilities.
     </p>
     <ol class="postList">
      <li class="graf graf--li graf--startsWithDoubleQuote graf-after--p" id="0953" name="0953">
       “*” matches exactly one character. So, both characters are consumed.
      </li>
     </ol>
     <p class="graf graf--p graf-after--li" id="6180" name="6180">
      <strong class="markup--strong markup--p-strong">
       isMatch(“a__”, “*__”) = isMatch(“__”, “__”)
      </strong>
     </p>
     <p class="graf graf--p graf-after--p" id="67fc" name="67fc">
      2. “*” matches zero characters. So, only “*” is consumed.
     </p>
     <p class="graf graf--p graf-after--p" id="3c8d" name="3c8d">
      <strong class="markup--strong markup--p-strong">
       isMatch(“a__”, “*__”) = isMatch(“a__”, “__”)
      </strong>
     </p>
     <p class="graf graf--p graf-after--p" id="54a1" name="54a1">
      3. “*” matches one or more characters. So, only “a” is consumed.
     </p>
     <p class="graf graf--p graf-after--p" id="2371" name="2371">
      <strong class="markup--strong markup--p-strong">
       isMatch(“a__”, “*__”) = isMatch(“__”, “*__”)
      </strong>
     </p>
     <p class="graf graf--p graf-after--p" id="43a2" name="43a2">
      Let’s put a visual representation.
     </p>
     <p class="graf graf--p graf-after--p" id="7fa5" name="7fa5">
      Below is the matcher tree for “aaa” and “*?a”.
     </p>
     <figure class="graf graf--figure graf-after--p" id="ca84" name="ca84">
      <img class="graf-image" data-height="1208" data-image-id="1*qqdeoTUmJ0nU9hPUeJikzw.png" data-width="3326" src="https://cdn-images-1.medium.com/max/800/1*qqdeoTUmJ0nU9hPUeJikzw.png"/>
      <figcaption class="imageCaption">
       <strong class="markup--strong markup--figure-strong">
        isMatch(aaa, *?a) = isMatch(aa, ?a) or isMatch(aaa, ?a) or isMatch(aa, *?a)
       </strong>
      </figcaption>
     </figure>
     <p class="graf graf--p graf-after--figure" id="ce8f" name="ce8f">
      Respectively, below are the matcher trees for these 3 child nodes.
     </p>
    </div>
    <div class="section-inner sectionLayout--outsetRow" data-paragraph-count="3">
     <figure class="graf graf--figure graf--layoutOutsetRow is-partialWidth graf-after--p" id="11f4" name="11f4" style="width: 19.138%;">
      <img class="graf-image" data-height="1134" data-image-id="1*zdJhv2YmLb2aAWrfSCNe9g.png" data-width="902" src="https://cdn-images-1.medium.com/max/400/1*zdJhv2YmLb2aAWrfSCNe9g.png"/>
     </figure>
     <figure class="graf graf--figure graf--layoutOutsetRowContinue is-partialWidth graf-after--figure" id="d45a" name="d45a" style="width: 18.416%;">
      <img class="graf-image" data-height="1148" data-image-id="1*E0YMLyzxrSYy5fmhsfpx9w.png" data-width="878" src="https://cdn-images-1.medium.com/max/400/1*E0YMLyzxrSYy5fmhsfpx9w.png"/>
     </figure>
     <figure class="graf graf--figure graf--layoutOutsetRowContinue is-partialWidth graf-after--figure" id="5811" name="5811" style="width: 62.446%;">
      <img class="graf-image" data-height="1135" data-image-id="1*mgcrgMzqFy3V1WnZaW2Hhw.png" data-width="2944" src="https://cdn-images-1.medium.com/max/800/1*mgcrgMzqFy3V1WnZaW2Hhw.png"/>
      <figcaption class="imageCaption" style="width: 160.138%; left: -60.138%;">
       <strong class="markup--strong markup--figure-strong">
        isMatch(aa, ?a) = isMatch(a, a) ||| isMatch(aaa, ?a) = isMatch(aa, a) ||| isMatch(aa, *?a) = isMatch(a, ?a) or isMatch(aa, ?a) or isMatch(a, *?a)
       </strong>
      </figcaption>
     </figure>
    </div>
    <div class="section-inner sectionLayout--insetColumn">
     <p class="graf graf--p graf-after--figure" id="09a5" name="09a5">
      You should now realize that I started coloring the nodes that appear more than once in distinct colors. So, even at this second step, we have a duplicate node, the blue
      <strong class="markup--strong markup--p-strong">
       isMatch(aa, ?a).
      </strong>
     </p>
     <p class="graf graf--p graf-after--p" id="58f2" name="58f2">
      At this point, the visual representation allows us to reach a similar conclusion even within this picture. Each “*” leads to an exponential growth in the number of computational steps, as it creates 3 separate branches.
     </p>
     <figure class="graf graf--figure graf-after--p" id="6189" name="6189">
      <img class="graf-image" data-height="3757" data-image-id="1*aaZ_QwKL688B1qJulyQtsQ.png" data-is-featured="true" data-width="7648" src="https://cdn-images-1.medium.com/max/800/1*aaZ_QwKL688B1qJulyQtsQ.png"/>
      <figcaption class="imageCaption">
       The whole matcher tree of isMatch(aaa, *?a). Same colored nodes are duplicates.
      </figcaption>
     </figure>
     <p class="graf graf--p graf-after--figure" id="a588" name="a588">
      The green nodes are the isMatch(“”, “”) nodes, reaching such a node means that we actually reached a match.
     </p>
     <p class="graf graf--p graf-after--p" id="7460" name="7460">
      Even within this small example with only one “*” node, we can see 5 duplicates. So, can we actually compute the number of steps? In the general case, probably no. I’ll give you the numbers for a specific set of cases though.
     </p>
     <p class="graf graf--p graf-after--p" id="6a08" name="6a08">
      Let’s examine
      <strong class="markup--strong markup--p-strong">
       isMatch(a…a, *…*)
      </strong>
      for different lengths of “a” and “*”. Below, I have written two numbers, the first one is the number of calls to
      <strong class="markup--strong markup--p-strong">
       isMatch(“”, “”)
      </strong>
      , and the second is the number of all function calls for that query.
     </p>
     <pre class="graf graf--pre graf-after--p graf--preV2" data-code-block-lang="css" data-code-block-mode="2" id="9a9b" name="9a9b" spellcheck="false"><span class="pre--content">isMatch(<span class="hljs-selector-tag">a</span>, *): <span class="hljs-number">2</span>, <span class="hljs-number">5</span><br><span class="hljs-built_in">isMatch</span>(a, **): <span class="hljs-number">4</span>, <span class="hljs-number">11</span><br/><span class="hljs-built_in">isMatch</span>(a, ***): <span class="hljs-number">6</span>, <span class="hljs-number">19</span><br/><span class="hljs-built_in">isMatch</span>(a, ****): <span class="hljs-number">8</span>, <span class="hljs-number">29</span><br/><span class="hljs-built_in">isMatch</span>(a, *****): <span class="hljs-number">10</span>, <span class="hljs-number">41</span><br/><span class="hljs-built_in">isMatch</span>(aa, *): <span class="hljs-number">2</span>, <span class="hljs-number">8</span><br/><span class="hljs-built_in">isMatch</span>(aa, **): <span class="hljs-number">8</span>, <span class="hljs-number">25</span><br/><span class="hljs-built_in">isMatch</span>(aa, ***): <span class="hljs-number">18</span>, <span class="hljs-number">56</span><br/><span class="hljs-built_in">isMatch</span>(aa, ****): <span class="hljs-number">32</span>, <span class="hljs-number">105</span><br/><span class="hljs-built_in">isMatch</span>(aa, *****): <span class="hljs-number">50</span>, <span class="hljs-number">176</span><br/><span class="hljs-built_in">isMatch</span>(aaa, *): <span class="hljs-number">2</span>, <span class="hljs-number">11</span><br/><span class="hljs-built_in">isMatch</span>(aaa, **): <span class="hljs-number">12</span>, <span class="hljs-number">45</span><br/><span class="hljs-built_in">isMatch</span>(aaa, ***): <span class="hljs-number">38</span>, <span class="hljs-number">127</span><br/><span class="hljs-built_in">isMatch</span>(aaa, ****): <span class="hljs-number">88</span>, <span class="hljs-number">289</span><br/><span class="hljs-built_in">isMatch</span>(aaa, *****): <span class="hljs-number">170</span>, <span class="hljs-number">571</span><br/><span class="hljs-built_in">isMatch</span>(aaaa, *): <span class="hljs-number">2</span>, <span class="hljs-number">14</span><br/><span class="hljs-built_in">isMatch</span>(aaaa, **): <span class="hljs-number">16</span>, <span class="hljs-number">71</span><br/><span class="hljs-built_in">isMatch</span>(aaaa, ***): <span class="hljs-number">66</span>, <span class="hljs-number">244</span><br/><span class="hljs-built_in">isMatch</span>(aaaa, ****): <span class="hljs-number">192</span>, <span class="hljs-number">661</span><br/><span class="hljs-built_in">isMatch</span>(aaaa, *****): <span class="hljs-number">450</span>, <span class="hljs-number">1522</span><br/><span class="hljs-built_in">isMatch</span>(aaaaa, *): <span class="hljs-number">2</span>, <span class="hljs-number">17</span><br/><span class="hljs-built_in">isMatch</span>(aaaaa, **): <span class="hljs-number">20</span>, <span class="hljs-number">103</span><br/><span class="hljs-built_in">isMatch</span>(aaaaa, ***): <span class="hljs-number">102</span>, <span class="hljs-number">419</span><br/><span class="hljs-built_in">isMatch</span>(aaaaa, ****): <span class="hljs-number">360</span>, <span class="hljs-number">1325</span><br/><span class="hljs-built_in">isMatch</span>(aaaaa, *****): <span class="hljs-number">1002</span>, <span class="hljs-number">3509</span><br/><br/>Some big <span class="hljs-built_in">examples</span>(these do not have the total number)<br/><br/><span class="hljs-built_in">isMatch</span>(aaaaaaaaaa, **********): <span class="hljs-number">4780008</span><br/><span class="hljs-built_in">isMatch</span>(aaaaaaaaaa, ***********): <span class="hljs-number">11414898</span><br/><span class="hljs-built_in">isMatch</span>(aaaaaaaaaa, ************): <span class="hljs-number">25534368</span><br/><span class="hljs-built_in">isMatch</span>(aaaaaaaaaa, *************): <span class="hljs-number">53972178</span><br/><span class="hljs-built_in">isMatch</span>(aaaaaaaaaa, **************): <span class="hljs-number">108568488</span><br/><span class="hljs-built_in">isMatch</span>(aaaaaaaaaaa, **********): <span class="hljs-number">10377180</span><br/><span class="hljs-built_in">isMatch</span>(aaaaaaaaaaa, ***********): <span class="hljs-number">26572086</span><br/><span class="hljs-built_in">isMatch</span>(aaaaaaaaaaa, ************): <span class="hljs-number">63521352</span><br/><span class="hljs-built_in">isMatch</span>(aaaaaaaaaaa, *************): <span class="hljs-number">143027898</span><br/><span class="hljs-built_in">isMatch</span>(aaaaaaaaaaa, **************): <span class="hljs-number">305568564</span><br/><span class="hljs-built_in">isMatch</span>(aaaaaaaaaaaa, **********): <span class="hljs-number">21278640</span><br/><span class="hljs-built_in">isMatch</span>(aaaaaaaaaaaa, ***********): <span class="hljs-number">58227906</span><br/><span class="hljs-built_in">isMatch</span>(aaaaaaaaaaaa, ************): <span class="hljs-number">148321344</span><br/><span class="hljs-built_in">isMatch</span>(aaaaaaaaaaaa, *************): <span class="hljs-number">354870594</span><br/><span class="hljs-built_in">isMatch</span>(aaaaaaaaaaaa, **************): <span class="hljs-number">803467056</span><br/><span class="hljs-built_in">isMatch</span>(aaaaaaaaaaaaa, **********): <span class="hljs-number">41517060</span><br/><span class="hljs-built_in">isMatch</span>(aaaaaaaaaaaaa, ***********): <span class="hljs-number">121023606</span><br/><span class="hljs-built_in">isMatch</span>(aaaaaaaaaaaaa, ************): <span class="hljs-number">327572856</span><br/><span class="hljs-built_in">isMatch</span>(aaaaaaaaaaaaa, *************): <span class="hljs-number">830764794</span><br/><span class="hljs-built_in">isMatch</span>(aaaaaaaaaaaaa, **************): <span class="hljs-number">1989102444</span></br></span></pre>
     <p class="graf graf--p graf-after--pre" id="fd7e" name="fd7e">
      I have tried to uncover some deep function running in the back, but I wasn’t able to find any mathematical equations. If anyone is, I would love to hear your results. But it is clear that length has a multiplicative effect and quickly gets very large.
     </p>
     <p class="graf graf--p graf-after--p" id="11ea" name="11ea">
      Of course, this number by itself is not very meaningful as
      <strong class="markup--strong markup--p-strong">
       isMatch(“”, “”)
      </strong>
      is actually cheaper than the memoization call, but I think it gives an intuition on the number of duplicate computations. So, how do we memorize this? I have implemented a very simple cache in the code below.
     </p>
     <pre class="graf graf--pre graf-after--p graf--preV2" data-code-block-lang="python" data-code-block-mode="2" id="daeb" name="daeb" spellcheck="false"><span class="pre--content"><span class="hljs-comment"># Call counter for the measurements in this articc</span><br/>call_counts = {}<br/><span class="hljs-comment"># Call cacher </span><br/>calls = {}<br/><br/><span class="hljs-keyword">def</span> <span class="hljs-title function_">isMatch</span>(<span class="hljs-params">s: <span class="hljs-built_in">str</span>, p: <span class="hljs-built_in">str</span></span>) -&gt; <span class="hljs-built_in">bool</span>:<br/>    <span class="hljs-comment">## Caching Parts</span><br/><br/>    <span class="hljs-comment"># Call counter</span><br/>    <span class="hljs-keyword">if</span> (s, p) <span class="hljs-keyword">in</span> call_counts:<br/>        call_counts[(s, p)] += <span class="hljs-number">1</span><br/>    <span class="hljs-keyword">else</span>:<br/>        call_counts[(s, p)] = <span class="hljs-number">1</span><br/><br/>    <span class="hljs-comment"># Memoization</span><br/>    <span class="hljs-keyword">if</span> (s, p) <span class="hljs-keyword">in</span> calls:<br/>        <span class="hljs-keyword">return</span> calls[(s, p)]<br/><br/>    <span class="hljs-comment">## Base cases</span><br/><br/>    <span class="hljs-comment"># When both are consumed, it's a match</span><br/>    <span class="hljs-keyword">if</span> <span class="hljs-built_in">len</span>(s) == <span class="hljs-number">0</span> <span class="hljs-keyword">and</span> <span class="hljs-built_in">len</span>(p) == <span class="hljs-number">0</span>:<br/>        calls[(s, p)] = <span class="hljs-literal">True</span><br/>        <span class="hljs-keyword">return</span> <span class="hljs-literal">True</span><br/>    <br/>    <span class="hljs-comment"># When pattern is consumed, it's not a match</span><br/>    <span class="hljs-keyword">if</span> <span class="hljs-built_in">len</span>(p) == <span class="hljs-number">0</span>:<br/>        calls[(s, p)] = <span class="hljs-literal">False</span><br/>        <span class="hljs-keyword">return</span> <span class="hljs-literal">False</span><br/>    <br/>    <span class="hljs-comment"># When string is consumed, it's a match if the rest of the pattern is all '*'</span><br/>    <span class="hljs-keyword">if</span> <span class="hljs-built_in">len</span>(s) == <span class="hljs-number">0</span>:<br/>        <span class="hljs-keyword">return</span> p[<span class="hljs-number">0</span>] == <span class="hljs-string">'*'</span> <span class="hljs-keyword">and</span> isMatch(s, p[<span class="hljs-number">1</span>:])<br/>    <br/>    <span class="hljs-comment">## Recursive cases</span><br/><br/>    <span class="hljs-comment"># Consume both if they match</span><br/>    <span class="hljs-comment"># a___ &lt;&gt; a___</span><br/>    <span class="hljs-keyword">if</span> s[<span class="hljs-number">0</span>] == p[<span class="hljs-number">0</span>]:<br/>        <span class="hljs-keyword">return</span> isMatch(s[<span class="hljs-number">1</span>:], p[<span class="hljs-number">1</span>:])<br/>    <br/>    <span class="hljs-comment"># Consume both if pattern is '?'</span><br/>    <span class="hljs-comment"># a___ &lt;&gt; ?___</span><br/>    <span class="hljs-keyword">if</span> p[<span class="hljs-number">0</span>] == <span class="hljs-string">'?'</span>:<br/>        <span class="hljs-keyword">return</span> isMatch(s[<span class="hljs-number">1</span>:], p[<span class="hljs-number">1</span>:])<br/>    <br/>    <span class="hljs-comment"># There are 3 cases for '*'</span><br/>    <span class="hljs-comment"># a___ &lt;&gt; *___</span><br/>    <span class="hljs-keyword">if</span> p[<span class="hljs-number">0</span>] == <span class="hljs-string">'*'</span>:<br/>        <span class="hljs-comment"># 1. Consume both: so that '*' matches 1 character</span><br/>        c1 = isMatch(s[<span class="hljs-number">1</span>:], p[<span class="hljs-number">1</span>:])<br/>        <span class="hljs-comment"># 2. Consume string, but not pattern: so that '*' matches 1 or more characters</span><br/>        c2 = isMatch(s[<span class="hljs-number">1</span>:], p)<br/>        <span class="hljs-comment"># 3. Consume pattern, but not string: so that '*' matches 0 characters</span><br/>        c3 = isMatch(s, p[<span class="hljs-number">1</span>:])<br/>        <span class="hljs-keyword">return</span> c1 <span class="hljs-keyword">or</span> c2 <span class="hljs-keyword">or</span> c3<br/><br/>    calls[(s, p)] = <span class="hljs-literal">False</span><br/>    <span class="hljs-keyword">return</span> <span class="hljs-literal">False</span><br/><br/><span class="hljs-built_in">print</span>(isMatch(<span class="hljs-string">'aa'</span>, <span class="hljs-string">'a'</span>)) <span class="hljs-comment"># False</span><br/><span class="hljs-built_in">print</span>(isMatch(<span class="hljs-string">'aa'</span>, <span class="hljs-string">'*'</span>)) <span class="hljs-comment"># True</span><br/><span class="hljs-built_in">print</span>(isMatch(<span class="hljs-string">'cb'</span>, <span class="hljs-string">'?a'</span>)) <span class="hljs-comment"># False</span><br/><span class="hljs-built_in">print</span>(isMatch(<span class="hljs-string">'adceb'</span>, <span class="hljs-string">'*a*b'</span>)) <span class="hljs-comment"># True</span><br/><span class="hljs-built_in">print</span>(isMatch(<span class="hljs-string">'acdcb'</span>, <span class="hljs-string">'a*c?b'</span>)) <span class="hljs-comment"># False</span><br/><span class="hljs-built_in">print</span>(isMatch(<span class="hljs-string">'adceb'</span>, <span class="hljs-string">'*a*b*'</span>)) <span class="hljs-comment"># True</span></span></pre>
     <p class="graf graf--p graf-after--pre" id="64e6" name="64e6">
      This memoization is kind of hacky, in the sense that you would not able to copy-paste this code into leetcode, but it’s certainly adaptable. Instead of using the strings for the cacher, it’s easy to use the indexes, which in turn means you don’t actually need a map, but rather just a simple 2d array that allows O(1)(constant) indexing.
     </p>
     <h3 class="graf graf--h3 graf-after--p" id="d2ef" name="d2ef">
      Conclusion
     </h3>
     <p class="graf graf--p graf-after--h3 graf--trailing" id="9f97" name="9f97">
      I like this problem better than the 3sum problem in the first article, as it allows a much more principled way of memoization. The fact that 3sum depended on calls to 2sum was a bit crude and maybe harder to internalize. But isMatch depending entirely on itself allows one to see the call tree much better. If you have any other problems you want solved in different articles, let me know!
     </p>
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
   <a href="https://medium.com/p/36cebb419d56">
    <time class="dt-published" datetime="2023-06-10T21:07:08.681Z">
     June 10, 2023
    </time>
   </a>
   .
  </p>
  <p>
   <a class="p-canonical" href="https://medium.com/@alpkeles99/learners-guide-to-dynamic-programming-2-36cebb419d56">
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
