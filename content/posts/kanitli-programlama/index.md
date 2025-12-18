+++
title = "Formal Metotlar ve Kanıtlı Programlama"
date = "2025-12-18"
[taxonomies]
tags = ['software engineering', 'formal methods']
language = ["tr"]
+++

Hatalar, günümüzde programlamanın ve yazılım mühendisliğinin ayrılmaz bir parçası. Yazdığımız programlarda hatalar olacağını, bu hataların
kaçınılmaz olduğunu, bu kaçınılmazlığın değiştirilemez olduğunu kabul ediyoruz, programlama etrafındaki kültürü bu şekilde geliştirdik.
Linux Kernel'ından kullandığımız tarayıcılara, tarayıcılarda ziyaret ettiğimiz web sitelerine, bu sitelerin mobil uygulamalarına kullandığımız
her yazılım ürününde hataların olmasını bekliyoruz. Diğer yanda, bilgisayar bilimlerinin niş bir köşesinde **formal metotlar** adında,
yazdığımız programların doğruluğunu arttırmak ve geliştirmek üzerine kurulu bir alan var. Formal metotlar, programlama dillerinin
ve onları kullanarak yazdığımız programların teorisini ve anlamını inceleyen, yeri geldiğinde programlarımızı analiz ederek onlardaki
hataları keşfedebilen, yeri geldiğinde bizim amaçlarımıza uygun programları sentezleyen, yeri geldiğinde ise yazdığımız programlarda
hiçbir hata olmadığını matematiksel olarak kanıtlayabilen metotlar. Bu yazıda bunların sonuncusundan, yazdığımız programların doğruluğunu
kanıtlayabildiğimiz yöntemlerden, teknolojilerden, programlama dillerinden bahsedeceğim.

**Buna girmeden önce, bu yazının neden bugünün bağlamında önemli olduğuna dair küçük bir dipnot açayım:**

