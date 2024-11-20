+++
title = "Lokasyon Bazlı Ödeme Hakkında Bazı Düşünceler"
date = "2022-01-16"
[taxonomies]
tags = ['software engineering']
language = ["tr"]
+++

<article class="h-entry">
 <section class="e-content" data-field="body">
  <section class="section section--body section--first section--last" name="23e5">
   <div class="section-content">
    <div class="section-inner sectionLayout--insetColumn">
     <h3 class="graf graf--h3 graf--leading graf--title" id="7751" name="7751">
      Lokasyon Bazlı Ödeme Hakkında Bazı Düşünceler
     </h3>
     <figure class="graf graf--figure graf-after--h3" id="9492" name="9492">
      <img class="graf-image" data-height="960" data-image-id="1*29CZclPcQpx6oWpSuW1r0Q.png" data-is-featured="true" data-width="1440" src="https://cdn-images-1.medium.com/max/800/1*29CZclPcQpx6oWpSuW1r0Q.png"/>
     </figure>
     <p class="graf graf--p graf-after--figure" id="5d22" name="5d22">
      Son günlerde yazılımcı Twitter’ında maaşlarla ilgili genel bir tartışma dönüyor. Bu tarz durumlarda fikirlerimizi Twitter üzerinden yazmaya çalıştığımızda sitenin yapısı gereği genelde kısa/temelini kuramadığımız/yeterli açıklama yapamadığımız bir şekilde ifade ediyoruz. (Kimse için önemli olduğundan değil ama yine de) Kendi düşüncelerimi ve argümanlarımı bir blog postta toplamak istedim. Tartışmayı etik bir düzleme koymaktan ziyade(ahlaki bakış açısının görece subjektif olduğunu düşünüyorum), daha finansal olarak incelemeye çalışacağım.
     </p>
     <p class="graf graf--p graf-after--p" id="f369" name="f369">
      Tartışmanın genel ekseni şu şekilde. A şirketi X ve Y şehirlerinden/ülkelerinden 2 farklı kişi(tartışma bağlamında genelde yazılımcı) çalıştırıyor. Bu kişilerin aldıkları maaş neye göre belirlenmeli? Yaptıkları işe göre mi? Yoksa yaşadıkları yerin yaşam masrafına göre mi? Soru günün sonunda bu kadar basit kalmıyor, tek bir cevapta birleştirmek de imkansıza yakın, ama deneyelim bakalım.
     </p>
     <h4 class="graf graf--h4 graf-after--p" id="34d0" name="34d0">
      Basit bir senaryodan başlayıp, senaryoyu çeşitlendirerek durumları analiz etmeye çalışalım.
     </h4>
     <h3 class="graf graf--h3 graf-after--h4" id="a4a7" name="a4a7">
      En Basit Senaryo:
     </h3>
     <ul class="postList">
      <li class="graf graf--li graf-after--h3" id="06f2" name="06f2">
       X çalışanı İstanbul’da yaşıyor. Yaşam masrafı 10.000 ₺
      </li>
      <li class="graf graf--li graf-after--li" id="3a50" name="3a50">
       Y çalışanı Ankara’da yaşıyor. Yaşam masrafı 7.000 ₺
      </li>
      <li class="graf graf--li graf-after--li" id="eb75" name="eb75">
       Şirket yer bazlı maaş uygulaması yapmıyor, aynı pozisyonda aynı işi yapan bu iki kişiye aynı maaşı veriyor, bu maaş da 12.000 ₺ olsun.
      </li>
     </ul>
     <p class="graf graf--p graf-after--li" id="f51d" name="f51d">
      Bu noktada Ankara’da çalışan kişi net bir şekilde avantajlı oluyor(mu acaba?). Ay sonunda bir kişinin elinde 5.000₺ kalırken diğerinde 2.000₺ kalıyor. Twitter’da birkaç defa gördüğüm argümanlardan birisi herkesin eninde sonunda Ankara’ya taşınacağı.(orijinal örnekte aklımda Hindistan/Los Angeles olarak kalmış bu şehirler)Bu argümanı birkaç sebepten ötürü çok da mantıklı göremiyorum.
     </p>
     <ul class="postList">
      <li class="graf graf--li graf-after--p" id="70a2" name="70a2">
       Ankara/İstanbul arasındaki tek fark yaşam masrafı değil. Sosyokültürel yapı, ulaşım, barınma imkanları, aktivite çeşitliliği, yaşam tarzı… Burada akla gelmeyecek pek çok daha farklı nokta var. İnsanlar bir şehirde yaşamayı seçerken orada en iyi maaşı aldıkları için seçmek zorunda değiller, özellikle aldıkları maaş zaten kendilerine yeten bir maaşsa. Herkesin maaş maksimizasyonuna gideceğine inanmak biraz insanlıktan uzak bir bakış açısı gibi geliyor bana.
      </li>
      <li class="graf graf--li graf-after--li" id="6716" name="6716">
       Aynı şekilde, bu tarz bir “taşınma” hareketi o kadar basit nitelendirilebilecek bir hareket değil. Para insanların hayatındaki tek motivasyon değil.
      </li>
     </ul>
     <p class="graf graf--p graf-after--li" id="db78" name="db78">
      Bu noktada tartışmanın eksenini şirket bakış açısına kaydırmak gerekiyor. Şirketler sınırlı kaynakla maksimum kar elde etme hedefiyle yönetilen kurumlar. Ödedikleri maaş da bu kaynaklardan birisi. Bu da şu şekilde bir sonuca yol açıyor.
     </p>
     <ul class="postList">
      <li class="graf graf--li graf-after--p" id="d820" name="d820">
       A ve B şirketlerini ele alalım.
      </li>
      <li class="graf graf--li graf-after--li" id="d9fa" name="d9fa">
       2 çalışan için de 2 şirketin toplam ödeme bütçesi 24.000₺ olsun.
      </li>
      <li class="graf graf--li graf-after--li" id="c1a5" name="c1a5">
       A şirketi lokasyon bağımsız ödeme yapsın, yani yukarıdaki gibi X çalışanına da Y çalışanına da bu ödemeyi 12.000₺ olarak bölüştürsün.
      </li>
      <li class="graf graf--li graf-after--li" id="8076" name="8076">
       B şirketi lokasyon bazlı ödeme yapsın.
      </li>
      <li class="graf graf--li graf-after--li" id="dfd7" name="dfd7">
       X çalışanına 10.000 + 3.500 = 13.500₺
      </li>
      <li class="graf graf--li graf-after--li" id="c397" name="c397">
       Y çalışanına 7.000 + 3.500 = 10.500₺
      </li>
     </ul>
     <p class="graf graf--p graf-after--li" id="8b19" name="8b19">
      Hem şirketlerin, hem de çalışanların tek motivasyonunun para olduğunu varsayalım.
     </p>
     <p class="graf graf--p graf-after--p" id="2c51" name="2c51">
      Eşit ücret ödeyen şirket her yerden çalışan alabilir. Dolayısıyla zaten lokasyon bazlı ödeme yapan şirkette daha düşük ücret alacak olan Ankaralı çalışan eşit ücret ödeyen A şirketine gitmeyi tercih edecektir.
     </p>
     <p class="graf graf--p graf-after--p" id="c8cc" name="c8cc">
      Lokasyon bazlı ödeme yapan şirketin en temel amacı İstanbullu çalışanı kaybetmemek. Ama bunu yaparken Ankaralı hiçbir çalışanı alamayacağı için(herkesin hayattaki tek motivasyonu para olduğundan hepsi A şirketine gitti), B şirketi tamamen İstanbullu çalıştırmak zorunda. Bu noktada B şirketi lokalizasyon yapmadığı duruma göre daha zararda hale geldi.
     </p>
     <p class="graf graf--p graf-after--p" id="dc5e" name="dc5e">
      Yani tüm market açık olsa, herkes tamamen para odaklı çalışsa, şirketlerin verebildiği ücretler birbiriyle eşit olsa şirketin lokalizasyon yapması mantıksız. E peki bu şirketler bunu neden yapıyor? Çünkü şirketlerin finansal güçleri birbirine eşit değil.
     </p>
     <h3 class="graf graf--h3 graf-after--p" id="3b7e" name="3b7e">
      Senaryo 2:
     </h3>
     <p class="graf graf--p graf-after--h3" id="1f2a" name="1f2a">
      İstanbul/Ankara’yı gelin İstanbul/Silikon Vadisi yapalım.
     </p>
     <ul class="postList">
      <li class="graf graf--li graf-after--p" id="d271" name="d271">
       İstanbul’da yaşam masrafı 10.000₺
      </li>
      <li class="graf graf--li graf-after--li" id="b05d" name="b05d">
       Silikon Vadisinde yaşam masrafı 100.000₺
      </li>
      <li class="graf graf--li graf-after--li" id="2fac" name="2fac">
       A şirketi bu zamana kadar Silikon Vadisinde iş yapan bir şirket olsun, dolayısıyla çalışanlarına 120.000₺ ödüyor olsun. Şirket uzaktan çalışmanın avantajlarını görüp İstanbul’daki iyi yazılımcıları almak istiyor olsun. Şirket İstanbul’daki yazılımcılara 120.000₺ ödese İstanbul’da başka şirkette yazılımcı kalmaz. Ama bu durum 40.000₺ için de geçerli. Dolayısıyla şirketin bakış açısından 120.000₺’ye 1 yazılımcı çalıştırmaktansa 40.000₺’ye 3 yazılımcı çalıştırmak çok mantıklı hale geliyor. Bu ücret ile yarışabilecek yerel hiçbir şirket olmadığından dolayı çok rahat bir şekilde istediği yazılımcıyı alabiliyor.
      </li>
     </ul>
     <p class="graf graf--p graf-after--li" id="3066" name="3066">
      Burada yazılımcıların ne yaptığını tartışmak gerekiyor.
     </p>
     <ul class="postList">
      <li class="graf graf--li graf-after--p" id="da9f" name="da9f">
       Taşınmak kolay olsa, yazılımcı İstanbul’dan Los Angeles’a taşınabilir. Maaş’tan sonra elinde kalan para aynı bile olacak olsa, gideceği ofisin imkanları, orada kazanacağı network, önüne açılacak diğer ihtimaller çok daha büyük olacaktır. Ancak hepimizin bildiği gibi ülkeler arası taşınmanın bürokratik, siyasi, kültürel, ekonomik, sosyal çok fazla engeli var.
      </li>
      <li class="graf graf--li graf-after--li" id="01a2" name="01a2">
       Para harici elementleri elediğimizden dolayı, yazılımcıların önünde bu şirketlerden gelecek teklifi kabul etmekten başka seçenek kalmıyor.
      </li>
     </ul>
     <p class="graf graf--p graf-after--li" id="3f55" name="3f55">
      Peki ya bir Türk bir küresel şirket yerine, 2 tane küresel şirketi tartışırsak ne olacak?
     </p>
     <h3 class="graf graf--h3 graf-after--p" id="4ec4" name="4ec4">
      Senaryo 3:
     </h3>
     <ul class="postList">
      <li class="graf graf--li graf-after--h3" id="baee" name="baee">
       A şirketi İstanbul’a 40.000₺, Silikon Vadisine 120.000₺ ödüyor olsun.
      </li>
      <li class="graf graf--li graf-after--li" id="4194" name="4194">
       B şirketi İstanbul’a da, Silikon Vadisine de 80.000₺ ödüyor olsun.
      </li>
      <li class="graf graf--li graf-after--li" id="b9a0" name="b9a0">
       Silikon vadisindeki tüm yazılımcılar A şirketine gidecek.
      </li>
      <li class="graf graf--li graf-after--li" id="03f8" name="03f8">
       İstanbul’daki tüm yazılımcılar B şirketine gidecek.
      </li>
      <li class="graf graf--li graf-after--li" id="747f" name="747f">
       Yani şirket açısından baktığımızda lokalizasyon sayesinde yine kar edemiyor hale gelecek.
      </li>
     </ul>
     <p class="graf graf--p graf-after--li" id="4a5b" name="4a5b">
      Bu durumda yapılacak en basit varsayım, yurtdışı bazlı firmaların lokalizasyonla aslında kar edememeleri gerektiği. Peki nasıl kar ediyorlar? Yerel şirketlerin verdikleri maaşları ezerek. Piyasada yazılımcı sayısı küresel firmaların ihtiyaç duyduğunun çok üstünde. Bu şirketler lokalizasyon uygulayarak hala piyasadan ihtiyaç duydukları tüm yazılımcıları toplayabiliyorlar.
     </p>
     <p class="graf graf--p graf-after--p" id="45a1" name="45a1">
      Bu zamana kadar her şeyi şirketler açısından konuştuk, çok fazla basitleştirmiş olsam da genel manasıyla iç dinamiklerin en azından belli bir kısmını kapsayabildiğimi umuyorum. Bu noktada topu freelancer yazılımcılara çevirmek istiyorum.
     </p>
     <p class="graf graf--p graf-after--p" id="d890" name="d890">
      Bahsettiğim şirket ücreti lokasyona göre ayarlar ona göre çalışan bulur dinamiğinin tamamen simetriği freelancer ücreti lokasyona göre ayarlar ona göre çalışacak iş bulur konseptinde tutuyor. Şirketlerin yaptığı ne derece etikse ve komikse, freelancer’ın yaptığını da benzer değerlendirmek gerekecektir. Kısaca açıklamak gerekirse.
     </p>
     <ul class="postList">
      <li class="graf graf--li graf-after--p" id="ac29" name="ac29">
       A Freelancer’ı lokalizasyon yapıyor, İngiltere’deki işe 20.000₺, Türkiye’deki işe 5000₺ alıyor.
      </li>
      <li class="graf graf--li graf-after--li" id="ec15" name="ec15">
       B Freelancer’ı lokalizasyon yapmıyor. İki işe de 12.500₺ alıyor.
      </li>
      <li class="graf graf--li graf-after--li" id="c910" name="c910">
       A kişisi Türkiye’deki tüm işleri alırken, B kişisi İngiltere’deki tüm işleri alıyor olacak.
      </li>
     </ul>
     <p class="graf graf--p graf-after--li" id="ab5e" name="ab5e">
      3 senaryonun hepsi benzer şekilde bu duruma uyarlanabilir.
     </p>
     <p class="graf graf--p graf-after--p" id="c2c7" name="c2c7">
      Burada gerçek hayatta çok daha kompleks olan market analizleri, etik, para harici tüm motivasyonları yok sayarak durumu belli bir seviyede analiz etmeye çalıştım; bu halinde bile üzerine düşünürken emin olamadığım çok fazla nokta oldu. Günün sonucunda varabildiğim tek sonuç şu, Twitter’da birbirimize 280 karakterle ahkem kesmeden önce biraz daha düşünmek gerekiyor sanırım.
     </p>
     <p class="graf graf--p graf-after--p graf--trailing" id="de43" name="de43">
      Benim şahsi düşüncem ne peki? Tabii ki serbest piyasada herkes her şeyi yapabilir, ama ben lokalizasyon yapan bir şirkette çalışmam. Kısa vade kar maksimizasyonu yapan şirketin uzun vade vizyonundan o şirketteki yazılımcının da fayda sağlayacağını düşünmüyorum. Şirketler kar odaklı varlıklar, çalışanların yaptığı her iş eninde sonunda paraya dönüşüyor. Bence bir şirket bir çalışana yaptığı işin şirkete değerine göre ücret ödemeli, paranın çalışan için değerine göre değil. Şirketle çalışan arasındaki kontratın işin kendisinin değerinden uzaklaşıp tamamen paraya bağlı hassas bir dengeye dönüşmesi halinde herhangi bir çalışanın şirketine bağlı olacağını düşünmüyorum. Belki de günümüzde yazılımcıların 6 ay, 1 yıl gibi sürelerle sürekli iş değiştirmesinin ardında yatan sebeplerden birisi budur, bilemiyorum. Karmaşık bir konu, kalp kırmaya, kesin hükümlerde bulunmaya gerek yok gibi hissediyorum; hiçbirimiz tam anlamıyla haklı değiliz.
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
   <a href="https://medium.com/p/8ac9bb1161ca">
    <time class="dt-published" datetime="2022-01-17T01:35:39.065Z">
     January 17, 2022
    </time>
   </a>
   .
  </p>
  <p>
   <a class="p-canonical" href="https://medium.com/@alpkeles99/lokasyon-bazl%C4%B1-%C3%B6deme-hakk%C4%B1nda-baz%C4%B1-d%C3%BC%C5%9F%C3%BCnceler-8ac9bb1161ca">
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
