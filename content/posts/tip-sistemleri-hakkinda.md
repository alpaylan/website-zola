+++
title = "Tip Sistemleri Hakkında"
date = "2024-12-01"
[taxonomies]
tags = ['programming languages']
language = ["tr"]
+++

Tip sistemleri(type systems), programlama aktivitesinin temelinde yer almalarına rağmen gözümüzün önünden kaçan, programlama dillerinin özellikleri arasında çoğu zaman düşünmediğimiz, en az konuştuklarımızdan birisi. Bu yazıyı tip sistemlerinin günlük programlama pratiklerimizi nasıl yönlendirdiğini merkeze alarak yazmaya çalışacağım.

## Tip Sistemi Nedir?

Her programlama dili, bazen dikkatli bir matematiksel dizaynın sonucunda oluşturulmuş, bazen de yaratıcısının tercihlerini yansıtacak şekilde bir tip sistemi içerir. Tip sistemleri, programlama dilindeki işlemlerin geçerliliğine dair yargılarda bulunmamızı sağlar, geçersiz işlemler sonucunda bizlere hata mesajları verir. Tip sisteminin dizaynı yazdığımız programların ne kadar *jenerik* olabildiğini, kullandığımız kodun içerisinde yazmamız gereken *tip işaretçilerini*(type annotations), kullandığımız editörden aldığımız *tip ipuçlarını*(type hints) etkiler.

Küçük bir aritmetik dili ile yolumuza başlayalım. Dilin yapısının tanımlanmasına BNF(Backus-Naur Form) adı verilen, programlama dillerinin gramerlerini ifade etmek için kullanılan bir notasyondan faydalanacağız.

```bnf  
e ::= e + e | e - e | e && e | e < e | e > e
  | 1 | 2 | 3 …
```

Sırada, bu dildeki işlemlerin *anlamına*(semantics) karar vermek gerekiyor. Sırasıyla elimizdeki işlemler toplama(`+`), çıkarma(`-`), mantıksal ve(`&&`), küçüktür(`<`), ve büyüktür(`>`) işlemleri. Peki `(3 < 5) + 2` bize nasıl bir anlam ifade etmeli? Böyle bir işleme izin vermeli miyiz? Yoksa hata mı vermeliyiz? İzin verirsek nasıl bir sonuç vermeliyiz, hata verirsek nasıl bir hata vermeliyiz? Hadi gelin bu tarz bir işlemle karşılaştıklarında şu anki popüler programlama dillerinin neler yaptığını inceleyelim.  
Python, Javascript, C:

```txt
3
```

Typescript:

```txt
Operator '+' cannot be applied to types 'boolean' and 'number'.  
```

Rust:

```txt
  error[E0369]: cannot add `{integer}` to `bool`   
  --> error.rs:8:13  
  |  
8 |     (3 < 5) + 2;  
  |     ------- ^ - {integer}  
  |     |  
  |     bool  
```

Java:

```txt
error.java:6: error: bad operand types for binary operator '+'  
((3 < 5) + 2);  
    ^  
  first type:  boolean  
  second type: int  
```

Gördüğümüz üzere, Python, Javascript ve C `(3 < 5) + 2` programını gördüklerinde `3  < 5`’i toplama bağlamında 1 olarak yorumlayıp cevabı 3 bulurken,  Typescript, Rust ve Java toplamanın mantıksal bir ifade(boolean) ile bir sayı(number, integer ya da int) arasında geçerli olmadığına karar verip, buna dayanarak programımızı reddediyorlar. Diller arasındaki bu farklılıklar, tip sistemlerinden kaynaklanıyor. Yazdığımız programlardaki her bir ifadenin bir tipi var, tip sistemleri ise programın içerisinde yer alan farklı ifadeleri programlama dilimizdeki yapıları kullanarak bir araya getirme aşamasında bizim hatalarımızı keşfetmemize imkan sağlıyorlar.

Peki Python, Javascript ve C aynı tip sistemini mi kullanıyorlar, basit bir örnekle görebiliyoruz ki hayır. Dilimize sicimleri(string) eklediğimizde Python ve Javascript arasındaki farkı görebiliyoruz. Yeni işlemimiz `”alp” + 3`.

