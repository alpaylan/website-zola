+++
title = "Introduction to Property Based Testing"
date = "2023-03-14"
[taxonomies]
tags = ['testing']
language = ["en"]
+++

<h1 id="introduction-to-property-based-testing">
 Introduction to Property Based Testing
</h1>
<p>
 Property Based Random Testing is a flavor of testing that aims to use higher level specifications for testing instead
    of hand-writing or generating tests. It was first developed by Koen Claessen and John Hughes in 1999 as a software
    library for Haskell, called QuickCheck. There has been substantial development in the field since then, I will not
    bore you with lots of details as the purpose of this writing is to familiarize you with PBT(Property Based Testing).
</p>
<p>
 To give a sense of what is happening, let’s first start by talking about Unit Tests.
</p>
<p>
 A Unit Test is a test case aimed into testing a unit of a program, conventionally a function.
</p>
<div class="sourceCode" id="cb1">
 <pre class="sourceCode python"><code data-code-block-lang="python"><span id="cb1-1"><a aria-hidden="true" href="#cb1-1" tabindex="-1"></a><span class="kw">def</span> sort_test_1():</span>
<span id="cb1-2"><a aria-hidden="true" href="#cb1-2" tabindex="-1"></a>    l <span class="op">=</span> [<span class="dv">2</span>, <span class="dv">1</span>, <span class="dv">3</span>, <span class="dv">4</span>]</span>
<span id="cb1-3"><a aria-hidden="true" href="#cb1-3" tabindex="-1"></a>    sorted_l <span class="op">=</span> dummy_sort(l)</span>
<span id="cb1-4"><a aria-hidden="true" href="#cb1-4" tabindex="-1"></a>    <span class="cf">assert</span> sorted_l <span class="op">==</span> [<span class="dv">1</span>, <span class="dv">2</span>, <span class="dv">3</span>, <span class="dv">4</span>]</span></code></pre>
</div>
<p>
 Above, you see a very simple test case for a function called dummy sort, which from the name and the structure it
    feels is supposed to sort a given function of possibly integers in ascending order.
</p>
<p>
 But, this test case doesn’t actually give us very much knowledge on the function under test. It gives us a few clues
    we could perhaps generalize such as;
</p>
<ol type="1">
 <li>
  Function sorts the list [2, 1, 3, 4] correctly
 </li>
 <li>
  (1) could imply that the function sorts all lists of length 4 correctly.
 </li>
 <li>
  (1) also could imply that the function sorts all lists of integer permutations from 1 up to n.
 </li>
 <li>
  (1) also could imply that the function sorts all lists of all lengths containing positive integers.
 </li>
 <li>
  (1) also could imply this function sorts any type of list containing arbitrary integers in arbitrary length.
 </li>
</ol>
<p>
 We might be expecting any one of the properties from (1–4), but a better possibility is that we are expecting 5. We
    could also expect properties 1–4, but the example also wouldn’t generalize to those, at least those other than
    property (1).
</p>
<p>
 So ideally, we would need to create a set of examples that could represent the set of all cases we want our function
    to work on, so we need a way of defining this representative.
</p>
<p>
 This is possible via creating what we will call properties in our code. Let me demonstrate with an example.
</p>
<div class="sourceCode" id="cb2">
 <pre class="sourceCode python"><code class="sourceCode python"><span id="cb2-1"><a aria-hidden="true" href="#cb2-1" tabindex="-1"></a><span class="kw">def</span> sort_test_prop_1():</span>
<span id="cb2-2"><a aria-hidden="true" href="#cb2-2" tabindex="-1"></a>    l <span class="op">=</span> [<span class="dv">2</span>, <span class="dv">1</span>, <span class="dv">3</span>, <span class="dv">4</span>]</span>
<span id="cb2-3"><a aria-hidden="true" href="#cb2-3" tabindex="-1"></a>    sorted_l <span class="op">=</span> dummy_sort(l)</span>
<span id="cb2-4"><a aria-hidden="true" href="#cb2-4" tabindex="-1"></a>    <span class="cf">assert</span> is_sorted(sorted_l)</span>
<span id="cb2-5"><a aria-hidden="true" href="#cb2-5" tabindex="-1"></a></span>
<span id="cb2-6"><a aria-hidden="true" href="#cb2-6" tabindex="-1"></a><span class="kw">def</span> is_sorted(candidate_list):</span>
<span id="cb2-7"><a aria-hidden="true" href="#cb2-7" tabindex="-1"></a>    <span class="cf">if</span> <span class="bu">len</span>(candidate_list) <span class="op">==</span> <span class="dv">0</span>:</span>
<span id="cb2-8"><a aria-hidden="true" href="#cb2-8" tabindex="-1"></a>        <span class="cf">return</span> <span class="va">True</span></span>
<span id="cb2-9"><a aria-hidden="true" href="#cb2-9" tabindex="-1"></a>    pivot <span class="op">=</span> candidate_list[<span class="dv">0</span>]</span>
<span id="cb2-10"><a aria-hidden="true" href="#cb2-10" tabindex="-1"></a>    <span class="cf">for</span> item <span class="kw">in</span> candidate_list:</span>
<span id="cb2-11"><a aria-hidden="true" href="#cb2-11" tabindex="-1"></a>        <span class="cf">if</span> pivot <span class="op">&gt;</span> item:</span>
<span id="cb2-12"><a aria-hidden="true" href="#cb2-12" tabindex="-1"></a>            <span class="cf">return</span> <span class="va">False</span></span>
<span id="cb2-13"><a aria-hidden="true" href="#cb2-13" tabindex="-1"></a>        <span class="cf">else</span>:</span>
<span id="cb2-14"><a aria-hidden="true" href="#cb2-14" tabindex="-1"></a>            pivot <span class="op">=</span> item</span>
<span id="cb2-15"><a aria-hidden="true" href="#cb2-15" tabindex="-1"></a>    <span class="cf">return</span> <span class="va">True</span></span></code></pre>
</div>
<p>
 Function is_sorted checks if the list is monotonically increasing, meaning if no element is less than the element
    right before. As a logical statement, we can write is_sorted as
</p>
<p>
 If you look carefully, you will see that this property that we wrote actually does not cover our needs. Suppose we
    have an implementation of dummy_sort as given below.
</p>
<div class="sourceCode" id="cb3">
 <pre class="sourceCode python"><code class="sourceCode python"><span id="cb3-1"><a aria-hidden="true" href="#cb3-1" tabindex="-1"></a><span class="kw">def</span> dummy_sort(l):</span>
