+++
title = "Yazılım Projeleri: Kapsamlı Rehber"
date = "2023-11-15"
[taxonomies]
tags = ['software engineering']
language = ["tr"]
+++

<article class="h-entry">
 <section class="e-content" data-field="body">
  <section class="section section--body section--first section--last" name="fcc3">
   <div class="section-content">
    <div class="section-inner sectionLayout--insetColumn">
     <h3 class="graf graf--h3 graf--leading graf--title" id="657a" name="657a">
      Yazılım Projeleri: Kapsamlı Rehber
     </h3>
     <p class="graf graf--p graf-after--h3" id="8402" name="8402">
      Yazıya başlamadan önce, bu yazının kimlere yönelik olduğunu belirteyim.
     </p>
     <p class="graf graf--p graf-after--p" id="7811" name="7811">
      <strong class="markup--strong markup--p-strong">
       1-
      </strong>
      Yazılımda görece yeniysen, kendini halk arasında “junior” olarak tabir edilen grupta görüyorsan,
     </p>
     <p class="graf graf--p graf-after--p" id="f1a1" name="f1a1">
      <strong class="markup--strong markup--p-strong">
       2-
      </strong>
      Kendini geliştirmek için proje yapmak istiyor, ancak ne yapacağını bilemiyorsan,
     </p>
     <p class="graf graf--p graf-after--p" id="1e11" name="1e11">
      <strong class="markup--strong markup--p-strong">
       3-
      </strong>
      Hackernews klonu gibi projelerden ziyade kendini teknik olarak geliştirebileceğin projelerle ilgilenmek istiyorsan,
     </p>
     <p class="graf graf--p graf-after--p" id="fe53" name="fe53">
      <strong class="markup--strong markup--p-strong">
       4-
      </strong>
      Yazılıma “eğer uygulamamda sağlamak istediğim bir özelliğin kütüphanesi yoksa oturur kendim yazarım” bakış açısıyla bakıyorsan,
     </p>
     <p class="graf graf--p graf-after--p" id="e96f" name="e96f">
      O zaman bu yazı senin için yararlı olabilir. Yakın bir arkadaşım olan
      <a class="markup--user markup--p-user" data-action="show-user-card" data-action-type="hover" data-action-value="bc40f811ddfc" data-anchor-type="2" data-href="https://medium.com/u/bc40f811ddfc" data-user-id="bc40f811ddfc" href="https://medium.com/u/bc40f811ddfc" target="_blank">
       Ozan Sazak
      </a>
      ’ın aynı konuda kendi görüşlerini yazdığı bir makaleyi de aşağıya bırakıyorum, ilgini çekiyorsa onu da okuyabilirsin.
     </p>
     <div class="graf graf--mixtapeEmbed graf-after--p" id="5dbc" name="5dbc">
      <a class="markup--anchor markup--mixtapeEmbed-anchor" data-href="https://sazak.io/blog/fantastic-side-projects-and-where-to-find-them-2023-09-03/" href="https://sazak.io/blog/fantastic-side-projects-and-where-to-find-them-2023-09-03/" title="https://sazak.io/blog/fantastic-side-projects-and-where-to-find-them-2023-09-03/">
       <strong class="markup--strong markup--mixtapeEmbed-strong">
        Fantastic Side Projects and Where to Find Them
       </strong>
       <br/>
       <em class="markup--em markup--mixtapeEmbed-em">
        Here are the advices you need to check if you're searching for a cool side project idea.
       </em>
       sazak.io
      </a>
      <a class="js-mixtapeImage mixtapeImage u-ignoreBlock" data-media-id="42cf3d37831fbf003a512909dc13cbfe" data-thumbnail-img-id="0*88O0jNAEhfzYISAj" href="https://sazak.io/blog/fantastic-side-projects-and-where-to-find-them-2023-09-03/" style="background-image: url(https://cdn-images-1.medium.com/fit/c/160/160/0*88O0jNAEhfzYISAj);">
      </a>
     </div>
     <h3 class="graf graf--h3 graf-after--mixtapeEmbed" id="38b8" name="38b8">
      Şimdi sizin aklınızda 2 soru var. Proje nedir, nasıl yapılır?
     </h3>
     <p class="graf graf--p graf-after--h3" id="cc48" name="cc48">
      Bir yazılım projesi bir alışveriş listesi uygulaması yazmaktan kendi programlama dilini geliştirmeye kadar çok geniş bir yelpazede yer alabilir. Aşağıda kendim bir projeyi değerlendirirken kullandığım 2 önemli ekseni içeren küçük bir tablo çizdim. Burada
      <strong class="markup--strong markup--p-strong">
       Teknik Derinlik
      </strong>
      projenin daha teorik, daha tasarımsal taraftaki zorluğunu anlatırken,
      <strong class="markup--strong markup--p-strong">
       Teknik Genişlik
      </strong>
      ise projenin ne kadar geniş bir teknoloji yelpazesi bilmeyi gerektirdiğinden bahsediyor.
     </p>
     <figure class="graf graf--figure graf-after--p" id="8f26" name="8f26">
      <img class="graf-image" data-height="1805" data-image-id="1*TUfyBa2OxrOiY6ZE8Eg7QA.png" data-is-featured="true" data-width="2916" src="https://cdn-images-1.medium.com/max/800/1*TUfyBa2OxrOiY6ZE8Eg7QA.png"/>
     </figure>
     <p class="graf graf--p graf-after--figure" id="2260" name="2260">
      Tabii bu tablo fazlasıyla basitleştirilmiş durumda şu an(bir eksende hareket ederken diğerinde tamamen sabit kalmıyoruz aslında) ancak ana fikir, bir projenin teknik derinliği olmadan teknik genişliği olabileceği, aynı zamanda teknik genişliği olmadan teknik derinliği olabileceği. En temelde baktığınızda fullstack bir şekilde son teknolojileri kullanarak geliştirdiğiniz todo uygulamasının tüm bilgilerini tarayıcıda saklayan bir ToDo uygulamasından teknik derinlik anlamında bir farkı yok, yalnızca daha fazla farklı teknolojileri birbirine entegre etmenizi gerektiriyor. Diğer yandan neredeyse hiçbir ek teknolojiye ihtiyaç duymadan yeni bir programlama dili, terminal oyunu, veri sıkıştırma uygulaması, metinden konu analizi, resim editörü oluşturabilirsiniz.
     </p>
     <p class="graf graf--p graf-after--p" id="c8dc" name="c8dc">
      Bu yazının kalanında neden teknik derinliği yüksek ancak teknik genişliği dar projeleri daha yararlı gördüğümden bahsedip, bu tarz projelerde nasıl adımlar atılacağını anlatıp, 2 adet proje örneği vereceğim.
     </p>
     <h3 class="graf graf--h3 graf-after--p" id="2b3c" name="2b3c">
      Proje Seçerken Neye Dikkat Etmeliyim?
     </h3>
     <p class="graf graf--p graf-after--h3" id="4cc2" name="4cc2">
      Yazılımın temelinde modelleme var. Bir uygulama yazdığınızda, o uygulamada sakladığınız verileri, o uygulamanın kullanıcı arayüzünü, kullanıcı aksiyonlarını modellemeniz gerekiyor. Bu noktada kendi modellerimizi oluştururken, genelde başkalarının oluşturduğu modellerin üstüne kurguluyoruz. Veri tabanı olan interaktif bir web sitesi tasarlıyor olalım mesela, öncelikle “client/server” modelinin üzerine kurulmuş bir veri şeması oluşturuyoruz. Hangi veri nerde/nasıl saklanıyor, client ve server arasında ne gibi veriler aktarılıyor? Sonrasında genelde kullandığımız kütüphanenin ve framework’ün bize verdiği birtakım bileşenleri kullanarak kullanıcı aksiyonlarını modelliyoruz. Kullanıcının karşısındaki ekrana metin kutuları, butonlar, yazılar koyarak kullanıcının bizim uygulamamız ile etkileşime geçmesini sağlıyoruz, etkileşimin sonucuna göre uygulamamızın durumunu güncelliyoruz.
     </p>
     <p class="graf graf--p graf-after--p" id="5afc" name="5afc">
      Peki bazı uygulamaları diğerinden bizim için daha zor kılan ne? Benim buradaki ilk düşüncem, aslında her türlü uygulamanın çok zor olduğu. Biz bugün bir web sitesini modellerken alttaki network’ün modeliyle ilgilenmiyoruz, o model bizim için tarayıcı tarafından soyutlanmış. Basit bir
      <code class="markup--code markup--p-code">
       fetch
      </code>
      ile dünyanın herhangi bir yerinden istediğimiz veriyi çekebiliyoruz, aslında arkada ne kadar kompleks bir mekanizmanın döndüğünün hiçbir şekilde farkında olmadan.
     </p>
     <p class="graf graf--p graf-after--p" id="b6c8" name="b6c8">
      Bu noktada bir uygulamayı zor yapan ilk etmen, o uygulama için ihtiyaç duyduğumuz bileşenlere sahip olmamak. Çoğu kişinin hiç düşünmeden kullandığı bileşenlerin kendileri çoğu zaman düşünmeyeceğimiz kadar kompleks aslında. Eğer merak ediyorsanız, bir gün
      <code class="markup--code markup--p-code">
       &lt;input type="text"&gt;
      </code>
      yazdığınızda karşınıza çıkan metin kutusunu kendi kendinize sıfırdan yazmaya çalışın. Ne kadar zor olduğunu göreceksiniz.
     </p>
     <p class="graf graf--p graf-after--p" id="20c2" name="20c2">
      Neyse ki, modern teknoloji, açık kaynak, yüz binlerce şirket ve milyarlarca dolar yatırım sonrasında hayal edebileceğimiz her alanda ve konuda istemeyeceğimiz kadar hazır bileşen mevcut. Elimizin altında, yalnızca birkaç sorguyla ulaşılabilir durumda bu bileşenlerin hepsi. Hiçbir şekilde sıfırdan yeni bir bileşen oluşturmadan, yalnızca varolan bileşenleri birbiriyle doğru şekilde bağlayarak yazılım ürünleri üretmek mümkün, hatta ve hatta endüstrinin ciddi bir çoğunluğu bu şekilde ilerliyor. Dolayısıyla siz de kendi hobi projenizde aynı şekilde ihtiyaç duyduğunuz bileşenleri araştırıp bularak ilerleyebilirsiniz, çok güzel projeler de yapabilirsiniz. Bu tarz projeler benim
      <strong class="markup--strong markup--p-strong">
       sığ ve geniş
      </strong>
      olarak nitelendirdiğim proje kümesine giriyor. Teorik bir bilgiye, matematiğe, algoritmalara, kendi veri yapınızı tasarlamaya ihtiyaç yok, bol bol araştırma yapmaya, framework ve kütüphane kullanmayı öğrenmeye, farklı araçları doğru şekillerde birleştirmeye ihtiyaç var.
     </p>
     <p class="graf graf--p graf-after--p" id="98f0" name="98f0">
      <strong class="markup--strong markup--p-strong">
       Benim şahsi gözlemim, bu tarz projeler yapmanın (1) insanın motivasyonunu kırdığı, (2) uzun vadede kişinin gelişimini yavaşlattığı, (3) yeterince eğlenceli olmadığı yönünde.
      </strong>
     </p>
     <p class="graf graf--p graf-after--p" id="e8fe" name="e8fe">
      Yazının başında da bahsettiğim gibi, eğer ki
      <em class="markup--em markup--p-em">
       kütüphanesi yoksa ben oturur yazarım
      </em>
      diyenlerdenseniz, yazının kalanında size
      <strong class="markup--strong markup--p-strong">
       derin ve dar
      </strong>
      projeler tasarlamayı göstereceğim.
     </p>
     <h3 class="graf graf--h3 graf-after--p" id="db6f" name="db6f">
      Öğrenmeden Öğrenmek
     </h3>
     <p class="graf graf--p graf-after--h3" id="ba29" name="ba29">
      Bu ana kadar teknik derinliğin ne demek olduğunu bilerek biraz gizledim. Teorik bilgiden kastım ne mesela? Bir proje nasıl diğerinden teknik olarak daha derin oluyor? Gelin bir vaka çalışması üzerinden gidelim.
     </p>
     <p class="graf graf--p graf-after--p" id="9a8e" name="9a8e">
      <a class="markup--anchor markup--p-anchor" data-href="https://p5js.org/get-started/" href="https://p5js.org/get-started/" rel="noopener" target="_blank">
       p5.js
      </a>
      yüzbinlerce kullanıcısı olan bir Javascript çizim kütüphanesi.
     </p>
     <div class="graf graf--mixtapeEmbed graf-after--p" id="f233" name="f233">
      <a class="markup--anchor markup--mixtapeEmbed-anchor" data-href="https://editor.p5js.org/" href="https://editor.p5js.org/" title="https://editor.p5js.org/">
       <strong class="markup--strong markup--mixtapeEmbed-strong">
        p5.js Web Editor
       </strong>
       <br/>
       <em class="markup--em markup--mixtapeEmbed-em">
        A web editor for p5.js, a JavaScript library with the goal of making coding accessible to artists, designers…
       </em>
       editor.p5js.org
      </a>
      <a class="js-mixtapeImage mixtapeImage mixtapeImage--empty u-ignoreBlock" data-media-id="b0db2b9d06fda7098fa97f1c76367601" href="https://editor.p5js.org/">
      </a>
     </div>
     <p class="graf graf--p graf-after--mixtapeEmbed" id="7f67" name="7f67">
      Diyelim ki ben bugün size hadi gelin sıfırdan bir tane p5 yazalım desem, ne yapardınız?
     </p>
     <p class="graf graf--p graf-after--p" id="0ba0" name="0ba0">
      Öncelikle, birisi size böyle bir şey sorarsa kesinlikle evet demeyin. Önce projenin
      <a class="markup--anchor markup--p-anchor" data-href="https://github.com/processing/p5.js" href="https://github.com/processing/p5.js" rel="noopener" target="_blank">
       github’ını
      </a>
      bir inceleyin, yüzlerce katılımcısı olan bir projeyi sıfırdan yazmak yerine ona katkıda bulunun. Diğer yandan öğrenmek amacıyla bir p5 klonu yazmak aslında çok da zor değil.
     </p>
     <h4 class="graf graf--h4 graf-after--p" id="31c7" name="31c7">
      Adım 1: Basitleştirme
     </h4>
     <p class="graf graf--p graf-after--h4" id="fa8d" name="fa8d">
      Bir projeye başlamanın ilk adımı projeyi basit hale getirmek. p5.js içinde ses, video, 2d/3d grafikler, kullanıcı aksiyonları, metin desteği falan derken inanılmaz büyük bir proje. Bu projeyi basitleştirmenin yolu da bunun küçük bir alt kümesini seçmek. Gelin sadece 2d grafikleri çizebileceğiniz bir kütüphane ile başlayalım. Hatta daha da basit başlayalım,
      <strong class="markup--strong markup--p-strong">
       ben bir resim üzerine 2 tane kare çizdirebilir miyim?
      </strong>
     </p>
     <p class="graf graf--p graf-after--p" id="63e0" name="63e0">
      Daha önce bu konuda hiç düşünmediyseniz biraz düşünmeye çalışın. Nedir bir resim? Nasıl çizilir? Bir dikdörtgen çizmek ne demektir?
     </p>
     <p class="graf graf--p graf-after--p" id="8410" name="8410">
      İlk başta aklınıza gelen cevap yüksek ihtimalle bir resmin pikseller bütünü olduğu olmalı. Resim çizmek demek o piksellerin her birine bir renk atamak demek. Bir dikdörtgen ise belli bir matematiksel denkleme uyan piksellerin aynı renkte boyanması. Aşağıda da basit bir typescript tanımı var resim veri yapısı için.
     </p>
     <pre class="graf graf--pre graf-after--p graf--preV2" data-code-block-lang="typescript" data-code-block-mode="1" id="092a" name="092a" spellcheck="false"><span class="pre--content"><span class="hljs-keyword">type</span> <span class="hljs-title class_">Color</span> = { <span class="hljs-attr">r</span>: <span class="hljs-built_in">number</span>, <span class="hljs-attr">g</span>: <span class="hljs-built_in">number</span>, <span class="hljs-attr">b</span>: <span class="hljs-built_in">number</span> };<br><span class="hljs-keyword">type</span> <span class="hljs-title class_">Point</span> = { <span class="hljs-attr">x</span>: <span class="hljs-built_in">number</span>, <span class="hljs-attr">y</span>: <span class="hljs-built_in">number</span> };<br><span class="hljs-keyword">type</span> <span class="hljs-title class_">Image</span> = {<br/>  <span class="hljs-attr">width</span>: <span class="hljs-built_in">number</span>,<br/>  <span class="hljs-attr">height</span>: <span class="hljs-built_in">number</span>,<br/>  <span class="hljs-attr">pixels</span>: <span class="hljs-title class_">Map</span>&lt;<span class="hljs-title class_">Point</span>, <span class="hljs-title class_">Color</span>&gt;<br/>}</br></br></span></pre>
     <p class="graf graf--p graf-after--pre" id="4d51" name="4d51">
      Mesela benim buradaki
      <code class="markup--code markup--p-code">
       Image
      </code>
      tanımım seyrek(sparse) bir tanım. Bir resmi aynı zamanda yoğun(dense) olarak da tanımlayabilirdim. Farklı tanımların kolaylaştırdığı farklı operasyonlar var.
     </p>
     <pre class="graf graf--pre graf-after--p graf--preV2" data-code-block-lang="typescript" data-code-block-mode="1" id="5725" name="5725" spellcheck="false"><span class="pre--content"><span class="hljs-keyword">type</span> <span class="hljs-title class_">DenseImage</span> = {<br/>  <span class="hljs-attr">width</span>: <span class="hljs-built_in">number</span>,<br/>  <span class="hljs-attr">height</span>: <span class="hljs-built_in">number</span>,<br/>  <span class="hljs-attr">pixels</span>: <span class="hljs-title class_">Color</span>[][]<br/>}</span></pre>
     <p class="graf graf--p graf-after--pre" id="fd9c" name="fd9c">
      E peki dikdörtgen çizmek ne demek?
     </p>
     <pre class="graf graf--pre graf-after--p graf--preV2" data-code-block-lang="typescript" data-code-block-mode="2" id="9b87" name="9b87" spellcheck="false"><span class="pre--content"><span class="hljs-keyword">const</span> <span class="hljs-title function_">rect</span> = (<span class="hljs-params">img: Image, p1: Point, p2: Point, c: Color</span>) =&gt; {<br/><br/>  <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> i = p1.<span class="hljs-property">x</span> ; i &lt; p2.<span class="hljs-property">x</span> ; i++) {<br/>    <span class="hljs-comment">// Üst kenar</span><br/>    img.<span class="hljs-property">pixels</span>.<span class="hljs-title function_">set</span>({<span class="hljs-attr">x</span>: i, <span class="hljs-attr">y</span>: p1.<span class="hljs-property">y</span>}, c);<br/>    <span class="hljs-comment">// Alt kenar</span><br/>    img.<span class="hljs-property">pixels</span>.<span class="hljs-title function_">set</span>({<span class="hljs-attr">x</span>: i, <span class="hljs-attr">y</span>: p2.<span class="hljs-property">y</span>}, c);<br/>  }<br/><br/>  <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> i = p1.<span class="hljs-property">y</span> ; i &lt; p2.<span class="hljs-property">y</span> ; i++) {<br/>    <span class="hljs-comment">// Sol kenar</span><br/>    img.<span class="hljs-property">pixels</span>.<span class="hljs-title function_">set</span>({<span class="hljs-attr">x</span>: p1.<span class="hljs-property">x</span>, <span class="hljs-attr">y</span>: i}, c);<br/>    <span class="hljs-comment">// Sağ kenar</span><br/>    img.<span class="hljs-property">pixels</span>.<span class="hljs-title function_">set</span>({<span class="hljs-attr">x</span>: p2.<span class="hljs-property">x</span>, <span class="hljs-attr">y</span>: i}, c);<br/>  }<br/>}</span></pre>
     <p class="graf graf--p graf-after--pre" id="4070" name="4070">
      Alın size bir adet dikdörtgen çizme fonksiyonu. Tabii fonksiyonun bazı eksikleri var(p1 sol üst, p2 sağ alt nokta olmak zorunda, aynı zamanda köşelerde boş pikseller var, bir de 1 kenarlar 1 piksel sadece).
     </p>
     <p class="graf graf--p graf-after--p" id="da74" name="da74">
      Peki bu resmi üretmek kendi başına yetiyor mu? Bir de çizmek gerekmiyor mu? Bu konuda MDN’in HTML Canvas’ı kullanmak takip edebileceğiniz basit bir rehberi var, aşağıya bırakıyorum.
     </p>
     <div class="graf graf--mixtapeEmbed graf-after--p" id="6d9f" name="6d9f">
      <a class="markup--anchor markup--mixtapeEmbed-anchor" data-href="https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API/Tutorial/Pixel_manipulation_with_canvas" href="https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API/Tutorial/Pixel_manipulation_with_canvas" title="https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API/Tutorial/Pixel_manipulation_with_canvas">
       <strong class="markup--strong markup--mixtapeEmbed-strong">
        Pixel manipulation with canvas - Web APIs | MDN
       </strong>
       <br/>
       <em class="markup--em markup--mixtapeEmbed-em">
        Until now we haven't looked at the actual pixels of our canvas. With the ImageData object you can directly read and…
       </em>
       developer.mozilla.org
      </a>
      <a class="js-mixtapeImage mixtapeImage u-ignoreBlock" data-media-id="845a4310f3500f3e2c26dc0668e8e646" data-thumbnail-img-id="0*58bVhpfq0mVxwlEl" href="https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API/Tutorial/Pixel_manipulation_with_canvas" style="background-image: url(https://cdn-images-1.medium.com/fit/c/160/160/0*58bVhpfq0mVxwlEl);">
      </a>
     </div>
     <p class="graf graf--p graf-after--mixtapeEmbed" id="ad05" name="ad05">
      <strong class="markup--strong markup--p-strong">
       Öğrenmeden öğrenmek, tam olarak az önceki süreci geçirmek demek aslında.
      </strong>
     </p>
     <p class="graf graf--p graf-after--p" id="5ce1" name="5ce1">
      Fark ettiyseniz HTML Canvas haricinde hiçbir ek soyutlamaya ya da teknolojiye ihtiyaç duymadık. Resimin kendisi için kendi veri modelimizi kullandık, bu modelin üzerine kendi dikdörtgen modelimizi kurguladık. Öğrenmeden öğrenmenin temeli, yeni teknolojiler veyahut soyutlamalara sırtını dayamadan mantık ve matematik üzerine kurulu bir şekilde yazılım geliştirmekten geliyor. Mesela şu anda kenarlar 1 piksel, kenar kalınlığı oluşturmak için ne yapmamız gerekirdi? Tabii ki olay sadece basitleştirerek bitmiyor. Pikseller zaten bir ızgara şeklinde olduğu için dik çizgileri çizmek çok kolay. Peki ya üçgen çizmek istersek? O zaman yamuk bir çizgi çizmemiz gerekecek. Eğer bu yamuk çizgiyi az önce dik çizgiyi çizdiğimiz gibi çizmeye çalışırsak karşımıza bir çizgiden ziyade aşağıdaki gibi kırıklı bir çizgi gelecek.
     </p>
     <figure class="graf graf--figure graf-after--p" id="955b" name="955b">
      <img class="graf-image" data-height="480" data-image-id="1*K8rodt0tly07NfKYWBf1xQ.jpeg" data-width="640" src="https://cdn-images-1.medium.com/max/800/1*K8rodt0tly07NfKYWBf1xQ.jpeg"/>
     </figure>
     <p class="graf graf--p graf-after--figure" id="af14" name="af14">
      Bu noktaya kadarki mantığı takip edersek bu tarz problemleri de kendimiz çözmemiz gerektiğini söyleyeceğimi düşünebilirsiniz, bunu söylemeyeceğim. Bu tarz problemler benim
      <strong class="markup--strong markup--p-strong">
       teknik derinlik
      </strong>
      adını verdiğim kategoride yer alıyor. Bu problemlerin çözümleri teorik, matematiksel çözümler.
     </p>
     <h4 class="graf graf--h4 graf-after--p" id="48ab" name="48ab">
      Adım 2: İşin Tekniğini Öğrenmek
     </h4>
     <p class="graf graf--p graf-after--h4" id="dc1b" name="dc1b">
      Yukarıdaki problemin çözümünü araştırdığımda kısa bir çözümle 2 tane algoritma buldum.
     </p>
     <p class="graf graf--p graf-after--p" id="3033" name="3033">
      1-
      <a class="markup--anchor markup--p-anchor" data-href="https://en.wikipedia.org/wiki/Xiaolin_Wu%27s_line_algorithm" href="https://en.wikipedia.org/wiki/Xiaolin_Wu%27s_line_algorithm" rel="noopener" target="_blank">
       Xiaolin Wu’s line algorithm
      </a>
     </p>
     <p class="graf graf--p graf-after--p" id="cb87" name="cb87">
      2-
      <a class="markup--anchor markup--p-anchor" data-href="https://en.wikipedia.org/wiki/Bresenham%27s_line_algorithm" href="https://en.wikipedia.org/wiki/Bresenham%27s_line_algorithm" rel="noopener" target="_blank">
       Bresenham’s line algorithm
      </a>
     </p>
     <p class="graf graf--p graf-after--p" id="71e8" name="71e8">
      Karşılaştığımız problemlere karşı genelde 3 tip yaklaşımımız var.
     </p>
     <p class="graf graf--p graf-after--p" id="a87f" name="a87f">
      <strong class="markup--strong markup--p-strong">
       1-
      </strong>
      Ben bu problemi çözen bir kütüphane bulayım.
     </p>
     <p class="graf graf--p graf-after--p" id="f3ff" name="f3ff">
      <strong class="markup--strong markup--p-strong">
       2-
      </strong>
      Ben bu problemin nasıl çözüleceğini öğrenip kendim çözeyim.
     </p>
     <p class="graf graf--p graf-after--p" id="02c7" name="02c7">
      <strong class="markup--strong markup--p-strong">
       3-
      </strong>
      Ben bu problemi çözmeyeyim, ya da daha basit/farklı bir versiyonunu çözeyim.
     </p>
     <p class="graf graf--p graf-after--p" id="b266" name="b266">
      <strong class="markup--strong markup--p-strong">
       Adım 2
      </strong>
      , burada problemin çözümünü öğrenip kendin çözme yolunu(2. seçenek) öneriyor.
     </p>
     <p class="graf graf--p graf-after--p" id="2153" name="2153">
      <strong class="markup--strong markup--p-strong">
       Bu noktada bir dipnot düşmek istiyorum.
      </strong>
      Bu problemleri çözmek sizin iş hayatınızda düzenli olarak yapacağınız bir iş olmayabilir. Hatta çoğu zaman eğer bir problem zaten çözülmüşse gider kütüphanesini kullanırız, neden ben kütüphane kullanmayıp var olan kütüphaneleri tekrar yazayım diye soruyor olabilirsiniz.
      <strong class="markup--strong markup--p-strong">
       Haklısınız.
      </strong>
      İş hayatında zaten böyle yapmalısınız, ancak yeri geldiğinde
      <strong class="markup--strong markup--p-strong">
       kendi problemlerinizi de çözebiliyor
      </strong>
      olmalısınız. Kendi problemlerinizi çözemiyor olmak bir problemi çözmek için bir kütüphane olmadığında (1. seçeneği uygulayamadığınızda) problemi çözmemek, belki de daha kötü bir kullanıcı tecrübesini kabul etmek(3. seçeneği uygulamak) anlamına geliyor.
     </p>
     <p class="graf graf--p graf-after--p" id="d9b7" name="d9b7">
      Seçenek 2'yi uygulamaya devam ettikçe işiniz kolaylaşacak. Kendi problemlerinizi çözmeye alıştığınızda karşınıza gelen diğer problemlerin çözümlerine nasıl ulaşabildiğini daha iyi öğreneceksiniz, belki de normal şartlar altında kütüphane bulamadığınız için iptal edeceğiniz bir özelliği oturup vakit harcayacak ekleyeceksiniz uygulamanıza.
     </p>
     <p class="graf graf--p graf-after--p" id="d8ee" name="d8ee">
      İşin tekniğini öğrenmek her zaman makale okumak demek değil. Soyutlamaların altını görmeye çalışmak demek. Başkalarının veri modellerini anlamaya çalışmak demek. Bir resmin 2 tane farklı gösteriminden bahsetmiştik(Sparse ve Dense), bunlar yalnızca 2 seçenek mi elimizdeki? Hangi seçeneği kullanmak hangi durumlarda daha mantıklı? JPEG, SVG, PNG, BMP gibi farklı formatlar nasıl avantajlar sağlıyor? Resimin üzerine animasyon yaratmak istesek nasıl bir veri modeli geliştirmemiz gerekir?
     </p>
     <p class="graf graf--p graf-after--p" id="44c4" name="44c4">
      Soyutlamaların arkasındaki mekanikleri anladıkça, bilgisayarlar sizi daha az şaşırtmaya başlayacak. Mesela ben şu sıralar bir dosya editörü geliştiriyorum, onun yüzünden dosya editörlerinin veri modellerini anlamayı kafaya taktım biraz. Kullandığım editörlerin neyi nasıl yaptığına dikkat ederek arkadaki modeli tahmin edebiliyorum. Metnin pozisyonunu hesaplarken nasıl hesaplıyorlar, Microsoft Word’de sinir olduğum özelliklerin sebebi ne onları görebiliyorum. Yine benzer bir şekilde Whatsapp’ta bir metni aramaya çalışırken arkadaki veri yapısını hangi aramaları kolaylaştırdığı, hangi aramaları zorlaştırdığı üzerinden hayal edebiliyorum. Ne işe yarıyor bunlar derseniz, kendi kendime gülüp geçmem haricinde çok bir işime yaramıyor. Ancak bana öyle geliyor ki beni günlük hayatımda daha iyi bir mühendis ve araştırmacı haline getiriyor.
     </p>
     <h4 class="graf graf--h4 graf-after--p" id="3549" name="3549">
      Adım 3: Yeri Geldiğinde Genişlemek
     </h4>
     <p class="graf graf--p graf-after--h4" id="83a5" name="83a5">
      Tabii ki her maksimalist argüman gibi, öğrenmeden öğrenmenin de uç noktası pratik değil. Hiçbir teknoloji kullanmadan tüm bir uygulamayı tek başınıza
      <strong class="markup--strong markup--p-strong">
       yazamazsınız.
      </strong>
      Mümkün değil. Dolayısıyla neyi öğrenmek istediğinize, hangi konseptlerin ilginizi çektiğine, uygulamanızın hangi kısımlarının sizin için daha temel olduğuna göre bir öncelik geliştirip, kalan kısımda tabii ki var olan ekosisteme sırtınızı dayayabilmelisiniz. Ancak projenin temeli, sizin kendinizi geliştirmek istediğiniz
      <strong class="markup--strong markup--p-strong">
       domain
      </strong>
      olmalı.
     </p>
     <h3 class="graf graf--h3 graf-after--p" id="7629" name="7629">
      Nası Projeler Seçmeliyim?
     </h3>
     <p class="graf graf--p graf-after--h3" id="6611" name="6611">
      E peki nasıl bulabilirim bu tarz projeler diye düşünüyorsanız, aslında günlük hayatta kullandığınız servislerin çoğunun basit bir versiyonunu yazmayı deneyebilirsiniz.
     </p>
     <ul class="postList">
      <li class="graf graf--li graf-after--p" id="2c34" name="2c34">
       Toy Version Control System: Kendi git’inizi yazmak istemez miydiniz? İstediğiniz tüm özellikleri koyma şansınız var hem de.
      </li>
      <li class="graf graf--li graf-after--li" id="dccb" name="dccb">
       Custom Textbox: Hepimizin her gün kullandığı html textbox aslında altında çok eğlenceli mekanikler içeriyor. Yazdığınız metnin piksellerini hesaplayıp ona göre alt satıra inmeli misiniz, kullanıcı ok tuşlarına bastığında işaretçiyi nereye götürmelisiniz?
      </li>
      <li class="graf graf--li graf-after--li" id="8ee7" name="8ee7">
       Toy Image Editor: Bu yazıda başladığımız sistemi bir adım öteye götürüp kendi resim editörünüzü yazmak istemez misiniz?
      </li>
      <li class="graf graf--li graf-after--li" id="0e22" name="0e22">
       Toy Grammarly: Eğer dil bilgisi veya kuralları ilginizi çekiyorsa, yazdığınız metni kendi gramer motorunuz ile kontrol etmeye çalışmak ister misiniz?
      </li>
     </ul>
     <p class="graf graf--p graf-after--li graf--trailing" id="29ec" name="29ec">
      Bu projelerden bahsetmemin sebebi, daha önce üzerine düşündüğüm, ya buna uğraşsam ne eğlenirim dediğim projeler olması. Uç seviyede bir uygulama yazmanıza gerek yok son kullanıcıyı düşünen, ancak günlük hayatta nasıl işlediğini hiç düşünmeye ihtiyaç duymadan kullandığınız uygulamaları yazmaya çalıştığınızda o uygulamalara dair olan bakış açınız da değişecek bence.
      <strong class="markup--strong markup--p-strong">
       Eğer ki sizin aklınıza gelen uygulamalar varsa onları da cevap olarak yazın, tartışalım!
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
   <a href="https://medium.com/p/8f883ed82275">
    <time class="dt-published" datetime="2023-11-15T23:33:07.594Z">
     November 15, 2023
    </time>
   </a>
   .
  </p>
  <p>
   <a class="p-canonical" href="https://medium.com/@alpkeles99/yaz%C4%B1l%C4%B1m-projeleri-kapsaml%C4%B1-rehber-8f883ed82275">
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