Python:

```txt
Traceback (most recent call last):  
  File "<python-input-0>", line 1, in <module>  
    "alp" + 3  
    ~~~~~~^~~  
TypeError: can only concatenate str (not "int") to str  
```

Javascript:

```txt
"alp3"
```

Burada yaşanan farklılıkların sebebi otomatik tip çevirisi(implicit coercion) kurallarının dilden dile farklı olması. Popüler kültürde bunu bazen zayıf/güçlü tipleme(weak/strong typing) olarak duysak da, bu terimler dilleri kategorize etmek için yeterince kesin değil. Daha ziyade tip sisteminin içerisine yerleştirilmiş tip çeviri kuralları.  
O zaman, başta bahsettiğimiz `(3 < 5) + 2` işleminin reddedildiği bir tip sistemi tasarlayalım. Burada tip teorisi(type theory) notasyonunu kullanarak tip sistemini yazabiliriz. Notasyonu aşağıdan yukarıya okumak gerekiyor. Sayı sabitlerinin tipi ile başlayalım.

```txt
----------------------(integer)
Γ, 0,1,2… : integer

```

Bu kural, bize şunu söylüyor.

- `Γ(Gamma)`:  Şu anda programdaki diğer ifadelerin tiplerini tutan bir mapping.  
- (`0,1,2… : integer):` 0, 1, 2… sayı sabitlerinin tipinin tamsayı(integer) olduğunun ifadesi.  
- Uzun çizgi(`----`):  Altta verilen tip yargısının(typing judgement) geçerli olması için gerekli tip yargıları.

Bu örnekte çizginin üstünde bir gereksinim olmadığı için, programdaki herhangi bir sayı sabiti gördüğümüzde o sabitin tipinin `integer` olduğunu söyleyebiliyoruz.

```txt  
Γ, e1 : integer        Γ, e2 : integer  
---------------------------------------(+)  
        Γ, e1 + e2 : integer  
```

İkinci baktığımız kural ise bize şunu söylüyor, iki ifadenin toplamı, eğer toplamın sağ ve sol kollarının tipi tamsayı ise tamsayı olur. Bu kuralı programdaki herhangi bir toplama işleminin doğru tiplere sahip olduğunu kanıtlamak için kullanabiliriz. Bunun için de türetim ağacı(derivation tree) adını verdiğimiz kuralları üst üste koyarak büyük ifadelerin tiplerine karar verdiğimiz bir metot kullanıyoruz.  

```txt
1 : integer        2 : integer  
------------------------------  
      1 + 2 : integer              3 : integer  
---------------------------------------------------  
              (1 + 2) + 3: integer  
```

Bu kuralı aşağıdan yukarıya doğru okursak, `(1 + 2) + 3`ün tipinin tamsayı olması için, `1 + 2`nin tipinin tamsayı olması gerekir, onun için de 1 ve 2’nin tiplerinin tamsayı olması gerekir, diğer yanda da 3’ün tipinin tamsayı olması gerekir. Bir türetim ağacı yazdığımızda ağacın tüm yapraklarının(leaf) en başta bahsettiğimiz ek gereksinimi olmayan kurallardan birisi olması gerekir. Aşağıda, sırasıyla çıkarma(`-`), küçüktür(`<`), büyüktür(`>`) ve mantıksal ve(`&&`) kurallarını okuyabilirsiniz.

```txt
Γ, e1 : integer        Γ, e2 : integer  
---------------------------------------(-)  
          Γ, e1 - e2 : bool


Γ, e1 : integer        Γ, e2 : integer  
---------------------------------------(<)  
          Γ, e1 < e2 : bool


Γ, e1 : integer        Γ, e2 : integer  
---------------------------------------(>)  
          Γ, e1 > e2 : bool


Γ, e1 : bool           Γ, e2 : bool  
---------------------------------------(&&)  
          Γ, e1 && e2 : bool  
```

Eğer ki yazılan  bir program için bir türetim ağacı üretemiyorsak, o halde o programa biz hatalı-tipli(ill-typed) deriz. Misal, yukarıdaki tip sisteminde `(3 < 5) + 2` programı için bir türetim ağacı yok, çünkü `(e1: bool + e2: integer)` için kullanabileceğimiz herhangi bir kural yok, dolayısıyla türetim esnasında sıkışıyoruz(stuck).

```txt
3 : integer     5: integer  
--------------------------  
      (3 < 5): bool        2: integer  
-----------------------------------------  
            (3 < 5) + 2 : ??  
```

Dolayısıyla eğer ki bu ifadenin makul-tipli(well-typed) olmasını istiyorsak tip sistemine bu ifadenin tipini belirleyecek yeni kurallar eklememiz gerekiyor. Bunu yapmanın birden fazla yolu var, ilki de şu.

```txt
Γ, e1 : bool  
-----------------(b->i)  
Γ, e1 : integer  
```

Bu kural sayesinde, `(3<5): bool` tiplemesini `(3<5): integer` tiplemesine çevirebiliyoruz. Diğer ihtimalde ise herhangi bir bool tipinde değeri integer’a çevirmek yerine, bu çeviriyi yalnızca toplama işlemi esnasında yapabiliriz.

```txt
Γ, e1 : bool           Γ, e2 : integer  
---------------------------------------(b+i)  
        Γ, e1 + e2 : integer  
```

Ancak bu durumda tek bir kural bizim için yeterli değil. Çünkü bu kural `(3<5)+2` için yeterliyken, `2+(3<5)` için değil. Dolayısıyla kuralın ters versiyonuna ihtiyacımız da var.

```txt
Γ, e1 : integer            Γ, e2 : bool  
---------------------------------------(i+b)  
        Γ, e1 + e2 : integer  
```

Burada bu kuralların hepsinin sözdizimsel(syntactic) olduğu gerçeğini net bir şekilde görebiliyoruz. Bizler kendi kafamızda `a+b` ile `b+a`yı birbiri ile ilişkilendirsek de, üzerinde çalıştığımız sisteme bu tarz kuralların hepsini tek tek kodlamamız gerekiyor. Hem `i+b` hem de `b+i` şeklinde 2 kural yazmak yerine, ikinci kuralı daha genel bir kural olan toplamın değişebilirliği (commutativity) olarak da yazabilirdik.

```txt
Γ, e2 + e1 : T  
---------------(commutative)  
Γ, e1 + e2 : T  
```

Fark ettiyseniz, ilk kez `e1, e2` gibi ifade değişkenlerinin(expression variable) yanı sıra bir tip değişkeni(type variable) olan `T`’yi kullandık.  Elimizdeki toplama, karşılaştırma ve mantıksal ifadelerin üzerine programlama dillerinde kullandığımız `if-else` ya da fonksiyon uygulaması(function application) gibi yapılar işin içerisinde girdiğinde bu tarz tip değişkenleri tip sisteminin çok daha içerisinde oluyor. Mesela, aşağıda dile `if-else` ifadesi(expression) eklediğimizde kullanacağımız kuralı inceleyelim.

```txt
Γ, e1 : bool        Γ, e2 : T           Γ, e3 : T  
---------------------------------------------------(if-else)  
          Γ, if e1 then e2 else e3 : T  
```

Bu kuralı okursak, `if-else` ifadesinin makul-tipli olması için `` e1 `` ifadesinin bir boolean olması, `` e2 `` ve `` e3 `` ifadelerinin de aynı `` T `` tipine sahip olması gerek.  
Bir diğer genel kural ise fonksiyon çağrısı(function call).

```txt
Γ, e1 : T1     
Γ, e2 : T2 …  Γ, en : Tn
Γ, fn : (T1, T2…Tn) -> T    
--------------------------------------------------------(fn-call)  
Γ, fn(e1, e2…en) : T  
```

Bu kuralı okumak için de, `` (T1,T2, … Tn) `` tiplerinde girdileri kullanarak `` T `` tipinde bir çıktı üreten bir fonksiyonu çağırmak için, fonksiyona sağladığımız girdilerin sırasıyla `` T1, T2…Tn `` tiplerine sahip olması gerek.

Bu kurallar ile birlikte, bir tip sistemi nasıl yazılır hakkında kısa bir giriş yapmış olduk. Şimdi, tip sistemlerinin nasıl kullanıldığını tartışalım.

## Statik ve Dinamik Tip Sistemleri

Tip sistemleri ile ilgili ilk tartışma statik ya da dinamik olmaları. Bu yazıda bu tartışmayı mümkün olduğunca ileri atmak istedim, çünkü statiklik ve dinamiklik bir programın bir tip sistemince makul-tipli kabul edilip edilmemesine katkıda bulunsa da, tip sisteminin kendi dizaynı çok daha etkili.

Sistemin statik veya dinamik olması bir programın kabul edilip edilmemesinden ziyade, hangi noktada reddedileceğini etkiliyor. Statik tip sistemi
implementasyonları programın derleme zamanında(compile time) tip bilgisini kullanarak programın tipini kontrol ederken, dinamik tip sistemleri programın çalışma zamanında(run time) tip bilgisini kullanarak programın tipini kontrol ediyor. Tabii ki bu farklılık, tip sisteminin kendi dizaynını da yeri geldiğinde etkileyebiliyor, çünkü statik bir sistemde tip bilgilerini taşıyıp programın herhangi bir girdi için makul tipli olduğunu kanıtlamak gerekirken, dinamik bir sistemde programın çalışması esnasında sahip olduğumuz tip bilgilerinden yararlanabiliyoruz.

Statik ve dinamik sistemler arasındaki en büyük fark `if-then-else` gibi şartlı(conditional) ifadelerde ortaya çıkıyor. Yukarıda örnek verdiğim tip sisteminde `if-else` ifadesi için yazdığımız kuralda hatırlıyorsanız `then` ve `else` kollarının tipleri aynı olmalıydı. Bu kural, statik tip sistemlerinde sıkça gördüğümüz bir kural, çünkü statik bir tip sistemi programa hangi kol ile devam edileceğini bilmediği için programın devamında
iki kolun da tip bilgisini taşımak zorunda. Buna bir alternatif birlik tipleri(union types) kullanmak, örneğini Typescript'te görebiliriz.

```typescript
let a: string | number = Math.random() > 0.5 ? "alperen" : 3;
```

Yukarıdaki kod içerisinde kullandığımız üçlü-şart-ifadesi(ternary if-expression) içerisinde `then` ve `else` kolları farklı tipler dönüyor, dolayısıyla
bizim sonuçta elde ettiğimiz tip `string | number` (string **veya** number) oluyor. Bu kuralı şu şekilde yazabiliriz.

```txt
Γ, e1 : bool     Γ, e2 : T1       Γ, e3 : T2
--------------------------------------------(if-else-union)  
    Γ, if e1 then e2 else e3 : T1 | T2  
```

Bu iki kuralı dinamik tipli bir tip sisteminde yazmamıza gerek bile yok, ileriye doğru taşımamız gereken tip bilgisini programın çalışma zamanında elde edebiliyoruz. Bu durumda, programın sonucunu hesaplarken(evaluation) hangi kolun seçildiğine göre ileriye doğru ileteceğimiz tip bilgisini değiştirebiliriz.

```txt
    Γ, e2 : T
--------------------------------------------(if-true)  
    Γ, if True then e2 else e3 : T

    Γ, e3 : T
--------------------------------------------(if-false)  
    Γ, if False then e2 else e3 : T
```

Aşağıda, girdi `alperen` olmadığı sürece tip hatası verecek bir Python programını görebilirsiniz. Aynı programı statik bir tip sisteminde yazdığımızda
tip kontrolcüsü derleme zamanında hata verecektir, çünkü `a` değişkenininin `alperen` olmadığı koşulunda `a` değişkenine makul bir tip atamak mümkün değil.

```python
a = input()

if a == “alperen”:  
  return 3 + 5  
else:  
  return “a” + 3  
```

Dinamik tip sistemlerinin bir diğer farkı da tip denetimi(type inspection). Statik tip sistemlerinin sağladığı en büyük artılardan birisi programdaki tipler derleme esnasında belirli olduğu için derleme zamanında(compile time) tip bilgisinin kullanılması, ancak programın çalışması zamanında(run time) tip bilgisinin silinmiş olması. Bu sayede dinamik tip sistemlerinde ortaya çıkan tip bilgisinden kaynaklı performans kaybından kaçabiliyoruz. Diğer yanda, çalışma zamanında tip bilgisine erişimimizin olması da dinamik tip sistemlerinde heterojen listeler (heterogeneous lists) gibi veri yapılarını yazıp kullanabilmemize imkan sağlıyor. Teoride statik bir tip sisteminde de heterojen listeler oluşturabilsek de, bu listenin elemanları üzerinde herhangi bir işlem yapabiliyor olmamız mümkün değil. Yine bir Python programıyla örnekleyelim.

```python
l = [1, True, “alperen”]

for elem in l:  
  if type(elem) == int:  
    print(“Element bir tamsayı”)  
  elif type(elem) == bool:  
    print(“Element mantıksal bir değer”)  
  else:  
    print(“Element tipini bilmiyoruz”)  
```

Aynı programı, Rust gibi bir programlama dilinde yazmamız mümkün değil, çünkü Rust listenin tipinin heterojen olmasına izin vermiyor. E peki statik tipli bir programlama dili implementasyonunda farklı tipten değerleri içeren bir liste oluşturamaz mıyız? Bu sorunun cevabını vermek için gelin çok-tiplilikten(polymorphism) bahsedelim.

## Jenerik, Çok Tipli Programlar

Bahsettiğim gibi, statik tipli dillerde heterojen veri yapıları oluşturup elemanların tiplerine göre çalışma zamanında karar almak çok mümkün değil. Ancak programlamada jenerik veri yapıları çok önemli, liste(List), yığın(Stack), kuyruk(Queue), ağaç(Tree) gibi sandık(container) veri yapılarını jeneriklikleri sayesinde farklı farklı tipler için kullanabiliyoruz. Bu tarz veri yapılarına çok-tipli veri yapıları diyoruz, ve `` List<T>, Stack<T>, Queue<T>, Tree<T> `` şeklinde `` T `` tipi ile parametrik olarak yazıyoruz. Burada `` T `` tipi ile ilgili hiçbir şey bilmediğimiz için, bu veri yapıları üzerinde yazdığımız fonksiyonlarda dolayısıyla alttaki tipe dair herhangi bir varsayım yapamıyoruz, yalnızca veri yapısının üzerinde herhangi bir `T` tipi ile çalışacak fonksiyonlar yazabiliyoruz. Buna literatürde Parametrik Çok Tiplilik(Parametric Polymorphism) diyoruz. Parametrik Çok Tipli programlar aldıkları tip parametresinin tip sınırlamalarına(type bound) bağlı olarak tip kontrolünden geçerler.

Yukarıda bahsettiğim `List<T>` gibi bir programda `T` üzerinde herhangi bir sınırlandırma olmadığı için, listenin elemanlarıyla hiçbir işlem yapamayız. Bu da demek oluyor ki, biz bu liste için bir ekrana basma(printing) fonksiyonu yazamayız, çünkü listenin elemanları için bir `print` fonksiyonumuz yok. E peki bu veri yapıları üzerine bu tarz içerdeki elemanları kullanan bir fonksiyon yazmak istersek nasıl yazıyoruz?

Rust programlama dili bunu `Trait` sistemi ile çözüyor. Fonksiyonlar, tip olarak yalnızca katı tipler(concrete types) almıyor, bunun yanında tip sınırlandırmaları da alabiliyorlar.

```rust  
fn print_list<T: Display>(t: List<T>)
```

Örnek verdiğim fonksiyon `T` tipini `Display` trait’ine sahip bir tip olarak sınırlandırıyor. `Display` sınırlandırmasına sahip olan tipler Rust’ın jenerik `print` fonksiyonuna erişim sahibi olduğu için, biz bu tipler üzerine bir liste için de `print` fonksiyonu yazabiliyoruz.

Parametrik Çok Tiplilik çok-tipli programlar yazmanın tek yolu değil. Ayrık Çok Tiplilik(ad hoc polymorphism) ya da Alt-Tipleme(Subtyping) kullanarak da çok-tipli programlar yazabiliyoruz.

### Ayrık Çok Tiplilik

Ayrık Çok Tiplilik için, kullandığımız programlama dilinin aynı fonksiyonu farklı tipler için tekrar tekrar yazmamıza izin vermesi yeterli oluyor. Aşağıda, aynı fonksiyonun `` (to_string) `` iki farklı tip (bool, int) için 2 farklı kez yazılabildiğini görüyoruz. Programda bir noktada `print` fonksiyonu çağrıldığında derleyici fonksiyonun girdisinin tipine göre doğru `print` fonksiyonunu seçip, onu kullanıyor.

```rust
fn to_string(b: bool) -> String  
fn to_string(i: int) -> String  
```

Ayrık Çok Tiplilik kullanıldığında ortada bir parametrizasyon yok, ancak yine de aynı fonksiyonu farklı tipler için kullanabiliyoruz. C++ tip sistemi
bu tarz çok-tiplilik için çok uygun bir örnek. Parametrik çok-tiplilik tip sisteminin içine gömülmüş değil, yani C++ tip kontrolcüsünün bir fonksiyonu
parametrik çok-tipli olarak tipleme şansı yok. Ancak C++ dilinde de `List<T>` gibi veri yapıları görebiliyoruz, bunlar üzerine fonksiyonlar yazabiliyoruz.
Bunu yapabilmemizin sebebi ise C++ tipinin bir şablon sistemi(templates) ile ayrık çok-tipliliği birleştirerek parametrik çok-tiplilik ilüzyonu yaratması.

Yukarıda verdiğim Rust örneğinde de, aynı örneğin C++ versiyonunda da derleme sonrasında çalıştırdığımız kod aslında monomorfik, yani tek-tipli. Ancak
derleme esnasında, Rust fonksiyonu çok-tipli olarak tip kontrolcüsüne verip, ortaya çıkabilecek tip hatalarını tek-tipleştirme(monomorphization) işlemi öncesinde keşfederken, C++ önce şablon doldurma(template instantiation) ile tek-tipli bir fonksiyon üretiyor, ve bu fonksiyonu derlerken tip hatalarını keşfediyor. Bu sebepten dolayı C++ şablon sistemi ile yazılan programlarda ortaya çıkan hatalar daha kriptik olabiliyor.

### Alt-Tipleme

Nesne Yönelimli Programlama(Object Oriented Programming) bize çok-tipli programlar yazmak için farklı bir mekanizma sağlıyor, bunun adı da alt-tipleme(subtyping). Alt tipleme esasında bir tipin diğerinin özelliklerini miras alabilmesi(inheritance) üzerinden kurgulanıyor. Örnek vermek gerekirse, Java dilindeki tüm sınıflar `Object` üst sınıfının(superclass) çocukları, ya da torunları, daha da teknik tabiriyle alt sınıfları(subclass). Bir alt-tip, üst-tipinin tüm fonksiyonlarına ve özelliklerine sahip bir tiptir. Dolayısıyla Java’da heterojen bir liste yazmak istesek, `List<object>` tipinde bir liste oluşturmamız yeter, çünkü `List<object>` tipinde bir liste `object` tipinin tüm alt-sınıflarını içerebilir, ve Java’daki tüm tipler `object` tipinin bir alt sınıfıdır.  
Alt-tiplemenin ortaya çıktığı tek nokta nesne yönelimli programlama değil, yapısal tipler(structural types) da alt tipleme ile ilgili konuşurken karşımıza sık çıkan başka bir konsept.

## Yapısal ve İsimsel Tipler

Yapısal tipler(structural types) ve isimsel tipler(nominal types) kullandığımız dillerde yine sıkça ortaya çıkan, ancak tip sisteminin arkasında saklandığı için çok konuşmadığımız bir ikilem. Bazı tip sistemleri yapısal ve isimsel tipler arasında bir seçim yapsa da, pek çok dilde ikisini de gözlemleyebiliyoruz. İsimsel tipler, adından da anlaşılacağı üzere, bir tipin isimlendirilmesinden ortaya çıkıyor. Ben bir X tipi oluşturduğumda, o tipte bir değer ancak ve ancak başka bir X tipinde değer ile karşılaştırılabilir, ya da yer değiştirebilir. Yapısal tipler sayesinde kullandığımız tipler artık anonim hale gelebiliyor. Typescript’te bir objeye `` {x: number, y: number} `` tipini verdiğimizde bu tipe bir isim vermek zorunda değiliz, tip sistemi her objenin yapısını(şeklini) tutuyor, ve objeleri bu yapılar ile tanımlıyor. Dolayısıyla tip sisteminin gözüne aşağıda tanımladığımız `Point` ve `Vector` tipleri farklı tipler değil, dolayısıyla yer değiştirebilirler.

```typescript  
type Point = {x: number, y: number}  
type Vector = {x: number, y: number}  
```

Eğer ki bu program isimsel bir tip sistemi kullanarak yazılıyorsa, ki bunun için Java, Rust, C++, Python gibi pek çok dilde örnekler verebiliriz, bu iki tip farklı tiplerdir, ve birbirleri ile yer değiştiremezler.

Yapısal tiplerde alt-tipleme nesne yönelimli programlamadaki gibi kasıtlı bir miras yapısından ziyade, tip yapısının kendisinden ortaya çıkar. Örnek vermek gerekirse, `` {x: number, y: number} `` yapısal tipi `` {x: number} `` yapısal tipinin bir alt-tipidir, çünkü programda `` {x: number} `` tipinde bir obje bekleyen herhangi bir noktada onun yerine `` {x: number, y: number} `` tipinde bir obje kullanılabilir.

Peki, tip sistemleri tipleri programda nasıl takip ediyor? Neden bazı programlama dillerinde tanımlama esnasında her değişkenin tipini yazmak zorundayken diğerlerinde `let` ya da `var` yazıp geçebiliyoruz, ve neden bazen bu dillerde de bunu başaramıyoruz, Swift programlama dilinde neden 20 satırlık bir kodu derlemek bazen 45 saniye sürebiliyor? Bunları anlamak için biraz da tip kontrolü(typechecking) ve tip çıkarımı(type inference) kavramlarını tartışalım.

## Tip Kontrolü ve Tip Çıkarımı

Yazının en başında, Tip Sistemlerinin ne olduğu hakkında konuşurken tip kontrolü(typechecking) hakkında biraz bilgi vermiştik aslında. Tip kontrolü, verilen programın makul-tipli(well-typed) ya da hatalı-tipli(ill-typed) olup olmadığına karar veren prosedür. Tip kontrolü algoritmalarının amacı programdaki ifadelerin tiplerinin tip sistemi üzerinde tamamlanabilecek bir türetim ağacı ürettiğini kanıtlamak. Yazının başındaki gibi basit tip sistemleri ile çalışırken tipleme kurallarını(typing rules) tersine çevirerek mekanik bir şekilde bir tip kontrolü algoritması üretebiliyoruz.

Ancak modern programlama dillerinde tip sistemleri yalnızca basit seviyede tip kontrolü için kullanılmıyor. Programlama dilleri tip sistemlerinde program hakkında daha detaylı bilgiler toplayıp, bu bilgileri programı optimize etmek için, ya da program üzerinde kısıtlar oluşturmak için kullanabiliyorlar. Misal, Rust programlama dili tip sisteminde programdaki değerlerin sahiplik(ownership) ilişkilerini takip ederek program hafızasını takip eden ek bir çöp toplayıcı(garbage collector) olmadan derleme zamanında hafıza güvenliği(compile-time memory safety) sağlayabiliyor. Rust’ın bu kabiliyeti bu zamana kadar C ve C++’ın neredeyse tamamen sahip olduğu yüksek performanslı programlar alanında ciddi bir kabul görmesini sağladı. Tip sisteminde takip edilen bilgi miktarı arttıkça, tip çıkarımı ihtiyacı büyüyor. Çünkü normal şartlarda bir C programı yazarken programda tanımlanan her değişkenin tipini yazmak basit. Ancak bir Rust programı yazarken programdaki tüm değişken ömrü işaretçilerini(lifetime annotations) elle yazmak mümkün değil, eğer Rust böyle bir efor gerektirseydi, kimse kullanmazdı.

Yalnızca Rust’ın değişken ömrü işaretçileri gibi ileri seviye tip sistemlerinde değil, günlük programlama aktivitelerinde de tip çıkarımı önemli bir rol oynuyor. Programdaki her bir değişken için elle tip işaretçisi yazmak hiçbir programcının çok hoşuna giden bir durum değil. Buna çözüm olarak literatürde pek çok tip çıkarım algoritması var, en ünlüsü de `Hindley-Milner(HM) Type System` ile birlikte ortaya çıkan tip çıkarım algoritması.  Rust, OCaml, Haskell gibi diller HM tip sistemini küçük varyasyonlar ile kullanıyorlar.

## İleri Seviye Tip Sistemleri

Yazıyı, ileri seviye tip sistemlerinden biraz daha bahsederek bitireyim. Bir önceki kısımda Rust’tan bahsettik, Rust tarzı tip sistemlerine kaynak-odaklı tip sistemleri(resource-oriented type systems) deniyor. Bu tarz tip sistemleri programdaki objelerin sahiplik ilişkilerini takip ederek objelerin yanlış kullanımlarını engelliyorlar. Diğer yanda akışkan tipler(liquid types) kullanan sistemler tip üzerinde daha detaylı sınırlamalar oluşturabiliyor. Mesela bir akışkan tip sisteminde `{n | n % 2 == 0}` şeklinde ifade edilen yalnızca çift sayıları içeren bir tipe sahip olabiliyoruz. Liquid Haskell, Flux(Rust) gibi tip sistemleri bu dillerin klasik sistemlerini akışkan hale getirmeye çalışıyor. Diğer yanda bağımlı tipler(Dependent Types) programlama dilleri ve mantık arasındaki bariyerleri indirip, programların aynı zamanda kanıtlama asistanları(proof assistants) olarak kullanılmasına da izin veriyor. Coq, Agda, Lean gibi kanıt asistanları sayesinde doğruluğunu kanıtlayabildiğimiz programlar ve algoritmalar geliştirebiliyoruz. Bunun haricinde bilgi takip kontrolü(IFC-Information Flow Control) bazlı tip sistemleri programlardaki gizli verilerin açığa sızmayacağını kanıtlayabiliyor, aynı zamanda son yıllarda çıkan bazı tip sistemleri programların belirli bir zaman ya da uzay kompleksitesini aşmayacağını kanıtlamak üzerine çalışıyor.

## Kapanış

Başta bahsettiğim gibi, tip sistemleri kullandığımız dillerdeki programlama aktivitelerimizi ciddi miktarda etkiliyor. Hatalı-tipli programlarda aldığımız hata mesajlarından, kendi programlarımızdaki hata durumlarını halletme metotlarımıza(error handling), eşzamanlı programlamaya(concurrent programming) programlama dilleri ile etkileştiğimiz pek çok yüzey dilin tip sisteminden geçiyor. Swift dilinin tip kontrolcüsünün çok-tipli programlardaki tip kontrolü algoritması üssel geri-çekilme(exponential backtracking) uyguladığı için kontrolcü ile uyuşmayan kısa programlar inanılmaz uzun sürede hata verebiliyor, hatta sırf bunun için Swift dilinde hızlı derlenen programlar yazma üzerine teknikler öğretiyor insanlar birbirlerine.

Durum buyken, tip sistemlerinin bu kadar opak ve arka planda kalması, yazdığımız programlarda ortaya çıkan tip hatalarının nasıl ortaya çıktığını çoğu zaman bilmiyor ya da anlamıyor olmamız benim içimde hep üzücü bir gerçek olarak kaldı. Bu sebepten bu yazıyı Türkçe’de yazmak, Türkçe programlama literatürüne yeni bir alan aktarmak istedim. Eğer buraya kadar okuduysanız çok teşekkür ederim.

Sevgiler,  
Alperen Keleş
