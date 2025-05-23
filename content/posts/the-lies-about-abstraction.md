+++
title = "The Lies About Abstraction"
date = "2023-12-02"
[taxonomies]
tags = ['software engineering']
language = ["en"]
+++

<article class="h-entry">
 <section class="e-content" data-field="body">
  <section class="section section--body section--first section--last" name="816d">
   <div class="section-content">
    <div class="section-inner sectionLayout--insetColumn">
     <h3 class="graf graf--h3 graf--leading graf--title" id="61a0" name="61a0">
      The Lies About Abstraction
     </h3>
     <p class="graf graf--p graf-after--h3" id="4ed6" name="4ed6">
      Below is an excerpt from
      <a class="markup--anchor markup--p-anchor" data-href="http://streetcoder.org" href="http://streetcoder.org" rel="noopener ugc nofollow noopener" target="_blank">
       Street Coder
      </a>
      , where
      <a class="markup--user markup--p-user" data-action="show-user-card" data-action-type="hover" data-action-value="cfcbc8090ec" data-anchor-type="2" data-href="https://medium.com/u/cfcbc8090ec" data-user-id="cfcbc8090ec" href="https://medium.com/u/cfcbc8090ec" target="_blank">
       Sedat Kapanoglu
      </a>
      talks about benefits of layering in software.
     </p>
     <blockquote class="graf graf--blockquote graf-after--p" id="df42" name="df42">
      A business layer doesn’t know anything about databases or storage techniques. It calls on the database layer for that. The database layer encapsulates the database functionality in a DB-agnostic fashion. This kind of separation of concerns can make the testability of business logic easier because we can easily plug a mocked implementation of the storage layer into the business layer.
      <strong class="markup--strong markup--blockquote-strong">
       More importantly, that architecture allows us to change a DB behind the scenes without changing a single line of code in the business layer, or in the web layer, for that matter.
      </strong>
     </blockquote>
     <p class="graf graf--p graf-after--blockquote" id="88c5" name="88c5">
      Although the sentiment is nice in theory, I think the reality does not conform to the sentiment. This article is a response to the idea that layering allows for seamlessly changing a layer without any consequences for the rest of the system. I argue that all abstractions come with leakage, meaning that they have
      <strong class="markup--strong markup--p-strong">
       untested/unspecified
      </strong>
      characteristics that might surface after such changes.
     </p>
     <figure class="graf graf--figure graf-after--p" id="b21b" name="b21b">
      <img class="graf-image" data-height="3456" data-image-id="1*0IxAsbazZbSAFZYq89FfpA.png" data-is-featured="true" data-width="6912" src="https://cdn-images-1.medium.com/max/800/1*0IxAsbazZbSAFZYq89FfpA.png"/>
     </figure>
     <h4 class="graf graf--h4 graf-after--figure" id="bce1" name="bce1">
      So, what is a layer?
     </h4>
     <p class="graf graf--p graf-after--h4" id="ae97" name="ae97">
      Abstraction is commonplace in software engineering. Layering is a type of abstraction where a software module is concerned with implementing a specific set of functionality for some data type, agreeing on a set of
      <strong class="markup--strong markup--p-strong">
       contracts specifying the preconditions and postconditions of the module.
      </strong>
     </p>
     <p class="graf graf--p graf-after--p" id="5134" name="5134">
      Layers are useful constructs that allow for building software, especially as teams and projects get larger. Below is a common architecture depicting 4 layers of a Web Application, taken from Street Coder.
     </p>
     <figure class="graf graf--figure graf-after--p" id="dedb" name="dedb">
      <img class="graf-image" data-height="1198" data-image-id="1*AZyKWLl97t8X1myGxWOaug.png" data-width="2746" src="https://cdn-images-1.medium.com/max/800/1*AZyKWLl97t8X1myGxWOaug.png"/>
     </figure>
     <p class="graf graf--p graf-after--figure" id="64a9" name="64a9">
      Although one does not need these layers to create a web application, their existence makes software development process more manageable by reducing the mental load of the developers, allowing them to think more locally.
     </p>
     <h4 class="graf graf--h4 graf-after--p" id="040d" name="040d">
      Well, what is a contract?
     </h4>
     <p class="graf graf--p graf-after--h4" id="f5da" name="f5da">
      A contract is the expectations(preconditions) and guarantees (postconditions) of a layer. Contracts can have different levels of formality depending on the language. The most common contract you have seen is
      <strong class="markup--strong markup--p-strong">
       types
      </strong>
      . In a statically typed language, the type system proves that the function will receive an input and provide an output of a specific type, as opposed to dynamically typed languages where input to the layer might have any type, and the layer might produce an output of any type. Unlike types, most contracts are far from proven if you are not in a research programming language focused on
      <a class="markup--anchor markup--p-anchor" data-href="https://en.wikipedia.org/wiki/Formal_verification#:~:text=Formal%20verification%20of%20software%20programs,systems%2C%20and%20lightweight%20formal%20methods." href="https://en.wikipedia.org/wiki/Formal_verification#:~:text=Formal%20verification%20of%20software%20programs,systems%2C%20and%20lightweight%20formal%20methods." rel="noopener" target="_blank">
       formal verification
      </a>
      . I will call such unproven contracts
      <strong class="markup--strong markup--p-strong">
       “soft contracts”
      </strong>
      for the rest of this article, as they can be broken unlike the
      <strong class="markup--strong markup--p-strong">
       “hard contracts”
      </strong>
      that are proven. Examples of soft contracts include
      <strong class="markup--strong markup--p-strong">
       validation, sanitization, null pointer checks, tests, and beliefs about the inner workings of software
      </strong>
      in general.
     </p>
     <p class="graf graf--p graf-after--p" id="7865" name="7865">
      A typical example of sanitization in a web application is
      <a class="markup--anchor markup--p-anchor" data-href="https://en.wikipedia.org/wiki/SQL_injection" href="https://en.wikipedia.org/wiki/SQL_injection" rel="noopener" target="_blank">
       input sanitization against SQL Injections attacks
      </a>
      . When writing a web application, we usually ask for inputs from the user. If the input is not properly processed before constructing an SQL query, a malicious user may be able to extract private information from the database.
      <strong class="markup--strong markup--p-strong">
       The belief that the input to the database is sanitized is a soft contract because of 2 reasons.
      </strong>
     </p>
     <p class="graf graf--p graf-after--p" id="6589" name="6589">
      Imagine we have a function
      <code class="markup--code markup--p-code">
       sanitize(dangerous_query_string: str) -&gt; SanitizedQuery
      </code>
      that produces a
      <strong class="markup--strong markup--p-strong">
       SanitizedQuery
      </strong>
      datatype given a string taken from the user. The first problem is that
      <strong class="markup--strong markup--p-strong">
       we can only believe that SanitizedQuery is actually sanitized
      </strong>
      , we cannot actually
      <strong class="markup--strong markup--p-strong">
       know
      </strong>
      it. We can
      <strong class="markup--strong markup--p-strong">
       test
      </strong>
      it, we can
      <strong class="markup--strong markup--p-strong">
       code review,
      </strong>
      we can
      <strong class="markup--strong markup--p-strong">
       pray to God,
      </strong>
      but as history of software engineering has shown us, our beliefs are very prone to be false. The second problem is that having such separate types are not feasible in many cases, because doing so leads to almost every single function having its own output type, leading to an unreadable codebase very very fast. This leads to the fact that function signature is usually
      <code class="markup--code markup--p-code">
       sanitize(dangerous_query_string: str) -&gt; str
      </code>
      in practice, which means we lose the information tracking capabilities of the type system.
     </p>
     <p class="graf graf--p graf-after--p" id="dce8" name="dce8">
      What happens when a soft contract is invalid? Well, anything might happen. As layers down path will assume that contract is valid, they will naively execute such input, leading to potentially catastrophic results.
     </p>
     <h4 class="graf graf--h4 graf-after--p" id="1f01" name="1f01">
      Where is the lie here?
     </h4>
     <p class="graf graf--p graf-after--h4" id="e7f4" name="e7f4">
      So far, I talked about layers, and contracts between layers that allow for composing different layers with each other. The composition relies on the expectations of the consuming module and the guarantees of the producer. For example, if the producer guarantees to output sanitized strings, the consumer will not try to sanitize such inputs again, enabling better scaling by providing separation of concerns between different modules.
     </p>
     <p class="graf graf--p graf-after--p" id="3c44" name="3c44">
      The problem here is that a soft contract is as good as it is observable. If you cannot test/verify the validity of a contract condition, then you cannot trust that the consumer will correctly handle inputs provided by the producer. Going back to the example at the beginning, your assumption must be that changing
      <strong class="markup--strong markup--p-strong">
       your database layer will only guarantee you correctness on your tested behaviors, and nothing more.
      </strong>
     </p>
     <p class="graf graf--p graf-after--p" id="c93d" name="c93d">
      With behavior such as input-output that is frequently and easily tested, we might actually achieve seamless transfer as we alternate a layer. So, it might be possible to switch your entire DB by keeping the input layer of the database layer intact.
      <strong class="markup--strong markup--p-strong">
       The problem is now you need to think about the unobservables?
      </strong>
      <strong class="markup--strong markup--p-strong">
       All behaviors of your previous implementation that affects the users is now part of your contract.
      </strong>
      Your new implementation may have the exact IO as the old one, but what about performance? Depending on the DB implementation, different query types will have different performance characteristics. Such differences are subtle and hard to catch, especially as the notion of correctness is built on IO for today’s software systems, so we don’t have the adequate tools to understand such
      <strong class="markup--strong markup--p-strong">
       bugs
      </strong>
      .
     </p>
     <h4 class="graf graf--h4 graf-after--p" id="45a8" name="45a8">
      Let’s close up
     </h4>
     <p class="graf graf--p graf-after--h4 graf--trailing" id="fefb" name="fefb">
      The blanket sentence that layering allows for seamless switching of an intermediate layer by keeping its public interface intact is a nice one, but it is false. Public interface only tells us what functions exist, and what their types are. Tests and code review provide extra guarantees, but they are incomplete tools for describing the total contract of a function, which leads to the fact that it is very hard to judge the results of a switch. Thank you for reading up to here!
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
   <a href="https://medium.com/p/5d7a85e2c9f7">
    <time class="dt-published" datetime="2023-12-02T19:40:22.182Z">
     December 2, 2023
    </time>
   </a>
   .
  </p>
  <p>
   <a class="p-canonical" href="https://medium.com/@alpkeles99/the-lies-about-abstraction-5d7a85e2c9f7">
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
