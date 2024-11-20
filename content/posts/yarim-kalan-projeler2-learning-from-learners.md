+++
title = "Yarım Kalan Projeler#2: Learning from Learners"
date = "2022-12-19"
[taxonomies]
tags = ['half-finished projects', 'computer science', 'learning from learners']
language = ["tr"]
+++

<article class="h-entry">
 <section class="e-content" data-field="body">
  <section class="section section--body section--first section--last" name="722f">
   <div class="section-content">
    <div class="section-inner sectionLayout--insetColumn">
     <h3 class="graf graf--h3 graf--leading graf--title" id="ef31" name="ef31">
      Yarım Kalan Projeler#2: Learning from Learners
     </h3>
     <p class="graf graf--p graf-after--h3" id="7950" name="7950">
      Learning from Learners, kısaca LFL, ortaya çıktığı dönem beni çok heyecanlandırmıştı. Doktoraya yeni başlamanın da etkisiyle çok yeni konseptler öğrendiğim için, bu konseptleri tanımayan benim gibi başkalarına da aktarabilmeyi hayal ettim. İlk yazı, doktoramın ana odağında bulunan Property-Based Testing üzerineydi.
     </p>
     <div class="graf graf--mixtapeEmbed graf-after--p" id="01e7" name="01e7">
      <a class="markup--anchor markup--mixtapeEmbed-anchor" data-href="https://medium.com/learning-from-learners/learners-guide-to-property-based-testing-1-ce979c1a58a1" href="https://medium.com/learning-from-learners/learners-guide-to-property-based-testing-1-ce979c1a58a1" title="https://medium.com/learning-from-learners/learners-guide-to-property-based-testing-1-ce979c1a58a1">
       <strong class="markup--strong markup--mixtapeEmbed-strong">
        Learner’s Guide to Property Based Testing#1
       </strong>
       <br/>
       <em class="markup--em markup--mixtapeEmbed-em">
        Property Based Random Testing is a flavor of testing that aims to use higher level specifications for testing instead…
       </em>
       medium.com
      </a>
      <a class="js-mixtapeImage mixtapeImage u-ignoreBlock" data-media-id="19a1af58cac5358feef1ed754df15c73" data-thumbnail-img-id="1*92Av2ZbXV98Ryo1C0cxpFw.png" href="https://medium.com/learning-from-learners/learners-guide-to-property-based-testing-1-ce979c1a58a1" style="background-image: url(https://cdn-images-1.medium.com/fit/c/160/160/1*92Av2ZbXV98Ryo1C0cxpFw.png);">
      </a>
     </div>
     <p class="graf graf--p graf-after--mixtapeEmbed" id="ba5f" name="ba5f">
      Her şeyden önemlisi, benim için LFL’in önemli olma sebebi başkalarıyla birlikte yazabilme şansıydı. Çevremdeki insanların da motive olacağını düşünüp, onların da kendi öğrendikleriyle ilgili yazmasını planlamıştım. Tek bir yazıyla kalmasından açık olmalı ki proje maalesef devam etmedi.
     </p>
     <p class="graf graf--p graf-after--p" id="6cf3" name="6cf3">
      Blog için arkada yatan fikirler de şu şekildeydi.
     </p>
     <ol class="postList">
      <li class="graf graf--li graf-after--p" id="3e8e" name="3e8e">
       <strong class="markup--strong markup--li-strong">
        Kullandığımız pek çok aracın arkasında yatan fikir aslında basit. Öğrenmenin önündeki engeller bu araçların performans, hata idaresi gibi gerekliliklerinden kaynaklı olarak kompleks olmasından kaynaklanıyor. Oyuncak bir arama motoru yazmak değil; kullanılabilecek, işe yarayacak bir arama motoru yazmak zor mesela.(Küçük bir örnek:
       </strong>
       <a class="markup--anchor markup--li-anchor" data-href="https://anvil.works/blog/how-to-build-a-search-engine" href="https://anvil.works/blog/how-to-build-a-search-engine" rel="noopener" target="_blank">
        https://anvil.works/blog/how-to-build-a-search-engine
       </a>
       <strong class="markup--strong markup--li-strong">
        )
       </strong>
      </li>
      <li class="graf graf--li graf-after--li" id="ea47" name="ea47">
       <strong class="markup--strong markup--li-strong">
        Alanda uzun süre geçirmiş insanlar bu araçların karmaşıklıklarına aşina olduklarından onlar için yeni öğrenen bir insan bakış açısından bakmak zor. Dolayısıyla bu yazılar yeni öğrenenler tarafından yazılmalı.
       </strong>
      </li>
     </ol>
     <p class="graf graf--p graf-after--li" id="c43a" name="c43a">
      Bu iki fikri birleştirdiğimde, ortaya Learning from Learners ortaya çıktı. İlk yazı da beni şahsen tatmin edebilecek durumdaydı gayet. Hatta üstüne şöyle tasarım ruhundan uzak bir kapak fotoğrafı bile tasarlamıştım.
     </p>
     <figure class="graf graf--figure graf-after--p" id="c7a1" name="c7a1">
      <img class="graf-image" data-height="924" data-image-id="1*eaf4FAPoXMv7g7ISq2dtEA.png" data-is-featured="true" data-width="1640" src="https://cdn-images-1.medium.com/max/800/1*eaf4FAPoXMv7g7ISq2dtEA.png"/>
     </figure>
     <p class="graf graf--p graf-after--figure" id="128f" name="128f">
      Projenin yarım kalmasının sebebi öncelikle konseptin genelleştirilememesi, ikinci olarak da yanıma yazar bulamamam oldu.
     </p>
     <h4 class="graf graf--h4 graf-after--p" id="bbef" name="bbef">
      <strong class="markup--strong markup--h4-strong">
       Konseptin Genelleştirilememesi
      </strong>
     </h4>
     <p class="graf graf--p graf-after--h4" id="87cf" name="87cf">
      Property-Based Testing konsept olarak neredeyse hiçbir arka plan gerektirmeden anlatılabiliyor. Dolayısıyla kısa bir yazıda tüm bir konsepti sıfırdan basit kod örnekleri üzerinden anlatabiliyorum.
     </p>
     <p class="graf graf--p graf-after--p" id="9d3a" name="9d3a">
      Diğer yandan aynı fikri “Automated Theorem Prover, SAT Solver, Fuzzer, Bitwise Algorithms” gibi alanlara uygulamaya çalıştığımda, arka planda çok daha fazla bilgi sağlamam gerektiğini fark ettim. Nasıl tek bir yazıda tüm bilgiyi toplayacağımdan emin olmadığım için bu yazıların neredeyse hepsi yarım kaldı. Diğer bir ihtimal ise benim bu konseptlere Property Based Testing kadar hakim olmamam, o yüzden nasıl basit konsept örnekleri oluşturabileceğimi bilmemem de olabilir.
     </p>
     <h4 class="graf graf--h4 graf-after--p" id="a03a" name="a03a">
      Yazar Bulamamam
     </h4>
     <p class="graf graf--p graf-after--h4" id="a44e" name="a44e">
      Herhalde fikri ilk bulduğumda yaklaşık 50 kişiye yazdım, yazılar da toplam 1000 kişi tarafından okundu ancak ben gelip yazayım diyen toplamda
      <strong class="markup--strong markup--p-strong">
       0 kişi çıktı.
      </strong>
      Ben de fikrin en tatlı taraflarından birisi başkalarıyla beraber çalışma fırsatı olduğu için motivasyonumu kaybettim. Belki de birkaç tane daha yazı yazabilseydim, ortaya çıkan momentumla başkaları da motive olabilirdi. Bilemiyorum.
     </p>
     <h4 class="graf graf--h4 graf-after--p" id="1c0a" name="1c0a">
      Proje Şu An Ne Durumda?
     </h4>
     <p class="graf graf--p graf-after--h4" id="00c8" name="00c8">
      Yaklaşık 1 yıldır yazı yazılmamış olmasına rağmen, ben hala umutluyum. Hala konseptler yeterince basitleştirilirse alttaki öz fikri korurken belli bir seviyede kullanılabilir ve anlaşılabilir oyuncak projelerde birleştirilebilir diye düşünüyorum. Aklımda bazı yazılar var:
     </p>
     <ul class="postList">
      <li class="graf graf--li graf-after--p" id="c277" name="c277">
       Coverage Measuring
      </li>
      <li class="graf graf--li graf-after--li" id="6aba" name="6aba">
       Fuzz-testing
      </li>
      <li class="graf graf--li graf-after--li" id="64e0" name="64e0">
       Automated Theorem Solving
      </li>
      <li class="graf graf--li graf-after--li" id="44f0" name="44f0">
       Writing a Simulation for X
      </li>
      <li class="graf graf--li graf-after--li" id="9543" name="9543">
       Encryption
      </li>
     </ul>
     <p class="graf graf--p graf-after--li graf--trailing" id="c360" name="c360">
      <strong class="markup--strong markup--p-strong">
       Eğer bu tarz yazılar yazmak hoşunuza giderse beni haberdar ederseniz çok sevinirim. Belki yeterince ilgi çıkarsa birlikte devam ederiz.
      </strong>
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
   <a href="https://medium.com/p/a77403afb1da">
    <time class="dt-published" datetime="2022-12-19T11:33:50.124Z">
     December 19, 2022
    </time>
   </a>
   .
  </p>
  <p>
   <a class="p-canonical" href="https://medium.com/@alpkeles99/yar%C4%B1m-kalan-projeler-2-learning-from-learners-a77403afb1da">
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