<span id="cb3-2"><a aria-hidden="true" href="#cb3-2" tabindex="-1"></a>    <span class="cf">return</span> []</span></code></pre>
</div>
<p>
 You will see that this means dummy_sort will always give a sorted list back to you, just not the one you would want.
</p>
<p>
 So a better property could be writing the test as.
</p>
<div class="sourceCode" id="cb4">
 <pre class="sourceCode python"><code class="sourceCode python"><span id="cb4-1"><a aria-hidden="true" href="#cb4-1" tabindex="-1"></a><span class="kw">def</span> sort_test_prop_2():</span>
<span id="cb4-2"><a aria-hidden="true" href="#cb4-2" tabindex="-1"></a>    l <span class="op">=</span> [<span class="dv">2</span>, <span class="dv">1</span>, <span class="dv">3</span>, <span class="dv">4</span>]</span>
<span id="cb4-3"><a aria-hidden="true" href="#cb4-3" tabindex="-1"></a>    sorted_l <span class="op">=</span> dummy_sort(l)</span>
<span id="cb4-4"><a aria-hidden="true" href="#cb4-4" tabindex="-1"></a>    <span class="cf">assert</span> is_sorted(sorted_l) <span class="kw">and</span> elements_same(l, sorted_l)</span>
<span id="cb4-5"><a aria-hidden="true" href="#cb4-5" tabindex="-1"></a></span>
<span id="cb4-6"><a aria-hidden="true" href="#cb4-6" tabindex="-1"></a><span class="kw">def</span> elements_same(l1, l2):</span>
<span id="cb4-7"><a aria-hidden="true" href="#cb4-7" tabindex="-1"></a>    <span class="cf">return</span> <span class="bu">set</span>(l1) <span class="op">==</span> <span class="bu">set</span>(l2)</span></code></pre>
</div>
<p>
 We just added a new check that looks if both lists have the same elements. Which would mean that if l contains an
    element that sorted_l does not contain, then our function does not do the right thing.
</p>
<p>
 Yet, a careful reader will also realize the problem with this property. We can falsify it with the test case given
    below.We just added a new check that looks if both lists have the same elements. Which would mean that if l contains
    an element that sorted_l does not contain, then our function does not do the right thing.
</p>
<p>
 Yet, a careful reader will also realize the problem with this property. We can falsify it with the test case given
    below.
</p>
<div class="sourceCode" id="cb5">
 <pre class="sourceCode python"><code class="sourceCode python"><span id="cb5-1"><a aria-hidden="true" href="#cb5-1" tabindex="-1"></a><span class="kw">def</span> sort_test_prop_3():</span>
<span id="cb5-2"><a aria-hidden="true" href="#cb5-2" tabindex="-1"></a>    l <span class="op">=</span> [<span class="dv">2</span>, <span class="dv">2</span>, <span class="dv">1</span>, <span class="dv">3</span>, <span class="dv">4</span>]</span>
<span id="cb5-3"><a aria-hidden="true" href="#cb5-3" tabindex="-1"></a>    sorted_l <span class="op">=</span> dummy_sort(l)</span>
<span id="cb5-4"><a aria-hidden="true" href="#cb5-4" tabindex="-1"></a>    <span class="cf">assert</span> is_sorted(sorted_l) <span class="kw">and</span> elements_same(l, sorted_l)</span>
<span id="cb5-5"><a aria-hidden="true" href="#cb5-5" tabindex="-1"></a></span>
<span id="cb5-6"><a aria-hidden="true" href="#cb5-6" tabindex="-1"></a><span class="kw">def</span> dummy_sort():</span>
<span id="cb5-7"><a aria-hidden="true" href="#cb5-7" tabindex="-1"></a>    <span class="cf">return</span> [<span class="dv">1</span>, <span class="dv">2</span>, <span class="dv">3</span>, <span class="dv">4</span>]</span></code></pre>
</div>
<p>
 As one familiar with Python’s set data structure will see, a set will delete the duplicate elements in a list, hence
    this property will not be powerful enough too.
</p>
<div class="sourceCode" id="cb6">
 <pre class="sourceCode python"><code class="sourceCode python"><span id="cb6-1"><a aria-hidden="true" href="#cb6-1" tabindex="-1"></a><span class="kw">def</span> sort_test_prop_4():</span>
<span id="cb6-2"><a aria-hidden="true" href="#cb6-2" tabindex="-1"></a>    l <span class="op">=</span> [<span class="dv">2</span>, <span class="dv">2</span>, <span class="dv">1</span>, <span class="dv">3</span>, <span class="dv">4</span>]</span>
<span id="cb6-3"><a aria-hidden="true" href="#cb6-3" tabindex="-1"></a>    sorted_l <span class="op">=</span> dummy_sort(l)</span>
<span id="cb6-4"><a aria-hidden="true" href="#cb6-4" tabindex="-1"></a>    <span class="cf">assert</span> is_sorted(sorted_l) <span class="kw">and</span> is_permutation(l, sorted_l)</span>
<span id="cb6-5"><a aria-hidden="true" href="#cb6-5" tabindex="-1"></a></span>
<span id="cb6-6"><a aria-hidden="true" href="#cb6-6" tabindex="-1"></a><span class="kw">def</span> is_permutation(l1, l2):</span>
<span id="cb6-7"><a aria-hidden="true" href="#cb6-7" tabindex="-1"></a>    <span class="cf">for</span> item <span class="kw">in</span> l1:</span>
<span id="cb6-8"><a aria-hidden="true" href="#cb6-8" tabindex="-1"></a>        <span class="cf">if</span> item <span class="kw">in</span> l2:</span>
<span id="cb6-9"><a aria-hidden="true" href="#cb6-9" tabindex="-1"></a>            l2.remove(item)</span>
<span id="cb6-10"><a aria-hidden="true" href="#cb6-10" tabindex="-1"></a>        <span class="cf">else</span>:</span>
<span id="cb6-11"><a aria-hidden="true" href="#cb6-11" tabindex="-1"></a>            <span class="cf">return</span> <span class="va">False</span></span>
<span id="cb6-12"><a aria-hidden="true" href="#cb6-12" tabindex="-1"></a>    <span class="cf">return</span> <span class="bu">len</span>(l2) <span class="op">==</span> <span class="dv">0</span></span></code></pre>
</div>
<p>
 So this was our final property for testing. The resulting list must be sorted, and it should be a permutation of the
    initial list. If I did not do any mistakes in writing the is_permutation function, this function must be properly
    tested using this property.
