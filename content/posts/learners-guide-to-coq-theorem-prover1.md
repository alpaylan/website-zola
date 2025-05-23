+++
title = "Learner’s Guide to Coq Theorem Prover#1"
date = "2023-04-21"
[taxonomies]
tags = ['software engineering', 'algorithms', 'formal verification']
language = ["en"]
+++

<article class="h-entry">
 <section class="e-content" data-field="body">
  <section class="section section--body section--first section--last" name="88bb">
   <div class="section-content">
    <div class="section-inner sectionLayout--insetColumn">
     <h3 class="graf graf--h3 graf--leading graf--title" id="2f61" name="2f61">
      Learner’s Guide to Coq
                            Theorem Prover#1
     </h3>
     <p class="graf graf--p graf-after--h3" id="16f6" name="16f6">
      Before I begin, I must state that I
                            am pretty much not qualified to write about theorem proving in Coq, but that was pretty much
                            the idea behind Learning From Learners, so I decided to try anyway.
     </p>
     <figure class="graf graf--figure graf-after--p" id="616c" name="616c">
      <img class="graf-image" data-height="242" data-image-id="1*dugdANnZXpIZV9h4d6y3ag.png" data-is-featured="true" data-width="618" src="https://cdn-images-1.medium.com/max/800/1*dugdANnZXpIZV9h4d6y3ag.png"/>
      <figcaption class="imageCaption">
       <a class="markup--anchor markup--figure-anchor" data-href="https://xkcd.com/1856/" href="https://xkcd.com/1856/" rel="noopener" target="_blank">
        https://xkcd.com/1856/
       </a>
      </figcaption>
     </figure>
     <p class="graf graf--p graf-after--figure" id="c77f" name="c77f">
      If you want a more
                            comprehensive lecture style interactive book, go with a classic,
      <a class="markup--anchor markup--p-anchor" data-href="https://softwarefoundations.cis.upenn.edu" href="https://softwarefoundations.cis.upenn.edu" rel="noopener" target="_blank">
       Software
                                Foundations
      </a>
      ; if you wanna have your mind blown by dependent types, go with
      <a class="markup--anchor markup--p-anchor" data-href="http://adam.chlipala.net/cpdt/" href="http://adam.chlipala.net/cpdt/" rel="noopener" target="_blank">
       CPDT
      </a>
      ; if you
                            were as confused as I was when you hear about dependent types, I may be a good starting
                            point to show you “How to Start Playing Around With Coq”.
     </p>
     <p class="graf graf--p graf-after--p" id="7f45" name="7f45">
      So, what is Coq? According to
      <a class="markup--anchor markup--p-anchor" data-href="https://en.wikipedia.org/wiki/Coq" href="https://en.wikipedia.org/wiki/Coq" rel="noopener" target="_blank">
       Wikipedia
      </a>
      :
     </p>
     <blockquote class="graf graf--blockquote graf--startsWithDoubleQuote graf-after--p" id="69d1" name="69d1">
      “
      <strong class="markup--strong markup--blockquote-strong">
       Coq
      </strong>
      is an
      <a class="markup--anchor markup--blockquote-anchor" data-href="https://en.wikipedia.org/wiki/Proof_assistant" href="https://en.wikipedia.org/wiki/Proof_assistant" rel="noopener" target="_blank" title="Proof assistant">
       interactive theorem prover
      </a>
      first released in 1989. It allows for
                            expressing
      <a class="markup--anchor markup--blockquote-anchor" data-href="https://en.wikipedia.org/wiki/Mathematics" href="https://en.wikipedia.org/wiki/Mathematics" rel="noopener" target="_blank" title="Mathematics">
       mathematical
      </a>
      assertions, mechanically checks proofs of these
                            assertions, helps find formal proofs, and extracts a certified program from the
      <a class="markup--anchor markup--blockquote-anchor" data-href="https://en.wikipedia.org/wiki/Constructive_proof" href="https://en.wikipedia.org/wiki/Constructive_proof" rel="noopener" target="_blank" title="Constructive proof">
       constructive proof
      </a>
      of its
      <a class="markup--anchor markup--blockquote-anchor" data-href="https://en.wikipedia.org/wiki/Formal_specification" href="https://en.wikipedia.org/wiki/Formal_specification" rel="noopener" target="_blank" title="Formal specification">
       formal specification
      </a>
      ”.
     </blockquote>
     <p class="graf graf--p graf-after--blockquote" id="9f89" name="9f89">
      What is Coq? I hear you
                            asking again. Simply put, it’s a programming system that allows you to prove your programs.
                            You can write theorems about your code which then you can prove. It’s like testing, but
                            without the testing part, and it actually works.
     </p>
     <p class="graf graf--p graf-after--p" id="6b23" name="6b23">
      Let’s see the Hello World example
                            for Coq.
     </p>
     <figure class="graf graf--figure graf--iframe graf-after--p" id="281f" name="281f">
      <script src="https://gist.github.com/alpaylan/54cd1482e242e15283bf1c351cbe8cdc.js">
      </script>
     </figure>
     <p class="graf graf--p graf-after--figure" id="b95d" name="b95d">
      Let’s break this down.
      <code class="markup--code markup--p-code">
       bool
      </code>
      is your old classic
      <code class="markup--code markup--p-code">
       true
      </code>
      and
      <code class="markup--code markup--p-code">
       false
      </code>
      .
      <code class="markup--code markup--p-code">
       negb
      </code>
      is “Negate-Bool”.
      <code class="markup--code markup--p-code">
       negb_involutive
      </code>
      is the interesting part.
     </p>
     <p class="graf graf--p graf-after--p" id="e5ce" name="e5ce">
      <code class="markup--code markup--p-code">
       \forall b: bool, negb(negb b) = b
      </code>
      is our
                            first theorem. We can actually easily check it for each both
      <code class="markup--code markup--p-code">
       true
      </code>
      and
      <code class="markup--code markup--p-code">
       false
      </code>
      to see that it is true.
     </p>
     <p class="graf graf--p graf-after--p" id="7d87" name="7d87">
      <code class="markup--code markup--p-code">
       b=true: negb(negb true) = negb false = true
      </code>
     </p>
     <p class="graf graf--p graf-after--p" id="34c5" name="34c5">
      <code class="markup--code markup--p-code">
       b=false: negb(negb false) = negb true = false
      </code>
     </p>
     <p class="graf graf--p graf-after--p" id="0f77" name="0f77">
      In fact, the proof is exactly the
                            same. Of course, to understand that, you need to understand what is going on.
     </p>
     <p class="graf graf--p graf-after--p" id="897f" name="897f">
      When Coq sees the “Vernacular”
      <code class="markup--code markup--p-code">
       Theorem
      </code>
      , it expects a proof of the theorem
                            after its definition. Proofs conventionally start with the
      <code class="markup--code markup--p-code">
       Proof
      </code>
      vernacular, denoting the beginning of
                            the proof for documentation. The proof we see above is a sequence of “Tactics”, which are
                            basically building blocks for your proof. They hide the complexity of Coq “Proof Terms”, and
                            allow you to see your proof as a set of instructions.
     </p>
     <p class="graf graf--p graf-after--p" id="94fd" name="94fd">
      Let me try to give a
      <strong class="markup--strong markup--p-strong">
       quick
      </strong>
      explanation of that paragraph.
     </p>
     <p class="graf graf--p graf-after--p" id="39f4" name="39f4">
      A Coq program does not have a
                            special proof mode. It is just a program. The difference is, it has dependent types. These
                            are types that depend on values. They allow you to write your types as theorems. So,
      <code class="markup--code markup--p-code">
       \forall b: bool, negb(negb b) = b
      </code>
      is the type
                            of
      <code class="markup--code markup--p-code">
       negb_involutive
      </code>
      . What do programs
                            written in statically-typed languages do? They type-check.
     </p>
     <p class="graf graf--p graf-after--p" id="5f5b" name="5f5b">
      So, when you have a definition that
                            has a theorem as its type, you are supposed to write its proof, which would be the code that
                            will allow the function to type-check correctly. It is not much different than the fact that
                            we need a function returning integer to return an integer.
      <strong class="markup--strong markup--p-strong">
       (Kidding)
      </strong>
     </p>
     <p class="graf graf--p graf-after--p" id="c2e7" name="c2e7">
      This phenomenon of “types are
                            theorems, programs are proofs” arises from
      <a class="markup--anchor markup--p-anchor" data-href="https://en.wikipedia.org/wiki/Curry–Howard_correspondence" href="https://en.wikipedia.org/wiki/Curry–Howard_correspondence" rel="noopener" target="_blank">
       Curry-Howard
                                Correspondence
      </a>
      for anyone curious to go more into detail.
     </p>
     <p class="graf graf--p graf-after--p" id="4ae7" name="4ae7">
      <em class="markup--em markup--p-em">
       For the Javascript people, Tactics are like JSX elements
                                hiding the HTML/CSS/Js behind.
      </em>
     </p>
     <p class="graf graf--p graf-after--p" id="8135" name="8135">
      A Vernacular is a top-level
                            statement to tell Coq program is going to behave in a certain way. There are many different
                            vernaculars,
      <code class="markup--code markup--p-code">
       Inductive, Definition, Proof
      </code>
      are three examples we have on the small piece of code.
     </p>
     <p class="graf graf--p graf-after--p" id="5d78" name="5d78">
      Now, we can go inside the proof.
     </p>
     <pre class="graf graf--pre graf-after--p graf--preV2" data-code-block-lang="coq" data-code-block-mode="0" id="6be9" name="6be9" spellcheck="false"><span class="pre--content">Proof.<br/>intros b. <br/>destruct b eqn:E.<br/>- reflexivity.<br/>- reflexivity.<br/>Qed.</span></pre>
     <ul class="postList">
      <li class="graf graf--li graf-after--pre" id="6248" name="6248">
       <code class="markup--code markup--li-code">
        Proof
       </code>
       is used to denote the start of
                                sequence of tactics.
      </li>
      <li class="graf graf--li graf-after--li" id="1920" name="1920">
       <code class="markup--code markup--li-code">
        intros b
       </code>
       turns
       <code class="markup--code markup--li-code">
        \forall b
       </code>
       into
       <code class="markup--code markup--li-code">
        b
       </code>
       in order to operate on the variable.
      </li>
      <li class="graf graf--li graf-after--li" id="55a2" name="55a2">
       <code class="markup--code markup--li-code">
        destruct b eqn:E
       </code>
       is “Proof by Cases”.
                                Remember,
       <code class="markup--code markup--li-code">
        Inductive bool
       </code>
       had two
                                “constructors/members”,
       <code class="markup--code markup--li-code">
        true
       </code>
       and
       <code class="markup--code markup--li-code">
        false
       </code>
       . Hence, destructing b gives you
                                two cases,
       <code class="markup--code markup--li-code">
        b=true
       </code>
       and
       <code class="markup--code markup--li-code">
        b=false
       </code>
       , we have now decided the value
                                of the variable.
      </li>
      <li class="graf graf--li graf-after--li" id="ae28" name="ae28">
       Each
       <code class="markup--code markup--li-code">
        -
       </code>
       allows us to focus on a single case,
       <code class="markup--code markup--li-code">
        reflexivity
       </code>
       just checks if two sides
                                of the equality is “definitionally equal”. What definitional equality is a question I
                                will not try to answer here.
      </li>
      <li class="graf graf--li graf-after--li" id="51cc" name="51cc">
       <code class="markup--code markup--li-code">
        Qed
       </code>
       signals Coq that we have finished
                                our proof, and we are ready for proof-checking. If proof-checking goes through, we start
                                to
       <a class="markup--anchor markup--li-anchor" data-href="https://tenor.com/bQ9Ws.gif" href="https://tenor.com/bQ9Ws.gif" rel="nofollow noopener" target="_blank">
        https://tenor.com/bQ9Ws.gif
       </a>
       ; else, we missed something in the
                                proof.
      </li>
     </ul>
     <p class="graf graf--p graf-after--li" id="af2d" name="af2d">
      As you see, there are lots of stuff
                            going on the background, even the simplest example of a proof has to go through some
                            complicated explanations. Yet, Coq is pretty good at abstracting many of these
                            complications, as does all of our other programming systems.
     </p>
     <p class="graf graf--p graf-after--p" id="0d73" name="0d73">
      I am thinking of moving on with
                            these series with some follow-up articles. They will be much simplified/cut versions of
                            Software Foundations, designed to mostly intrigue rather than teach. If this piece has
                            attracted your interest in proved programming and Coq, please check the sources I leave
                            below and let me know so I get motivated to write more about this.
     </p>
     <ul class="postList">
      <li class="graf graf--li graf-after--p" id="9861" name="9861">
       Software Foundations:
       <a class="markup--anchor markup--li-anchor" data-href="https://softwarefoundations.cis.upenn.edu/" href="https://softwarefoundations.cis.upenn.edu/" rel="noopener" target="_blank">
        https://softwarefoundations.cis.upenn.edu/
       </a>
      </li>
      <li class="graf graf--li graf-after--li" id="e762" name="e762">
       CPDT:
       <a class="markup--anchor markup--li-anchor" data-href="http://adam.chlipala.net/cpdt/" href="http://adam.chlipala.net/cpdt/" rel="noopener" target="_blank">
        http://adam.chlipala.net/cpdt/
       </a>
      </li>
      <li class="graf graf--li graf-after--li" id="92dc" name="92dc">
       Coq Website:
       <a class="markup--anchor markup--li-anchor" data-href="https://coq.inria.fr/a-short-introduction-to-coq" href="https://coq.inria.fr/a-short-introduction-to-coq" rel="noopener" target="_blank">
        https://coq.inria.fr/a-short-introduction-to-coq
       </a>
      </li>
      <li class="graf graf--li graf-after--li" id="6baa" name="6baa">
       Turkish Youtube Video by
       <a class="markup--anchor markup--li-anchor" data-href="http://joomy.korkutblech.com" href="http://joomy.korkutblech.com" rel="noopener" target="_blank">
        <strong class="markup--strong markup--li-strong">
         Joomy
        </strong>
       </a>
       :
       <a class="markup--anchor markup--li-anchor" data-href="https://www.youtube.com/watch?v=llQTJuO65Kk" href="https://www.youtube.com/watch?v=llQTJuO65Kk" rel="noopener" target="_blank">
        https://www.youtube.com/watch?v=llQTJuO65Kk
       </a>
      </li>
      <li class="graf graf--li graf-after--li" id="6e08" name="6e08">
       Learn X in Y Minutes:
       <a class="markup--anchor markup--li-anchor" data-href="https://learnxinyminutes.com/docs/coq/" href="https://learnxinyminutes.com/docs/coq/" rel="noopener" target="_blank">
        https://learnxinyminutes.com/docs/coq/
       </a>
      </li>
     </ul>
    </div>
    <div class="section-inner sectionLayout--outsetRow" data-paragraph-count="2">
     <figure class="graf graf--figure graf--layoutOutsetRow is-partialWidth graf-after--li" id="b5f9" name="b5f9" style="width: 47.424%;">
      <img class="graf-image" data-height="640" data-image-id="1*DORzPabprYmsShRUBYN3jA.png" data-width="577" src="https://cdn-images-1.medium.com/max/600/1*DORzPabprYmsShRUBYN3jA.png"/>
     </figure>
     <figure class="graf graf--figure graf--layoutOutsetRowContinue is-partialWidth graf-after--figure graf--trailing" id="a276" name="a276" style="width: 52.576%;">
      <img class="graf-image" data-height="200" data-image-id="1*e5SHfheTSuANvryZ8m6NYg.png" data-width="200" src="https://cdn-images-1.medium.com/max/800/1*e5SHfheTSuANvryZ8m6NYg.png"/>
      <figcaption class="imageCaption" style="width: 190.201%; left: -90.201%;">
       Left(Le coq
                                mécanisé taken from Ilya Sergey’s website, created by
       <a class="markup--anchor markup--figure-anchor" data-href="https://www.liliaanisimova.com/" href="https://www.liliaanisimova.com/" rel="noopener" target="_blank">
        https://www.liliaanisimova.com/
       </a>
       ), Right(Coq logo from Twitter)
      </figcaption>
     </figure>
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
   <a href="https://medium.com/p/e380c9e360b8">
    <time class="dt-published" datetime="2023-04-21T04:19:48.296Z">
     April 21, 2023
    </time>
   </a>
   .
  </p>
  <p>
   <a class="p-canonical" href="https://medium.com/@alpkeles99/learners-guide-to-coq-theorem-prover-1-e380c9e360b8">
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
