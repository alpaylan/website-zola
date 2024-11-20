+++
title = "Learner’s Guide to Property Based Testing#1"
date = "2021-11-10"
[taxonomies]
tags = ['software engineering', 'testing', 'computer science', 'learning from learners']
language = ["en"]
+++

<article class="h-entry">
 <section class="e-content" data-field="body">
  <section class="section section--body section--first section--last" name="62c7">
   <div class="section-content">
    <div class="section-inner sectionLayout--insetColumn">
     <h3 class="graf graf--h3 graf--leading graf--title" id="bc17" name="bc17">
      Learner’s Guide to Property Based Testing#1
     </h3>
     <figure class="graf graf--figure graf-after--h3" id="aefd" name="aefd">
      <img class="graf-image" data-height="924" data-image-id="1*92Av2ZbXV98Ryo1C0cxpFw.png" data-is-featured="true" data-width="1640" src="https://cdn-images-1.medium.com/max/800/1*92Av2ZbXV98Ryo1C0cxpFw.png"/>
     </figure>
     <p class="graf graf--p graf-after--figure" id="2fbe" name="2fbe">
      Property Based Random Testing is a flavor of testing that aims to use higher level specifications for testing instead of hand-writing or generating tests. It was first developed by Koen Claessen and John Hughes in 1999 as a software library for Haskell, called QuickCheck. There has been substantial development in the field since then, I will not bore you with lots of details as the purpose of this writing is to familiarize you with PBT(Property Based Testing).
     </p>
     <p class="graf graf--p graf-after--p" id="8047" name="8047">
      To give a sense of what is happening, let’s first start by talking about Unit Tests.
     </p>
     <p class="graf graf--p graf-after--p" id="c0ab" name="c0ab">
      A Unit Test is a test case aimed into testing a unit of a program, conventionally a function.
     </p>
     <figure class="graf graf--figure graf--iframe graf-after--p" id="ea2b" name="ea2b">
      <script src="https://gist.github.com/alpaylan/d4b79f19ff5f50c042c64bb8c9bb8047.js">
      </script>
     </figure>
     <p class="graf graf--p graf-after--figure" id="41ba" name="41ba">
      Above, you see a very simple test case for a function called $dummy\_sort$, which from the name and the structure it feels is supposed to sort a given function of possibly integers in ascending order.
     </p>
     <p class="graf graf--p graf-after--p" id="a73c" name="a73c">
      But, this test case doesn’t actually give us very much knowledge on the function under test. It gives us a few clues we could perhaps generalize such as;
     </p>
     <p class="graf graf--p graf-after--p" id="21eb" name="21eb">
      1- Function sorts the list [2, 1, 3, 4] correctly
     </p>
     <p class="graf graf--p graf-after--p" id="eaee" name="eaee">
      2- (1) could imply that the function sorts all lists of length 4 correctly.
     </p>
     <p class="graf graf--p graf-after--p" id="c25d" name="c25d">
      3- (1) also could imply that the function sorts all lists of integer permutations from 1 up to n.
     </p>
     <p class="graf graf--p graf-after--p" id="5ca7" name="5ca7">
      4- (1) also could imply that the function sorts all lists of all lengths containing positive integers.
     </p>
     <p class="graf graf--p graf-after--p" id="0fd3" name="0fd3">
      5- (1) also could imply this function sorts any type of list containing arbitrary integers in arbitrary length.
     </p>
     <p class="graf graf--p graf-after--p" id="f2cd" name="f2cd">
      We might be expecting any one of the properties from (1–4), but a better possibility is that we are expecting 5. We could also expect properties 1–4, but the example also wouldn’t generalize to those, at least those other than property (1).
     </p>
     <p class="graf graf--p graf-after--p" id="3c53" name="3c53">
      So ideally, we would need to create a set of examples that could represent the set of all cases we want our function to work on, so we need a way of defining this representative.
     </p>
     <p class="graf graf--p graf-after--p" id="18ee" name="18ee">
      This is possible via creating what we will call properties in our code. Let me demonstrate with an example.
     </p>
     <figure class="graf graf--figure graf--iframe graf-after--p" id="3e6e" name="3e6e">
      <script src="https://gist.github.com/alpaylan/93c49cbfe2b25116733813db18d7fb7b.js">
      </script>
     </figure>
     <p class="graf graf--p graf-after--figure" id="57ef" name="57ef">
      Function
      <strong class="markup--strong markup--p-strong">
       <em class="markup--em markup--p-em">
        is_sorted
       </em>
      </strong>
      checks if the list is monotonically increasing, meaning if no element is less than the element right before. As a logical statement, we can write
      <strong class="markup--strong markup--p-strong">
       <em class="markup--em markup--p-em">
        is_sorted
       </em>
      </strong>
      as
     </p>
     <figure class="graf graf--figure graf-after--p" id="f976" name="f976">
      <img class="graf-image" data-height="77" data-image-id="1*qj4PFKlqjuaKx-y0fX6m8Q.png" data-width="467" src="https://cdn-images-1.medium.com/max/800/1*qj4PFKlqjuaKx-y0fX6m8Q.png"/>
     </figure>
     <p class="graf graf--p graf-after--figure" id="af18" name="af18">
      If you look carefully, you will see that this property that we wrote actually does not cover our needs. Suppose we have an implementation of
      <strong class="markup--strong markup--p-strong">
       <em class="markup--em markup--p-em">
        dummy_sort
       </em>
      </strong>
      as given below.
     </p>
     <figure class="graf graf--figure graf--iframe graf-after--p" id="0e9e" name="0e9e">
      <script src="https://gist.github.com/alpaylan/9e60cb01bf37eaba6fab4d841d788c03.js">
      </script>
     </figure>
     <p class="graf graf--p graf-after--figure" id="40cf" name="40cf">
      You will see that this means
      <strong class="markup--strong markup--p-strong">
       <em class="markup--em markup--p-em">
        dummy_sort
       </em>
      </strong>
      will always give a sorted list back to you, just not the one you would want.
     </p>
     <p class="graf graf--p graf-after--p" id="807d" name="807d">
      So a better property could be writing the test as.
     </p>
     <figure class="graf graf--figure graf--iframe graf-after--p" id="492b" name="492b">
      <script src="https://gist.github.com/alpaylan/2539c4d0d7342f6d24ac6137e21ac407.js">
      </script>
     </figure>
     <p class="graf graf--p graf-after--figure" id="f5d3" name="f5d3">
      We just added a new check that looks if both lists have the same elements. Which would mean that if
      <strong class="markup--strong markup--p-strong">
       <em class="markup--em markup--p-em">
        l
       </em>
      </strong>
      contains an element that
      <strong class="markup--strong markup--p-strong">
       <em class="markup--em markup--p-em">
        sorted_l
       </em>
      </strong>
      does not contain, then our function does not do the right thing.
     </p>
     <p class="graf graf--p graf-after--p" id="ae8a" name="ae8a">
      Yet, a careful reader will also realize the problem with this property. We can falsify it with the test case given below.
     </p>
     <figure class="graf graf--figure graf--iframe graf-after--p" id="41c2" name="41c2">
      <script src="https://gist.github.com/alpaylan/f3d320dc44dc07d010fed2d740462f65.js">
      </script>
     </figure>
     <p class="graf graf--p graf-after--figure" id="febd" name="febd">
      As one familiar with Python’s set data structure will see, a set will delete the duplicate elements in a list, hence this property will not be powerful enough too.
     </p>
     <figure class="graf graf--figure graf--iframe graf-after--p" id="928e" name="928e">
      <script src="https://gist.github.com/alpaylan/962e02c4c4d864d167e4e45039144ccc.js">
      </script>
     </figure>
     <p class="graf graf--p graf-after--figure" id="c610" name="c610">
      So this was our final property for testing. The resulting list must be sorted, and it should be a permutation of the initial list. If I did not do any mistakes in writing the is_permutation function, this function must be properly tested using this property.
     </p>
     <p class="graf graf--p graf-after--p" id="6e21" name="6e21">
      There is another way of testing this, we could use a so-called Test Oracle for our property. Let’s say that we tested our
      <strong class="markup--strong markup--p-strong">
       <em class="markup--em markup--p-em">
        dummy_sort
       </em>
      </strong>
      extensively, and we used it in our software project for some time, we are quite sure that our function holds. And let’s assume we did not do Property Based Testing the first time, we were young and naive, we only did unit tests on the function, and we now want to use property based testing.
     </p>
     <p class="graf graf--p graf-after--p" id="94e2" name="94e2">
      Now, we can use another notion of truth for our new sorting algorithm, whatever
      <strong class="markup--strong markup--p-strong">
       <em class="markup--em markup--p-em">
        dummy_sort
       </em>
      </strong>
      returns is our truth.
     </p>
     <figure class="graf graf--figure graf--iframe graf-after--p" id="06fa" name="06fa">
      <script src="https://gist.github.com/alpaylan/ace95fd9a8b6fbc392cde41446733f05.js">
      </script>
     </figure>
     <p class="graf graf--p graf-after--figure" id="ad7f" name="ad7f">
      As our truth is defined using a previous implementation, we can use that implementation to test our new implementation. This is especially useful for testing optimizations and refactors in our code.
     </p>
     <p class="graf graf--p graf-after--p" id="3fc7" name="3fc7">
      So what do we do, we now have a great testing infrastructure, we can just write a bunch of test cases without writing their results as given below.
     </p>
     <figure class="graf graf--figure graf--iframe graf-after--p" id="9ddc" name="9ddc">
      <script src="https://gist.github.com/alpaylan/49ac9f3a711790ad27b358eddc24bf32.js">
      </script>
     </figure>
     <p class="graf graf--p graf-after--figure" id="5abe" name="5abe">
      It doesn’t seem great, right. We still have to write all of these tests, which is better than writing tests and the results, but still it feels like we could have something better.
     </p>
     <p class="graf graf--p graf-after--p" id="a5be" name="a5be">
      Wait, we actually do! John Hughes and Koen Claessen has invented exactly that process.
     </p>
     <figure class="graf graf--figure graf--iframe graf-after--p" id="ccbf" name="ccbf">
      <script src="https://gist.github.com/alpaylan/f6d0554608be1bc00e0c78908e2e0c6e.js">
      </script>
     </figure>
     <p class="graf graf--p graf-after--figure" id="4def" name="4def">
      Strictly speaking, what they invented is so much greater, fancier, and smarter than this, but it still relies on the same idea. A better version is given below.
     </p>
     <figure class="graf graf--figure graf--iframe graf-after--p" id="2726" name="2726">
      <script src="https://gist.github.com/alpaylan/66edcd6e00a0c46d85c16198e10bda5f.js">
      </script>
     </figure>
     <p class="graf graf--p graf-after--figure" id="c975" name="c975">
      So what’s better about this process is that
     </p>
     <p class="graf graf--p graf-after--p" id="e700" name="e700">
      1- It remembers how many tests it has done, so it can be a bit stateful and remember the past in some sense. A simple example is we can generate lists based on logarithm of i, which would allow creating larger examples as we move forward with the tests, hoping that larger test cases might catch bugs smaller test cases could not demonstrate.
     </p>
     <p class="graf graf--p graf-after--p" id="b083" name="b083">
      2- It “shrinks” the failing test case. Shrinking means finding a minimal example using a failed test case. Let’s say that our fancy sorting function has a bug, it crashes when the list has negative numbers. This bug is found with the following test case.
     </p>
     <pre class="graf graf--pre graf-after--p" id="8b40" name="8b40"><code class="markup--code markup--pre-code">[11, 1,1,1,1,-1,1,2,442,34,2,4]</code></pre>
     <p class="graf graf--p graf-after--pre" id="4629" name="4629">
      But it could actually be found using.
     </p>
     <pre class="graf graf--pre graf-after--p" id="3d85" name="3d85"><code class="markup--code markup--pre-code">[-1]</code></pre>
     <p class="graf graf--p graf-after--pre" id="fece" name="fece">
      If I had given you the first list as the failing case, it would take a lot of time to debug. There are lots of cases, maybe the function crashes with lists of size more than 10, or it cannot handle cases where 4 list elements are same.
     </p>
     <p class="graf graf--p graf-after--p" id="c23e" name="c23e">
      But the second test case makes it very clear where the problem is and how to find and debug it.
     </p>
     <p class="graf graf--p graf-after--p" id="3bfa" name="3bfa">
      Let me give you a very simple and not-so-smart generator and shrinker for the case given above.
     </p>
     <figure class="graf graf--figure graf--iframe graf-after--p" id="3d68" name="3d68">
      <script src="https://gist.github.com/alpaylan/5d58af2914f98c6bdbee76bf9eb9f74c.js">
      </script>
     </figure>
     <p class="graf graf--p graf-after--figure" id="dca0" name="dca0">
      This generation function generates random integers from the interval
      <strong class="markup--strong markup--p-strong">
       <em class="markup--em markup--p-em">
        [-5, 10000)
       </em>
      </strong>
      for a list of size
      <strong class="markup--strong markup--p-strong">
       <em class="markup--em markup--p-em">
        log2size
       </em>
      </strong>
      .
     </p>
     <figure class="graf graf--figure graf--iframe graf-after--p" id="137b" name="137b">
      <script src="https://gist.github.com/alpaylan/eb5d8f5f2381d5b09bf7ea821bb2cf96.js">
      </script>
     </figure>
     <p class="graf graf--p graf-after--figure" id="c40d" name="c40d">
      This shrinking function tries to shrink the list by truncating it from the beginning. At each step, a smaller list is created by excluding the first element; this allows creating minimal examples for debugging the actual problem.
     </p>
     <p class="graf graf--p graf-after--p" id="7cb0" name="7cb0">
      This is the intuition behind Property Based Testing. There is a lot more to talk about, there is fuzzing, mutation based property based testing; there are clever ways of generating, shrinking, testing, writing properties… I want to write about those in the future too, I hope this was an interesting read for you.
     </p>
     <p class="graf graf--p graf-after--p" id="3f37" name="3f37">
      For those interested, here are some more interesting reading to follow through.
     </p>
     <ul class="postList">
      <li class="graf graf--li graf-after--p" id="629b" name="629b">
       Original QuickCheck Paper (
       <a class="markup--anchor markup--li-anchor" data-href="https://www.cs.tufts.edu/~nr/cs257/archive/john-hughes/quick.pdf" href="https://www.cs.tufts.edu/~nr/cs257/archive/john-hughes/quick.pdf" rel="noopener" target="_blank">
        https://www.cs.tufts.edu/~nr/cs257/archive/john-hughes/quick.pdf
       </a>
       )
      </li>
      <li class="graf graf--li graf-after--li" id="6265" name="6265">
       A Description of Random PBT and Fuzzing explaining motivations behind it by Leo and Mike (
       <a class="markup--anchor markup--li-anchor" data-href="https://plum-umd.github.io/projects/random-testing.html" href="https://plum-umd.github.io/projects/random-testing.html" rel="noopener" target="_blank">
        https://plum-umd.github.io/projects/random-testing.html
       </a>
       )
      </li>
      <li class="graf graf--li graf-after--li" id="8491" name="8491">
       A (probably better than mine) medium post on PBT (
       <a class="markup--anchor markup--li-anchor" data-href="https://medium.com/criteo-engineering/introduction-to-property-based-testing-f5236229d237" href="https://medium.com/criteo-engineering/introduction-to-property-based-testing-f5236229d237" target="_blank">
        https://medium.com/criteo-engineering/introduction-to-property-based-testing-f5236229d237
       </a>
       )
      </li>
      <li class="graf graf--li graf-after--li" id="3581" name="3581">
       A talk by John Huges, “Dont Write Tests” (
       <a class="markup--anchor markup--li-anchor" data-href="https://www.youtube.com/watch?v=hXnS_Xjwk2Y" href="https://www.youtube.com/watch?v=hXnS_Xjwk2Y" rel="noopener" target="_blank">
        https://www.youtube.com/watch?v=hXnS_Xjwk2Y
       </a>
       )
      </li>
     </ul>
     <p class="graf graf--p graf-after--li" id="8088" name="8088">
      Aside from the gists given above, I also uploaded the code to a single file for anyone interested as a convenience.
     </p>
     <p class="graf graf--p graf-after--p graf--trailing" id="10dc" name="10dc">
      <a class="markup--anchor markup--p-anchor" data-href="https://github.com/alpaylan/technical-blog-code/blob/main/pbt-1.py" href="https://github.com/alpaylan/technical-blog-code/blob/main/pbt-1.py" rel="nofollow noopener" target="_blank">
       https://github.com/alpaylan/technical-blog-code/blob/main/pbt-1.py
      </a>
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
   <a href="https://medium.com/p/ce979c1a58a1">
    <time class="dt-published" datetime="2021-11-11T04:29:26.672Z">
     November 11, 2021
    </time>
   </a>
   .
  </p>
  <p>
   <a class="p-canonical" href="https://medium.com/@alpkeles99/learners-guide-to-property-based-testing-1-ce979c1a58a1">
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
