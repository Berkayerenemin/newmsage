# MSAGE #
MSAGE powered by Python3\
MSAGE developed by Berkay Eren EMİN

![forks](https://img.shields.io/github/forks/Berkayerenemin/newmsage)
![stars](https://img.shields.io/github/stars/Berkayerenemin/newmsage)
![msage](https://img.shields.io/github/issues/Berkayerenemin/newmsage)

## MSAGE nedir?

Açık kaynak kodlu, kullanıcıların kendi sunucularına veya MSAGE'in sunucularına bağlanarak yeni odalar kurup arkadaşlarıyla mesajlaştıkları bir uygulamadır. GNU Lisansı ile lisanslanmıştır.

---
### MSAGE / Geliştirmeler

2019 yılının Ağustos ayında son Commit'i yapılan **eski** MSAGE uygulaması hakkında yapılan geliştirmeler ve yapılacak geliştirmeler hakkında yol haritası:

**Altyapı Değişiklikleri:**

Eski ve tek bir uygulama üzerinden çalışan sistem 3 farklı uygulama halinde paket bir yapı halini aldı. Bu paket içerisindeki 3 uygulama sırasıyla; *Starter, New User, Msage*

Buna ek olarak güncelleme sistemi getirildi. Böylelikle uygulamanın sürdürülebilirliği ve erişim kolaylığı arttırıldı. 

>Ayrıca paket içerisindeki 3 uygulama; kullanıcının yaptığı işlemlerin, uygulama tarafından kontrolünü de arttırmıştır.

**Tasarımsal Değişiklikler:**

Eskiden tek bir uygulama üzerinden *Tab'lar* üzerinden dolaşılan ve tasarımı 1900'lerden kalma MSAGE'şimdi açık bir ton kullanılarak yapılan tasarımsal hatlara sahip. 

>Dil değişikliği ve gece/gündüz özelliği eklenecektir.

Yapılan tasarım daha soft olmakla birlikte modernliğin getirdiği özellikleri de barındırmakta. Yeni kullanıcı giriş sayfasındaki *Hakkında* ve *Neden İstiyoruz?* kısımları eski uygulamanın aksine daha modern tarzda konumlandırıldı. Bunun dışında ana uygulamada bulunan kullancı ve oda isimlerinin bulunduğu kısımlar değiştirilmiş olup eskiden metinsel şekilde olan bazı *-özel mesaj ve odaya katılma-* özellikler grafiksel yetenekler sayesinde modernize edilmiştir.

Buna ek olarak bulunan odanın ismi ve ayrıntılarını içeren bir kısım da üst tarafa eklenmiş olup, uygulamadaki tüm butonlar yeniden revize edilmiştir. 

---
### Msage / Eklenecek Özellikler

- Mesajlar için şifreleme sistemi
- Ekran paylaşma özelliği
- Odalardaki deneyimi geliştirmeye yönelik işlemler
- MacOs, Linux, IOS ve Android için uygulama 
- Ek profil özellikleri
---
### Kurulum ve Daha Fazlası

Tüm dosyalar Python 3.9.6 ile yazılmıştır ve 01.09.2021 tarihine içerdiği kütüphanelerin en güncel sürümü kullanılmıştır.

İçerdiği kütüphaneler:

- Server:
```
socket
threading
pickle
os
```
- Starter:
```
PyQt5
sys
os
socket
threading
pickle
subprocess
```
- Updater:
```
sys
os
socket
subprocess
```
- New User
```
PyQt5
os
socket
pickle
```
- Msage
```
PyQt5
sys
socket
threading
```
>Uygulamayı çalıştırmak için öncelikle serverı (*msgsw.py*) çalıştırmak gerekmektedir. Sunucu tarafında tüm işlemler bu kadardır. Kullanıcı tarafında gerekli işlemleri başlatabilmek için starterı (*starter.py*) çalıştırmak gerekmektedir. 
---

### Update Mekanizması

Update mekanizması sunucu ve kullanıcı olmak üzere iki kısımdan çalışmaktadır. Serverda -*msgsw.py*- 108. satırda starter adlı soketin gönderdiği numara değeri versiyon bilgisini içermektedir. (01.09.2021)

Kullanıcı tarafında ise Starterda -*starter.py*- 72. satırda bulunan c2 isimli soket üzerinden alınan data ise sunucudan gelen versiyon bilgisidir. Eğer sunucudaki belirtilen versiyon starterdaki versiyondan büyük ise güncelleme gerekmektedir.

Buna göre update mekanizmasını çalıştırabilirsiniz.

---
### oto.txt Dosyası Hakkında
oto.txt dosyası yeni kullanıcı için giriş sayfasından sonra oluşmaktadır. Bu txt dosyası kullanıcının şifre, isim ve bazı profil bilgilerini içermektedir. Bu dosyanın tamamı sunucuya hiçbir şekilde gönderilmemektedir. Kullanıcının ilk girişinin ardından tekrar uygulamayı açtığında otomatik olarak bilgilerinin belirli bir kısmınının sunucuya gönderilmesi için tutulmaktadır. 

Bu dosyada erişimi olan diğer dosyalar:

- starter.py
- newuser.py
---
### .ui Dosyaları Hakkında

.ui dosyaları PyQt5 kütüphanesi ile ilgilidir ve tamamen tasarım odaklı hazırlanmıştır. Tüm .ui dosyaları Qt Designer ile tasarlanmıştır. 

---
## What is MSAGE?
It is an open source application where users can connect to their own servers or to MSAGE's servers, set up new rooms and chat with friends. Licensed with GNU License.

![MsageLogo](https://github.com/Berkayerenemin/msage/blob/master/MSAGE.png)

