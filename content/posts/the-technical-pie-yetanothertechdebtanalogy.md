+++
title = "The Technical Pie (Yet-Another-Tech-Debt-Analogy)"
date = "2023-06-16"
[taxonomies]
tags = ['software engineering']
language = ["en"]
+++

<article class="h-entry">
 <section class="e-content" data-field="body">
  <section class="section section--body section--first section--last" name="4582">
   <div class="section-content">
    <div class="section-inner sectionLayout--insetColumn">
     <h3 class="graf graf--h3 graf--leading graf--title" id="2b4e" name="2b4e">
      The Technical Pie (Yet-Another-Tech-Debt-Analogy)
     </h3>
     <p class="graf graf--p graf-after--h3" id="f457" name="f457">
      Yesterday, I was listening to a talk by
      <a class="markup--anchor markup--p-anchor" data-href="https://twitter.com/TitusWinters" href="https://twitter.com/TitusWinters" rel="noopener" target="_blank">
       @TitusWinters
      </a>
      on why the current metaphors for “technical debt” are insufficient and fail to capture the reality of the situation. So, before going into the metaphors, what is the definition these metaphors try to capture?
     </p>
     <p class="graf graf--p graf-after--p" id="1088" name="1088">
      Here is a definition from wikipedia:
     </p>
     <blockquote class="graf graf--blockquote graf--hasDropCapModel graf-after--p" id="093e" name="093e">
      In
      <a class="markup--anchor markup--blockquote-anchor" data-href="https://en.wikipedia.org/wiki/Software_development" href="https://en.wikipedia.org/wiki/Software_development" rel="noopener" target="_blank">
       software development
      </a>
      , or any other IT field (e.g., Infrastructure, Networking, etc.)
      <strong class="markup--strong markup--blockquote-strong">
       technical debt
      </strong>
      (also known as
      <strong class="markup--strong markup--blockquote-strong">
       design debt
      </strong>
      <a class="markup--anchor markup--blockquote-anchor" data-href="https://en.wikipedia.org/wiki/Technical_debt#cite_note-Girish_2014-1" href="https://en.wikipedia.org/wiki/Technical_debt#cite_note-Girish_2014-1" rel="noopener" target="_blank">
       [1]
      </a>
      or
      <strong class="markup--strong markup--blockquote-strong">
       code debt
      </strong>
      ) is the implied cost of future reworking required when choosing an easy but limited solution instead of a better approach that could take more time.
     </blockquote>
     <p class="graf graf--p graf-after--blockquote" id="34f1" name="34f1">
      Here is another definition from a Dagstuhl in 2016:
     </p>
     <blockquote class="graf graf--blockquote graf--hasDropCapModel graf-after--p" id="5bb0" name="5bb0">
      In software-intensive systems, technical debt is a collection of design or implementation constructs that are expedient in the short term, but set up a technical context that can make future changes more costly or impossible. Technical debt presents an actual or contingent liability whose impact is limited to internal system qualities, primarily maintainability and evolvability.
     </blockquote>
     <p class="graf graf--p graf-after--blockquote" id="d048" name="d048">
      Although I don’t remember the exact wording, Titus had another definition that I really liked, where the basic idea was “technical debt is the difference between the software we have, and the software we wish we had”.
     </p>
     <p class="graf graf--p graf-after--p" id="3f5a" name="3f5a">
      So, these are some of the definitions. Even though there isn’t an agreement on a fixed definition, probably all engineer have some internal conception of it. Technical debt is sometimes the doc or the test we didn’t write, sometimes the one edge case we didn’t handle, sometimes the design we know will force us to a redesign but we are using for now. It doesn’t even have to be this negative, sometimes it is the decisions we take in conditions we know will change, where we have to make a choice even though we know that’s probably not the right one.
     </p>
     <p class="graf graf--p graf-after--p" id="df74" name="df74">
      What about the metaphors? There were four of them in the presentation.
     </p>
     <ol class="postList">
      <li class="graf graf--li graf-after--p" id="0816" name="0816">
       <strong class="markup--strong markup--li-strong">
        Debt.
       </strong>
       This is the classic example. It’s very intuitive, we think we are borrowing some time/money from our future selves. The interest rate acts as the cost of pushing the effort to future.
      </li>
      <li class="graf graf--li graf-after--li" id="8932" name="8932">
       <strong class="markup--strong markup--li-strong">
        Pollution.
       </strong>
       Pollution is an interesting metaphor. The idea is basically that you are creating some pollution in your coding environment, which will require some cleanup at some point in the future. You are not the only one affected, other members, teams or organizations are also affected by the pollution you create.
      </li>
      <li class="graf graf--li graf-after--li" id="33e9" name="33e9">
       <strong class="markup--strong markup--li-strong">
        Cooking.
       </strong>
       Cooking has a more intuitive connection to software development, as it relays the idea of product development. When you are cooking, you might take shortcuts, you might leave some item on the sink at a particular moment as it is convenient, but you’ll have to pick it up in the future. If you leave too many things, you might suddenly encounter a full kitchen sink, representing the non-linear nature of technical debt, which is not really captured with the
       <strong class="markup--strong markup--li-strong">
        debt
       </strong>
       metaphor.
      </li>
      <li class="graf graf--li graf-after--li" id="ba95" name="ba95">
       <strong class="markup--strong markup--li-strong">
        Gardening.
       </strong>
       Gardening is taking the cooking metaphor one step forward. You are not just crafting a product, you also have to maintain it. Additionally, gardens are scalable, so you might be able to imagine a very large garden you need to attend to as you think of a bigger project. For cooking, it is hard to imagine how scaling up works.
      </li>
     </ol>
     <p class="graf graf--p graf-after--li" id="ee79" name="ee79">
      None of these metaphors perfectly captures the underlying idea of what software developers talk about when they mention technical debt. One could imagine how “not writing docs” convey into cooking. If you don’t write your recipes properly, how would your apprentice learn to use them? On the other hand, how does “not writing tests” convey into these examples, I don’t really know.
     </p>
     <p class="graf graf--p graf-after--p" id="acce" name="acce">
      The solution Titus had to this rather incompleteness of these metaphors was to throw them out. Instead of trying to talk about debt, pollution, failure to organize the kitchen or the garden, talk about inefficiencies. Tech debt is a problem because it creates other problems. It creates inefficiencies for the future of our engineering teams. Why don’t we just talk about inefficiencies and how to mitigate them?
     </p>
     <p class="graf graf--p graf-after--p" id="cb16" name="cb16">
      I have 2 disagreements with this idea;
     </p>
     <ol class="postList">
      <li class="graf graf--li graf-after--p" id="b1c5" name="b1c5">
       People tend to become very attached to powerful metaphors. Metaphors and analogies travel around, affect people much more deeply than arguments. Inefficiencies is much more abstract than debt, hence I don’t think it’s really possible in practice to make people talk about inefficiencies when talking about technical debt.
      </li>
      <li class="graf graf--li graf-after--li" id="2f8e" name="2f8e">
       Inefficiency is such an umbrella term, it is rather applicable to almost any domain, any concept. This generality makes it easy to classify virtually anything on the efficiency scale. I think that’s harmful because it makes tech debt “boring”.
      </li>
     </ol>
     <p class="graf graf--p graf-after--li" id="44fc" name="44fc">
      I also come up with another suggestion for a new metaphor,
      <strong class="markup--strong markup--p-strong">
       The Technical Pie
      </strong>
      .
     </p>
     <p class="graf graf--p graf-after--p" id="185a" name="185a">
      The technical pie relies on the fact that functional requirements are both related, and also orthogonal to quality requirements. I view the development of software as a non-linear journey.
     </p>
     <figure class="graf graf--figure graf-after--p" id="69df" name="69df">
      <img class="graf-image" data-height="697" data-image-id="1*b6vbOH_IH9C_JcquzfG-Mg.png" data-width="951" src="https://cdn-images-1.medium.com/max/800/1*b6vbOH_IH9C_JcquzfG-Mg.png"/>
     </figure>
     <p class="graf graf--p graf-after--figure" id="ef8f" name="ef8f">
      Think of the black dot as the beginning, each line as a functional requirement along the way. We sometimes struggle with the requirements, we go around, but we consistently move as we develop our project. What happens when quality requirements also come into play? I argue that our previous stack-like line based process becomes a circle.
     </p>
     <figure class="graf graf--figure graf-after--p" id="e325" name="e325">
      <img class="graf-image" data-height="1074" data-image-id="1*Rm2fi3ZeoJNtLyX6xFdYwA.png" data-width="1086" src="https://cdn-images-1.medium.com/max/800/1*Rm2fi3ZeoJNtLyX6xFdYwA.png"/>
     </figure>
     <p class="graf graf--p graf-after--figure" id="281a" name="281a">
      Whereas each layer of the circle represents a feature we develop, the direction of the arrow represents our perfect process. Within a perfect process with perfect quality, we would be moving alongside this perfect line. Yet, this isn’t what happens in real world.
     </p>
     <figure class="graf graf--figure graf-after--p" id="25eb" name="25eb">
      <img class="graf-image" data-height="1083" data-image-id="1*L2Amyz4mBBjdgK_XWdCb5g.png" data-width="2493" src="https://cdn-images-1.medium.com/max/800/1*L2Amyz4mBBjdgK_XWdCb5g.png"/>
     </figure>
     <p class="graf graf--p graf-after--figure" id="75fa" name="75fa">
      Consider these two examples. The left(green) case showcases a path where we finally align with the quality requirements, whereas the right(red) case shows that even though we have reached our functional goals, we are far from the quality requirements.
     </p>
     <p class="graf graf--p graf-after--p" id="d795" name="d795">
      So, what is technical debt?
     </p>
     <figure class="graf graf--figure graf-after--p" id="4b09" name="4b09">
      <img class="graf-image" data-height="1084" data-image-id="1*1mekx_uJLm1WTrizAEnF5Q.png" data-is-featured="true" data-width="2493" src="https://cdn-images-1.medium.com/max/800/1*1mekx_uJLm1WTrizAEnF5Q.png"/>
     </figure>
     <p class="graf graf--p graf-after--figure graf--trailing" id="ed80" name="ed80">
      Technical debt here is the blue slice, in other words, The Technical Pie. As you are developing a product, you have a target quality that can actually change in different phases. That is your baseline. Your efforts, as well as allowing you to develop your features, push or pull you towards this ideal quality line. The Technical Pie is the difference. To eat the pie, you either need to create a long term path to close the gap between the ideal and the reality, or quickly close the gap by pausing development of new features for a while, or some hybrid option between the two. You can also always change your ideal results.
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
   <a href="https://medium.com/p/e53a919c9e9f">
    <time class="dt-published" datetime="2023-06-16T05:36:43.585Z">
     June 16, 2023
    </time>
   </a>
   .
  </p>
  <p>
   <a class="p-canonical" href="https://medium.com/@alpkeles99/the-technical-pie-yet-another-tech-debt-analogy-e53a919c9e9f">
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
