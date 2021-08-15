import socket 
import threading 
import time
import json
import sqlite3
import pickle

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s3 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s4 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s5 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sunucuCalısıyor = True
print("Sunucu hatasız açıldı.")

ip = "127.0.0.1"
port = 25565
port1 = 25566
port2 = 25567
port3 = 25568
portodasayisi = 12255
portkullanicisayisi = 13255
print("İp ve portlar belirlendi.")

app = {}
app["anaoda"] = {}
baglantılar = []
kullaniciprofilleri=[]

s.bind((ip, port))
s1.bind((ip,port1))
s2.bind((ip,port2))
s3.bind((ip,port3))
s4.bind((ip, portodasayisi))
s5.bind((ip, portkullanicisayisi))
print("Bağlantılar dinlemeye alındı.")

"""with sqlite3.connect('quit.db') as db:
    c = db.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS msg (id INTEGER NOT NULL ,message TEXT NOT NULL);')
    c.execute('CREATE TABLE IF NOT EXISTS user (id INTEGER NOT NULL ,username TEXT NOT NULL ,email TEXT NOT NULL ,acıklama TEXT NOT NULL);')
    db.commit()
print("Database ve gerekli tablolar oluşturuldu.")"""

def resimfoto():
    f = open(kullaniciadi+".jpg", "wb")
    data = clientprofil.recv(1024)
    if not data:
        print("Data yok")
        pass
    else:
        f.write(data)
    f.close()
print("Karşıdan resim alma ve olduğu alana yazma fonksiyonu tanımlandı.")

def hall(client, kullaniciadi, app, clientCalisiyor):
    while clientCalisiyor:
        mesaj = client.recv(1024).decode("utf8")
        mesaj2 = str(kullaniciadi)+" : "+mesaj
        print(mesaj2)
        name = list(app["anaoda"].keys())
        print(app["anaoda"].items)
        print(app["anaoda"].keys())
        print(name)

        try:
            for k,v in app["anaoda"].items():
                v.send(mesaj2.encode("utf8")) 
        except:
            print("Mesaj alımı-gönderiminde bir hata oluştu.")


def roomnumbersend(roomclient, app, clientCalisiyor):
    numberroom = list(app.keys())
    print(numberroom)
    mesaj3 ="\n".join(numberroom)
    print(mesaj3)
    roomclient.send(mesaj3.encode("utf8"))

def kullanicinumber(usernclient, app, clientCalisiyor, anaodadamı, odaadi):
    if anaodadamı == True:
        name = list(app["anaoda"].keys())
        mesaj4="\n".join(name)
        usernclient.send(mesaj4.encode("utf8"))
    else:
        nameroom = list(app[odaadi].keys())
        mesaj5="\n".join(baglantılar)
        usernclient.send(mesaj5.encode("utf8"))


while sunucuCalısıyor:
    try:
        s.listen()
        starter,address = s.accept()
        print("Bağlanan starter ile bağlantı kuruldu.")
        print(starter)
        print(address)
        starter.send("1".encode("utf8"))
        print("Versiyon bilgisi gönderildi.")
        update= starter.recv(1024).decode("utf8")
        if update == "update":
            print("Bağlanan client güncel.")
            bilgi = starter.recv(1024).decode("utf8")
            if bilgi == "yenigiris":
                print("Yeni giriş yapılacak.")
                s1.listen()
                print("Bilgilerin gönderileceği soket bağlantıları dinliyor.")
                try:
                    newuser,addresss2 = s1.accept()
                    print("Yeni giriş sayfası ile bağlantı kuruldu.")
                except:
                    print("Bağlantı kurulmadı.")
                    s.close()
                    s1.close()
                try:
                    a = newuser.recv(2048)
                    data = pickle.loads(a)
                    print(data)
                    kullaniciadi = data[2]
                    print("Kullanıcı giriş verileri alındı.")
                except:
                    print("Kullanıcı giriş verileri alınamadı.")
                    pass
                    #Bağlanan soket kapatılacak.
                print(kullaniciadi)
                baglantılar.append(kullaniciadi)
                print(baglantılar)
                print("Kullanıcı profili listesine kullanıcı adı yazıldı.")
                clientCalisiyor = True
                print("Kullanıcı ana programı çalışıyor.")
                s3.listen()
                client,address3 = s3.accept()
                print(client)
                s4.listen()
                roomclient,address4 = s4.accept()
                app["anaoda"][kullaniciadi] = client
                threading.Thread(target = hall, args = (client, kullaniciadi, app, clientCalisiyor)).start()
                roomnumberthread = threading.Thread(target = roomnumbersend, args = (roomclient, app, clientCalisiyor))
                roomnumberthread.start()
                usernumberthread = threading.Thread(target = kullanicinumber, args = (usernclient, app, clientCalisiyor, anaodadamı, False))
                usernumberthread.start()
            elif bilgi == "otogiris":
                s1.listen()
                print("Bilgilerin gönderileceği soket bağlantıları dinliyor.")
                try:
                    olduser,addresss2 = s1.accept()
                    print("Otogiriş için bağlantı kuruldu.")
                except:
                    print("Bağlantı kurulamadı. (Otogiriş)")
                    s.close()
                    s1.close()
                try:
                    a2 = olduser.recv(2048)
                    data = pickle.loads(a2)
                    print(data)
                    kullaniciadi = data[2]
                    print("Kullanıcı giriş verileri alındı.")
                except:
                    print("Kullanıcı giriş verileri alınamadı.")
                    pass
                    #Bağlanan soket kapatılacak.
                print(kullaniciadi)
                baglantılar.append(kullaniciadi)
                print(baglantılar)
                print("Kullanıcı profili listesine kullanıcı adı yazıldı.")
                clientCalisiyor = True
                print("Kullanıcı ana programı çalışıyor.")
                s3.listen()
                client,address3 = s3.accept()
                anaodadamı = True
                print(client)
                s4.listen()
                roomclient,address4 = s4.accept()
                s5.listen()
                usernclient,address5 = s5.accept()
                app["anaoda"][kullaniciadi] = client
                threading.Thread(target = hall, args = (client, kullaniciadi, app, clientCalisiyor)).start()
                roomnumberthread = threading.Thread(target = roomnumbersend, args = (roomclient, app, clientCalisiyor))
                roomnumberthread.start()
                usernumberthread = threading.Thread(target = kullanicinumber, args = (usernclient, app, clientCalisiyor, anaodadamı, False))
                usernumberthread.start()
            else:
                pass

        else:
            #Bu kısım updater yapıldıktan sonra yazılacaktır.
            file1=open("starter.py","rb").read()
            file2=open("starter.ui", "rb").read()
            file3=open("newuser.py", "rb").read()
            file4=open("msagenewuser.ui", "rb").read()
            #update.sendall(file)
            #print("Starter için py dosyası gönderildi.")
            #time.sleep(15)
            #update.sendall(file2)
            #print(Starter için yükleme tamamlandı.

            
    except:
        print("Bağlantı hatası.")
        break