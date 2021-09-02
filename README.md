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
### MSAGE / Eklenecek Özellikler

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

---
### MSAGE / Enhancements

The roadmap for the developments and improvements to be made on the August 2019 application:

**Infrastructure Changes**

The old system, which works through a single application, has become a package structure in 3 different applications. The 3 applications in this package are respectively; Startup, New User, Msage

In addition, the update system was introduced. Thus, the sustainability and ease of access of the application was increased.

>In addition, 3 applications in the package, increased the control of the user's actions by the application.

**Design Changes**

MSAGE, whose design dates back to 1900 and which used to be navigated through *Tabs* through a single application, now has design lines made using a light tone.

> Language change and day/night feature will be added.

Although the design is softer, it also contains the features brought by modernity. *About* and *Why Do We Want It?* on the new user login page parts of it are positioned in a more modern style, unlike the old practice. Apart from this, the sections with user and room names in the main application have been changed, and some *-private message and room-joining-* features that used to be textual have been modernized thanks to graphical capabilities.

In addition, a section containing the name and details of the room found has been added to the top, and all the buttons in the application have been revised.

---

### MSAGE / Features to Add

- Encryption system for messages
- Screen sharing feature
- Actions to improve the experience in rooms
- App for MacOs, Linux, IOS and Android
- Additional profile features

---

### Setup and More

All files were written in Python 3.9.6 and the most up-to-date version of the libraries included as of 01.09.2021 was used.

Libraries included:

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

>To run the application, it is necessary to run the server (*msgsw.py*) first. That's enough for the server side. It is necessary to run the starter (*starter.py*) in order to start the necessary operations on the user's side.

---

### Update Mechanism

The update mechanism works in two parts, the server and the user. On the server -*msgsw.py*- On line 108, the number value sent by the socket named starter contains the version information. (01.09.2021)

On the user side, the data received over the socket named c2 in the Starter -*starter.py*- line 72 is the version information coming from the server. If the specified version on the server is greater than the version on the starter, an update is required.

Accordingly, you can run the update mechanism.

---

### About oto.txt File

The auto.txt file is created after the login page for the new user. This txt file contains the user's password, name and some profile information. This entire file is not sent to the server in any way. When the user opens the application again after the first login, a certain part of the information is automatically kept to be sent to the server.

Other files with access in this file:

- starter.py
- newuser.py

---

### About .ui Files

The .ui files are related to the PyQt5 library and are purely design-oriented. All .ui files are designed with Qt Designer.

---

Logo:

![MsageLogo](https://github.com/Berkayerenemin/msage/blob/master/MSAGE.png)

