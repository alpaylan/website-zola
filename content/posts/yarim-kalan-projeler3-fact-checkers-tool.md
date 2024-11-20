+++
title = "Yarım Kalan Projeler#3: Fact Checker’s Tool"
date = "2022-12-21"
[taxonomies]
tags = ['half-finished projects', 'computer science']
language = ["tr"]
+++

<article class="h-entry">
 <section class="e-content" data-field="body">
  <section class="section section--body section--first section--last" name="5f0f">
   <div class="section-content">
    <div class="section-inner sectionLayout--insetColumn">
     <h3 class="graf graf--h3 graf--leading graf--title" id="aa06" name="aa06">
      Yarım Kalan Projeler#3: Fact Checker’s Tool
     </h3>
     <p class="graf graf--p graf-after--h3" id="2ef1" name="2ef1">
      Asıl ismiyle “Fact Checker’s Tool” ya da “FCT”, farklı kişi ve kurumlar tarafından “FactHacker”, “FactChecker”, “Fact Maker” gibi birbirinden ilginç isimlerle hitap edilen, en sonda karmaşıklıklardan kurtulmak için “Factly” adını verdiğimiz bu projenin hedefi aslında çok basitti,
      <strong class="markup--strong markup--p-strong">
       yalan haberlerin keşfedilmesine yardımcı olmak.
      </strong>
     </p>
     <p class="graf graf--p graf-after--p" id="0c6a" name="0c6a">
      Projenin detaylarına girmeden, nereden çıktığından bahsedeyim. Daha Covid-19'un ilk aylarındayken, girişimcilikle ilgilenen birkaç farklı kişi/kuruluş salgının yarattığı olumsuz etkileri azaltabilecek, düzeltebilecek projelerin ortaya çıkması için
      <strong class="markup--strong markup--p-strong">
       Coronathon
      </strong>
      adında bir hackathon düzenlemeye karar veriyor. 1 haftadan daha kısa bir sürede 100'den fazla takım ve 100'den fazla mentör bir araya toplanıyor. O sırada biz de
      <a class="markup--user markup--p-user" data-action="show-user-card" data-action-type="hover" data-action-value="3102d6d5f774" data-anchor-type="2" data-href="https://medium.com/u/3102d6d5f774" data-user-id="3102d6d5f774" href="https://medium.com/u/3102d6d5f774" target="_blank">
       Ahmet YÜKSEL
      </a>
      ile yarışmayı görüp katılmaya karar verdik,
      <a class="markup--user markup--p-user" data-action="show-user-card" data-action-type="hover" data-action-value="801f500f487e" data-anchor-type="2" data-href="https://medium.com/u/801f500f487e" data-user-id="801f500f487e" href="https://medium.com/u/801f500f487e" target="_blank">
       Ozan Akın
      </a>
      ve
      <a class="markup--user markup--p-user" data-action="show-user-card" data-action-type="hover" data-action-value="bc40f811ddfc" data-anchor-type="2" data-href="https://medium.com/u/bc40f811ddfc" data-user-id="bc40f811ddfc" href="https://medium.com/u/bc40f811ddfc" target="_blank">
       Ozan Sazak
      </a>
      ile birlikte 4 kişilik bir ekip kurduk. Birkaç farklı fikri tartıştıktan sonra FCT’de karar kıldık.
     </p>
     <p class="graf graf--p graf-after--p" id="ce37" name="ce37">
      <strong class="markup--strong markup--p-strong">
       Fact Checker’s Tool
      </strong>
      , Teyit.org veya Doğruluk Payı gibi haber doğrulama organizasyonların yalan haberleri daha hızlı keşfetmesine yardımcı olacak bir araç olarak tasarlandı.
     </p>
     <p class="graf graf--p graf-after--p" id="8b9b" name="8b9b">
      Projenin arkasındaki ana fikir çok basitti.
     </p>
     <blockquote class="graf graf--blockquote graf-after--p" id="14a9" name="14a9">
      <strong class="markup--strong markup--blockquote-strong">
       <em class="markup--em markup--blockquote-em">
        Yanlış haberlere inanan ve yanlış haberleri yayan kişiler yanlış haberlere inanmaya ve yanlış haberleri yaymaya devam edecektir.
       </em>
      </strong>
     </blockquote>
     <p class="graf graf--p graf-after--blockquote" id="9835" name="9835">
      Daha az şiirsel olacak olursam, daha öncesinde yanlış haberleri beğenen ve paylaşan davranışlarını tekrarlama ihtimali daha yüksektir. O halde, haberlerin yayılımını incelediğimizde, daha öncesinde yanlış haberleri beğenen ve paylaşan kişiler tarafından paylaşılmaları halinde yanlış haber olma ihtimalleri yüksek olacaktır.
     </p>
     <p class="graf graf--p graf-after--p" id="3026" name="3026">
      Burada, birkaç eksik noktayı doldurmak gerekiyor.
     </p>
     <ul class="postList">
      <li class="graf graf--li graf-after--p" id="1628" name="1628">
       Haber beğenmek ve paylaşmak ne demek, hangi platform üzerinde yapılıyor?
      </li>
      <li class="graf graf--li graf-after--li" id="8b51" name="8b51">
       Yanlış haber ne demek, neye göre ve nasıl tanımlanıyor?
      </li>
      <li class="graf graf--li graf-after--li" id="c4e9" name="c4e9">
       Bir haberin yanlış olduğuna nasıl karar veriyoruz? Bir haberin yanlış olma ihtimalinin yüksek olması bize ne anlatıyor?
      </li>
     </ul>
     <p class="graf graf--p graf-after--li" id="82a8" name="82a8">
      Projeyi Twitter üzerinde düşündük. Retweet mekaniğinin haberlerin yayılımını hızlandırması, yüksek kullanım seviyesi, diğer sosyal medya ağlarına göre daha çok haber paylaşımına elverişli olması ve haber paylaşımı için kullanılması, bir de üstüne geçmişte yalan haberlerin paylaşımına dair bilimsel bir literatür bulunmasından dolayı Twitter’ı mantıklı bulduk.
     </p>
     <p class="graf graf--p graf-after--p" id="de38" name="de38">
      Yanlış haberleri ise, doğru haberlerin tersi üzerinden tanımladık. Teyit.org, Doğruluk Payı gibi haber doğrulama organizasyonları IFCN(International Fact-Checking Network) adı verilen, haber doğrulama üzerine standartlar, rehberler ve yönlendiriciler sağlayan büyük bir organizasyonun içinde yer alıyorlar. IFCN tarafından kabul edilen organizasyonların yaptığı haberleri doğru haber olarak kabul ettik. Bu haberlerin yalanladığı tüm haberleri ise yanlış olarak. Bu şekilde, Twitter içindeki her bir hesabın bu haberlere dair attıkları tweet’lere dayanarak oluşturulan bir
      <strong class="markup--strong markup--p-strong">
       güvenilirlik puanı
      </strong>
      oluştu.
     </p>
     <p class="graf graf--p graf-after--p" id="0fbe" name="0fbe">
      Bu haberlere dair tweet atmayanlar için de bu güvenilirlik puanlarını HITS(Hyperlink-Induced Topic Search) adı verilen, arama motorlarının web sayfalarının sıralamasına karar vermek için kullandıkları bir algoritmayı kullanarak oluşturduk.
     </p>
     <p class="graf graf--p graf-after--p" id="f945" name="f945">
      Yeni bir haber ortaya çıktığında, o haberi yayan kullanıcıların güvenilirlik puanlarına dayalı olarak o habere de bir güvenilirlik puanı atanıyor. Bu puan belli bir eşik sınırın altındaysa haber doğrulama ajanslarına haberin araştırılması için bildirim gönderiliyor.
     </p>
     <p class="graf graf--p graf-after--p" id="6edc" name="6edc">
      Bu süreci bir akış diyagramı olarak göstermek istersek aşağıdaki gibi bir sonuçlar karşılaşıyoruz.
     </p>
     <figure class="graf graf--figure graf-after--p" id="d065" name="d065">
      <img class="graf-image" data-height="1552" data-image-id="1*BU6VfdqFaHGYYPJt_ZjF0w.png" data-width="2750" src="https://cdn-images-1.medium.com/max/800/1*BU6VfdqFaHGYYPJt_ZjF0w.png"/>
      <figcaption class="imageCaption">
       Akış Diyagramı
      </figcaption>
     </figure>
     <p class="graf graf--p graf-after--figure" id="144e" name="144e">
      Fikrin çıkış noktası Covid-19 salgınının ilk dönemlerinde(ve gördüğümüz üzere sonrasında) yaşanan bilgi kirliliğinin azaltılmasına katkıda bulunmaktı.
     </p>
     <p class="graf graf--p graf-after--p" id="9e90" name="9e90">
      <strong class="markup--strong markup--p-strong">
       Maalesef ki bunlardan hiçbirisi gerçekten hayata geçmedi.
      </strong>
     </p>
     <p class="graf graf--p graf-after--p" id="9344" name="9344">
      Yukarıdaki diyagramı incelediğinizde, “Stance Detection-Duruş Çıkarımı” adlı bir hamle görüyorsunuz.
      <strong class="markup--strong markup--p-strong">
       Duruş Çıkarımı
      </strong>
      , bir tweet’i alıp onun ne ile ilgili olduğunu ve aynı zamanda o konuya bakış açısını anlamak demek.
     </p>
     <p class="graf graf--p graf-after--p" id="81bb" name="81bb">
      Biz, konunun içine biraz daha girdiğimizde fark ettik ki bunu güvenilir ve kaliteli bir şekilde yapmanın bir yolu yok, en azından biz bilmiyoruz ve bulamıyoruz. Bunu da, neyse ki hiçbir yerden yatırım veya fon almadan, kimseye yanlış vaadler sunmadan fark etmiş olduk.
     </p>
     <p class="graf graf--p graf-after--p" id="7a6a" name="7a6a">
      Bu farkındalık anı da, Ağustos ayında sıcak Ankara güneşinin altında çalışırken geldi. O dönem proje bir şekilde Boğaziçi TTO’nun(Teknoloji Transfer Ofisi) dikkatini çekmişti, onlara yaptığımız sunum sonucunda bizim için ciddi bir miktarda yardımda bulunacaklardı. Ortaya finansal bir yükümlülük girince, girdiğimiz işten emin olmak için tekrardan projenin çalışması için gerekli bileşenlerin her birini tek tek incelemeye başladık. “
      <strong class="markup--strong markup--p-strong">
       Proje neden başarısız olabilir?”
      </strong>
      sorusunu defalarca sorduk.
     </p>
     <p class="graf graf--p graf-after--p" id="56f3" name="56f3">
      Cevabımızı, “Topic Modelling” için kullanmayı düşündüğümüz “LDA(Latent Dirichlet Allocation)” algoritmasının sabit bir konu sayısıyla çalıştığını fark ettiğimizde verdik. LDA’nın kullandığı istatistiksel model bir
      <strong class="markup--strong markup--p-strong">
       K
      </strong>
      sayısı alıyor, metinleri o sayıda farklı konuya ayırmayı deniyor. En baştan itibaren zaten tweet’lerin ironik ve komedi içerikleri, sosyal medyanın dinamikleri, tweet’lerin kısa olması dolayısıyla konularının anlaşılamaması gibi problemlerin varlığını tahmin ettiğimiz için sisteme dair zaten belli şüphelerimiz ve korkularımız mevcuttu. Bunların hepsinin üstüne bir de kullanmayı düşündüğümüz modelin kullanımımıza uygun olmadığını gördüğümüzde,
      <a class="markup--user markup--p-user" data-action="show-user-card" data-action-type="hover" data-action-value="3102d6d5f774" data-anchor-type="2" data-href="https://medium.com/u/3102d6d5f774" data-user-id="3102d6d5f774" href="https://medium.com/u/3102d6d5f774" target="_blank">
       Ahmet YÜKSEL
      </a>
      ’e döndüm ve dedim ki “Bırakalım. Bu proje olmayacak ben inancımı kaybettim”. Tek problem LDA olsaydı belki Topic Modelling için başka yollar arayabilirdik, ama projenin temelinin yeterince sağlam olmadığına dair inancımıza yeni problemler eklenince bizim için inanç eşiğini geçmiş olduk, projeyi tamamen bıraktık.
     </p>
     <p class="graf graf--p graf-after--p" id="997d" name="997d">
      Sürece bakınca, proje bize çok ilginç tecrübeler yaşattı.
      <a class="markup--user markup--p-user" data-action="show-user-card" data-action-type="hover" data-action-value="3102d6d5f774" data-anchor-type="2" data-href="https://medium.com/u/3102d6d5f774" data-user-id="3102d6d5f774" href="https://medium.com/u/3102d6d5f774" target="_blank">
       Ahmet YÜKSEL
      </a>
      Faruk Eczacıbaşı ile toplantı yaptı, ben Habertürk’e çıktım, ODTÜ Teknokent’te ofis kiralamak için pazarlık yaptık.
      <a class="markup--anchor markup--p-anchor" data-href="https://aiethicslab.com" href="https://aiethicslab.com" rel="noopener" target="_blank">
       AI Ethics Lab
      </a>
      projeyle ilgili bir rapor yazdı, ilk kez bir projemizi gerçekleştirsek oluşabilecek etik problemleri düşünme fırsatı bulduk. Teyit.org’un
      <a class="markup--anchor markup--p-anchor" data-href="https://factoryprogram.org" href="https://factoryprogram.org" rel="noopener" target="_blank">
       Factory Bootcamp
      </a>
      ’ine katıldık, insanların teknik olarak imkansız fikirleri sanki mümkünmüş gibi sunmasına açık açık şahit olduk. Raporlar yazdık, sunumlar hazırladık, gelir modelleri tasarladık, hatalar yaptık, bir noktada günde 10–12 saat toplantıya giriyor çalışıyorduk.
      <a class="markup--user markup--p-user" data-action="show-user-card" data-action-type="hover" data-action-value="3102d6d5f774" data-anchor-type="2" data-href="https://medium.com/u/3102d6d5f774" data-user-id="3102d6d5f774" href="https://medium.com/u/3102d6d5f774" target="_blank">
       Ahmet YÜKSEL
      </a>
      ile o dönemde şimdiki dostluğumuzun temellerini attık. Tek bir kelimeyle,
      <strong class="markup--strong markup--p-strong">
       öğrendik
      </strong>
      . Sürekli bir şekilde öğrendik, tecrübe edindik.
     </p>
     <p class="graf graf--p graf-after--p" id="59c9" name="59c9">
      Bu yazıyı yazmak için o dönem hazırladığım bazı dökümanlara baktım, yazım hataları, tasarım hataları, açık bir şekilde mantıksal boşlukları olan fikirler… Geriye bakıp kendini beğenmemek ne güzel bir hismiş onu tekrar hatırladım; gelişmenin önemini gördüm.
     </p>
     <p class="graf graf--p graf-after--p" id="cfe9" name="cfe9">
      <strong class="markup--strong markup--p-strong">
       Bu projenin tekrardan ayağa kalkma şansı olduğunu düşünmüyorum. Bu projeden aldığım en büyük ders, denemek gerektiği. Bir şeyleri deneyip, hayal edip, heyecanlanıp, emek ve vakit harcamak gerek. En güzel anılar böyle böyle birikiyor.
      </strong>
     </p>
     <p class="graf graf--p graf-after--p" id="44f9" name="44f9">
      Aşağıda o dönemde hazırladığımız sunum ve raporlardan bazı parçalar paylaşıyorum.
     </p>
     <p class="graf graf--p graf-after--p" id="a2bf" name="a2bf">
      <strong class="markup--strong markup--p-strong">
       Konsept Logolar:
      </strong>
     </p>
    </div>
    <div class="section-inner sectionLayout--outsetRow" data-paragraph-count="3">
     <figure class="graf graf--figure graf--layoutOutsetRow is-partialWidth graf-after--p" id="6936" name="6936" style="width: 33.333%;">
      <img class="graf-image" data-height="916" data-image-id="1*Yvhs70dtt9gxAokEAgoxSw.png" data-width="936" src="https://cdn-images-1.medium.com/max/400/1*Yvhs70dtt9gxAokEAgoxSw.png"/>
     </figure>
     <figure class="graf graf--figure graf--layoutOutsetRowContinue is-partialWidth graf-after--figure" id="8212" name="8212" style="width: 33.333%;">
      <img class="graf-image" data-height="916" data-image-id="1*1G_me43zHNiTyTwLDYxWng.png" data-is-featured="true" data-width="936" src="https://cdn-images-1.medium.com/max/400/1*1G_me43zHNiTyTwLDYxWng.png"/>
     </figure>
     <figure class="graf graf--figure graf--layoutOutsetRowContinue is-partialWidth graf-after--figure" id="f7f6" name="f7f6" style="width: 33.333%;">
      <img class="graf-image" data-height="916" data-image-id="1*pBxfGxdb4_uaQhgwnLLVZQ.png" data-width="936" src="https://cdn-images-1.medium.com/max/400/1*pBxfGxdb4_uaQhgwnLLVZQ.png"/>
     </figure>
    </div>
    <div class="section-inner sectionLayout--outsetRow" data-paragraph-count="3">
     <figure class="graf graf--figure graf--layoutOutsetRow is-partialWidth graf-after--figure" id="cd49" name="cd49" style="width: 33.333%;">
      <img class="graf-image" data-height="916" data-image-id="1*qpKQovkLyL_d8Tv8Ty7DnA.png" data-width="936" src="https://cdn-images-1.medium.com/max/400/1*qpKQovkLyL_d8Tv8Ty7DnA.png"/>
     </figure>
     <figure class="graf graf--figure graf--layoutOutsetRowContinue is-partialWidth graf-after--figure" id="04d7" name="04d7" style="width: 33.333%;">
      <img class="graf-image" data-height="916" data-image-id="1*KJ7hDQbmnASvKYxgc2BTXg.png" data-width="936" src="https://cdn-images-1.medium.com/max/400/1*KJ7hDQbmnASvKYxgc2BTXg.png"/>
     </figure>
     <figure class="graf graf--figure graf--layoutOutsetRowContinue is-partialWidth graf-after--figure" id="0c1c" name="0c1c" style="width: 33.333%;">
      <img class="graf-image" data-height="916" data-image-id="1*r61K7I-k1vwu0aa4Fi1GYw.png" data-width="936" src="https://cdn-images-1.medium.com/max/400/1*r61K7I-k1vwu0aa4Fi1GYw.png"/>
     </figure>
    </div>
    <div class="section-inner sectionLayout--outsetRow" data-paragraph-count="2">
     <figure class="graf graf--figure graf--layoutOutsetRow is-partialWidth graf-after--figure" id="2cb0" name="2cb0" style="width: 50%;">
      <img class="graf-image" data-height="916" data-image-id="1*W8rG8FweSkqhsZuFnukPbg.png" data-width="936" src="https://cdn-images-1.medium.com/max/600/1*W8rG8FweSkqhsZuFnukPbg.png"/>
     </figure>
     <figure class="graf graf--figure graf--layoutOutsetRowContinue is-partialWidth graf-after--figure" id="1bb2" name="1bb2" style="width: 50%;">
      <img class="graf-image" data-height="916" data-image-id="1*Rd5cQv6Z3q4ECcwgZ0-v9A.png" data-width="936" src="https://cdn-images-1.medium.com/max/600/1*Rd5cQv6Z3q4ECcwgZ0-v9A.png"/>
     </figure>
    </div>
    <div class="section-inner sectionLayout--outsetColumn">
     <figure class="graf graf--figure graf--layoutOutsetCenter graf-after--figure" id="c04a" name="c04a">
      <img class="graf-image" data-height="916" data-image-id="1*VOSvmCy2Vji6uUKiExvMdw.png" data-width="936" src="https://cdn-images-1.medium.com/max/1200/1*VOSvmCy2Vji6uUKiExvMdw.png"/>
     </figure>
    </div>
    <div class="section-inner sectionLayout--insetColumn">
     <p class="graf graf--p graf-after--figure" id="3d01" name="3d01">
      <strong class="markup--strong markup--p-strong">
       Rapor:
      </strong>
     </p>
     <p class="graf graf--p graf-after--p" id="60d4" name="60d4">
      <a class="markup--anchor markup--p-anchor" data-href="https://docs.google.com/document/d/1uQoKRDd3uPeJPnOCGKmAJ5UdCoqCvs2WjW7Uxj9G-OA/edit?usp=sharing" href="https://docs.google.com/document/d/1uQoKRDd3uPeJPnOCGKmAJ5UdCoqCvs2WjW7Uxj9G-OA/edit?usp=sharing" rel="nofollow noopener" target="_blank">
       https://docs.google.com/document/d/1uQoKRDd3uPeJPnOCGKmAJ5UdCoqCvs2WjW7Uxj9G-OA/edit?usp=sharing
      </a>
     </p>
     <p class="graf graf--p graf-after--p" id="52f8" name="52f8">
      <strong class="markup--strong markup--p-strong">
       Sunum:
      </strong>
     </p>
     <figure class="graf graf--figure graf--iframe graf-after--p graf--trailing" id="7dd4" name="7dd4">
      <iframe frameborder="0" height="559" scrolling="no" src="https://docs.google.com/presentation/embed?id=17n8KwAs2lorS_pONGmbEDJCioBhM2Cp9&amp;size=l" width="700">
      </iframe>
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
   <a href="https://medium.com/p/c2db010d6655">
    <time class="dt-published" datetime="2022-12-21T13:28:52.547Z">
     December 21, 2022
    </time>
   </a>
   .
  </p>
  <p>
   <a class="p-canonical" href="https://medium.com/@alpkeles99/yar%C4%B1m-kalan-projeler-3-fact-checkers-tool-c2db010d6655">
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
