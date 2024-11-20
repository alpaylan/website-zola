+++
title = "Proje Günlükleri: CVDL(CV Description Language)#1"
date = "2022-01-10"
[taxonomies]
tags = []
language = ["tr"]
+++

<article class="h-entry">
 <section class="e-content" data-field="body">
  <section class="section section--body section--first section--last" name="c9aa">
   <div class="section-content">
    <div class="section-inner sectionLayout--insetColumn">
     <h3 class="graf graf--h3 graf--leading graf--title" id="783e" name="783e">
      Proje Günlükleri:
                            CVDL(CV Description Language)#1
     </h3>
     <p class="graf graf--p graf-after--h3" id="dc24" name="dc24">
      Merhabalar, Proje Günlükleri
                            konseptinin ilk yazısı olduğu için projenin kendisine girmeden biraz daha serinin
                            konseptinden bahsetmek istedim.
     </p>
     <p class="graf graf--p graf-after--p" id="5a95" name="5a95">
      Üniversiteye geldiğimden beri
                            sürekli farklı alanlarda farklı tarzlarda projelerle ilgileniyorum. Geldiğimiz yıl 4 kişi
                            yurt mutfağında matkapla aluminyum deldiğimiz zamanlardan oturup kendi programlama dilimizi
                            tasarlamaya çalıştığımız zamanlara pek çok farklı insan grubuyla pek çok farklı işle
                            uğraştım. Bunların hepsini yaparken çok farklı tecrübeler yaşadım, her tecrübeden yeni bakış
                            açıları kazandım. Maalesef ki bunları kimse ile paylaşma şansım olmadı, hatta ve hatta
                            yazıya aktarmadığım için bu tecrübelerin ciddi bir kısmı benim bilinçaltımda kayboldu gitti,
                            ben bile hatırlamıyorum.
     </p>
     <p class="graf graf--p graf-after--p" id="bbff" name="bbff">
      Bu sebeptendir ki çok uzun süredir
                            aklımda içinde bulunduğum projelerle ilgili günlüğümsü yazılar yazıp bunları paylaşmak
                            vardı. Hem yaşadıklarımı dokümante etmek, gelecekte geriye baktığımda hatırlayabileceğim bir
                            anı defteri oluşturmak; hem de kendi projesine girişeceklere yol haritası olabilecek
                            öneriler ortaya koymak, bakın bunları bunları yapabilirsiniz belki aklınıza gelmemiştir
                            diyebilmek, karşılarına çıkabilecek problemlere önden hazırlıklı olmalarını sağlamak
                            istiyorum.
     </p>
     <p class="graf graf--p graf-after--p" id="bafc" name="bafc">
      Bu noktada kendi başıma girmeye
                            çabaladığım ilk açık kaynaklı proje olan CVDL ile başlamanın güzel bir fikir olduğuna karar
                            verdim. Nedenlerini aşağıda açıklayayım.
     </p>
     <ul class="postList">
      <li class="graf graf--li graf-after--p" id="e6f4" name="e6f4">
       Normal şartlarda şu zamana
                                kadar yazdığım hiçbir açık kaynaklı kodun birileri tarafından kullanılması gibi bir
                                amacım olmamıştı, bu zamana kadar ya şirket/ödev/proje kapsamında kapalı kaynaklı kodlar
                                yazdım; ya da açık kaynaklı yazdığım herhangi bir kodu yalnızca portfolyom genişlesin,
                                Github hesabım dolsun diye yazdım. İlk kez başkaları tarafından kullanılmasını
                                beklediğim bir yazılım projesine giriştiğim için oradan alacağım tecrübelerin bunu
                                sonradan deneyeceklere ışık olabileceğini düşünüyorum.
      </li>
      <li class="graf graf--li graf-after--li" id="7d11" name="7d11">
       İlk kez kompleks bir projeye
                                tek başıma giriyorum, teknik yükü üstleniyorum. Bu zamana kadarki çok basit bir
                                karmaşıklığın üstündeki tüm projelerde yanımda birileri oldu, ben de genel olarak kod
                                yazmayı, yazılım mühendisliği yapmayı sevmeyen birisi olarak kaçabildiğim kadar kaçtım
                                teknik yükü üstüme almaktan. Algoritma tasarımı, genel sistem mimarisi, iş modeli gibi
                                kodlamanın kendisinden uzak taraflara doğru kendimi ittim hep.
      </li>
      <li class="graf graf--li graf-after--li" id="1a9b" name="1a9b">
       Neden bu sefer bunu bozdum,
                                çünkü fikri satabildiğim kimse yok. Herkes iyi ya güzel fikir demesine rağmen fikri en
                                çok benimseyen hala benim. Ben de dedim madem böyle bir durum var dene bakalım, en kötü
                                ne kaybedersin ki. 2–3 kişiyle birlikte ilerleyeceğiz gibi duruyor, teknik liderlik
                                tarafında onlara iş verme, kod inceleme, açık kaynak proje yönetimi gibi taraflarda da
                                tecrübe kazanmam gerekecek, çok muhtemel ki bir sürü hata yapacağım, sizlere yazacağım,
                                siz de okuyup ya ‘A evet çok mantıklı iyi ki okumuşum’ diyeceksiniz, ya da ‘Salağa bak
                                şunu bile düşünmemiş bi de oturmuş blog yazıp bir şey anlatmaya çalışıyor’ diyip
                                güleceksiniz, her halükarda sizlere ya bir şey öğretmiş ya da güldürmüş olacağım.
      </li>
     </ul>
     <p class="graf graf--p graf-after--li" id="f9f7" name="f9f7">
      Proje sürecinin detaylarına
                            girmeden önce projenin ne olduğundan bahsedeyim.
     </p>
     <figure class="graf graf--figure graf-after--p" id="b64b" name="b64b">
      <img class="graf-image" data-height="572" data-image-id="1*RVnF3B_ZRK12iRgjwjVb7A.png" data-is-featured="true" data-width="1145" src="https://cdn-images-1.medium.com/max/800/1*RVnF3B_ZRK12iRgjwjVb7A.png"/>
     </figure>
     <p class="graf graf--p graf-after--figure" id="4a3f" name="4a3f">
      CVDL açık kaynaklı bir CV
                            Formatı oluşturulması için bir inisiyatif. Hepimiz şu zamana kadar CV hazırladık, pek çok
                            web sitesi(CV Builder), Latex, Word, Canva… gibi farklı metotlar izledik. Bu metotların
                            hepsinin problemleri var.
     </p>
     <h3 class="graf graf--h3 graf-after--p" id="342e" name="342e">
      CV Builder
     </h3>
     <ul class="postList">
      <li class="graf graf--li graf-after--h3" id="126a" name="126a">
       Çoğu paralı
      </li>
      <li class="graf graf--li graf-after--li" id="76c1" name="76c1">
       Bayağı kullanışlı
      </li>
      <li class="graf graf--li graf-after--li" id="4fe4" name="4fe4">
       Kullandığınız siteye
                                limitlisiniz, onun verdiği özelleştirmelerin üstüne çıkamıyorsunuz. Buna ilaveten CV’mi
                                ordan alayım da başka yere çıkarayım diyemiyorsunuz, size yalnızca bir adet PDF veriyor
      </li>
      <li class="graf graf--li graf-after--li" id="84fa" name="84fa">
       Para vermeyi bıraktığınız
                                anda CV’niz kayboluyor, sıfırdan hazırlamak için tüm o eforu harcamak zorundasınız
      </li>
      <li class="graf graf--li graf-after--li" id="6070" name="6070">
       Ortada bir veriden ziyade bir
                                hesap olduğu için, gel ben senle CV’mi paylaşayım sen otur aynı şablondan yap
                                diyemiyorsunuz bir arkadaşınıza, çoğu zaman aynı siteden üyelik alsa bile sıfırdan her
                                şeyi hazırlaması lazım
      </li>
      <li class="graf graf--li graf-after--li" id="a132" name="a132">
       Aynısı sizin için de geçerli,
                                eski CV’nizden kurtulmaya karar verip yenisini hazırlamak isteseniz başınız ağrıyor
      </li>
      <li class="graf graf--li graf-after--li" id="e90a" name="e90a">
       Hata kaza site kapansa, şu
                                zamana kadar yaptığınız her şey kaybolacak
      </li>
     </ul>
     <h3 class="graf graf--h3 graf-after--li" id="1e7d" name="1e7d">
      Word/Canva/Latex
     </h3>
     <ul class="postList">
      <li class="graf graf--li graf-after--h3" id="b08d" name="b08d">
       Üçü de ücretsiz
      </li>
      <li class="graf graf--li graf-after--li" id="5a10" name="5a10">
       Canva ve Word’de hazırlanan
                                CV’lerin estetik olma ihtimali inanılmaz düşük
      </li>
      <li class="graf graf--li graf-after--li" id="0a0d" name="0a0d">
       Latex öğrenmek zor, o
                                spesifik şablonda nasıl CV yazıldığını öğrenmek daha zor, 3 yıldır aynı şablonu
                                kullanıyorum hala bir şey yaparken zorlanıyorum
      </li>
      <li class="graf graf--li graf-after--li" id="4199" name="4199">
       Üçü de çok fazla efor
                                istiyor, aşırı kullanışsızlar
      </li>
     </ul>
     <h3 class="graf graf--h3 graf-after--li" id="80bb" name="80bb">
      CVDL
     </h3>
     <ul class="postList">
      <li class="graf graf--li graf-after--h3" id="9dc7" name="9dc7">
       CVDL ile amacım bu iki farklı
                                tarafın iyi özelliklerini birleştirmek.
      </li>
      <li class="graf graf--li graf-after--li" id="b240" name="b240">
       Kullanışlı bir web sitesi
                                olsa, ama CV’nin ham haline de ulaşabilsen, isteyen herkes şablon tasarlayabilse, para
                                ödemek zorunda kalmasan, bunların hepsi de senin elinde olsa bu sayede site kapansa
                                hiçbir şey kaybetmesen tadından yenmez değil mi?
      </li>
      <li class="graf graf--li graf-after--li" id="e15d" name="e15d">
       Yenmez tabii. Ben de oturdum
                                başladım acaba bunu yapabilir miyiz diye.
      </li>
     </ul>
     <p class="graf graf--p graf-after--li" id="060d" name="060d">
      Sistemin kendisine girmeden önce
                            kodunu da şöyle bir bırakayım.
     </p>
     <div class="graf graf--mixtapeEmbed graf-after--p" id="15d1" name="15d1">
      <a class="markup--anchor markup--mixtapeEmbed-anchor" data-href="https://github.com/alpaylan/cvdl" href="https://github.com/alpaylan/cvdl" title="https://github.com/alpaylan/cvdl">
       <strong class="markup--strong markup--mixtapeEmbed-strong">
        GitHub - alpaylan/cvdl: CV
                                    Description Language
       </strong>
       <br/>
       <em class="markup--em markup--mixtapeEmbed-em">
        CV
                                    Description Language is the first part of a project aiming to create an open source
                                    format for description of…
       </em>
       github.com
      </a>
      <a class="js-mixtapeImage mixtapeImage u-ignoreBlock" data-media-id="a0acbdb86cfc1487daf6570dc3645138" data-thumbnail-img-id="0*0Zw75mU8VqiLh-G3" href="https://github.com/alpaylan/cvdl" style="background-image: url(https://cdn-images-1.medium.com/fit/c/160/160/0*0Zw75mU8VqiLh-G3);">
      </a>
     </div>
     <p class="graf graf--p graf-after--mixtapeEmbed" id="2b67" name="2b67">
      Mantık şu şekilde
                            çalışıyor, 3 tane ayrı dosya var arka planda.
     </p>
     <h3 class="graf graf--h3 graf-after--p" id="13c0" name="13c0">
      (Eğer yazılımcı değilseniz
                            aşağıdaki dosya açıklamalarını atlayabilirsiniz)
     </h3>
     <p class="graf graf--p graf-after--h3" id="b40d" name="b40d">
      1- CVCD(CV Content Document)
                            Dosyası
     </p>
     <p class="graf graf--p graf-after--p" id="e504" name="e504">
      Bu dosyada aslında sen CV’nin
                            içeriğini yazıyorsun. Hangi okullara gittin, nerelerde staj yaptın, hangi dilleri ne derece
                            biliyorsun… Nasıl Word’e yazıyorsan aynı şekilde yazıyorsun. Tek fark şu, normalde Word’e
                            yazarken başlığı ayarlıyordun, neyin nerde duracağıyla ilgileniyordun falan, onların
                            hiçbirisi yok; sadece içerik var.
     </p>
     <p class="graf graf--p graf-after--p" id="f661" name="f661">
      2- CVSD(CV Schema Document) Dosyası
     </p>
     <p class="graf graf--p graf-after--p" id="1f34" name="1f34">
      CV’yi yazarken aslında yazdığımız
                            her bir bilginin bir anlamı var, arkada bağlı olduğu bir kavram, konsept var, mesela örnek
                            vereyim.
     </p>
     <figure class="graf graf--figure graf-after--p" id="44f7" name="44f7">
      <img class="graf-image" data-height="200" data-image-id="1*n9tVn28Od93ilfcg9xJyTg.png" data-width="1900" src="https://cdn-images-1.medium.com/max/800/1*n9tVn28Od93ilfcg9xJyTg.png"/>
     </figure>
     <p class="graf graf--p graf-after--figure" id="a7f2" name="a7f2">
      Yukarda benim CV’mden okulda
                            öğretim asistanlığı yaptığım bir kısmı görüyorsunuz, bu aslında 4 e ayrılmış durumda.
     </p>
     <p class="graf graf--p graf-after--p" id="d1fe" name="d1fe">
      1- Organizasyon Adı: University of
                            Maryland — Computer Science Department
     </p>
     <p class="graf graf--p graf-after--p" id="2465" name="2465">
      2- İş Tanımı: Teaching Assistant for
                            CMSC351 — Algorithms Class
     </p>
     <p class="graf graf--p graf-after--p" id="9857" name="9857">
      3- Lokasyon: Maryland, USA
     </p>
     <p class="graf graf--p graf-after--p" id="5a93" name="5a93">
      4- Tarih: August 2021 — Present
     </p>
     <p class="graf graf--p graf-after--p" id="d6e8" name="d6e8">
      CVSD dosyası bu şekilde şemalar
                            tanımlıyor. Mesela bu eleman tipi aşağıdaki şekilde tanımlanmış durumda.
     </p>
     <pre class="graf graf--pre graf-after--p" id="6704" name="6704">["Organization"]<br/>name = "Short Text"<br/>location = "Short Text"<br/>text = "Long Text"<br/>role = "Short Text"<br/>start_date = ["Short Text", "Date"]<br/>end_date = ["Short Text", "Date"]</pre>
     <p class="graf graf--p graf-after--pre" id="e969" name="e969">
      Bu şemalar birazdan
                            tanımlayacağımız üçüncü dosya tipinde kullanılacak, şu an için önemli değiller. Genel olarak
                            içeriklerimizin tipini, hatta adı üstünde şemasını tasarlıyorlar.
     </p>
     <p class="graf graf--p graf-after--p" id="247a" name="247a">
      Bu şemalar CVDL sisteminin açık
                            kaynak tarafını besleyecekler. İnsanlar Şema/Dizayn çiftleri oluşturup paylaşabilecekler.
     </p>
     <p class="graf graf--p graf-after--p" id="a405" name="a405">
      3- CVDD(CV Design Document) Dosyası
     </p>
     <p class="graf graf--p graf-after--p" id="1143" name="1143">
      CVCD ve CVSD dökümanları CV’nin
                            içeriğine dair bazı betimlemeler yapmışken, CV’nin görünümüne dair herhangi bir tanım
                            yapmamışlardı. CVDD bu tanımları içeriyor.
     </p>
     <p class="graf graf--p graf-after--p" id="722b" name="722b">
      Hangi içerik nereye yerleştirilmeli,
                            boşluklar, fontlar, renkler… CV üzerinde yapılması gereken ne kadar tasarım kararı varsa
                            bunların hepsi CVDD dökümanında sağlanacak.
     </p>
     <p class="graf graf--p graf-after--p" id="1cfa" name="1cfa">
      Bu dosyaların içerikleri kimleri
                            ilgilendiriyor, tema/şema yazmak isteyenleri, kendi CV’sinin en küçük detayına kadar kontrol
                            edebilmek isteyenleri, tabii ki genel popülasyon bunu yapmak istemeyecek. Bu noktada bizler
                            yazılan tema/şemaları paylaştığımız, arkadaki koda dokunmadan ücretsiz bir şekilde şu anki
                            CV yaratıcılarının ara yüzüne sahip bir web sitesi oluşturacağız. Bu sitedeki tüm şemalar,
                            temalar açık kaynaklı olacak, oluşturulan CV’lerin arka planındaki dökümanlar da
                            kullanıcıyla paylaşılacak. Bu sayede kimse bir siteye, bir kuruma bağlı olmayacak, projeyi
                            ben yarın bıraksam ertesi gün başkası toparlayabilecek.
     </p>
     <h3 class="graf graf--h3 graf-after--p" id="dad3" name="dad3">
      (Eğer yazılımcı değilseniz buradan
                            devam edebilirsiniz)
     </h3>
     <p class="graf graf--p graf-after--h3" id="327c" name="327c">
      Projenin ne olduğunu anlattığıma
                            göre, neler yaşandığına değinebilirim.
     </p>
     <h3 class="graf graf--h3 graf-after--p" id="b178" name="b178">
      Peki bu zamana kadar projede
                            neler oldu?
     </h3>
     <p class="graf graf--p graf-after--h3" id="243b" name="243b">
      1- Fikir aklıma geldi(taaa ne zaman
                            önce), çevremdekilere anlattım, fikrin kendisi de aşırı ham olduğundan güzel bir tepki
                            alamadım.
     </p>
     <p class="graf graf--p graf-after--p" id="79f2" name="79f2">
      2- Oturup gerçekten kodlamaya
                            başlamaya çalıştım. Kendimi limitlememek için öncelikle tamamen sıfırdan bir dilmiş gibi
                            davrandım. Gerçekten yazmaya başlayınca bu kadar özgürlüğe ihtiyaç duymadığımı gördüm,
                            betimleme dili olarak TOML kullanmaya karar verdim.
     </p>
     <p class="graf graf--p graf-after--p" id="c323" name="c323">
      3- Bu noktada daha TOML kararını
                            vermeden önce aşırı heyecanlı ve sabırsız bir insan olduğumdan projeyi Twitter ve Reddit’te
                            paylaştım. Twitter’dan 0'a yakın dönüş aldım, Reddit’ten çok güzel dönüşler aldım.
                            Öncelikle hiç tanımadığım insanlardan projenin gerçekten yararlı olabileceğini duyma fırsatı
                            duymuş oldum, bu motivasyonumu inanılmaz arttırdı. Buna ek olarak ilk kez Github’da
                            3'ten fazla yıldız aldım, o da çalışmam gerektiği inancımı büyüttü. Ayrıca schema.org ve
                            jsonresume.org gibi fikrimi geliştirebileceğim benzer inisiyatiflerden haberdar olma şansım
                            oldu. Eğer benzer bir durumdaysanız, heyecanlı olduğunuz bir fikriniz varsa belli bir
                            olgunluğa eriştikten sonra Reddit’te paylaşmanın çok faydalı olacağını düşünüyorum. Twitter
                            tarafındaysa doğru (projeyle ilgilenecek) bir Twitter çevresine sahip olmamamdan kaynaklı
                            olarak böyle oldu muhtemelen, gelecekte nasıl tepkiler alırım bilemiyorum tabii.
     </p>
     <p class="graf graf--p graf-after--p" id="4f44" name="4f44">
      4- Projede benle birlikte çalışmaya
                            gönüllü 2 kişi çıktı şu ana kadar. Onlarla nasıl bir görev paylaşımı yapmalıyım, yazılan
                            kodlar nasıl test edilmeli, genel sistem nasıl dizayn edilmeli gibi gibi pek çok
                            kararsızlıkla karşı karşıyayım. Hata yapacağım muhtemel değil, kesin. Sabırsızlıkla da
                            bekliyorum bu süreçte neler yapacağımı, büyük ihtimalle vakit kazanmak yerine üstüne vakit
                            kaybedeceğim bunu yapayım derken, ama öğrenmek için kesinlikle değeceğini düşünüyorum.
     </p>
     <p class="graf graf--p graf-after--p" id="a768" name="a768">
      5- İlk aşamada daha basit bir
                            sistemle küçük bir prototip çıkarmayı umuyorum. Sonrasında geri bildirim ala ala büyür,
                            ilerleriz gibi geliyor. Bu süreçleri de mümkün olduğunca sık ve şeffaf bir şekilde bu
                            günlüklerde paylaşıyor olacağım.
     </p>
     <p class="graf graf--p graf-after--p graf--trailing" id="b2c6" name="b2c6">
      Benim için de yeni
                            bir konsept olduğundan her türlü yoruma minnettar olurum açıkçası. Eleştiridir, ‘bak böyle
                            yapmışsın ama çok da olmamış gibi’ dir, her türlü yoruma açığım. Şimdiden çok teşekkür
                            ederim, sağlıcakla!
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
   <a href="https://medium.com/p/c77ace318b71">
    <time class="dt-published" datetime="2022-01-11T00:11:24.312Z">
     January 11, 2022
    </time>
   </a>
   .
  </p>
  <p>
   <a class="p-canonical" href="https://medium.com/@alpkeles99/proje-g%C3%BCnl%C3%BCkleri-cvdl-cv-description-language-1-c77ace318b71">
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