</p>
<p>
 There is another way of testing this, we could use a so-called Test Oracle for our property. Let’s say that we tested
    our dummy_sort extensively, and we used it in our software project for some time, we are quite sure that our
    function holds. And let’s assume we did not do Property Based Testing the first time, we were young and naive, we
    only did unit tests on the function, and we now want to use property based testing.
</p>
<p>
 Now, we can use another notion of truth for our new sorting algorithm, whatever dummy_sort returns is our truth.
</p>
<div class="sourceCode" id="cb7">
 <pre class="sourceCode python"><code class="sourceCode python"><span id="cb7-1"><a aria-hidden="true" href="#cb7-1" tabindex="-1"></a><span class="kw">def</span> sort_test_prop_5():</span>
<span id="cb7-2"><a aria-hidden="true" href="#cb7-2" tabindex="-1"></a>    l <span class="op">=</span> [<span class="dv">2</span>, <span class="dv">2</span>, <span class="dv">1</span>, <span class="dv">3</span>, <span class="dv">4</span>]</span>
<span id="cb7-3"><a aria-hidden="true" href="#cb7-3" tabindex="-1"></a>    dummy_sorted_l <span class="op">=</span> dummy_sort(l)</span>
<span id="cb7-4"><a aria-hidden="true" href="#cb7-4" tabindex="-1"></a>    fancy_sorted_l <span class="op">=</span> fancy_sort(l)</span>
<span id="cb7-5"><a aria-hidden="true" href="#cb7-5" tabindex="-1"></a>    <span class="cf">assert</span> dummy_sort(l) <span class="op">==</span> fancy_sort(l)</span></code></pre>
</div>
<p>
 As our truth is defined using a previous implementation, we can use that implementation to test our new
    implementation. This is especially useful for testing optimizations and refactors in our code.
</p>
<p>
 So what do we do, we now have a great testing infrastructure, we can just write a bunch of test cases without writing
    their results as given below.
</p>
<div class="sourceCode" id="cb8">
 <pre class="sourceCode python"><code class="sourceCode python"><span id="cb8-1"><a aria-hidden="true" href="#cb8-1" tabindex="-1"></a><span class="kw">def</span> test_fancy_sort(l):</span>
<span id="cb8-2"><a aria-hidden="true" href="#cb8-2" tabindex="-1"></a>    dummy_sorted_l <span class="op">=</span> dummy_sort(l)</span>
<span id="cb8-3"><a aria-hidden="true" href="#cb8-3" tabindex="-1"></a>    fancy_sorted_l <span class="op">=</span> fancy_sort(l)</span>
<span id="cb8-4"><a aria-hidden="true" href="#cb8-4" tabindex="-1"></a>    <span class="cf">assert</span> dummy_sort(l) <span class="op">==</span> fancy_sort(l)</span>
<span id="cb8-5"><a aria-hidden="true" href="#cb8-5" tabindex="-1"></a></span>
<span id="cb8-6"><a aria-hidden="true" href="#cb8-6" tabindex="-1"></a><span class="kw">def</span> test_many_cases():</span>
<span id="cb8-7"><a aria-hidden="true" href="#cb8-7" tabindex="-1"></a>    list_of_cases <span class="op">=</span> [</span>
<span id="cb8-8"><a aria-hidden="true" href="#cb8-8" tabindex="-1"></a>    [],</span>
<span id="cb8-9"><a aria-hidden="true" href="#cb8-9" tabindex="-1"></a>    [<span class="dv">1</span>],</span>
<span id="cb8-10"><a aria-hidden="true" href="#cb8-10" tabindex="-1"></a>    [<span class="dv">2</span>, <span class="dv">1</span>],</span>
<span id="cb8-11"><a aria-hidden="true" href="#cb8-11" tabindex="-1"></a>    [<span class="dv">3</span>, <span class="dv">1</span>, <span class="dv">2</span>],</span>
<span id="cb8-12"><a aria-hidden="true" href="#cb8-12" tabindex="-1"></a>    [<span class="dv">5</span>, <span class="dv">1</span>, <span class="dv">2</span>, <span class="dv">4</span>]</span>
<span id="cb8-13"><a aria-hidden="true" href="#cb8-13" tabindex="-1"></a>    ]</span>
<span id="cb8-14"><a aria-hidden="true" href="#cb8-14" tabindex="-1"></a>    <span class="cf">for</span> case <span class="kw">in</span> list_of_cases:</span>
<span id="cb8-15"><a aria-hidden="true" href="#cb8-15" tabindex="-1"></a>        test_fancy_sort(case)</span></code></pre>
</div>
<p>
 It doesn’t seem great, right. We still have to write all of these tests, which is better than writing tests and the
    results, but still it feels like we could have something better.
</p>
<p>
 Wait, we actually do! John Hughes and Koen Claessen has invented exactly that process.
</p>
<div class="sourceCode" id="cb9">
 <pre class="sourceCode python"><code class="sourceCode python"><span id="cb9-1"><a aria-hidden="true" href="#cb9-1" tabindex="-1"></a><span class="kw">def</span> test_many_cases_smart():</span>
<span id="cb9-2"><a aria-hidden="true" href="#cb9-2" tabindex="-1"></a>    <span class="cf">for</span> _ <span class="kw">in</span> <span class="bu">range</span>(<span class="dv">1000</span>):</span>
<span id="cb9-3"><a aria-hidden="true" href="#cb9-3" tabindex="-1"></a>        case <span class="op">=</span> generate_test_case_for_sorting()</span>
<span id="cb9-4"><a aria-hidden="true" href="#cb9-4" tabindex="-1"></a>        test_fancy_sort(case)</span></code></pre>
</div>
<p>
 Strictly speaking, what they invented is so much greater, fancier, and smarter than this, but it still relies on the
    same idea. A better version is given below.
</p>
<div class="sourceCode" id="cb10">
 <pre class="sourceCode python"><code class="sourceCode python"><span id="cb10-1"><a aria-hidden="true" href="#cb10-1" tabindex="-1"></a><span class="kw">def</span> test_many_cases_even_smarter():</span>