Formal metotlar ve kanıtlı programlama, tarihin çok büyük bir kısmında kullanım olarak zor ve niş bir pozisyonda kaldı.
Bugün bu alanlarla uğraşan insanları incelediğinizde belki %90'ının akademik ortamlarda, akademik projelerde bununla uğraştığını
görebilirsiniz. Bugün, bu gerçekliğin hızla değişebileceği bir ortama giriyoruz, Martin Kleppman'ın geçtiğimiz hafta
["Yapay Zeka Formal Doğrulamayı Anaakım Hale Getirecek"](https://martin.kleppmann.com/2025/12/08/ai-formal-verification.html) yazısıyla,
kanıtlı programlama yapabildiğimiz Lean programlama dilinde yapay zekayla matematik kanıtlama üzerine ürünler geliştiren [Harmonic](https://harmonic.fun/news#blog-post-aristotle-tech-report), [Axiom](https://axiommath.ai/territory/building-the-reasoning-engine-at-axiom), [Nous](https://venturebeat.com/ai/nous-research-just-released-nomos-1-an-open-source-ai-that-ranks-second-on) gibi girişimlerin yaygınlaşmasıyla,
[Claude Code](https://arxiv.org/abs/2510.09907v1), [Kiro](https://kiro.dev/blog/property-based-testing/) gibi yapay zeka destekli kod
editörlerinin hafif formal metotlar (lightweight formal methods) adıyla anılan Property-Based Testing özelliğini eklemesiyle, yapay zekanın
ürettiği kodları [doğrulama probleminin](https://alperenkeles.com/posts/verifiability-is-the-limit/) çözümüne giden yolun formal metotlar
olduğuna dair ciddi belirtiler görüyoruz. Ben şahsen bu gidişatın devam edeceğine, ve kanıtlama programlamanın önemli bir rol oynayacağına
inanıyorum, o yüzden bugün formal metotları ana akıma taşımak her zamankinden daha kolay, ve belki de her zamankinden daha değerli.

## Basit Gözüken Programların Tehlikelerine Bir Örnek

Programlama dillerindeki numerik tipler (`int`, `uint`, `float`, `double`, `number`) programlamaya başladığımız günden
itibaren elimizin altında olan yapılar. Doğal sayılarla yapılacak işlemleri `int`/`uint` gibi tamsayı ve doğal sayıları
temsil eden tiplerle, reel ya da rasyonel sayılarla yapılacak işlemleri ise `float`/`double` (bundan sonra Javascript'teki
versiyonuna sadık kalarak `number` diyeceğim) tipleriyle yapıyoruz. Bu tipler, her ne kadar matematiksel objeleri temsil etmede
kullanılsa da o objelerin tüm özelliklerine sahip değiller. Bunun en klasik örneklerinden birisi `number` tipinin toplamada
alttaki reel sayıdan beklenmeyen sonuçlar üretmesi.

```js
0.1 + 0.2 === 0.3 // false
0.1 + 0.2 // 0.30000000000000004
```

Bu örnekte matematiksel olarak `0.1 + 0.2 = 0.3` olmasını beklerken, modern bilgisayarların kullandığı IEEE-754 Floating Point
standardı beklediğimiz sonuca yakın, ancak farklı bir çıktı veriyor. Bu çok da büyük bir problem değil gibi gözükebilir, daha
ciddi bir sıkıntıyı inceleyelim.

Klasik, okul yıllarında ilk yazdığımız algoritmalardan birini, İkili Aramayı (Binary Search) inceleyelim:

```java
public static int binarySearch(int[] a, int key) {
    int low = 0;
    int high = a.length - 1;

    while (low <= high) {
        int mid = (low + high) / 2;
        int midVal = a[mid];

        if (midVal < key)
             low = mid + 1
         else if (midVal > key)
             high = mid - 1;
         else
             return mid; // key found
     }
     return -(low + 1);  // key not found.
}
```

İsterseniz bu noktada bir durun, bu koddaki hatayı görmeye çalışın.

Hata, 6. satırdaki iki tamsayının ortalamasını hesaplayan kodda (`int mid = (low + high) / 2;`).
Problem, `int`'in tamsayı olmaması, `int` bilgisayarımızın hafızasında herhangi bir noktada yer alan
32 bitlik bir sekansın tamsayı olarak okunması. 32 bitlik bit sekansı bize 2^32 farklı değeri temsil
etme fırsatı veriyor, bunlar da `int` tipi için `[-2^31, 2^31 - 1]` aralığı. Eğer ki `low + high` 2^31'den
daha büyükse, üste taşma (overflow) dediğimiz fenomen ortaya çıkıyor, işlemin sonucunda ortaya çıkan bit sekansı
matematiksel hesaplama ile bilgisayarlı hesaplamanın birbirinden ayrışmasına sebep oluyor. Bu hata basit,
tecrübeli birinin yapmayacağı bir hata gibi görünebilir, ancak [Java standard kütüphanesinde](https://research.google/blog/extra-extra-read-all-about-it-nearly-all-binary-searches-and-mergesorts-are-broken/) bile karşılaşılan
bir hata bu.

Peki, **formal metotlar bu problemi çözebilir miydi?**

Önceklikle cevap, **evet**. Bu problemi çözebilecek birkaç farklı yöntem mevcut. Ancak problemi keşfetmeden önce,
problemi tanımlamamız gerekiyor. Bu örnekteki problem, tamsayı taşması (integer overflow). Neye ihtiyacımız var?
Programda herhangi bir noktada tamsayı taşması ihtimali varsa bunu keşfeden, bize raporlayan bir metodolojiye.
Hadi gelin bunun için programdaki tüm tamsayıları alabilecekleri aralıklarla işaretleyelim.

```java
int low = 0; // (low : [0, 0])
// Burada `a.length: int` aslında bize [-2^31, 2^31 - 1] değerini verirdi,
// ancak uzunluğun hesaplanma yönteminden dolayı hiçbir zaman negatif
// olamayacağını biliyoruz, o yüzden elimizde [0, 2^31 - 1] var.
int high = a.length - 1; // a.length : [0, 2^31 - 1] => high : [-1, 2^31 - 1]
```

Sıradaki işlem daha kompleks, çünkü elimizde 2 farklı seçenek var. While döngüsündeki
kontrole göre içine girip işleme devam edebiliriz, ya da döngüyü geçip fonksiyonun sonuna
atlayabiliriz, kolay olduğu için sona atladığımız duruma bakalım. Bunun için elimizdeki
araçlardan bir tanesi, döngü açımı (loop unrolling). Döngünün bir iterasyonunu bir `if`
olarak açıp, aynı anlamı (semantic) koruyabiliyoruz.

```java
    if (low <= high) {
        // Döngünün 1. iterasyonuna giriş yaptık.
        int mid = (low + high) / 2;
        int midVal = a[mid];

        if (midVal < key)
             low = mid + 1
         else if (midVal > key)
             high = mid - 1;
         else
             return mid; // key found 
        // Döngünün 1. iterasyonu bitti, 2. iterasyondan devam ediyoruz.
        while (low <= high) {
            int mid = (low + high) / 2;
            int midVal = a[mid];

            if (midVal < key)
                low = mid + 1
            else if (midVal > key)
                high = mid - 1;
            else
                return mid; // key found
        }
    }
    // Döngü 1 ya da daha fazla iterasyon sonrasında bitti.
    return -(low + 1);  // key not found.
```

Elimizdeki bir diğer araç ise `if` için. `if` gördüğümüz noktada, 2 ihtimal var,
ya `if` içindeki kontrol doğrudur ve içerideki hesaplamayı yaparız, ya da değer
yanlıştır ve `if` den bir sonraki hesaplamayla devam ederiz. Öncelikle 0 döngü durumundan,
yani `if` içerisindeki kontrolün ilk iterasyona girmeden yanlış olmasından başlayalım.

```java
// Var olan değişkenleri hatırlayalım
int low = 0; // (low : [0, 0])
int high = a.length - 1; // (high : [-1, 2^31 - 1])
if (low <= high) { // kontrol yanlış olmalı, demek ki (!low <= high), bu da demek ki (low > high) 
...
}
// (low > high) olan tek bir durum var, o da low = 0, high = -1.
return -(low + 1);  // dolayısıyla (- low + 1) = -1, taşma yok.
```

Tüm detayları vermeye çalıştığımda burası çok uzayacak, dolayısıyla buradan itibaren biraz hızlı gideceğim. Diğer
durumda `low <= high` olmalı, dolayısıyla `low: [0, 0]`, `high: [0, 2^31-1]` ile devam ediyoruz.

```java
int mid = (low + high) / 2; // Aralıklar üzerinde toplama ve bölme işlemi: ([0, 0] + [0, 2^31-1]) / 2 = [0, 2^30]
int midVal = a[mid]; // Dizinin elemanları hakkında bir bilgi sahibi değiliz, dolayısıyla midVal: [-2^31, 2^31 - 1]

// Eğer buraya kadarki hesaplamalarımız bizi bir kontrolün yanlış olduğu sonucuna ulaştırırsa,
// o dalı atlayabiliriz. Şu anda böyle bir sonuca ulaşamadığımız için 3 daldan ilerlemeleri ayrıca incelememiz gerekecek.
if (midVal < key) // midVal: [-2^31, 2^31 - 1], key: [-2^31, 2^31 - 1], midVal < key = ?? 
    low = mid + 1 // midVal < key = true, mid: [0, 2^30], dolayısıyla low: [1, 2^30 + 1]
else if (midVal > key) // midVal: [-2^31, 2^31 - 1], key: [-2^31, 2^31 - 1], midVal < key = false, midVal > key = false
    high = mid - 1; // midVal > key = true, mid: [0, 2^30], dolayısıyla high: [-1, 2^30 - 1]
else // midVal: [-2^31, 2^31 - 1], key: [-2^31, 2^31 - 1], midVal < key = false, midVal > key = false
    // (midVal < key) ve (midVal > key) yanlış, geriye yalnızca (midVal = key) kalıyor, dolayısıyla aradığımızı bulduk.
    return mid; // aradığımızı bulduğumuz için fonksiyondan çıktık, bu dalın devamında incelenecek bir şey yok, ilk
                // iki dala devam etmeliyiz.
```

Bu hesaplamanın sonucunda, elimizde artık 3 farklı evren var. Birisinde birinci iterasyonda aradığımız elemanı bulduk,
dolayısıyla işimiz bitti, devam etmemiz gerek yok. Diğerinde aradığımız eleman ortanın solunda, diğerinde sağında. Hadi
gelin aradığımız elemanın ortanın sağında olduğu `midVal < key` dalında, `low = mid + 1` sonucunda elimizdeki aralıkların
`midVal: [-2^31, 2^31 - 1]`, `key: [-2^31 + 1, 2^31 - 1]`, `low: [1, 2^30 + 1]`, `high: [0, 2^31-1]` evrenine gidelim.

Bu evrende, yine yukarda yaptığımız While döngüsünü açma, ikiye bölme, `if` kontrolünün içerisinde girme işlerini yapacağız.
Bunlar sonucunda 

```java
// low: [1, 2^30 + 1]`, high: [0, 2^31-1]
int mid = (low + high) / 2; // low + high = [1, 2^30 + 1] + [0, 2^31-1] = [0, 2^31 + 2^30]
```

32-bit tamsayılarla ifade edebildiğimiz en büyük tamsayının 2^31-1 olduğunu daha önce söylemiştik, ancak
fark ettiyseniz bu işlem sonucunda ortaya çıkan aralık bu sınırı aştı `[0, 2^31 + 2^30]`. Dolayısıyla
bu analiz ile kullanıcıya geri dönüp, senin bu işlemin potansiyel olarak senin tipinin sınırlarını aşıyor
diyebiliriz.

Burada yaptığımız analiz bir tip statik kod analizi (static code analysis), bu tarz analizler yalnızca tamsayı taşmalarına mı yarıyor, hayır.
Mesela [Facebook Infer](https://fbinfer.com) benzer analizleri milyonlarca satır C++ koduna uygulayarak koddaki hafıza güvenliği hatalarını
otomatik bir şekilde keşfetmeye, `NULL` işaretçileri (pointer) statik olarak keşfetmeye çalışıyor. Tahmin edebileceğiniz üzere bu yöntemlerin
hepsinin sınırları var, yoksa bugün Rust diye bir dile ihtiyacımız olmazdı, statik olarak C++'daki tüm hafıza güvenliği problemlerini
çözebilirdik, ancak çözemiyoruz. Dilin tasarımı, bizim o dil ile ilgili yapabileceğimiz analizleri kısıtlıyor. Dilde yapabildiğiniz her
dinamik işlem, statik olarak keşfedebileceğimiz bilgi miktarını azaltıyor. Bu sebepten ki Rust derleyicisinin reddedeceği hafıza
güvenliğinden yoksun programları C++ kabul ediyor, ya da herhangi bir statik programlama dilinin derleme zamanında engelleyeceği
hatalar ile Python, Javascript gibi dillerde çalışma esnasında karşılaşıyoruz. Java dilinin üzerine yazılan statik analiz araçlarının
en büyük kısıtlamalarından birisi Java'daki yansıma (reflection) özelliğinin analizin kesinliğini düşürüp analizi faydasız hale getirmesi.

Buraya kadar daha üst-seviye (meta level) doğruluk kavramlarından bahsettik, programın her noktasında tutması gereken, programlama dilinin
kendisi ile direkt olarak bağlı nitelikler bunlar, aynı zamanda bunlara bir çeşit güvenlik niteliği (safety property) diyoruz, çünkü
hiçbir zaman bozulmaması gereken nitelikler belirleyip, programımızın aldığı herhangi bir yol bu nitelikleri bozabiliyor mu onu arıyoruz.
Formal metotların programlamanın tamamına etki etmesi için, çok daha çeşitli niteliklere (properties) ihtiyacımız var, ve dahası
programcıların bu nitelikleri yazabilmesi için bir dil sağlamalıyız ki, doğruluk yalnızca bizim düşündüğümüz ve tasarladığımız
niteliklerden ibaret olmasın.

## Tip-Odaklı Geliştirme

Bu dillerden ilki, daha önce de bahsettiğim üzere, tipler. [Tip sistemleri](https://alperenkeles.com/posts/tip-sistemleri-hakkinda/),
bizim yazdığımız programları kısıtlayabilmemizi, tipleri kullanarak programların ulaşmaması gereken durumlardan kaçınmamıza izin veriyor.
Bundan bazen tip-odaklı geliştirme (type-driven programlama) olarak bahsedildiğini görebilirsiniz, bu yaklaşımın mottosu "Hatalı
durumları temsil edilemez yap" ([Make invalid states unrepresentable](https://lambda-the-ultimate.org/node/2216#comment-31690)).
Çoğu zaman, programlarımızda tip sisteminin izin verdiği, yani derleyicinin bir hata vermeyeceği, ancak aslında mümkün olmaması gereken
ihtimaller var. Tip-odaklı geliştirme bunları ortadan kaldırabiliyor.

```ts
type Insan = {
    isim: string,
    okul?: string,
    sirket?: string,
}
```

Yukarıdaki tip, bir kişiyi tanımlarken, `okul` ya da `sirket` alanlarının `undefined` olmasına izin veriyor. Alttaki veri modeline göre
bunun doğru olduğu noktalar vardır, ancak şu anda tartıştığımız evrende bir kişi ya okula, ya da şirkete gidebiliyor olsun. Yani bunların
ikisi de aynı anda var olamaz, ikisi de aynı anda boş da olamaz, ancak veri modelimiz buna izin veriyor. `{isim: "Alp"} as Insan` yazmak
tip hatası vermeyecek. Alternatif olarak, bu tipi aşağıdaki gibi tanımlayabilirdik:

```ts
type Insan   = { isim: string } & (Ogrenci | Calisan)
type Ogrenci = { okul: string }
type Calisan = { sirket: string }
```

Bu örnekte, `Insan` ya bir öğrenci olup okula sahip olacak, ya da bir çalışan olup şirkete; hiçbirisine sahip olmadığı durumlarda tip
sistemi bize hata verdiği için o ihtimal çalışma zamanında var olmayacak.

## Kontrat Bazlı Dizayn (Design by Contract)

Kontratlar fikir olarak nereden çıktı emin değilim, ancak benim şahsen bildiğim en eski popüler örnek Eiffel programlama dili. Kontratlar
bizim alttaki programa dair ne tarz varsayımlarımızın olduğunu (assumptions, preconditions), ne tarz sonuçlar beklediğimizi (postconditions),
programın hangi nitelikleri koruduğunu (invariants) tanımlamamızı sağlıyor. Aşağıda, Dafny programlama dilinde `Max` fonksiyonunun
tanımı var:

```dafny
method Max(a: int, b: int) returns (m: int)
  ensures m >= a
  ensures m >= b
  ensures m == a || m == b
{
  if a >= b {
    m := a;
  } else {
    m := b;
  }
}
```

Kontrat diyor ki, metodun ürettiği `m` değeri hem `a` hem de `b` parametrelerinden büyük eşit olmalı, hem de ikisinden
birisine eşit olmalıdır. Kontratın kendisi, fonksiyonun implementasyonundan bağımsız olarak neyin doğru olduğunu tanımlıyor,
Dafny ise derleme zamanında implementasyonun bu kontrata uyduğunu kanıtlıyor. Eğer implementasyonda bir hata varsa, mesela
tüm fonksiyonu silip yalnızca `m := b` yazarsak, `ensures m >= a` şartı kanıtlanamadığı için Dafny programı derlemeyecek.

Gelin bir de yukarıda bahsettiğimiz `midpoint` örneğine bakalım:

```dafny
method Midpoint(low: int, high: int) returns (mid: int)
    requires low <= high
    ensures mid * 2 >= low + high - 1
    ensures mid * 2 <= low + high
{
    mid := (low + high) / 2;
}
```

Dafny'de `int` çoğu anaakım programlama dilinin aksine 32 bitlik değil, dolayısıyla bu örnekte taşma konusunda endişelenmemiz
gerekmiyor. Onun yerine `requires` bize bu fonksiyonun hangi şartlar altında çağırılabildiğini söylüyor, ancak `low <= high` durumunda
bu fonksiyonu çağırabildiğimiz için içerde `if a < b` kontrolünü tekrar yapmadan sonucu hesaplayabiliyoruz, `midpoint`'i ise
çarpma işleminin sonucu üzerinden tanımlıyoruz.

Burada küçük programlardan bahsettiğime bakmayın, AWS yeni yazdığı Yetkilendirme Politikaları Dili (Authorization Policy Language) olan
[Cedar](https://www.amazon.science/blog/how-we-built-cedar-with-automated-reasoning-and-differential-testing)'ı önce Dafny'de geliştirdi,
benzer şekilde [şifreleme kütüphanesini](https://github.com/aws/aws-encryption-sdk) Dafny'de kanıtladı. Her ne kadar çok ciddi uzmanlık
ve zaman gerektirdiği için bu kütüphaneleri geliştirmek, yazdığımız programları kanıtlamak bugün zor olsa da, asıl soru bu aslında, yapay
zeka yardımıyla kanıtlamalı programlama yapabildiğimiz bir dünyada bu tarz teknolojileri kullanarak yazdığımız programların
doğruluğunu arttırabilir miyiz?