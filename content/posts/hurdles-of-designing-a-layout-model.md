+++
title = "Hurdles of Designing A Layout Model"
date = "2023-08-06"
[taxonomies]
tags = ['software engineering']
language = ["en"]
+++

<article class="h-entry">
 <section class="e-content" data-field="body">
  <section class="section section--body section--first section--last" name="c6fa">
   <div class="section-content">
    <div class="section-inner sectionLayout--insetColumn">
     <h3 class="graf graf--h3 graf--leading graf--title" id="31c6" name="31c6">
      Hurdles of Designing A
                            Layout Model
     </h3>
     <p class="graf graf--p graf-after--h3" id="9e49" name="9e49">
      For the past 2 weeks, I have been
                            working on designing my own layout model for the
      <a class="markup--anchor markup--p-anchor" data-href="http://github.com/alpaylan/cvdl" href="http://github.com/alpaylan/cvdl" rel="noopener" target="_blank">
       document generator I’ve been working on
      </a>
      . I have
                            successfully failed to come up with a sound modal that’s expressive enough for all my use
                            cases. I decided to document my pains for (1) clearing my vision, (2) maybe helping out
                            anyone who ever tries to go in similar routes, (3) finding people to help me design better
                            as the best way to get answers to your questions on the internet is to provide wrong
                            answers. So, let’s talk about some really wrong layout models.
     </p>
     <h3 class="graf graf--h3 graf-after--p" id="7e9c" name="7e9c">
      What is the problem I am trying
                            to solve?
     </h3>
     <p class="graf graf--p graf-after--h3" id="ef1c" name="ef1c">
      Before going into the details of
                            the design, it is important to talk about what I am trying to solve here. What is the
                            document this layout model is supposed to represent?
     </p>
     <p class="graf graf--p graf-after--p" id="1d76" name="1d76">
      I am working on
      <a class="markup--anchor markup--p-anchor" data-href="http://github.com/alpaylan/cvdl" href="http://github.com/alpaylan/cvdl" rel="noopener" target="_blank">
       CVDL(CV
                                Description Language),
      </a>
      which is a misleading name at this point, because the project
                            is really about designing an extensible structured layout generator. The layout generator
                            mainly depends on
      <strong class="markup--strong markup--p-strong">
       data
      </strong>
      and
      <strong class="markup--strong markup--p-strong">
       layout schemas.
      </strong>
     </p>
     <h4 class="graf graf--h4 graf-after--p" id="9d88" name="9d88">
      Data Schema
     </h4>
     <p class="graf graf--p graf-after--h4" id="30b3" name="30b3">
      A data schema defines a set of
                            fields and their types. Below, you see an example data schema for a work experience section
                            of a CV.
     </p>
     <pre class="graf graf--pre graf-after--p graf--preV2" data-code-block-lang="json" data-code-block-mode="1" id="375e" name="375e" spellcheck="false"><span class="pre--content"><span class="hljs-punctuation">{</span><br/>    <span class="hljs-attr">"schema-name"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"Work-Experience"</span><span class="hljs-punctuation">,</span><br/>    <span class="hljs-attr">"header-schema"</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">[</span><br/>        <span class="hljs-punctuation">{</span> <span class="hljs-attr">"name"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"Title"</span><span class="hljs-punctuation">,</span> <span class="hljs-attr">"type"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"String"</span> <span class="hljs-punctuation">}</span><br/>    <span class="hljs-punctuation">]</span><span class="hljs-punctuation">,</span><br/>    <span class="hljs-attr">"item-schema"</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">[</span><br/>        <span class="hljs-punctuation">{</span> <span class="hljs-attr">"name"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"Company"</span><span class="hljs-punctuation">,</span> <span class="hljs-attr">"type"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"String"</span> <span class="hljs-punctuation">}</span><span class="hljs-punctuation">,</span><br/>        <span class="hljs-punctuation">{</span> <span class="hljs-attr">"name"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"Position"</span><span class="hljs-punctuation">,</span> <span class="hljs-attr">"type"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"String"</span> <span class="hljs-punctuation">}</span><span class="hljs-punctuation">,</span><br/>        <span class="hljs-punctuation">{</span> <span class="hljs-attr">"name"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"Skills"</span><span class="hljs-punctuation">,</span> <span class="hljs-attr">"type"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"List&lt;String&gt;"</span> <span class="hljs-punctuation">}</span><span class="hljs-punctuation">,</span><br/>        <span class="hljs-punctuation">{</span> <span class="hljs-attr">"name"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"Date-Started"</span><span class="hljs-punctuation">,</span> <span class="hljs-attr">"type"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"Date"</span> <span class="hljs-punctuation">}</span><span class="hljs-punctuation">,</span><br/>        <span class="hljs-punctuation">{</span> <span class="hljs-attr">"name"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"Date-Finished"</span><span class="hljs-punctuation">,</span> <span class="hljs-attr">"type"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"Date | String"</span> <span class="hljs-punctuation">}</span><span class="hljs-punctuation">,</span><br/>        <span class="hljs-punctuation">{</span> <span class="hljs-attr">"name"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"Location"</span><span class="hljs-punctuation">,</span> <span class="hljs-attr">"type"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"String"</span> <span class="hljs-punctuation">}</span><span class="hljs-punctuation">,</span><br/>        <span class="hljs-punctuation">{</span> <span class="hljs-attr">"name"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"Text"</span><span class="hljs-punctuation">,</span> <span class="hljs-attr">"type"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"MarkdownString"</span> <span class="hljs-punctuation">}</span><br/>    <span class="hljs-punctuation">]</span><br/><span class="hljs-punctuation">}</span><span class="hljs-punctuation">,</span></span></pre>
     <h4 class="graf graf--h4 graf-after--pre" id="e683" name="e683">
      Layout Schema
     </h4>
     <p class="graf graf--p graf-after--h4" id="02c7" name="02c7">
      A layout schema defines a mapping
                            of the variables in the data schema into the document. Below, you can see both the visual
                            representation and the JSON version of a layout schema for a work experience section.
     </p>
     <figure class="graf graf--figure graf-after--p" id="e19a" name="e19a">
      <img class="graf-image" data-height="1553" data-image-id="1*aF9dyyAmuLv95QmDj5uhzQ.png" data-is-featured="true" data-width="1985" src="https://cdn-images-1.medium.com/max/800/1*aF9dyyAmuLv95QmDj5uhzQ.png"/>
      <figcaption class="imageCaption">
       An Item Layout Schema for “Work-Experience” section
      </figcaption>
     </figure>
     <pre class="graf graf--pre graf-after--figure graf--preV2" data-code-block-lang="json" data-code-block-mode="1" id="2d80" name="2d80" spellcheck="false"><span class="pre--content"><span class="hljs-punctuation">[</span><br/>    <span class="hljs-punctuation">{</span><br/>        <span class="hljs-attr">"schema-name"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"Work-Experience"</span><span class="hljs-punctuation">,</span><br/>        <span class="hljs-attr">"header-layout-schema"</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">{</span><br/>            <span class="hljs-attr">"Ref"</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">{</span><br/>                <span class="hljs-attr">"item"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"Title"</span><span class="hljs-punctuation">,</span><br/>                <span class="hljs-attr">"width"</span><span class="hljs-punctuation">:</span> <span class="hljs-number">70</span><br/>            <span class="hljs-punctuation">}</span><br/>        <span class="hljs-punctuation">}</span><span class="hljs-punctuation">,</span><br/>        <span class="hljs-attr">"item-layout-schema"</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">{</span><br/>            <span class="hljs-attr">"Stack"</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">{</span><br/>                <span class="hljs-attr">"elements"</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">[</span><br/>                    <span class="hljs-punctuation">{</span><br/>                        <span class="hljs-attr">"FrozenRow"</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">{</span><br/>                            <span class="hljs-attr">"elements"</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">[</span><br/>                                <span class="hljs-punctuation">{</span><br/>                                    <span class="hljs-attr">"Ref"</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">{</span><br/>                                        <span class="hljs-attr">"item"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"Company"</span><br/>                                    <span class="hljs-punctuation">}</span><br/>                                <span class="hljs-punctuation">}</span><span class="hljs-punctuation">,</span><br/>                                <span class="hljs-punctuation">{</span><br/>                                    <span class="hljs-attr">"FrozenRow"</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">{</span><br/>                                        <span class="hljs-attr">"elements"</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">[</span><br/>                                            <span class="hljs-punctuation">{</span><br/>                                                <span class="hljs-attr">"Ref"</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">{</span><br/>                                                    <span class="hljs-attr">"item"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"Date-Started"</span><br/>                                                <span class="hljs-punctuation">}</span><br/>                                            <span class="hljs-punctuation">}</span><span class="hljs-punctuation">,</span><br/>                                            <span class="hljs-punctuation">{</span><br/>                                                <span class="hljs-attr">"Text"</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">{</span><br/>                                                    <span class="hljs-attr">"item"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"-"</span><br/>                                                <span class="hljs-punctuation">}</span><br/>                                            <span class="hljs-punctuation">}</span><span class="hljs-punctuation">,</span><br/>                                            <span class="hljs-punctuation">{</span><br/>                                                <span class="hljs-attr">"Ref"</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">{</span><br/>                                                    <span class="hljs-attr">"item"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"Date-Finished"</span><br/>                                                <span class="hljs-punctuation">}</span><br/>                                            <span class="hljs-punctuation">}</span><br/>                                        <span class="hljs-punctuation">]</span><span class="hljs-punctuation">,</span><br/>                                        <span class="hljs-attr">"width"</span><span class="hljs-punctuation">:</span> <span class="hljs-number">30</span><br/>                                    <span class="hljs-punctuation">}</span><br/>                                <span class="hljs-punctuation">}</span><br/>                            <span class="hljs-punctuation">]</span><br/>                        <span class="hljs-punctuation">}</span><br/>                    <span class="hljs-punctuation">}</span><span class="hljs-punctuation">,</span><br/>                    <span class="hljs-punctuation">{</span><br/>                        <span class="hljs-attr">"Ref"</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">{</span><br/>                            <span class="hljs-attr">"item"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"Position"</span><span class="hljs-punctuation">,</span><br/>                            <span class="hljs-attr">"width"</span><span class="hljs-punctuation">:</span> <span class="hljs-number">70</span><br/>                        <span class="hljs-punctuation">}</span><br/>                    <span class="hljs-punctuation">}</span><span class="hljs-punctuation">,</span><br/>                    <span class="hljs-punctuation">{</span><br/>                        <span class="hljs-attr">"Ref"</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">{</span><br/>                            <span class="hljs-attr">"item"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"Text"</span><span class="hljs-punctuation">,</span><br/>                            <span class="hljs-attr">"width"</span><span class="hljs-punctuation">:</span> <span class="hljs-number">70</span><br/>                        <span class="hljs-punctuation">}</span><br/>                    <span class="hljs-punctuation">}</span><span class="hljs-punctuation">,</span><br/>                    <span class="hljs-punctuation">{</span><br/>                        <span class="hljs-attr">"Ref"</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">{</span><br/>                            <span class="hljs-attr">"item"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"Skills"</span><span class="hljs-punctuation">,</span><br/>                            <span class="hljs-attr">"width"</span><span class="hljs-punctuation">:</span> <span class="hljs-number">70</span><br/>                        <span class="hljs-punctuation">}</span><br/>                    <span class="hljs-punctuation">}</span><br/>                <span class="hljs-punctuation">]</span><br/>            <span class="hljs-punctuation">}</span><br/>        <span class="hljs-punctuation">}</span><br/>    <span class="hljs-punctuation">}</span><br/><span class="hljs-punctuation">]</span></span></pre>
     <h3 class="graf graf--h3 graf-after--pre" id="7f10" name="7f10">
      What is the problem I am
                            actually dealing with?
     </h3>
     <p class="graf graf--p graf-after--h3" id="2326" name="2326">
      So, if I have both of these schemas
                            working with each other, what’s the problem?
      <strong class="markup--strong markup--p-strong">
       What’s the hurdle?
      </strong>
     </p>
     <p class="graf graf--p graf-after--p" id="1219" name="1219">
      The hurdle is the fact that I will
                            not always receive such well constructed layouts.
     </p>
     <figure class="graf graf--figure graf-after--p" id="801c" name="801c">
      <img class="graf-image" data-height="1756" data-image-id="1*QEESd-Rn1TdpacbuAKn1hg.png" data-width="2609" src="https://cdn-images-1.medium.com/max/800/1*QEESd-Rn1TdpacbuAKn1hg.png"/>
     </figure>
     <p class="graf graf--p graf-after--figure" id="f8ef" name="f8ef">
      I need sane default behaviors
                            for people to use this system. What should I do if I receive a specification as above? There
                            are various options.
     </p>
     <ol class="postList">
      <li class="graf graf--li graf-after--p" id="e24e" name="e24e">
       <strong class="markup--strong markup--li-strong">
        Just throw an error:
       </strong>
       This is a bad
                                idea in general. You don’t see your Microsoft Word throwing errors when you try to do
                                monstrous stuff, it finds a way to squeeze it in.
      </li>
      <li class="graf graf--li graf-after--li" id="a5ec" name="a5ec">
       <strong class="markup--strong markup--li-strong">
        Wrap using some predefines strategy:
       </strong>
       When you start thinking about potential solutions, you can come up with two
                                main ones. The red strategy on the left is simpler. It implements wrapping on the
                                outmost layer by pushing any item that doesn’t fit to the next line. You could also have
                                some strategy like the blue on the right though, where you check assume boxes have their
                                own columns and they continue to grow there.
      </li>
     </ol>
    </div>
    <div class="section-inner sectionLayout--outsetRow" data-paragraph-count="2">
     <figure class="graf graf--figure graf--layoutOutsetRow is-partialWidth graf-after--li" id="8377" name="8377" style="width: 45.506%;">
      <img class="graf-image" data-height="2251" data-image-id="1*rQZhkNueNAHQvejYKggS-g.png" data-width="2370" src="https://cdn-images-1.medium.com/max/600/1*rQZhkNueNAHQvejYKggS-g.png"/>
     </figure>
     <figure class="graf graf--figure graf--layoutOutsetRowContinue is-partialWidth graf-after--figure" id="c95b" name="c95b" style="width: 54.494%;">
      <img class="graf-image" data-height="1876" data-image-id="1*dimtF5xAeW0wQHSjdRjjGA.png" data-width="2365" src="https://cdn-images-1.medium.com/max/800/1*dimtF5xAeW0wQHSjdRjjGA.png"/>
     </figure>
    </div>
    <div class="section-inner sectionLayout--insetColumn">
     <p class="graf graf--p graf-after--figure" id="c147" name="c147">
      3.
      <strong class="markup--strong markup--p-strong">
       Allow User to Configure:
      </strong>
      This requires
                            me to define ways of giving user control over the row wrapping they want to apply.
     </p>
     <p class="graf graf--p graf-after--p" id="6041" name="6041">
      In some sense, what I end up doing
                            is a combination of all three. There are always some implicit logic that defines some part
                            of the strategies, but I also try to provide a set of high level constructs for the
                            strategies. The main two I have right now are
      <code class="markup--code markup--p-code">
       FrozenRow
      </code>
      and
      <code class="markup--code markup--p-code">
       FlexRow
      </code>
      , where
      <code class="markup--code markup--p-code">
       FrozenRow
      </code>
      requires elements two stay in the
                            same line and fails if it cannot sustain this requirements; and
      <code class="markup--code markup--p-code">
       FlexRow
      </code>
      continues to put elements in the next
                            line.
     </p>
     <h3 class="graf graf--h3 graf-after--p" id="bc67" name="bc67">
      What did it take to come to this
                            solution?
     </h3>
     <p class="graf graf--p graf-after--h3" id="3cc6" name="3cc6">
      The first design I had did not
                            account for overflows.I quickly realized that wouldn’t end well for me.
     </p>
     <figure class="graf graf--figure graf-after--p" id="4910" name="4910">
      <img class="graf-image" data-height="589" data-image-id="1*A_QYHcZ7rT26JTTo5MT6uw.png" data-width="831" src="https://cdn-images-1.medium.com/max/800/1*A_QYHcZ7rT26JTTo5MT6uw.png"/>
     </figure>
     <p class="graf graf--p graf-after--figure" id="4758" name="4758">
      When I started thinking about
                            possible solutions, I realized three possible solutions.
     </p>
    </div>
    <div class="section-inner sectionLayout--outsetRow" data-paragraph-count="3">
     <figure class="graf graf--figure graf--layoutOutsetRow is-partialWidth graf-after--p" id="ad7b" name="ad7b" style="width: 34.062%;">
      <img class="graf-image" data-height="524" data-image-id="1*EI-z696oUkc1Ra_y7oXGyw.png" data-width="678" src="https://cdn-images-1.medium.com/max/600/1*EI-z696oUkc1Ra_y7oXGyw.png"/>
     </figure>
     <figure class="graf graf--figure graf--layoutOutsetRowContinue is-partialWidth graf-after--figure" id="7920" name="7920" style="width: 34.062%;">
      <img class="graf-image" data-height="524" data-image-id="1*NnjH-2JRccejc3297shq3A.png" data-width="678" src="https://cdn-images-1.medium.com/max/600/1*NnjH-2JRccejc3297shq3A.png"/>
     </figure>
     <figure class="graf graf--figure graf--layoutOutsetRowContinue is-partialWidth graf-after--figure" id="be72" name="be72" style="width: 31.877%;">
      <img class="graf-image" data-height="521" data-image-id="1*3TernvI6LgJHSuHxpCNd4A.png" data-width="631" src="https://cdn-images-1.medium.com/max/400/1*3TernvI6LgJHSuHxpCNd4A.png"/>
     </figure>
    </div>
    <div class="section-inner sectionLayout--insetColumn">
     <p class="graf graf--p graf-after--figure" id="589a" name="589a">
      The first(red) solution tries
                            to equally distribute each box into the next line. The second(blue) solution tries to
                            equalize the width of each box on the first line. The third(green) solution requires me to
                            throw boxes into newlines until the remaining ones with. I quickly decided to go with option
                            3 as others did not compose/cascade well and I wasn’t sure how useful they were out of some
                            contrived examples.
     </p>
     <p class="graf graf--p graf-after--p" id="b5ab" name="b5ab">
      <strong class="markup--strong markup--p-strong">
       The second point I had trouble was is the
                                flexible width components.
      </strong>
      If a component did not specify its width, how do you
                            decide it? The solution here came from the realization that you can always decide the width
                            of a component by using its parent and children. There is no such thing as an empty stack or
                            row, they must eventually reach to some text element. That text element defines their
                            minimum width. Also, the root element has the width of the document that defines the maximum
                            width. By bounding each element from both sides and wrapping if minimum width exceeds
                            maximum width, we can calculate exact sizes for all elements.
     </p>
     <h3 class="graf graf--h3 graf-after--p" id="aac0" name="aac0">
      Conclusion
     </h3>
     <p class="graf graf--p graf-after--h3 graf--trailing" id="cdcc" name="cdcc">
      Writing this article
                            actually made me realize some problems I thought were problems are not, so it’s been pretty
                            helpful for me :D I really hope it was also a fun read to some of you out there.
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
   <a href="https://medium.com/p/5973a2a7dc7a">
    <time class="dt-published" datetime="2023-08-06T04:07:27.006Z">
     August 6, 2023
    </time>
   </a>
   .
  </p>
  <p>
   <a class="p-canonical" href="https://medium.com/@alpkeles99/hurdles-of-designing-a-layout-model-5973a2a7dc7a">
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