<span id="cb10-2"><a aria-hidden="true" href="#cb10-2" tabindex="-1"></a>    <span class="cf">for</span> i <span class="kw">in</span> <span class="bu">range</span>(<span class="dv">1000</span>):</span>
<span id="cb10-3"><a aria-hidden="true" href="#cb10-3" tabindex="-1"></a>        case <span class="op">=</span> generate_test_case_for_sorting_smarter(i)</span>
<span id="cb10-4"><a aria-hidden="true" href="#cb10-4" tabindex="-1"></a>        <span class="cf">if</span> test_fancy_sort(case) <span class="op">==</span> <span class="st">"Fail"</span>:</span>
<span id="cb10-5"><a aria-hidden="true" href="#cb10-5" tabindex="-1"></a>            <span class="cf">return</span> shrink_failing_case(case)</span></code></pre>
</div>
<p>
 So what’s better about this process is that
</p>
<p>
 1- It remembers how many tests it has done, so it can be a bit stateful and remember the past in some sense. A simple
    example is we can generate lists based on logarithm of i, which would allow creating larger examples as we move
    forward with the tests, hoping that larger test cases might catch bugs smaller test cases could not demonstrate.
</p>
<p>
 2- It “shrinks” the failing test case. Shrinking means finding a minimal example using a failed test case. Let’s say
    that our fancy sorting function has a bug, it crashes when the list has negative numbers. This bug is found with the
    following test case.
</p>
<p>
 [11, 1,1,1,1,-1,1,2,442,34,2,4]
</p>
<p>
 But it could actually be found using.
</p>
<p>
 [-1]
</p>
<p>
 If I had given you the first list as the failing case, it would take a lot of time to debug. There are lots of cases,
    maybe the function crashes with lists of size more than 10, or it cannot handle cases where 4 list elements are
    same.
</p>
<p>
 But the second test case makes it very clear where the problem is and how to find and debug it.
</p>
<p>
 Let me give you a very simple and not-so-smart generator and shrinker for the case given above.
</p>
<div class="sourceCode" id="cb11">
 <pre class="sourceCode python"><code class="sourceCode python"><span id="cb11-1"><a aria-hidden="true" href="#cb11-1" tabindex="-1"></a><span class="kw">def</span> generate_test_case_for_sorting_smarter(size):</span>
<span id="cb11-2"><a aria-hidden="true" href="#cb11-2" tabindex="-1"></a>    actual_size <span class="op">=</span> math.log(size, <span class="dv">2</span>)</span>
<span id="cb11-3"><a aria-hidden="true" href="#cb11-3" tabindex="-1"></a>    generated_list <span class="op">=</span> []</span>
<span id="cb11-4"><a aria-hidden="true" href="#cb11-4" tabindex="-1"></a>    <span class="cf">for</span> _ <span class="kw">in</span> <span class="bu">range</span>(actual_size):</span>
<span id="cb11-5"><a aria-hidden="true" href="#cb11-5" tabindex="-1"></a>        generated_list.append(random.randint(<span class="op">-</span><span class="dv">5</span>, <span class="dv">10000</span>))</span>
<span id="cb11-6"><a aria-hidden="true" href="#cb11-6" tabindex="-1"></a>    <span class="cf">return</span> generated_list</span></code></pre>
</div>
<p>
 This generation function generates random integers from the interval [-5, 10000) for a list of size log2size.
</p>
<div class="sourceCode" id="cb12">
 <pre class="sourceCode python"><code class="sourceCode python"><span id="cb12-1"><a aria-hidden="true" href="#cb12-1" tabindex="-1"></a><span class="kw">def</span> shrink_failing_case(case):</span>
<span id="cb12-2"><a aria-hidden="true" href="#cb12-2" tabindex="-1"></a>    shrinked_case <span class="op">=</span> case[<span class="dv">1</span>:]</span>
<span id="cb12-3"><a aria-hidden="true" href="#cb12-3" tabindex="-1"></a>    <span class="cf">if</span> test_fancy_sort(shrinked_case) <span class="op">==</span> <span class="st">"Fail"</span>:</span>
<span id="cb12-4"><a aria-hidden="true" href="#cb12-4" tabindex="-1"></a>        <span class="cf">return</span> shrink_failing_case(shrinked_case)</span>
<span id="cb12-5"><a aria-hidden="true" href="#cb12-5" tabindex="-1"></a>    <span class="cf">else</span>:</span>
<span id="cb12-6"><a aria-hidden="true" href="#cb12-6" tabindex="-1"></a>        <span class="cf">return</span> case</span></code></pre>
</div>
<p>
 This shrinking function tries to shrink the list by truncating it from the beginning. At each step, a smaller list is
    created by excluding the first element; this allows creating minimal examples for debugging the actual problem.
</p>
<p>
 This is the intuition behind Property Based Testing. There is a lot more to talk about, there is fuzzing, mutation
    based property based testing; there are clever ways of generating, shrinking, testing, writing properties… I want to
    write about those in the future too, I hope this was an interesting read for you.
</p>
<p>
 For those interested, here are some more interesting reading to follow through.
</p>
<ul>
 <li>
  Original QuickCheck Paper (
  <a href="https://www.cs.tufts.edu/~nr/cs257/archive/john-hughes/quick.pdf">
   https://www.cs.tufts.edu/~nr/cs257/archive/john-hughes/quick.pdf
  </a>
  )
 </li>
 <li>
  A Description of Random PBT and Fuzzing explaining motivations behind it by Leo and Mike (
  <a href="https://plum-umd.github.io/projects/random-testing.html">
   https://plum-umd.github.io/projects/random-testing.html
  </a>
  )
 </li>
 <li>
  A (probably better than mine) medium post on PBT (
  <a href="https://medium.com/criteo-engineering/introduction-to-property-based-testing-f5236229d237">
   https://medium.com/criteo-engineering/introduction-to-property-based-testing-f5236229d237
  </a>
  )
 </li>
 <li>
  A talk by John Huges, “Dont Write Tests” (
  <a href="https://www.youtube.com/watch?v=hXnS_Xjwk2Y">
   https://www.youtube.com/watch?v=hXnS_Xjwk2Y
  </a>
  )
 </li>
</ul>
<p>
 Aside from the gists given above, I also uploaded the code to a single file for anyone interested as a convenience.
