# Güvercin Yuvası İlkesi

Gauss'un fikrine göre güvercin beslediğimizi düşünürsek, her akşam yuvalarına dönecek güvercinlerimiz var demektir. Eğer güvercinlerimizin sayısı (n) yuva sayısından (m) fazla ya da büyük eşit ise en az bir yuvada birden fazla güvercin olacaktır.

* ---> Güvercin Yasası Prensibine göre n güvercin sayısı ve m güvercin yuvası sayısı olmak üzere n>m durumunda bir güvercin yuvasında mutlaka birden fazla güvercin bulunmalıdır.

![](https://raw.githubusercontent.com/yildirimyy/pigeonhole-principle/master/screen/pigeon.jpg) 

## Örnek:

```
n = 5 güvercin, m = 4 yuva dersek;
En az bir yuva ⎡6/5⎤ güvercin bulundurur.
n ≤ m olma durumunda bile en az 1 güvercin olacaktır.

```

## Problem:
Bir torba 10 adet beyaz, 10 adet kırmızı ve 10 adet de mavi top bulunmaktadır. Bu torbadan rastgele seçilen toplardan 4 tanesinin aynı renk olması için toplamda kaç adet top seçilmesi gerekmektedir?

#### Çözüm:
```
Renk sayısına güvercin yuvası sayısı = 3 dersek;
Toplara da güvercin sayısı = 4 dersek;
10 tane rastgele şekilde top çekmemiz durumunda 4 adet top aynı renk olur.
⎡10/3⎤ = 4
```

![](https://raw.githubusercontent.com/yildirimyy/pigeonhole-principle/master/screen/ball_screen.png) 

## Problem:
Güvercin Yuvası İlkesinin Kullanımı ile π Sayısının Rasyonel Bir Yaklaşımı

#### Çözüm:
```
Bize 0π’den 1000π’ye kadar sayıların çarpımları verilmiş olsun. (0π = 0, 1π = 3.1415, 2π = 6.2831, ...) 
(Sayının ondalık basamağındaki ilk 3 sayı dikkate alınacak)

0’dan 1000’e kadar π’nin katları verildiğinde ilk 3 basamağın aynı olması için 1000 ihtimal vardır.
1001π verilirse Güvercin Yuvası İlkesinden yola çıkarak 2 çarpımın virgülden sonraki 3 hanesinin aynı olması gerektiği sonucuna varırız. 

m ve n’e virgülden sonraki 3 basamağın aynı olduğu sayılar ve m>n dersek;

mpi – npi = (m-n)pi --> pi = (mpi – npi) / (m-n)
Bu nedenle bu yöntem π'nin rasyonel bir yaklaşımı olarak kullanılabilir.
```

![](https://raw.githubusercontent.com/yildirimyy/pigeonhole-principle/master/screen/pi_screen.png) 


## See Also:
* http://louisrli.github.io/blog/2013/01/31/approximating-pi-pigeonhole-principle/
* https://www.geeksforgeeks.org/discrete-mathematics-the-pigeonhole-principle/
* https://www.geeksforgeeks.org/python-program-for-pigeonhole-sort/
* http://bilgisayarkavramlari.sadievrenseker.com/2009/12/10/guvercin-yuvasi-kaidesi-pigeonhole-principle/
* https://www.matematiksel.org/guvercin-yuvasi-prensibi/

## Authors

* *Yağmur Yıldırım* - [PigeonHolePrinciple](https://github.com/yildirimyy/pigeonhole-principle)


## License

[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.mit-license.org)

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
