+++
title = "Learner’s Guide to Dynamic Programming#1"
date = "2023-06-07"
[taxonomies]
tags = ['software engineering', 'algorithms']
language = ["en"]
+++

<article class="h-entry">
 <section class="e-content" data-field="body">
  <section class="section section--body section--first section--last" name="63f9">
   <div class="section-content">
    <div class="section-inner sectionLayout--insetColumn">
     <h3 class="graf graf--h3 graf--leading graf--title" id="8e5c" name="8e5c">
      Learner’s Guide to Dynamic Programming#1
     </h3>
     <p class="graf graf--p graf-after--h3" id="cb1a" name="cb1a">
      Dynamic programming is an algorithmic problem solving paradigm focused on recognization and elimination of repetitive computation. For this article, I’ll write a short introduction to dynamic programming, and move on to explaining how I try to look at dynamic programming problems.
     </p>
     <h3 class="graf graf--h3 graf-after--p" id="ad20" name="ad20">
      <strong class="markup--strong markup--h3-strong">
       Introduction to Dynamic Programming
      </strong>
     </h3>
     <p class="graf graf--p graf-after--h3" id="bcb5" name="bcb5">
      Dynamic programming rests on two simple properties of the algorithms and the problems it works on.
     </p>
     <p class="graf graf--p graf-after--p" id="5f87" name="5f87">
      Firstly, a problem needs to have
      <strong class="markup--strong markup--p-strong">
       optimal substructure property
      </strong>
      , namely the property that it is possible to use results of an algorithm for a substructure to compute the results of an algorithm for the whole structure. Let’s demistify this a bit.
     </p>
     <p class="graf graf--p graf-after--p" id="2fad" name="2fad">
      Let us look an implementation of array sum algorithm. One would write is as given below in Python in the iterative way.
     </p>
     <pre class="graf graf--pre graf-after--p graf--preV2" data-code-block-lang="python" data-code-block-mode="2" id="9944" name="9944" spellcheck="false"><span class="pre--content"><span class="hljs-keyword">def</span> <span class="hljs-title function_">sum</span>(<span class="hljs-params">array</span>):<br/>  res = <span class="hljs-number">0</span><br/>  <span class="hljs-keyword">for</span> i <span class="hljs-keyword">in</span> array:<br/>    res += i<br/>  <span class="hljs-keyword">return</span> i</span></pre>
     <p class="graf graf--p graf-after--pre" id="7e74" name="7e74">
      If we instead took the functional way to write it, it could look as below.
     </p>
     <pre class="graf graf--pre graf-after--p graf--preV2" data-code-block-lang="python" data-code-block-mode="2" id="e0f2" name="e0f2" spellcheck="false"><span class="pre--content"><span class="hljs-keyword">def</span> <span class="hljs-title function_">sum</span>(<span class="hljs-params">array</span>):<br/>  <span class="hljs-keyword">if</span> array == []:<br/>    <span class="hljs-keyword">return</span> <span class="hljs-number">0</span><br/>  <span class="hljs-keyword">return</span> array[<span class="hljs-number">0</span>] + <span class="hljs-built_in">sum</span>(array[<span class="hljs-number">1</span>:])</span></pre>
     <p class="graf graf--p graf-after--pre" id="d485" name="d485">
      Even though this looks like a simple change, it’s actually a fundamentally different solution. In the iterative version, if we were to try to put it in natural language, would basically say “Start with 0, add each element to the result, at the end of the array we will have all of them added to the result” while the second one would say “Empty array has a sum of 0, for any non-empty array, we can take the first element and the result of summing the rest, and just add those.
     </p>
     <p class="graf graf--p graf-after--p" id="90d5" name="90d5">
      So, if we have a list of items [3, 2, 7, 6], the first algorithm would sum it as
     </p>
     <pre class="graf graf--pre graf-after--p graf--preV2" data-code-block-lang="scss" data-code-block-mode="1" id="25ac" name="25ac" spellcheck="false"><span class="pre--content">((((<span class="hljs-number">0</span> + <span class="hljs-number">3</span>) + <span class="hljs-number">2</span>) + <span class="hljs-number">7</span>) + <span class="hljs-number">6</span>)</span></pre>
     <p class="graf graf--p graf-after--pre" id="ae27" name="ae27">
      Whereas the second algorithm would sum it as
     </p>
     <pre class="graf graf--pre graf-after--p graf--preV2" data-code-block-lang="scss" data-code-block-mode="1" id="53b3" name="53b3" spellcheck="false"><span class="pre--content">(<span class="hljs-number">3</span> + (<span class="hljs-number">2</span> + (<span class="hljs-number">7</span> + (<span class="hljs-number">6</span> + <span class="hljs-number">0</span>))))</span></pre>
     <p class="graf graf--p graf-after--pre" id="44c9" name="44c9">
      The real difference between them is, the second one explicitly relies on
      <strong class="markup--strong markup--p-strong">
       optimal substructure property
      </strong>
      . It follows the statement that we can just add the current number with the sum of the rest and the sum of the current array. I believe this line of thinking, especially for memoization-based dynamic programming becomes very important.
     </p>
     <p class="graf graf--p graf-after--p" id="5da9" name="5da9">
      The second property dynamic programming relies on is
      <strong class="markup--strong markup--p-strong">
       overlapping subproblems property
      </strong>
      . This property states that we do not use the results of the subproblems once, we do it many times, which means it makes sense to store those results and reuse them as needed. Let’s clarify further.
     </p>
     <p class="graf graf--p graf-after--p" id="7d56" name="7d56">
      In the
      <code class="markup--code markup--p-code">
       sum
      </code>
      example, it doesn’t make sense to use dynamic programming, simply because each value is computed exactly once. So, what would be an case where we have
      <strong class="markup--strong markup--p-strong">
       overlapping subproblems
      </strong>
      ? The canonical example is the fibonacci numbers.
     </p>
     <p class="graf graf--p graf-after--p" id="c969" name="c969">
      We all know and love fibonacci numbers,
      <code class="markup--code markup--p-code">
       f(n) = f(n-1) + f(n-2)
      </code>
      . When we write the paranthesis based computation tree, we will see something very interesting.
     </p>
     <pre class="graf graf--pre graf-after--p graf--preV2" data-code-block-lang="scss" data-code-block-mode="1" id="aa4e" name="aa4e" spellcheck="false"><span class="pre--content"><span class="hljs-built_in">f</span>(<span class="hljs-number">5</span>) = <span class="hljs-built_in">f</span>(<span class="hljs-number">4</span>) + <span class="hljs-built_in">f</span>(<span class="hljs-number">3</span>)<br/><span class="hljs-built_in">f</span>(<span class="hljs-number">4</span>) = <span class="hljs-built_in">f</span>(<span class="hljs-number">3</span>) + <span class="hljs-built_in">f</span>(<span class="hljs-number">2</span>)<br/><span class="hljs-built_in">f</span>(<span class="hljs-number">3</span>) = <span class="hljs-built_in">f</span>(<span class="hljs-number">2</span>) + <span class="hljs-built_in">f</span>(<span class="hljs-number">1</span>)<br/><span class="hljs-built_in">f</span>(<span class="hljs-number">2</span>) = <span class="hljs-number">1</span>, <span class="hljs-built_in">f</span>(<span class="hljs-number">1</span>) = <span class="hljs-number">1</span><br/><br/><span class="hljs-built_in">f</span>(<span class="hljs-number">5</span>) = (((<span class="hljs-number">1</span> + <span class="hljs-number">1</span>) + <span class="hljs-number">1</span>) + (<span class="hljs-number">1</span> + <span class="hljs-number">1</span>))</span></pre>
     <p class="graf graf--p graf-after--pre" id="36fb" name="36fb">
      One should realize that we compute f(3) = (1+1) twice, one for computing f(4), one for computing f(5). This is the
      <strong class="markup--strong markup--p-strong">
       overlapping subproblems property
      </strong>
      . When we are computing the same substructures repeatedly, and the substructures preserve the optimality, we can use dynamic programming.
     </p>
     <h3 class="graf graf--h3 graf-after--p" id="26bd" name="26bd">
      Some Personal Insights
     </h3>
     <p class="graf graf--p graf-after--h3" id="d521" name="d521">
      I think one particularly interesting/important realization I had in my own perspective to these problems is that the recursive paradigm for solving problems allows one to easily discover the overlapping subproblems. In my early years of working with algorithms problems, I would try to find ad hoc algorithms that could solve some cases I would come up with. Now, I start with small examples(recursion base cases), look for optimal substructures(recursive cases), look for overlapping substructures(function calls to be cached/memoized). I’ll apply this line of thinking for 3Sum problem.
     </p>
     <h4 class="graf graf--h4 graf-after--p" id="57d8" name="57d8">
      3Sum
     </h4>
     <p class="graf graf--p graf-after--h4" id="c04e" name="c04e">
      <strong class="markup--strong markup--p-strong">
       Problem Statement:
      </strong>
      Given an array and a number, return all triples that add up to the number.
     </p>
     <p class="graf graf--p graf-after--p" id="7851" name="7851">
      <strong class="markup--strong markup--p-strong">
       Small examples:
      </strong>
      If I have an array with 3 elements, then all I can do is check if they are equal to the number. If I have an array of 4 elements, I can do 2 things. (1) I can just take the sum of the first 3 elements, or I can take the last element with any two elements from the first 3 elements.
     </p>
     <p class="graf graf--p graf-after--p" id="a126" name="a126">
      <strong class="markup--strong markup--p-strong">
       Optimal Substructure:
      </strong>
      The small example gives me a perspective. For each element, there are two cases. Either the element is in the sum, or it is not. So, we look at 2 cases for each element; (1) Ask for the 3Sum of the rest of the array, (2) ask for all 2Sum’s of the rest of the array, check if adding my element to them results in the asked number.
     </p>
     <p class="graf graf--p graf-after--p" id="eb0c" name="eb0c">
      <strong class="markup--strong markup--p-strong">
       Overlapping Substructure:
      </strong>
      As I would realize if I tried to compute a length-5 array, this solution requires me to recompute 2Sum’s for the array each time I want to compute a 3Sum. Let’s write it similar to Fibonacci numbers.
     </p>
     <pre class="graf graf--pre graf-after--p graf--preV2" data-code-block-lang="python" data-code-block-mode="1" id="4d5d" name="4d5d" spellcheck="false"><span class="pre--content">3<span class="hljs-built_in">sum</span>([<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>, <span class="hljs-number">4</span>, <span class="hljs-number">5</span>], <span class="hljs-number">6</span>) = 3<span class="hljs-built_in">sum</span>([<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>, <span class="hljs-number">4</span>], <span class="hljs-number">6</span>) ++ 2sums([<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>, <span class="hljs-number">4</span>])<br/>3<span class="hljs-built_in">sum</span>([<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>, <span class="hljs-number">4</span>], <span class="hljs-number">6</span>) = 3<span class="hljs-built_in">sum</span>([<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>], <span class="hljs-number">6</span>) ++ 2sums([<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>])<br/><br/>Whereas<br/><br/>2sums([<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>, <span class="hljs-number">4</span>]) = 2sums([<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>]) * <span class="hljs-number">3</span></span></pre>
     <p class="graf graf--p graf-after--pre" id="0089" name="0089">
      Instead of the actual functions, I have written the number of steps associated with each computation, but the realization should be that we are computing
      <code class="markup--code markup--p-code">
       2sums([1, 2, 3])
      </code>
      twice, one for computing
      <code class="markup--code markup--p-code">
       3sum([1, 2, 3, 4], 6)
      </code>
      and one for computing
      <code class="markup--code markup--p-code">
       2sums([1, 2, 3, 4])
      </code>
      , and in fact that’s a property of
      <code class="markup--code markup--p-code">
       2sums
      </code>
      . Any array that computes its 2sum always computes 2sums’s of all of its subsets.
     </p>
     <p class="graf graf--p graf-after--p" id="2019" name="2019">
      Upon this realization, we will simply precompute 2sum and relieve ourselves of the responsibility of computing it every single time. Below is the actual code we would write for those who would like to test it by hand.
     </p>
     <pre class="graf graf--pre graf-after--p graf--preV2" data-code-block-lang="python" data-code-block-mode="2" id="85c5" name="85c5" spellcheck="false"><span class="pre--content"><span class="hljs-keyword">def</span> <span class="hljs-title function_">two_sums</span>(<span class="hljs-params">arr: <span class="hljs-built_in">list</span>[<span class="hljs-built_in">int</span>]</span>) -&gt; <span class="hljs-built_in">dict</span>[<span class="hljs-built_in">int</span>, <span class="hljs-built_in">tuple</span>[<span class="hljs-built_in">int</span>, <span class="hljs-built_in">int</span>]]:<br/>    <span class="hljs-string">"""<br/>    Returns a dictionary of all the two sums in the array<br/>    """</span><br/>    two_sum_dict = {}<br/>    <span class="hljs-keyword">for</span> i <span class="hljs-keyword">in</span> <span class="hljs-built_in">range</span>(<span class="hljs-built_in">len</span>(arr)):<br/>        <span class="hljs-keyword">for</span> j <span class="hljs-keyword">in</span> <span class="hljs-built_in">range</span>(i + <span class="hljs-number">1</span>, <span class="hljs-built_in">len</span>(arr)):<br/>            <span class="hljs-keyword">if</span> arr[i] + arr[j] <span class="hljs-keyword">not</span> <span class="hljs-keyword">in</span> two_sum_dict:<br/>                two_sum_dict[arr[i] + arr[j]] = [(arr[i], arr[j])]<br/>            <span class="hljs-keyword">else</span>:<br/>                two_sum_dict[arr[i] + arr[j]].append((arr[i], arr[j]))<br/>    <span class="hljs-keyword">return</span> two_sum_dict<br/><br/><span class="hljs-keyword">def</span> <span class="hljs-title function_">three_sum</span>(<span class="hljs-params">arr: <span class="hljs-built_in">list</span>[<span class="hljs-built_in">int</span>], <span class="hljs-built_in">sum</span>: <span class="hljs-built_in">int</span></span>) -&gt; <span class="hljs-built_in">list</span>[<span class="hljs-built_in">int</span>]:<br/>    <span class="hljs-keyword">if</span> <span class="hljs-built_in">len</span>(arr) &lt; <span class="hljs-number">3</span>:<br/>        <span class="hljs-keyword">return</span> []<br/><br/>    <span class="hljs-comment"># Compute 3sum for the first part.</span><br/>    c1 = three_sum(arr[:-<span class="hljs-number">1</span>], <span class="hljs-built_in">sum</span>)<br/>    <br/>    <span class="hljs-comment"># Compute 2sum for the first part</span><br/>    two_sum = two_sums(arr[:-<span class="hljs-number">1</span>])<br/><br/>    <span class="hljs-comment"># Check for all the pairs of numbers in the first part that conforms</span><br/>    <span class="hljs-comment"># to the given sum. </span><br/>    c2 = <span class="hljs-built_in">list</span>(<span class="hljs-built_in">map</span>(<span class="hljs-keyword">lambda</span> t: (t[<span class="hljs-number">0</span>], t[<span class="hljs-number">1</span>], arr[-<span class="hljs-number">1</span>]), two_sum.get(<span class="hljs-built_in">sum</span> - arr[-<span class="hljs-number">1</span>], [])))<br/><br/>    <span class="hljs-comment"># Merge two solutions</span><br/>    <span class="hljs-keyword">return</span> c1 + c2</span></pre>
     <p class="graf graf--p graf-after--pre" id="40e8" name="40e8">
      The cached version is somewhat trickier and not as neat as the version I provide above.
     </p>
     <pre class="graf graf--pre graf-after--p graf--preV2" data-code-block-lang="python" data-code-block-mode="2" id="546e" name="546e" spellcheck="false"><span class="pre--content"><span class="hljs-keyword">def</span> <span class="hljs-title function_">three_sum_cached</span>(<span class="hljs-params">arr: <span class="hljs-built_in">list</span>[<span class="hljs-built_in">int</span>], <span class="hljs-built_in">sum</span>: <span class="hljs-built_in">int</span>, two_sums: <span class="hljs-built_in">dict</span>[<span class="hljs-built_in">int</span>, <span class="hljs-built_in">tuple</span>[<span class="hljs-built_in">int</span>, <span class="hljs-built_in">int</span>]]</span>) -&gt; <span class="hljs-built_in">list</span>[<span class="hljs-built_in">int</span>]:<br/>    <span class="hljs-keyword">if</span> <span class="hljs-built_in">len</span>(arr) &lt; <span class="hljs-number">3</span>:<br/>        <span class="hljs-keyword">return</span> []<br/><br/>    <span class="hljs-comment"># Same function call with the original version</span><br/>    c1 = three_sum_cached(arr[:-<span class="hljs-number">1</span>], <span class="hljs-built_in">sum</span>, two_sums)<br/><br/>    <span class="hljs-comment"># Instead of the function call, we lookup from the precomputed dictionary</span><br/>    matching_two_sums = two_sums.get(<span class="hljs-built_in">sum</span> - arr[-<span class="hljs-number">1</span>], [])<br/><br/>    <span class="hljs-comment"># This is to prevent using the same number twice</span><br/>    filtered_two_sums = <span class="hljs-built_in">list</span>(<span class="hljs-built_in">filter</span>(<span class="hljs-keyword">lambda</span> t: t[<span class="hljs-number">0</span>] != arr[-<span class="hljs-number">1</span>] <span class="hljs-keyword">and</span> t[<span class="hljs-number">1</span>] != arr[-<span class="hljs-number">1</span>], matching_two_sums))<br/><br/>    c2 = <span class="hljs-built_in">list</span>(<span class="hljs-built_in">map</span>(<span class="hljs-keyword">lambda</span> t: (t[<span class="hljs-number">0</span>], t[<span class="hljs-number">1</span>], arr[-<span class="hljs-number">1</span>]), filtered_two_sums))<br/>    <span class="hljs-comment"># This is to prevent using the same triplets twice.</span><br/>    <span class="hljs-comment"># For example, we delete (1, 4, 3) and only leave (1, 3, 4)</span><br/>    filtered_c2 = <span class="hljs-built_in">list</span>(<span class="hljs-built_in">filter</span>(<span class="hljs-keyword">lambda</span> t: t[<span class="hljs-number">0</span>] &lt; t[<span class="hljs-number">1</span>] &lt; t[<span class="hljs-number">2</span>], c2))<br/><br/>    <span class="hljs-keyword">return</span> c1 + filtered_c2</span></pre>
     <p class="graf graf--p graf-after--pre" id="edc1" name="edc1">
      The second algorithm is somewhat crude, but that’s probably on me. I bet there are better ways of implementing the caching.
     </p>
     <p class="graf graf--p graf-after--p" id="fa23" name="fa23">
      <strong class="markup--strong markup--p-strong">
       Complexity: O(n²)(The time to compute the 2sums)
      </strong>
     </p>
     <p class="graf graf--p graf-after--p" id="adbf" name="adbf">
      Visually, while the original looks similar to this:
     </p>
     <figure class="graf graf--figure graf-after--p" id="6e24" name="6e24">
      <img class="graf-image" data-height="2304" data-image-id="1*uPxMi97vZ0vYqjGNHOTcFw.png" data-is-featured="true" data-width="4707" src="https://cdn-images-1.medium.com/max/800/1*uPxMi97vZ0vYqjGNHOTcFw.png"/>
     </figure>
     <p class="graf graf--p graf-after--figure" id="48b1" name="48b1">
      The cached implementation is similar to this:
     </p>
     <figure class="graf graf--figure graf-after--p" id="8a66" name="8a66">
      <img class="graf-image" data-height="2221" data-image-id="1*V92DTDFgYacxG3fP0Le-TQ.png" data-width="4527" src="https://cdn-images-1.medium.com/max/800/1*V92DTDFgYacxG3fP0Le-TQ.png"/>
     </figure>
     <p class="graf graf--p graf-after--figure" id="166a" name="166a">
      2Sum part is kind of cheating as I’ve not written that part of the algorithm recursively, so it’s more similar to this:
     </p>
     <figure class="graf graf--figure graf-after--p" id="3430" name="3430">
      <img class="graf-image" data-height="2679" data-image-id="1*Xhsmpc1uswA_Mn5ifl8trw.png" data-width="5439" src="https://cdn-images-1.medium.com/max/800/1*Xhsmpc1uswA_Mn5ifl8trw.png"/>
     </figure>
     <p class="graf graf--p graf-after--figure" id="1f6c" name="1f6c">
      Where 2Sums is the data structure that allows querying for tuples for a given amount in constant time.
     </p>
     <h3 class="graf graf--h3 graf-after--p" id="354e" name="354e">
      Conclusion
     </h3>
     <p class="graf graf--p graf-after--h3 graf--trailing" id="e4ca" name="e4ca">
      In this article, I tried to convey my method/perspective on solving algorithmic problems using dynamic programming. My methodology rests on first creating a naive recursive solution for a problem with optimal substructures, identifying overlapping substructures and caching/memoizing those function calls. Hope it’s useful!
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
   <a href="https://medium.com/p/f520a5b2ba4b">
    <time class="dt-published" datetime="2023-06-07T04:47:12.361Z">
     June 7, 2023
    </time>
   </a>
   .
  </p>
  <p>
   <a class="p-canonical" href="https://medium.com/@alpkeles99/learners-guide-to-dynamic-programming-1-f520a5b2ba4b">
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