</p>
<p>
 <a href="https://github.com/alpaylan/technical-blog-code/blob/main/pbt-1.py">
  https://github.com/alpaylan/technical-blog-code/blob/main/pbt-1.py
 </a>
 Introduction to Property Based Testing
 <p>
  Property Based Random Testing is a flavor of testing that aims to use higher level specifications for testing instead
    of hand-writing or generating tests. It was first developed by Koen Claessen and John Hughes in 1999 as a software
    library for Haskell, called QuickCheck. There has been substantial development in the field since then, I will not
    bore you with lots of details as the purpose of this writing is to familiarize you with PBT(Property Based Testing).
 </p>
 <p>
  To give a sense of what is happening, let’s first start by talking about Unit Tests.
 </p>
 <p>
  A Unit Test is a test case aimed into testing a unit of a program, conventionally a function.
 </p>
 <div class="sourceCode" id="cb1">
  <pre class="sourceCode python"><code data-code-block-lang="python"><span id="cb1-1"><a aria-hidden="true" href="#cb1-1" tabindex="-1"></a><span class="kw">def</span> sort_test_1():</span>
<span id="cb1-2"><a aria-hidden="true" href="#cb1-2" tabindex="-1"></a>    l <span class="op">=</span> [<span class="dv">2</span>, <span class="dv">1</span>, <span class="dv">3</span>, <span class="dv">4</span>]</span>
<span id="cb1-3"><a aria-hidden="true" href="#cb1-3" tabindex="-1"></a>    sorted_l <span class="op">=</span> dummy_sort(l)</span>
<span id="cb1-4"><a aria-hidden="true" href="#cb1-4" tabindex="-1"></a>    <span class="cf">assert</span> sorted_l <span class="op">==</span> [<span class="dv">1</span>, <span class="dv">2</span>, <span class="dv">3</span>, <span class="dv">4</span>]</span></code></pre>
 </div>
 <p>
  Above, you see a very simple test case for a function called dummy sort, which from the name and the structure it
    feels is supposed to sort a given function of possibly integers in ascending order.
 </p>
 <p>
  But, this test case doesn’t actually give us very much knowledge on the function under test. It gives us a few clues
    we could perhaps generalize such as;
 </p>
 <ol type="1">
  <li>
   Function sorts the list [2, 1, 3, 4] correctly
  </li>
  <li>
   (1) could imply that the function sorts all lists of length 4 correctly.
  </li>
  <li>
   (1) also could imply that the function sorts all lists of integer permutations from 1 up to n.
  </li>
  <li>
   (1) also could imply that the function sorts all lists of all lengths containing positive integers.
  </li>
  <li>
   (1) also could imply this function sorts any type of list containing arbitrary integers in arbitrary length.
  </li>
 </ol>
 <p>
  We might be expecting any one of the properties from (1–4), but a better possibility is that we are expecting 5. We
    could also expect properties 1–4, but the example also wouldn’t generalize to those, at least those other than
    property (1).
 </p>
 <p>
  So ideally, we would need to create a set of examples that could represent the set of all cases we want our function
    to work on, so we need a way of defining this representative.
 </p>
 <p>
  This is possible via creating what we will call properties in our code. Let me demonstrate with an example.
 </p>
 <div class="sourceCode" id="cb2">
  <pre class="sourceCode python"><code class="sourceCode python"><span id="cb2-1"><a aria-hidden="true" href="#cb2-1" tabindex="-1"></a><span class="kw">def</span> sort_test_prop_1():</span>
<span id="cb2-2"><a aria-hidden="true" href="#cb2-2" tabindex="-1"></a>    l <span class="op">=</span> [<span class="dv">2</span>, <span class="dv">1</span>, <span class="dv">3</span>, <span class="dv">4</span>]</span>
<span id="cb2-3"><a aria-hidden="true" href="#cb2-3" tabindex="-1"></a>    sorted_l <span class="op">=</span> dummy_sort(l)</span>
<span id="cb2-4"><a aria-hidden="true" href="#cb2-4" tabindex="-1"></a>    <span class="cf">assert</span> is_sorted(sorted_l)</span>
<span id="cb2-5"><a aria-hidden="true" href="#cb2-5" tabindex="-1"></a></span>
<span id="cb2-6"><a aria-hidden="true" href="#cb2-6" tabindex="-1"></a><span class="kw">def</span> is_sorted(candidate_list):</span>
<span id="cb2-7"><a aria-hidden="true" href="#cb2-7" tabindex="-1"></a>    <span class="cf">if</span> <span class="bu">len</span>(candidate_list) <span class="op">==</span> <span class="dv">0</span>:</span>
<span id="cb2-8"><a aria-hidden="true" href="#cb2-8" tabindex="-1"></a>        <span class="cf">return</span> <span class="va">True</span></span>
<span id="cb2-9"><a aria-hidden="true" href="#cb2-9" tabindex="-1"></a>    pivot <span class="op">=</span> candidate_list[<span class="dv">0</span>]</span>
<span id="cb2-10"><a aria-hidden="true" href="#cb2-10" tabindex="-1"></a>    <span class="cf">for</span> item <span class="kw">in</span> candidate_list:</span>
<span id="cb2-11"><a aria-hidden="true" href="#cb2-11" tabindex="-1"></a>        <span class="cf">if</span> pivot <span class="op">&gt;</span> item:</span>
<span id="cb2-12"><a aria-hidden="true" href="#cb2-12" tabindex="-1"></a>            <span class="cf">return</span> <span class="va">False</span></span>
<span id="cb2-13"><a aria-hidden="true" href="#cb2-13" tabindex="-1"></a>        <span class="cf">else</span>:</span>
<span id="cb2-14"><a aria-hidden="true" href="#cb2-14" tabindex="-1"></a>            pivot <span class="op">=</span> item</span>
<span id="cb2-15"><a aria-hidden="true" href="#cb2-15" tabindex="-1"></a>    <span class="cf">return</span> <span class="va">True</span></span></code></pre>
 </div>
 <p>
  Function is_sorted checks if the list is monotonically increasing, meaning if no element is less than the element
    right before. As a logical statement, we can write is_sorted as
 </p>
 <p>
  If you look carefully, you will see that this property that we wrote actually does not cover our needs. Suppose we
    have an implementation of dummy_sort as given below.
 </p>
 <div class="sourceCode" id="cb3">
  <pre class="sourceCode python"><code class="sourceCode python"><span id="cb3-1"><a aria-hidden="true" href="#cb3-1" tabindex="-1"></a><span class="kw">def</span> dummy_sort(l):</span>
