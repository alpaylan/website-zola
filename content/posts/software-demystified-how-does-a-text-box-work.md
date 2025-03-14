+++
title = "Software Demystified: How does a Text Box Work?"
date = "2023-11-24"
[taxonomies]
tags = ['software engineering', 'algorithms']
language = ["en"]
+++

<article class="h-entry">
 <section class="e-content" data-field="body">
  <section class="section section--body section--first section--last" name="3c6b">
   <div class="section-content">
    <div class="section-inner sectionLayout--insetColumn">
     <h3 class="graf graf--h3 graf--leading graf--title" id="6ee6" name="6ee6">
      Software Demystified: How does a Text Box Work?
     </h3>
     <p class="graf graf--p graf-after--h3" id="efd4" name="efd4">
      Below is an excerpt from
      <a class="markup--anchor markup--p-anchor" data-href="http://streetcoder.org" href="http://streetcoder.org" rel="noopener" target="_blank">
       Street Coder
      </a>
      , where
      <a class="markup--user markup--p-user" data-action="show-user-card" data-action-type="hover" data-action-value="cfcbc8090ec" data-anchor-type="2" data-href="https://medium.com/u/cfcbc8090ec" data-user-id="cfcbc8090ec" href="https://medium.com/u/cfcbc8090ec" target="_blank">
       Sedat Kapanoglu
      </a>
      talks about opacity in software.
     </p>
     <blockquote class="graf graf--blockquote graf--startsWithDoubleQuote graf-after--p" id="41fc" name="41fc">
      “Technology is becoming more opaque, like cars. People used to be able to repair their own cars. Now as the engines become increasingly advanced, all we see under the hood is a metal cover, like the one on a pharaoh’s tomb that will release cursed spirits onto whoever opens it. Software development technologies are no different.
      <strong class="markup--strong markup--blockquote-strong">
       Although almost everything is now open source, I think new technologies are more obscure than reverse-engineered code from a binary from the 1990s because of the immensely increased complexity of software.
      </strong>
      ”
     </blockquote>
     <p class="graf graf--p graf-after--blockquote" id="6dbb" name="6dbb">
      I agree with these sentiments, and actively argue against this opaqueness. This article is part of a series of
      <strong class="markup--strong markup--p-strong">
       Software Demystified
      </strong>
      articles that will try to build up components or systems we use in our everyday software development such as text boxes, search bars, or databases in the hope of removing some of the opaqueness in our understanding of these systems.
     </p>
     <h4 class="graf graf--h4 graf-after--p" id="57b3" name="57b3">
      So, what is a text box?
     </h4>
     <p class="graf graf--p graf-after--h4" id="15be" name="15be">
      This is actually a pretty good and important question, especially because it doesn’t have a right answer. A Text Box can be growing or fixed height, it might overflow vertically or horizontally, it might be multiline or single line, it can support emojis, or allow rich text editing, may be WYGIWYS or more verbose, it can allow for directives such as mentions, or spoiler marks.
     </p>
     <p class="graf graf--p graf-after--p" id="298f" name="298f">
      Aside from these features, the maximum allowed text size or trimming characteristics, keyboard shortcuts, rendering, mouse interactions are all part of the requirements for implementing a text box.
     </p>
     <p class="graf graf--p graf-after--p" id="c1fa" name="c1fa">
      In an ideal world, we would have a model of the text box that defines how any action transforms the state of the text box as below.
     </p>
     <figure class="graf graf--figure graf-after--p" id="ca1b" name="ca1b">
      <img class="graf-image" data-height="465" data-image-id="1*xkZviWTHq5S-EdFjOKogbw.png" data-width="2909" src="https://cdn-images-1.medium.com/max/800/1*xkZviWTHq5S-EdFjOKogbw.png"/>
     </figure>
     <p class="graf graf--p graf-after--figure" id="f303" name="f303">
      This model of course depends on the internal data representation of the text box.
     </p>
     <p class="graf graf--p graf-after--p" id="4356" name="4356">
      Let’s start with the one of the simplest text boxes possible.
     </p>
     <pre class="graf graf--pre graf-after--p graf--preV2" data-code-block-lang="css" data-code-block-mode="1" id="ae94" name="ae94" spellcheck="false"><span class="pre--content">Textbox V1<br/><span class="hljs-number">1</span>. No mouse actions.<br/><span class="hljs-number">2</span>. No ctrl/alt/shift actions.<br/><span class="hljs-number">3</span>. No newlines.<br/><span class="hljs-number">4</span>. Fixed <span class="hljs-attribute">width</span> and <span class="hljs-attribute">height</span>, grows <span class="hljs-selector-tag">to</span> <span class="hljs-attribute">right</span>.<br/><span class="hljs-number">5</span>. No rich text, fixed <span class="hljs-attribute">width</span> <span class="hljs-attribute">font</span>.</span></pre>
     <p class="graf graf--p graf-after--pre" id="9cc4" name="9cc4">
      This text box, in essense, has only 3 features.
     </p>
     <ol class="postList">
      <li class="graf graf--li graf-after--p" id="3d92" name="3d92">
       Add/delete a character
      </li>
      <li class="graf graf--li graf-after--li" id="72cb" name="72cb">
       Have a cursor and move the cursor using left/right arrows
      </li>
      <li class="graf graf--li graf-after--li" id="8c94" name="8c94">
       Focus the text view with respect to the cursor
      </li>
     </ol>
     <p class="graf graf--p graf-after--li" id="5ca4" name="5ca4">
      <strong class="markup--strong markup--p-strong">
       So, what are the tasks for the developer here?
      </strong>
     </p>
     <p class="graf graf--p graf-after--p" id="2138" name="2138">
      Well, the programmer has several jobs. The first one is the rendering. Given a set of characters, we need to render those to the screen. We don’t need to implement the rendering itself, but we need to know certain properties of the result in order to correctly determine the position of the cursor as well as what portion of the text to render and where.
     </p>
     <p class="graf graf--p graf-after--p" id="706b" name="706b">
      Simplification number 5 plays a big role here, because we have a fixed width font, meaning that each character has the same width, (1) we immediately know the amount of characters that fit in our box, (2) we can find the position of our cursor very cheaply. If our box is 128 pixels and we have a fixed character size of 10 pixels, we can leave 4 pixels of padding in each side and have exactly 12 characters in the text box.
     </p>
     <figure class="graf graf--figure graf-after--p" id="c8e6" name="c8e6">
      <img class="graf-image" data-height="434" data-image-id="1*i6Z2fmolfuaIFAUeeA2Gkw.png" data-width="1394" src="https://cdn-images-1.medium.com/max/800/1*i6Z2fmolfuaIFAUeeA2Gkw.png"/>
     </figure>
     <p class="graf graf--p graf-after--figure" id="9f75" name="9f75">
      As we start typing in characters, our cursor moves automatically with each hit to the keyboard.
     </p>
     <figure class="graf graf--figure graf-after--p" id="cf56" name="cf56">
      <img class="graf-image" data-height="434" data-image-id="1*Fe4_tNI3CsTxYHa-A705Cw.png" data-width="1394" src="https://cdn-images-1.medium.com/max/800/1*Fe4_tNI3CsTxYHa-A705Cw.png"/>
     </figure>
     <p class="graf graf--p graf-after--figure" id="7bef" name="7bef">
      Our cursor has
      <code class="markup--code markup--p-code">
       length(text) + 1
      </code>
      potential positions, before the first character, between the characters, and after the last character. One funny thing that I just realized is we could also specify the amount of consecutive spaces. Medium’s text box interestingly only allows for one consecutive space character, I wonder why.
     </p>
     <figure class="graf graf--figure graf-after--p" id="f9ff" name="f9ff">
      <img class="graf-image" data-height="434" data-image-id="1*4IngUVBkNzxmKfn44JCmJw.png" data-is-featured="true" data-width="1394" src="https://cdn-images-1.medium.com/max/800/1*4IngUVBkNzxmKfn44JCmJw.png"/>
     </figure>
     <p class="graf graf--p graf-after--figure" id="62f0" name="62f0">
      Hitting 12 characters is the first point our action has a different result. Before now, we rendered our text by starting from the very first character by leaving 4 empty pixels, then rendering each character with 10 pixel distances, deciding the position of the cursor by calculating
      <code class="markup--code markup--p-code">
       4 + cursor_position * 10
      </code>
      . Each typed character has increased the
      <code class="markup--code markup--p-code">
       cursor_position
      </code>
      by 1, and each deletion decreased it by 1, capped at 0. Now, we reached the case where
      <code class="markup--code markup--p-code">
       cursor_position == 12
      </code>
      , in which any new character does not change the cursor position, but rather changes the window of the text we render. This is easily doable by adding a
      <code class="markup--code markup--p-code">
       starting_position
      </code>
      that tracks where the rendering window of the text begins.
     </p>
     <p class="graf graf--p graf-after--p" id="2052" name="2052">
      Now, we need to specify the
      <code class="markup--code markup--p-code">
       starting_position
      </code>
      characteristics. Luckily, they are very easy, most of the time starting position does not change. It only changes when
      <code class="markup--code markup--p-code">
       cursor_position == 12
      </code>
      and the action tries to increase the cursor, or when
      <code class="markup--code markup--p-code">
       cursor_position == 0
      </code>
      and the action tries to decrease the cursor. (there is one extra case that I forgot to write in my first trial, I encourage the reader to think about what that is, as you see, it’s quite tricky to correctly specify the behavior of even the simplest version of the text box)
     </p>
     <figure class="graf graf--figure graf-after--p" id="00ae" name="00ae">
      <img class="graf-image" data-height="434" data-image-id="1*OSmz4E3-HAjpA2TGRJANiQ.png" data-width="1394" src="https://cdn-images-1.medium.com/max/800/1*OSmz4E3-HAjpA2TGRJANiQ.png"/>
     </figure>
     <p class="graf graf--p graf-after--figure" id="9f52" name="9f52">
      Above, you can see how the window slides as we add new characters.
     </p>
     <p class="graf graf--p graf-after--p" id="1eff" name="1eff">
      This is probably all we need to talk about TextBox V1. What are the next steps though?
     </p>
     <p class="graf graf--p graf-after--p" id="364d" name="364d">
      An easy thing to do is remove the first limitation and allow for mouse clicks. As we can easily determine the character at which mouse click happens, we can move the cursor at the end of that character. A harder mouse action is drag action, in the user presses the mouse at some character and drags the mouse to another part of the text. This behavior has the same computational model as shift + arrow keys, so implementing one gives us the other for free. The behavior is very similar to the cursor movement + text sliding described above, but it also requires us to remember where we started.
     </p>
     <p class="graf graf--p graf-after--p" id="0230" name="0230">
      Adding ctrl keys requires finding the first whitespace and jumping at the point.
     </p>
     <p class="graf graf--p graf-after--p" id="07c7" name="07c7">
      Adding new lines adds a new dimension to the box, where our actions can also have vertical movements. It also opens up the possibility of changing the data representation to use paragraphs or lines instead of a simple text, because for long texts, it would be vastly inefficient to implement them in terms of simple strings.
     </p>
     <p class="graf graf--p graf-after--p" id="9a82" name="9a82">
      Adding variable-width font complicates our cursor position calculations, line break computations, as well as mouse behaviors, because now it is much harder to determine how the original text is presented in the text box in a visual way. Before, the complexity was virtually constant, now it might be linear with respect to the size of the text.
     </p>
     <p class="graf graf--p graf-after--p" id="889b" name="889b">
      Adding rich text(colors, font sizes, font styles) requires us to create separate text runs that represent parts of the text with different qualities, and render them consecutively. Rich text also complicates the position calculations even further, because it prevents approximations. With a single style variable font, we can have a constant time approximate result, which is linear with respect to the number of text runs in a rich text setting.
     </p>
     <h4 class="graf graf--h4 graf-after--p" id="c00b" name="c00b">
      Why are all of these important?
     </h4>
     <p class="graf graf--p graf-after--h4 graf--trailing" id="fbc7" name="fbc7">
      To be fair, they probably aren’t if you are not developing the next blogging site, a new text editor or a new messaging app, hell they probably aren’t important even if you are doing one of those things because you would be using already existing components. The information in this article is more interesting than it is useful, and I think it allows for a rare type of thinking where we look behind the curtains of the opaque software world. I like to look behind the curtains, because I don’t like it when I am limited with the options available to me today, using the standart implementations available. I like to be limited with my own creativity.
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
   <a href="https://medium.com/p/c24d28198cfa">
    <time class="dt-published" datetime="2023-11-24T15:02:01.648Z">
     November 24, 2023
    </time>
   </a>
   .
  </p>
  <p>
   <a class="p-canonical" href="https://medium.com/@alpkeles99/software-demystified-how-does-a-text-box-work-c24d28198cfa">
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
