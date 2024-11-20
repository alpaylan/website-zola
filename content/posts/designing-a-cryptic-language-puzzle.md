+++
title = "Designing A Cryptic Language Puzzle"
date = "2024-03-23"
[taxonomies]
tags = ['puzzle']
language = ["en"]
+++

<article class="h-entry">
 <section class="e-content" data-field="body">
  <section class="section section--body section--first section--last" name="1d68">
   <div class="section-content">
    <div class="section-inner sectionLayout--insetColumn">
     <h3 class="graf graf--h3 graf--leading graf--title" id="d049" name="d049">
      Designing A Cryptic
                            Language Puzzle
     </h3>
     <p class="graf graf--p graf-after--h3" id="19bc" name="19bc">
      Last week, I published a Cryptic
                            Language called Kelesce on my website, with a given text as the puzzle, and some set of
                            clues I added to the website over the course of the week. Below is a small piece of the
                            puzzle and a link to the website.
     </p>
     <p class="graf graf--p graf-after--p" id="9b41" name="9b41">
      …
     </p>
     <p class="graf graf--p graf-after--p" id="d066" name="d066">
      <strong class="markup--strong markup--p-strong">
       If you are interested in solving the puzzle, DO
                                NOT READ the rest of this article, as it spoils the design and the solution. Click the
                                link below and go to the puzzle site.
      </strong>
     </p>
     <div class="graf graf--mixtapeEmbed graf-after--p" id="c860" name="c860">
      <a class="markup--anchor markup--mixtapeEmbed-anchor" data-href="https://puzzle.alperenkeles.com/" href="https://puzzle.alperenkeles.com/" title="https://puzzle.alperenkeles.com/">
       <strong class="markup--strong markup--mixtapeEmbed-strong">
        Kelesce
       </strong>
       <br/>
       <em class="markup--em markup--mixtapeEmbed-em">
        A fun coding
                                    puzzle
       </em>
       puzzle.alperenkeles.com
      </a>
      <a class="js-mixtapeImage mixtapeImage mixtapeImage--empty u-ignoreBlock" data-media-id="55cc0316df8b7f9d6fd704e4fe99016c" href="https://puzzle.alperenkeles.com/">
      </a>
     </div>
     <figure class="graf graf--figure graf-after--mixtapeEmbed" id="f674" name="f674">
      <img class="graf-image" data-height="968" data-image-id="1*kvp0GFtSjtPPMikVRWljaA.png" data-is-featured="true" data-width="2388" src="https://cdn-images-1.medium.com/max/800/1*kvp0GFtSjtPPMikVRWljaA.png"/>
      <figcaption class="imageCaption">
       First 10 words!
      </figcaption>
     </figure>
     <p class="graf graf--p graf-after--figure" id="f0aa" name="f0aa">
      This article is two fold. The
                            first part focuses my thought process on creating Kelesce, and the second part focuses on
                            the decipher implementation.
     </p>
     <h3 class="graf graf--h3 graf-after--p" id="59fc" name="59fc">
      A Very Short Cryptology Primer
     </h3>
     <p class="graf graf--p graf-after--h3" id="8f19" name="8f19">
      Cryptography 101 lectures usually
                            start with the history of cryptology, and the famous
      <a class="markup--anchor markup--p-anchor" data-href="https://en.wikipedia.org/wiki/Caesar_cipher" href="https://en.wikipedia.org/wiki/Caesar_cipher" rel="noopener" target="_blank">
       Caesar
                                Cipher
      </a>
      . In a caesar cipher, encryption relies on some distance metric
      <em class="markup--em markup--p-em">
       d
      </em>
      that shifts the value of each letter by the given
                            amount. Below, we see a Caesar(2), where each letter is mapped to the letter that comes 2
                            after them.
     </p>
     <figure class="graf graf--figure graf-after--p" id="8716" name="8716">
      <img class="graf-image" data-height="666" data-image-id="1*IkXv-Orws3cjSeet7MF-Rg.png" data-width="1252" src="https://cdn-images-1.medium.com/max/800/1*IkXv-Orws3cjSeet7MF-Rg.png"/>
      <figcaption class="imageCaption">
       A Simple Illustration of a Caesar Cipher
      </figcaption>
     </figure>
     <p class="graf graf--p graf-after--figure" id="efde" name="efde">
      It is pretty simple to come up
                            with a Caesar Cipher implementation on the fly. Below is a sample Python implementation for
                            a very naive Caesar Cipher.
     </p>
     <pre class="graf graf--pre graf-after--p graf--preV2" data-code-block-lang="python" data-code-block-mode="1" id="4a61" name="4a61" spellcheck="false"><span class="pre--content"><span class="hljs-comment"># This implementation assumes ASCII encoding, </span><br><span class="hljs-comment"># and all alphanumeric characters.</span><br/><span class="hljs-keyword">def</span> <span class="hljs-title function_">caesar_cipher</span>(<span class="hljs-params">text, shift</span>):<br/>    result = <span class="hljs-string">""</span><br/>    <span class="hljs-keyword">for</span> i <span class="hljs-keyword">in</span> <span class="hljs-built_in">range</span>(<span class="hljs-built_in">len</span>(text)):<br/>        char = text[i]<br/>        <span class="hljs-keyword">if</span> char.isupper():<br/>            result += <span class="hljs-built_in">chr</span>((<span class="hljs-built_in">ord</span>(char) + shift - <span class="hljs-number">65</span>) % <span class="hljs-number">26</span> + <span class="hljs-number">65</span>)<br/>        <span class="hljs-keyword">else</span>:<br/>            result += <span class="hljs-built_in">chr</span>((<span class="hljs-built_in">ord</span>(char) + shift - <span class="hljs-number">97</span>) % <span class="hljs-number">26</span> + <span class="hljs-number">97</span>)<br/>    <span class="hljs-keyword">return</span> result</br></span></pre>
     <p class="graf graf--p graf-after--pre" id="963b" name="963b">
      Deciphering a Caesar Cipher is
                            also rather straightforward. You can just try all 25 potential shifts and see which one
                            turns the cryptic result into a legible English sentence.
     </p>
     <h3 class="graf graf--h3 graf-after--p" id="a361" name="a361">
      How to Design A New Cipher for Fun
     </h3>
     <p class="graf graf--p graf-after--h3" id="2248" name="2248">
      So, we saw the oldest cipher in the
                            world, now the question is can we design a new one that is not already out there. (full
                            disclosure, I’m not a cryptography expert, and it’s very probably that my design is not
                            actually novel)
     </p>
     <p class="graf graf--p graf-after--p" id="bac3" name="bac3">
      There are several design principles
                            I use:
     </p>
     <ul class="postList">
      <li class="graf graf--li graf-after--p" id="885a" name="885a">
       The cipher-text should be
                                easy(and unambiguous) to decipher for someone who knows the ciphering mechanism.
      </li>
      <li class="graf graf--li graf-after--li" id="b5fa" name="b5fa">
       Cipher should consist of
                                multiple layers, so the game(of solving) has a feeling of progress, and it is easy to
                                provide hints when needed without spoiling all the fun.
      </li>
      <li class="graf graf--li graf-after--li" id="f6ef" name="f6ef">
       The layers should be not be
                                simply rigorous mathematical obfuscations, using magic numbers that can only be
                                discovered by some complex brute force search; but rather simple but interesting ideas.
      </li>
     </ul>
     <p class="graf graf--p graf-after--li" id="557a" name="557a">
      I guess you could say these are
                            kind of obvious, and not very helpful, so let’s try to get into the real thing. How to
                            design Kelesce?
     </p>
     <h4 class="graf graf--h4 graf-after--p" id="5a7c" name="5a7c">
      Phase 1: Decide on a
                            central theme.
     </h4>
     <p class="graf graf--p graf-after--h4" id="bc36" name="bc36">
      What should be the focus of the
                            language? Should it be text, emojis, maybe music? I could use sound waves and frequencies,
                            or I could go into 2d visual structures, which opens up a whole new world. I could use
                            polygons, blobs made out of bezier curves, I could add new dimensions using colors, or as in
                            the case of Kelesce,
      <strong class="markup--strong markup--p-strong">
       I could just use
                                lines
      </strong>
      .
     </p>
     <h4 class="graf graf--h4 graf-after--p" id="b81e" name="b81e">
      Phase 2: Decide on the unit of
                            analysis.
     </h4>
     <p class="graf graf--p graf-after--h4" id="ba5d" name="ba5d">
      Every cipher has a unit of
                            analysis, the smallest structure you can independently analyze. In the case of a Caesar
                            Cipher, the unit of analysis is one character. If instead we use a
      <a class="markup--anchor markup--p-anchor" data-href="https://en.wikipedia.org/wiki/Vigenère_cipher" href="https://en.wikipedia.org/wiki/Vigenère_cipher" rel="noopener" target="_blank">
       Vigenère
                                cipher
      </a>
      , which generalized Caesar Cipher to arbitrary length units by using a list of
                            shifts instead of only one. Whereas a Caesar Cipher might have
      <strong class="markup--strong markup--p-strong">
       2
      </strong>
      as its shift factor, a Vigenère
                            cipher has some list [2, 5, 3, 6], where all characters
      <code class="markup--code markup--p-code">
       % 4
      </code>
      is ciphered with 2, all characters
      <code class="markup--code markup--p-code">
       %4 + 1
      </code>
      is ciphered with 5 and so on. The unit
                            of analysis for a Vigenère cipher is the length of its key list.
     </p>
     <p class="graf graf--p graf-after--p" id="1bc9" name="1bc9">
      In our case, the unit of analysis is
                            a
      <strong class="markup--strong markup--p-strong">
       word.
      </strong>
      Each square in Kelesce is a
                            word, and the cipher-text for two different words do not depend on each other, hence they
                            can be separately analyzed.
     </p>
     <h4 class="graf graf--h4 graf-after--p" id="28a7" name="28a7">
      Phase 3: Start putting your
                            obfuscation layers in.
     </h4>
     <p class="graf graf--p graf-after--h4" id="73be" name="73be">
      Now that we decided on our theme
                            and the largest dependent cipher unit, we need to decide how to cipher it. We need to define
                            some
      <strong class="markup--strong markup--p-strong">
       signals
      </strong>
      and
      <strong class="markup--strong markup--p-strong">
       noise
      </strong>
      that will disguise our signals.
                            The signals define how we map the cipher-text with the plain-text, and the noise hides the
                            signals from the viewer.
     </p>
     <p class="graf graf--p graf-after--p" id="06fe" name="06fe">
      <strong class="markup--strong markup--p-strong">
       Layer 1: Represent every letter using
                                ratios.
      </strong>
     </p>
     <p class="graf graf--p graf-after--p" id="75e8" name="75e8">
      The first decision I made when
                            creating Kelesce was about how to express each letter, and I decided to use ratios that
                            increase/decrease by 0.05 throughout the English alphabet.
     </p>
     <pre class="graf graf--pre graf-after--p graf--preV2" data-code-block-lang="dart" data-code-block-mode="1" id="e4f9" name="e4f9" spellcheck="false"><span class="pre--content">A/a =&gt; <span class="hljs-number">1</span><br/>B/b =&gt; <span class="hljs-number">1.05</span><br/>C/c =&gt; <span class="hljs-number">0.95</span><br/>D/d =&gt; <span class="hljs-number">1.10</span><br/>E/e =&gt; <span class="hljs-number">0.90</span><br/>... and so <span class="hljs-keyword">on</span></span></pre>
     <p class="graf graf--p graf-after--pre" id="886e" name="886e">
      It is important to note that these
                            ratios can be actually used in so many different ways. I could use them as line lengths with
                            respect to some magic number, I could make them areas, or I could turn them into colors.
                            There goes my second decision.
     </p>
     <p class="graf graf--p graf-after--p" id="aed0" name="aed0">
      <strong class="markup--strong markup--p-strong">
       Layer 2: Represent each letter using 2
                                lines.
      </strong>
     </p>
     <p class="graf graf--p graf-after--p" id="5e2f" name="5e2f">
      I decided to use 2 lines for each
                            letter, where the ratio is the length of the first line to the length of the second line.
     </p>
     <figure class="graf graf--figure graf-after--p" id="8031" name="8031">
      <img class="graf-image" data-height="732" data-image-id="1*UmFQqWN9iizHeMYMs5OIqA.png" data-width="1730" src="https://cdn-images-1.medium.com/max/800/1*UmFQqWN9iizHeMYMs5OIqA.png"/>
     </figure>
     <p class="graf graf--p graf-after--figure" id="a213" name="a213">
      This decision has an important
                            consequence, namely that it reduces the scope of the cipher to mostly programmers, as it’s
                            quite hard to manually measure the ratios.
     </p>
     <p class="graf graf--p graf-after--p" id="42ae" name="42ae">
      So, now we know how to decode a
                            letter when we see one, we just compute the ratios of the lines and we are done, but where
                            do we even put the lines?
     </p>
     <p class="graf graf--p graf-after--p" id="c2e6" name="c2e6">
      <strong class="markup--strong markup--p-strong">
       Layer 3: Rotate, rotate, rotate,
                                rotate…
      </strong>
     </p>
     <p class="graf graf--p graf-after--p" id="ee83" name="ee83">
      We defined how to represent a word
                            in abstract terms, but how do we concretely place and compose the letters such that they are
                            unambiguously decipherable?
     </p>
     <p class="graf graf--p graf-after--p" id="eed4" name="eed4">
      <strong class="markup--strong markup--p-strong">
       The first decision
      </strong>
      I made is to put
                            them inside squares.
     </p>
     <p class="graf graf--p graf-after--p" id="583d" name="583d">
      <strong class="markup--strong markup--p-strong">
       The second decision
      </strong>
      is that each line
                            pair starts from a random position on one side of the square, and makes a counter-clockwise
                            turn(top-to-right, right-to-bottom…).
     </p>
     <p class="graf graf--p graf-after--p" id="bb82" name="bb82">
      <strong class="markup--strong markup--p-strong">
       The third decision
      </strong>
      is that the first
                            line starts from the top, and runs clockwise(top, right, bottom, left, top…).
     </p>
     <figure class="graf graf--figure graf-after--p" id="cfce" name="cfce">
      <img class="graf-image" data-height="961" data-image-id="1*wiseH3Xnj1e8rzMcRXEBYQ.png" data-width="2956" src="https://cdn-images-1.medium.com/max/800/1*wiseH3Xnj1e8rzMcRXEBYQ.png"/>
     </figure>
     <p class="graf graf--p graf-after--figure" id="b084" name="b084">
      The next question is how to
                            handle the fifth letter, because now we have ambiguity. If there are two lines starting at
                            the top, which one is the first and which one is the fifth?
     </p>
     <p class="graf graf--p graf-after--p" id="ba0b" name="ba0b">
      <strong class="markup--strong markup--p-strong">
       Layer 5: When in doubt, nest.
      </strong>
     </p>
     <p class="graf graf--p graf-after--p" id="df44" name="df44">
      This was an choice, when you need to
                            reuse a side, pick a position on the inner rectangle constrained by the previous word. See
                            the figure below for clarity.
     </p>
     <figure class="graf graf--figure graf-after--p" id="7ebb" name="7ebb">
      <img class="graf-image" data-height="954" data-image-id="1*ON8BjnIxFBBw4RGkFMl3sA.png" data-width="852" src="https://cdn-images-1.medium.com/max/800/1*ON8BjnIxFBBw4RGkFMl3sA.png"/>
     </figure>
     <p class="graf graf--p graf-after--figure" id="25c3" name="25c3">
      This way, when you are reading
                            the cipher-text, you start from the largest rectangle for the current edge of the rectangle,
                            and go progressively inside, as if you’re peeling an onion.
     </p>
     <p class="graf graf--p graf-after--p" id="de2a" name="de2a">
      <strong class="markup--strong markup--p-strong">
       Layer 6: Normalization
      </strong>
     </p>
     <p class="graf graf--p graf-after--p" id="72f3" name="72f3">
      As you might have realized, I never
                            talked about punctuations, and I use the same ratios for uppercase and lowercase letters, so
                            the given plain text is first processed into a normalized form, and then converted into the
                            lines and squares.
     </p>
     <p class="graf graf--p graf-after--p" id="b109" name="b109">
      The first part of the normalization
                            is that all characters that are not from the English alphabet are deleted, all characters
                            are lowercased, and words are merged together.
     </p>
     <pre class="graf graf--pre graf-after--p graf--preV2" data-code-block-lang="ini" data-code-block-mode="1" id="dff1" name="dff1" spellcheck="false"><span class="pre--content"><span class="hljs-attr">"Hello, World!"</span> =&gt; <span class="hljs-string">"helloworld"</span></span></pre>
     <p class="graf graf--p graf-after--pre" id="d36f" name="d36f">
      With that, we conclude our
                            obfuscation layers. There is one more small transformation I added for the sake of
                            aesthetics, but it doesn’t affect the cipher that much. I wanted the puzzle to look nicer,
                            so I added a little bit of padding words at the end. If the length of the text is not a
                            multiple of 5, then a number of “hahaha” is added to the text to make it a multiple of 5.
      <strong class="markup--strong markup--p-strong">
       So, the last word in the clue is
                                hahaha
      </strong>
      .
     </p>
     <h3 class="graf graf--h3 graf-after--p" id="9d85" name="9d85">
      Part 2: How to implement a
                            deciphering algorithm for Kelesce?
     </h3>
     <p class="graf graf--p graf-after--h3" id="0292" name="0292">
      I hope others who solve the puzzle
                            on their own post some write-ups, but for now I’ll share my own methodology.
     </p>
     <p class="graf graf--p graf-after--p" id="f84f" name="f84f">
      The 4th clue, which is “Two is all
                            you need”, actually refers to the solution, where 2 pixels are actually all you need. If you
                            can detect the starting and end points of a line, you can decide which letter it is.
     </p>
     <p class="graf graf--p graf-after--p" id="bdb1" name="bdb1">
      The algorithm for line detection is
                            rather cumbersome to implement but it’s not really complicated.
     </p>
     <p class="graf graf--p graf-after--p" id="c826" name="c826">
      <strong class="markup--strong markup--p-strong">
       The first step
      </strong>
      is to find all points
                            where a line is perpendicular to an edge.
     </p>
     <p class="graf graf--p graf-after--p" id="8d5c" name="8d5c">
      <strong class="markup--strong markup--p-strong">
       The second step
      </strong>
      is to follow the line
                            as far as it goes.
     </p>
     <p class="graf graf--p graf-after--p" id="4d14" name="4d14">
      <strong class="markup--strong markup--p-strong">
       The third step
      </strong>
      is to turn
                            counter-clockwise, and find the other edge.
     </p>
     <figure class="graf graf--figure graf-after--p" id="90e6" name="90e6">
      <img class="graf-image" data-height="1004" data-image-id="1*mrEDnG6zKF16X0dz_5jFAg.png" data-width="3057" src="https://cdn-images-1.medium.com/max/800/1*mrEDnG6zKF16X0dz_5jFAg.png"/>
     </figure>
     <p class="graf graf--p graf-after--figure" id="ca10" name="ca10">
      <strong class="markup--strong markup--p-strong">
       The forth step
      </strong>
      is to convert the line
                            ratios into letters, and order the letters in the way they are positioned, and we are done.
     </p>
     <p class="graf graf--p graf-after--p" id="cd6b" name="cd6b">
      Of course, this algorithm has a few
                            pitfalls(if a parallel line is right next to the edge, it might think there are 198 lines
                            leaning against that edge, or if there are two overlapping lines), but they don’t show up in
                            practice.
     </p>
     <figure class="graf graf--figure graf-after--p" id="dff9" name="dff9">
      <img class="graf-image" data-height="1001" data-image-id="1*h8_hO2Z-vb5P1CKIqFRo0Q.png" data-width="1929" src="https://cdn-images-1.medium.com/max/800/1*h8_hO2Z-vb5P1CKIqFRo0Q.png"/>
     </figure>
     <h3 class="graf graf--h3 graf-after--figure" id="a70d" name="a70d">
      Close-up
     </h3>
     <p class="graf graf--p graf-after--h3 graf--trailing" id="a2a9" name="a2a9">
      With that, I
                            conclude the article. If you tried to solve the puzzle, I hope you had fun trying! If you
                            just read the article, I hope you liked it!
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
   <a href="https://medium.com/p/36d480faec51">
    <time class="dt-published" datetime="2024-03-23T16:05:43.471Z">
     March 23, 2024
    </time>
   </a>
   .
  </p>
  <p>
   <a class="p-canonical" href="https://medium.com/@alpkeles99/designing-a-cryptic-language-puzzle-36d480faec51">
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