<span id="cb3-2"><a aria-hidden="true" href="#cb3-2" tabindex="-1"></a>    <span class="cf">return</span> []</span></code></pre>
 </div>
 <p>
  You will see that this means dummy_sort will always give a sorted list back to you, just not the one you would want.
 </p>
 <p>
  So a better property could be writing the test as.
 </p>
 <div class="sourceCode" id="cb4">
  <pre class="sourceCode python"><code class="sourceCode python"><span id="cb4-1"><a aria-hidden="true" href="#cb4-1" tabindex="-1"></a><span class="kw">def</span> sort_test_prop_2():</span>
<span id="cb4-2"><a aria-hidden="true" href="#cb4-2" tabindex="-1"></a>    l <span class="op">=</span> [<span class="dv">2</span>, <span class="dv">1</span>, <span class="dv">3</span>, <span class="dv">4</span>]</span>
<span id="cb4-3"><a aria-hidden="true" href="#cb4-3" tabindex="-1"></a>    sorted_l <span class="op">=</span> dummy_sort(l)</span>
<span id="cb4-4"><a aria-hidden="true" href="#cb4-4" tabindex="-1"></a>    <span class="cf">assert</span> is_sorted(sorted_l) <span class="kw">and</span> elements_same(l, sorted_l)</span>
<span id="cb4-5"><a aria-hidden="true" href="#cb4-5" tabindex="-1"></a></span>
<span id="cb4-6"><a aria-hidden="true" href="#cb4-6" tabindex="-1"></a><span class="kw">def</span> elements_same(l1, l2):</span>
<span id="cb4-7"><a aria-hidden="true" href="#cb4-7" tabindex="-1"></a>    <span class="cf">return</span> <span class="bu">set</span>(l1) <span class="op">==</span> <span class="bu">set</span>(l2)</span></code></pre>
 </div>
 <p>
  We just added a new check that looks if both lists have the same elements. Which would mean that if l contains an
    element that sorted_l does not contain, then our function does not do the right thing.
 </p>
 <p>
  Yet, a careful reader will also realize the problem with this property. We can falsify it with the test case given
    below.We just added a new check that looks if both lists have the same elements. Which would mean that if l contains
    an element that sorted_l does not contain, then our function does not do the right thing.
 </p>
 <p>
  Yet, a careful reader will also realize the problem with this property. We can falsify it with the test case given
    below.
 </p>
 <div class="sourceCode" id="cb5">
  <pre class="sourceCode python"><code class="sourceCode python"><span id="cb5-1"><a aria-hidden="true" href="#cb5-1" tabindex="-1"></a><span class="kw">def</span> sort_test_prop_3():</span>
<span id="cb5-2"><a aria-hidden="true" href="#cb5-2" tabindex="-1"></a>    l <span class="op">=</span> [<span class="dv">2</span>, <span class="dv">2</span>, <span class="dv">1</span>, <span class="dv">3</span>, <span class="dv">4</span>]</span>
<span id="cb5-3"><a aria-hidden="true" href="#cb5-3" tabindex="-1"></a>    sorted_l <span class="op">=</span> dummy_sort(l)</span>
<span id="cb5-4"><a aria-hidden="true" href="#cb5-4" tabindex="-1"></a>    <span class="cf">assert</span> is_sorted(sorted_l) <span class="kw">and</span> elements_same(l, sorted_l)</span>
<span id="cb5-5"><a aria-hidden="true" href="#cb5-5" tabindex="-1"></a></span>
<span id="cb5-6"><a aria-hidden="true" href="#cb5-6" tabindex="-1"></a><span class="kw">def</span> dummy_sort():</span>
<span id="cb5-7"><a aria-hidden="true" href="#cb5-7" tabindex="-1"></a>    <span class="cf">return</span> [<span class="dv">1</span>, <span class="dv">2</span>, <span class="dv">3</span>, <span class="dv">4</span>]</span></code></pre>
 </div>
 <p>
  As one familiar with Python’s set data structure will see, a set will delete the duplicate elements in a list, hence
    this property will not be powerful enough too.
 </p>
 <div class="sourceCode" id="cb6">
  <pre class="sourceCode python"><code class="sourceCode python"><span id="cb6-1"><a aria-hidden="true" href="#cb6-1" tabindex="-1"></a><span class="kw">def</span> sort_test_prop_4():</span>
<span id="cb6-2"><a aria-hidden="true" href="#cb6-2" tabindex="-1"></a>    l <span class="op">=</span> [<span class="dv">2</span>, <span class="dv">2</span>, <span class="dv">1</span>, <span class="dv">3</span>, <span class="dv">4</span>]</span>
<span id="cb6-3"><a aria-hidden="true" href="#cb6-3" tabindex="-1"></a>    sorted_l <span class="op">=</span> dummy_sort(l)</span>
<span id="cb6-4"><a aria-hidden="true" href="#cb6-4" tabindex="-1"></a>    <span class="cf">assert</span> is_sorted(sorted_l) <span class="kw">and</span> is_permutation(l, sorted_l)</span>
<span id="cb6-5"><a aria-hidden="true" href="#cb6-5" tabindex="-1"></a></span>
<span id="cb6-6"><a aria-hidden="true" href="#cb6-6" tabindex="-1"></a><span class="kw">def</span> is_permutation(l1, l2):</span>
<span id="cb6-7"><a aria-hidden="true" href="#cb6-7" tabindex="-1"></a>    <span class="cf">for</span> item <span class="kw">in</span> l1:</span>
<span id="cb6-8"><a aria-hidden="true" href="#cb6-8" tabindex="-1"></a>        <span class="cf">if</span> item <span class="kw">in</span> l2:</span>
<span id="cb6-9"><a aria-hidden="true" href="#cb6-9" tabindex="-1"></a>            l2.remove(item)</span>
<span id="cb6-10"><a aria-hidden="true" href="#cb6-10" tabindex="-1"></a>        <span class="cf">else</span>:</span>
<span id="cb6-11"><a aria-hidden="true" href="#cb6-11" tabindex="-1"></a>            <span class="cf">return</span> <span class="va">False</span></span>
<span id="cb6-12"><a aria-hidden="true" href="#cb6-12" tabindex="-1"></a>    <span class="cf">return</span> <span class="bu">len</span>(l2) <span class="op">==</span> <span class="dv">0</span></span></code></pre>
 </div>
 <p>
  So this was our final property for testing. The resulting list must be sorted, and it should be a permutation of the
    initial list. If I did not do any mistakes in writing the is_permutation function, this function must be properly
    tested using this property.
 </p>
 <p>
  There is another way of testing this, we could use a so-called Test Oracle for our property. Let’s say that we tested
    our dummy_sort extensively, and we used it in our software project for some time, we are quite sure that our
    function holds. And let’s assume we did not do Property Based Testing the first time, we were young and naive, we
    only did unit tests on the function, and we now want to use property based testing.
 </p>
 <p>
  Now, we can use another notion of truth for our new sorting algorithm, whatever dummy_sort returns is our truth.
 </p>
 <div class="sourceCode" id="cb7">
  <pre class="sourceCode python"><code class="sourceCode python"><span id="cb7-1"><a aria-hidden="true" href="#cb7-1" tabindex="-1"></a><span class="kw">def</span> sort_test_prop_5():</span>
