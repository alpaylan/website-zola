+++
title = "Learner’s Guide to Functional Programming#0: Sum Types, Booleans and Naturals in Javascript"
date = "2023-07-13"
[taxonomies]
tags = ['functional programming']
language = ["en"]
+++

<article class="h-entry">
 <section class="e-content" data-field="body">
  <section class="section section--body section--first section--last" name="3833">
   <div class="section-content">
    <div class="section-inner sectionLayout--insetColumn">
     <h3 class="graf graf--h3 graf--leading graf--title" id="b3ab" name="b3ab">
      Learner’s Guide to Functional Programming#1: Implementing Lists in JavaScript
     </h3>
     <p class="graf graf--p graf-after--h3" id="e891" name="e891">
      Although this article was written first, I suggest you read the prequel I read as background. Leaving the link below.
     </p>
     <div class="graf graf--mixtapeEmbed graf-after--p" id="a9d6" name="a9d6">
      <a class="markup--anchor markup--mixtapeEmbed-anchor" data-href="https://alpkeles99.medium.com/learners-guide-to-functional-programming-0-sum-types-booleans-and-naturals-in-javascript-d20a44ca808d" href="https://alpkeles99.medium.com/learners-guide-to-functional-programming-0-sum-types-booleans-and-naturals-in-javascript-d20a44ca808d" title="https://alpkeles99.medium.com/learners-guide-to-functional-programming-0-sum-types-booleans-and-naturals-in-javascript-d20a44ca808d">
       <strong class="markup--strong markup--mixtapeEmbed-strong">
        Learner’s Guide to Functional Programming#0: Sum Types, Booleans and Naturals in Javascript
       </strong>
       <br/>
       alpkeles99.medium.com
      </a>
      <a class="js-mixtapeImage mixtapeImage u-ignoreBlock" data-media-id="66a0a05c561ba009445d72b82cfbdb7c" data-thumbnail-img-id="1*rNub9K1VtRelmSjPVlWmvg.png" href="https://alpkeles99.medium.com/learners-guide-to-functional-programming-0-sum-types-booleans-and-naturals-in-javascript-d20a44ca808d" style="background-image: url(https://cdn-images-1.medium.com/fit/c/160/160/1*rNub9K1VtRelmSjPVlWmvg.png);">
      </a>
     </div>
     <p class="graf graf--p graf-after--mixtapeEmbed" id="f91c" name="f91c">
      There are many articles introducing functional programming. They mention immutability, first class functions, purity, recursion, and many other concepts with usually small examples of each one of them. In this series, I want to try a different way. We will implement functional data structures within using a very minimal subset of Javascript. No loops, no mutable variables, no builtins except primitive types.
     </p>
     <p class="graf graf--p graf-after--p" id="5571" name="5571">
      The first of these data structures is a list. A list is a very simple data structure, below is a simple definition of a list type in typescript.
     </p>
     <pre class="graf graf--pre graf-after--p graf--preV2" data-code-block-lang="typescript" data-code-block-mode="2" id="c870" name="c870" spellcheck="false"><span class="pre--content"><span class="hljs-keyword">type</span> <span class="hljs-title class_">List</span> = { <span class="hljs-attr">variant</span>: <span class="hljs-string">"nil"</span> } | { <span class="hljs-attr">variant</span>: <span class="hljs-string">"cons"</span>, <span class="hljs-attr">elem</span>: <span class="hljs-built_in">any</span>, <span class="hljs-attr">rest</span>: <span class="hljs-title class_">List</span> }</span></pre>
     <p class="graf graf--p graf-after--pre" id="5dd3" name="5dd3">
      Here, we either have a “nil” variant with no elements, and a “cons” variant with a en element, as well as the rest of the list. Before going into implementation details, let’s imagine how would such a list look like.
     </p>
     <figure class="graf graf--figure graf-after--p" id="1350" name="1350">
      <img class="graf-image" data-height="1993" data-image-id="1*irBBs3TmC-b_qyHBu179qw.png" data-is-featured="true" data-width="3415" src="https://cdn-images-1.medium.com/max/800/1*irBBs3TmC-b_qyHBu179qw.png"/>
      <figcaption class="imageCaption">
       Three lists with lengths 0, 1, and 2.
      </figcaption>
     </figure>
     <p class="graf graf--p graf-after--figure" id="f326" name="f326">
      Below are the same definitions in Javascript code.
     </p>
     <pre class="graf graf--pre graf-after--p graf--preV2" data-code-block-lang="javascript" data-code-block-mode="2" id="0e6d" name="0e6d" spellcheck="false"><span class="pre--content"><span class="hljs-keyword">const</span> emptyList = { <span class="hljs-attr">variant</span>: <span class="hljs-string">"nil"</span> }; \\ []<br><span class="hljs-keyword">const</span> singleElemList = { <span class="hljs-attr">variant</span>: <span class="hljs-string">"cons"</span>, <span class="hljs-attr">elem</span>: <span class="hljs-number">2</span>, <span class="hljs-attr">rest</span>: emptyList } \\ [<span class="hljs-number">1</span>]<br/><span class="hljs-keyword">const</span> twoElemList = {<br/>  { <span class="hljs-attr">variant</span>: <span class="hljs-string">"cons"</span>, <span class="hljs-attr">elem</span>: <span class="hljs-number">1</span>,<br/>  <span class="hljs-attr">rest</span>: { <span class="hljs-attr">variant</span>: <span class="hljs-string">"cons"</span>, <span class="hljs-attr">elem</span>: <span class="hljs-number">2</span>, <br/>  <span class="hljs-attr">rest</span>: emptyList }<br/>} <span class="hljs-comment">// [1, 2]</span></br></span></pre>
     <p class="graf graf--p graf-after--pre" id="caac" name="caac">
      We start from the first element with a
      <code class="markup--code markup--p-code">
       variant: "cons"
      </code>
      node, end we denote the end with a
      <code class="markup--code markup--p-code">
       variant: "nil"
      </code>
      node.
     </p>
     <p class="graf graf--p graf-after--p" id="d57c" name="d57c">
      Here, we will have two constructors, one per variant.
     </p>
     <pre class="graf graf--pre graf-after--p graf--preV2" data-code-block-lang="javascript" data-code-block-mode="2" id="3d5e" name="3d5e" spellcheck="false"><span class="pre--content"><span class="hljs-keyword">const</span> <span class="hljs-title function_">mkEmpty</span> = (<span class="hljs-params"></span>) =&gt; (<br/>    {<br/>        <span class="hljs-attr">variant</span>: <span class="hljs-string">"nil"</span><br/>    }<br/>)<br/><br/><span class="hljs-keyword">const</span> <span class="hljs-title function_">mkList</span> = (<span class="hljs-params">elem, rest</span>) =&gt; (<br/>    {<br/>        <span class="hljs-attr">variant</span>: <span class="hljs-string">"cons"</span>,<br/>        <span class="hljs-attr">elem</span>: elem,<br/>        <span class="hljs-attr">rest</span>: rest<br/>    }<br/>)</span></pre>
     <p class="graf graf--p graf-after--pre" id="2481" name="2481">
      If we want to make a list of only one item, we could easily compose them.
     </p>
     <pre class="graf graf--pre graf-after--p graf--preV2" data-code-block-lang="javascript" data-code-block-mode="1" id="10be" name="10be" spellcheck="false"><span class="pre--content"><span class="hljs-keyword">const</span> <span class="hljs-title function_">mkListFromElem</span> = (<span class="hljs-params">elem</span>) =&gt; (<br/>    <span class="hljs-title function_">mkList</span>(elem, <span class="hljs-title function_">mkEmpty</span>())<br/>)</span></pre>
     <p class="graf graf--p graf-after--pre" id="a0bb" name="a0bb">
      Implementing accessors is pretty straightforward.
     </p>
     <pre class="graf graf--pre graf-after--p graf--preV2" data-code-block-lang="javascript" data-code-block-mode="1" id="cde2" name="cde2" spellcheck="false"><span class="pre--content"><span class="hljs-keyword">const</span> <span class="hljs-title function_">isEmpty</span> = (<span class="hljs-params">list</span>) =&gt; (<br/>    list.<span class="hljs-property">variant</span> === <span class="hljs-string">"nil"</span><br/>)<br/><br/><br/><span class="hljs-comment">// Below, we introduce the list notation. ":" is the prepending operation.</span><br/><span class="hljs-comment">// (elem : rest) -&gt; elem</span><br/><span class="hljs-comment">// Get first element</span><br/><span class="hljs-keyword">const</span> <span class="hljs-title function_">head</span> = (<span class="hljs-params">list</span>) =&gt; (<br/>    list.<span class="hljs-property">elem</span><br/>)<br/><br/><span class="hljs-comment">// Get the rest of the list</span><br/><span class="hljs-comment">// (elem : rest) -&gt; rest</span><br/><span class="hljs-keyword">const</span> <span class="hljs-title function_">tail</span> = (<span class="hljs-params">list</span>) =&gt; (<br/>    list.<span class="hljs-property">rest</span><br/>)</span></pre>
     <p class="graf graf--p graf-after--pre" id="332c" name="332c">
      As we now have the basic building blocks at hand, we can start defining more complicated functions. The first is the length function.
     </p>
     <pre class="graf graf--pre graf-after--p graf--preV2" data-code-block-lang="javascript" data-code-block-mode="2" id="a6c5" name="a6c5" spellcheck="false"><span class="pre--content"><span class="hljs-comment">// length(elem:rest) = 1 + length(rest)</span><br/><span class="hljs-keyword">const</span> <span class="hljs-title function_">length</span> = (<span class="hljs-params">list</span>) =&gt; (<br/>    <span class="hljs-title function_">isEmpty</span>(list) ? <span class="hljs-number">0</span> : <span class="hljs-number">1</span> + <span class="hljs-title function_">length</span>(<span class="hljs-title function_">tail</span>(list))<br/>)</span></pre>
     <p class="graf graf--p graf-after--pre" id="91cb" name="91cb">
      The definition goes, is you have an empty list, that list has 0 length. For any other list, you can add one to the length of the rest of the list and return that.
     </p>
     <p class="graf graf--p graf-after--p" id="f333" name="f333">
      <code class="markup--code markup--p-code">
       length(list) = length([list.head]) + length([list.rest])
      </code>
      is the relation we are using for this function.
     </p>
     <p class="graf graf--p graf-after--p" id="4096" name="4096">
      Although we could continue implementing functions in ad hoc manners, now I will introduce you with Higher Order Functions map, filter and reduce. We will then use these functions as building blocks of more complex functions.
     </p>
     <pre class="graf graf--pre graf-after--p graf--preV2" data-code-block-lang="javascript" data-code-block-mode="2" id="fe98" name="fe98" spellcheck="false"><span class="pre--content"><span class="hljs-keyword">const</span> <span class="hljs-title function_">map</span> = (<span class="hljs-params">list, f</span>) =&gt; (<br/>    <span class="hljs-title function_">isEmpty</span>(list) ? <span class="hljs-title function_">mkEmpty</span>() : <span class="hljs-title function_">mkList</span>(<span class="hljs-title function_">f</span>(<span class="hljs-title function_">head</span>(list)), <span class="hljs-title function_">map</span>(<span class="hljs-title function_">tail</span>(list), f))<br/>)</span></pre>
     <p class="graf graf--p graf-after--pre" id="c5c8" name="c5c8">
      Map function applies a function
      <code class="markup--code markup--p-code">
       f
      </code>
      to all elements of a list. You can see that we are effectively recreating the list by computing
      <code class="markup--code markup--p-code">
       f
      </code>
      on
      <code class="markup--code markup--p-code">
       head(list)
      </code>
      and passing it to the
      <code class="markup--code markup--p-code">
       map(tail(list), f)
      </code>
      .
     </p>
     <pre class="graf graf--pre graf-after--p graf--preV2" data-code-block-lang="javascript" data-code-block-mode="2" id="2092" name="2092" spellcheck="false"><span class="pre--content"><span class="hljs-keyword">const</span> <span class="hljs-title function_">filter</span> = (<span class="hljs-params">list, p</span>) =&gt; (<br/>    <span class="hljs-title function_">isEmpty</span>(list) ?<br/>        <span class="hljs-title function_">mkEmpty</span>()<br/>        : <span class="hljs-title function_">f</span>(<span class="hljs-title function_">head</span>(list)) ?<br/>            <span class="hljs-title function_">mkList</span>(<span class="hljs-title function_">head</span>(list), <span class="hljs-title function_">filter</span>(<span class="hljs-title function_">tail</span>(list), p))<br/>            : <span class="hljs-title function_">filter</span>(<span class="hljs-title function_">tail</span>(list), p)<br/>)</span></pre>
     <p class="graf graf--p graf-after--pre" id="98f7" name="98f7">
      Filter takes a list, and a predicate
      <code class="markup--code markup--p-code">
       p
      </code>
      , a predicate is a type of function that returns a boolean. Filters create a list with the elements passing the predicate.
     </p>
     <pre class="graf graf--pre graf-after--p graf--preV2" data-code-block-lang="javascript" data-code-block-mode="2" id="00ad" name="00ad" spellcheck="false"><span class="pre--content"><span class="hljs-keyword">const</span> <span class="hljs-title function_">reduce</span> = (<span class="hljs-params">list, f, acc</span>) =&gt; (<br/>    <span class="hljs-title function_">isEmpty</span>(list) ? acc : <span class="hljs-title function_">reduce</span>(<span class="hljs-title function_">tail</span>(list), f, <span class="hljs-title function_">f</span>(acc, <span class="hljs-title function_">head</span>(list)))<br/>)</span></pre>
     <p class="graf graf--p graf-after--pre" id="5399" name="5399">
      Reduce is the last one of our building blocks. We use reduce to apply functions over the list by propagating the result. I usually find reduce the most confusing among these three, so let’s use reduce for some functions in order to allow a more comprehensive understanding.
     </p>
     <pre class="graf graf--pre graf-after--p graf--preV2" data-code-block-lang="javascript" data-code-block-mode="1" id="ec40" name="ec40" spellcheck="false"><span class="pre--content"><span class="hljs-comment">// Instead of recursively calling tail ourselves, we call reduce</span><br/><span class="hljs-comment">// with the initial value of 0, incremented for every node.</span><br/><span class="hljs-keyword">const</span> <span class="hljs-title function_">lenReduce</span> = (<span class="hljs-params">list, f</span>) =&gt; (<br/>    <span class="hljs-title function_">reduce</span>(list, <span class="hljs-function">(<span class="hljs-params">acc, elem</span>) =&gt;</span> acc + <span class="hljs-number">1</span>, <span class="hljs-number">0</span>)<br/>)<br/><br/><span class="hljs-comment">// Reverse initiates an empty list. At every point, we take the</span><br/><span class="hljs-comment">// head, prepend it to the accumulator.</span><br/><span class="hljs-keyword">const</span> <span class="hljs-title function_">reverse</span> = (<span class="hljs-params">list</span>) =&gt; (<br/>    <span class="hljs-title function_">reduce</span>(list, <span class="hljs-function">(<span class="hljs-params">acc, elem</span>) =&gt;</span> <span class="hljs-title function_">mkList</span>(elem, acc), <span class="hljs-title function_">mkEmpty</span>())<br/>)</span></pre>
     <p class="graf graf--p graf-after--pre" id="4861" name="4861">
      Another important building block is
      <code class="markup--code markup--p-code">
       concat
      </code>
      which allows us two concatenate two lists.
     </p>
     <pre class="graf graf--pre graf-after--p graf--preV2" data-code-block-lang="javascript" data-code-block-mode="2" id="1936" name="1936" spellcheck="false"><span class="pre--content"><span class="hljs-comment">// We will use ++ for concat notation.</span><br/><span class="hljs-comment">// concat(l1, l2) = l1 ++ l2</span><br/><br/><span class="hljs-comment">// If the first list is empty, we can just return the second list.</span><br/><span class="hljs-comment">// Otherwise, we concatenate the rest of the list with and prepend</span><br/><span class="hljs-comment">// the first element of the first list.</span><br/><span class="hljs-keyword">const</span> <span class="hljs-title function_">concat</span> = (<span class="hljs-params">list1, list2</span>) =&gt; (<br/>    <span class="hljs-title function_">isEmpty</span>(list1) ? <br/>        list2 <br/>        : <span class="hljs-title function_">mkList</span>(<span class="hljs-title function_">head</span>(list1), <span class="hljs-title function_">concat</span>(<span class="hljs-title function_">tail</span>(list1), list2))<br/>)</span></pre>
     <p class="graf graf--p graf-after--pre" id="b92c" name="b92c">
      As we have
      <code class="markup--code markup--p-code">
       concat
      </code>
      we can now define prepend and append.
     </p>
     <pre class="graf graf--pre graf-after--p graf--preV2" data-code-block-lang="javascript" data-code-block-mode="2" id="2a8f" name="2a8f" spellcheck="false"><span class="pre--content"><br/><span class="hljs-comment">// prepend(list, elem) = (elem : list)</span><br/><span class="hljs-keyword">const</span> <span class="hljs-title function_">prepend</span> = (<span class="hljs-params">list, elem</span>) =&gt; (<br/>    <span class="hljs-title function_">mkList</span>(elem, list)<br/>)<br/><br/><span class="hljs-comment">// append(list, elem) = list ++ [elem]</span><br/><span class="hljs-keyword">const</span> <span class="hljs-title function_">append</span> = (<span class="hljs-params">list, elem</span>) =&gt; (<br/>    <span class="hljs-title function_">concat</span>(list, <span class="hljs-title function_">mkListFromElem</span>(elem))<br/>)</span></pre>
     <p class="graf graf--p graf-after--pre" id="2777" name="2777">
      As you see, prepend is the same as
      <code class="markup--code markup--p-code">
       mkList
      </code>
      and
      <code class="markup--code markup--p-code">
       append
      </code>
      is equivalent to creating a one element list and concatenating it to the end.
     </p>
     <p class="graf graf--p graf-after--p" id="89fe" name="89fe">
      The last function we are implementing is the indexing function. Here, we pass the index parameter
      <code class="markup--code markup--p-code">
       n
      </code>
      and we decrease it as we move within the list.
     </p>
     <pre class="graf graf--pre graf-after--p graf--preV2" data-code-block-lang="javascript" data-code-block-mode="2" id="60e6" name="60e6" spellcheck="false"><span class="pre--content"><span class="hljs-comment">// nth((elem:rest), n) = nth(rest, n - 1)</span><br/><span class="hljs-keyword">const</span> <span class="hljs-title function_">nth</span> = (<span class="hljs-params">list, n</span>) =&gt; (<br/>    n === <span class="hljs-number">0</span> ? <span class="hljs-title function_">head</span>(list) : <span class="hljs-title function_">nth</span>(<span class="hljs-title function_">tail</span>(list), n - <span class="hljs-number">1</span>)<br/>)</span></pre>
     <p class="graf graf--p graf-after--pre" id="5d7e" name="5d7e">
      Below is the Github repository for the functions introduced within this article.
     </p>
     <div class="graf graf--mixtapeEmbed graf-after--p graf--trailing" id="3d91" name="3d91">
      <a class="markup--anchor markup--mixtapeEmbed-anchor" data-href="https://github.com/alpaylan/functional-ts/blob/main/List.ts" href="https://github.com/alpaylan/functional-ts/blob/main/List.ts" title="https://github.com/alpaylan/functional-ts/blob/main/List.ts">
       <strong class="markup--strong markup--mixtapeEmbed-strong">
        functional-ts/List.ts at main · alpaylan/functional-ts
       </strong>
       <br/>
       <em class="markup--em markup--mixtapeEmbed-em">
        Functional Data Structures in Typescript. Contribute to alpaylan/functional-ts development by creating an account on…
       </em>
       github.com
      </a>
      <a class="js-mixtapeImage mixtapeImage u-ignoreBlock" data-media-id="92f0723e5e9c5b92ed81aaf8cfac6ad1" data-thumbnail-img-id="0*Y2YP655OJeXvwVdi" href="https://github.com/alpaylan/functional-ts/blob/main/List.ts" style="background-image: url(https://cdn-images-1.medium.com/fit/c/160/160/0*Y2YP655OJeXvwVdi);">
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
   <a href="https://medium.com/p/8ec3946aa9ab">
    <time class="dt-published" datetime="2023-07-12T04:45:40.430Z">
     July 12, 2023
    </time>
   </a>
   .
  </p>
  <p>
   <a class="p-canonical" href="https://medium.com/@alpkeles99/learners-guide-to-functional-programming-1-implementing-lists-in-javascript-8ec3946aa9ab">
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