<span id="cb7-2"><a aria-hidden="true" href="#cb7-2" tabindex="-1"></a>    l <span class="op">=</span> [<span class="dv">2</span>, <span class="dv">2</span>, <span class="dv">1</span>, <span class="dv">3</span>, <span class="dv">4</span>]</span>
<span id="cb7-3"><a aria-hidden="true" href="#cb7-3" tabindex="-1"></a>    dummy_sorted_l <span class="op">=</span> dummy_sort(l)</span>
<span id="cb7-4"><a aria-hidden="true" href="#cb7-4" tabindex="-1"></a>    fancy_sorted_l <span class="op">=</span> fancy_sort(l)</span>
<span id="cb7-5"><a aria-hidden="true" href="#cb7-5" tabindex="-1"></a>    <span class="cf">assert</span> dummy_sort(l) <span class="op">==</span> fancy_sort(l)</span></code></pre>
 </div>
 <p>
  As our truth is defined using a previous implementation, we can use that implementation to test our new
    implementation. This is especially useful for testing optimizations and refactors in our code.
 </p>
 <p>
  So what do we do, we now have a great testing infrastructure, we can just write a bunch of test cases without writing
    their results as given below.
 </p>
 <div class="sourceCode" id="cb8">
  <pre class="sourceCode python"><code class="sourceCode python"><span id="cb8-1"><a aria-hidden="true" href="#cb8-1" tabindex="-1"></a><span class="kw">def</span> test_fancy_sort(l):</span>
<span id="cb8-2"><a aria-hidden="true" href="#cb8-2" tabindex="-1"></a>    dummy_sorted_l <span class="op">=</span> dummy_sort(l)</span>
<span id="cb8-3"><a aria-hidden="true" href="#cb8-3" tabindex="-1"></a>    fancy_sorted_l <span class="op">=</span> fancy_sort(l)</span>
<span id="cb8-4"><a aria-hidden="true" href="#cb8-4" tabindex="-1"></a>    <span class="cf">assert</span> dummy_sort(l) <span class="op">==</span> fancy_sort(l)</span>
<span id="cb8-5"><a aria-hidden="true" href="#cb8-5" tabindex="-1"></a></span>
<span id="cb8-6"><a aria-hidden="true" href="#cb8-6" tabindex="-1"></a><span class="kw">def</span> test_many_cases():</span>
<span id="cb8-7"><a aria-hidden="true" href="#cb8-7" tabindex="-1"></a>    list_of_cases <span class="op">=</span> [</span>
<span id="cb8-8"><a aria-hidden="true" href="#cb8-8" tabindex="-1"></a>    [],</span>
<span id="cb8-9"><a aria-hidden="true" href="#cb8-9" tabindex="-1"></a>    [<span class="dv">1</span>],</span>
<span id="cb8-10"><a aria-hidden="true" href="#cb8-10" tabindex="-1"></a>    [<span class="dv">2</span>, <span class="dv">1</span>],</span>
<span id="cb8-11"><a aria-hidden="true" href="#cb8-11" tabindex="-1"></a>    [<span class="dv">3</span>, <span class="dv">1</span>, <span class="dv">2</span>],</span>
<span id="cb8-12"><a aria-hidden="true" href="#cb8-12" tabindex="-1"></a>    [<span class="dv">5</span>, <span class="dv">1</span>, <span class="dv">2</span>, <span class="dv">4</span>]</span>
<span id="cb8-13"><a aria-hidden="true" href="#cb8-13" tabindex="-1"></a>    ]</span>
<span id="cb8-14"><a aria-hidden="true" href="#cb8-14" tabindex="-1"></a>    <span class="cf">for</span> case <span class="kw">in</span> list_of_cases:</span>
<span id="cb8-15"><a aria-hidden="true" href="#cb8-15" tabindex="-1"></a>        test_fancy_sort(case)</span></code></pre>
 </div>
 <p>
  It doesn’t seem great, right. We still have to write all of these tests, which is better than writing tests and the
    results, but still it feels like we could have something better.
 </p>
 <p>
  Wait, we actually do! John Hughes and Koen Claessen has invented exactly that process.
 </p>
 <div class="sourceCode" id="cb9">
  <pre class="sourceCode python"><code class="sourceCode python"><span id="cb9-1"><a aria-hidden="true" href="#cb9-1" tabindex="-1"></a><span class="kw">def</span> test_many_cases_smart():</span>
<span id="cb9-2"><a aria-hidden="true" href="#cb9-2" tabindex="-1"></a>    <span class="cf">for</span> _ <span class="kw">in</span> <span class="bu">range</span>(<span class="dv">1000</span>):</span>
<span id="cb9-3"><a aria-hidden="true" href="#cb9-3" tabindex="-1"></a>        case <span class="op">=</span> generate_test_case_for_sorting()</span>
<span id="cb9-4"><a aria-hidden="true" href="#cb9-4" tabindex="-1"></a>        test_fancy_sort(case)</span></code></pre>
 </div>
 <p>
  Strictly speaking, what they invented is so much greater, fancier, and smarter than this, but it still relies on the
    same idea. A better version is given below.
 </p>
 <div class="sourceCode" id="cb10">
  <pre class="sourceCode python"><code class="sourceCode python"><span id="cb10-1"><a aria-hidden="true" href="#cb10-1" tabindex="-1"></a><span class="kw">def</span> test_many_cases_even_smarter():</span>
<span id="cb10-2"><a aria-hidden="true" href="#cb10-2" tabindex="-1"></a>    <span class="cf">for</span> i <span class="kw">in</span> <span class="bu">range</span>(<span class="dv">1000</span>):</span>
<span id="cb10-3"><a aria-hidden="true" href="#cb10-3" tabindex="-1"></a>        case <span class="op">=</span> generate_test_case_for_sorting_smarter(i)</span>
<span id="cb10-4"><a aria-hidden="true" href="#cb10-4" tabindex="-1"></a>        <span class="cf">if</span> test_fancy_sort(case) <span class="op">==</span> <span class="st">"Fail"</span>:</span>
<span id="cb10-5"><a aria-hidden="true" href="#cb10-5" tabindex="-1"></a>            <span class="cf">return</span> shrink_failing_case(case)</span></code></pre>
 </div>
 <p>
  So what’s better about this process is that
 </p>
 <p>
  1- It remembers how many tests it has done, so it can be a bit stateful and remember the past in some sense. A simple
    example is we can generate lists based on logarithm of i, which would allow creating larger examples as we move
    forward with the tests, hoping that larger test cases might catch bugs smaller test cases could not demonstrate.
 </p>
 <p>
  2- It “shrinks” the failing test case. Shrinking means finding a minimal example using a failed test case. Let’s say
    that our fancy sorting function has a bug, it crashes when the list has negative numbers. This bug is found with the
    following test case.
 </p>
 <p>
  [11, 1,1,1,1,-1,1,2,442,34,2,4]
 </p>
 <p>
  But it could actually be found using.
 </p>
 <p>
  [-1]
 </p>
 <p>
  If I had given you the first list as the failing case, it would take a lot of time to debug. There are lots of cases,
    maybe the function crashes with lists of size more than 10, or it cannot handle cases where 4 list elements are
    same.
 </p>
 <p>
  But the second test case makes it very clear where the problem is and how to find and debug it.
 </p>
 <p>
  Let me give you a very simple and not-so-smart generator and shrinker for the case given above.
 </p>
 <div class="sourceCode" id="cb11">
  <pre class="sourceCode python"><code class="sourceCode python"><span id="cb11-1"><a aria-hidden="true" href="#cb11-1" tabindex="-1"></a><span class="kw">def</span> generate_test_case_for_sorting_smarter(size):</span>
<span id="cb11-2"><a aria-hidden="true" href="#cb11-2" tabindex="-1"></a>    actual_size <span class="op">=</span> math.log(size, <span class="dv">2</span>)</span>
<span id="cb11-3"><a aria-hidden="true" href="#cb11-3" tabindex="-1"></a>    generated_list <span class="op">=</span> []</span>
<span id="cb11-4"><a aria-hidden="true" href="#cb11-4" tabindex="-1"></a>    <span class="cf">for</span> _ <span class="kw">in</span> <span class="bu">range</span>(actual_size):</span>
<span id="cb11-5"><a aria-hidden="true" href="#cb11-5" tabindex="-1"></a>        generated_list.append(random.randint(<span class="op">-</span><span class="dv">5</span>, <span class="dv">10000</span>))</span>
<span id="cb11-6"><a aria-hidden="true" href="#cb11-6" tabindex="-1"></a>    <span class="cf">return</span> generated_list</span></code></pre>
 </div>
 <p>
  This generation function generates random integers from the interval [-5, 10000) for a list of size log2size.
 </p>
 <div class="sourceCode" id="cb12">
  <pre class="sourceCode python"><code class="sourceCode python"><span id="cb12-1"><a aria-hidden="true" href="#cb12-1" tabindex="-1"></a><span class="kw">def</span> shrink_failing_case(case):</span>
<span id="cb12-2"><a aria-hidden="true" href="#cb12-2" tabindex="-1"></a>    shrinked_case <span class="op">=</span> case[<span class="dv">1</span>:]</span>
<span id="cb12-3"><a aria-hidden="true" href="#cb12-3" tabindex="-1"></a>    <span class="cf">if</span> test_fancy_sort(shrinked_case) <span class="op">==</span> <span class="st">"Fail"</span>:</span>
<span id="cb12-4"><a aria-hidden="true" href="#cb12-4" tabindex="-1"></a>        <span class="cf">return</span> shrink_failing_case(shrinked_case)</span>
<span id="cb12-5"><a aria-hidden="true" href="#cb12-5" tabindex="-1"></a>    <span class="cf">else</span>:</span>
<span id="cb12-6"><a aria-hidden="true" href="#cb12-6" tabindex="-1"></a>        <span class="cf">return</span> case</span></code></pre>
 </div>
 <p>
  This shrinking function tries to shrink the list by truncating it from the beginning. At each step, a smaller list is
    created by excluding the first element; this allows creating minimal examples for debugging the actual problem.
 </p>
 <p>
  This is the intuition behind Property Based Testing. There is a lot more to talk about, there is fuzzing, mutation
    based property based testing; there are clever ways of generating, shrinking, testing, writing properties… I want to
    write about those in the future too, I hope this was an interesting read for you.
 </p>
 <p>
  For those interested, here are some more interesting reading to follow through.
 </p>
 <ul>
  <li>
   Original QuickCheck Paper (
   <a href="https://www.cs.tufts.edu/~nr/cs257/archive/john-hughes/quick.pdf">
    https://www.cs.tufts.edu/~nr/cs257/archive/john-hughes/quick.pdf
   </a>
   )
  </li>
  <li>
   A Description of Random PBT and Fuzzing explaining motivations behind it by Leo and Mike (
   <a href="https://plum-umd.github.io/projects/random-testing.html">
    https://plum-umd.github.io/projects/random-testing.html
   </a>
   )
  </li>
  <li>
   A (probably better than mine) medium post on PBT (
   <a href="https://medium.com/criteo-engineering/introduction-to-property-based-testing-f5236229d237">
    https://medium.com/criteo-engineering/introduction-to-property-based-testing-f5236229d237
   </a>
   )
  </li>
  <li>
   A talk by John Huges, “Dont Write Tests” (
   <a href="https://www.youtube.com/watch?v=hXnS_Xjwk2Y">
    https://www.youtube.com/watch?v=hXnS_Xjwk2Y
   </a>
   )
  </li>
 </ul>
 <p>
  Aside from the gists given above, I also uploaded the code to a single file for anyone interested as a convenience.
 </p>
 <p>
  <a href="https://github.com/alpaylan/technical-blog-code/blob/main/pbt-1.py">
   https://github.com/alpaylan/technical-blog-code/blob/main/pbt-1.py
  </a>
 </p>
</p>
