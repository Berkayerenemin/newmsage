import socket 
import threading 
import time
import json
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
s.listen()
s1.listen()
s2.listen()
s3.listen()
s4.listen()
s5.listen()
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
    starter,address = s.accept()
    print("Bağlanan starter ile bağlantı kuruldu.")
    print(starter,address)
    starter.send("1".encode("utf8"))
    print("Versiyon bilgisi gönderildi.")
    update= starter.recv(1024).decode("utf8")
    if not update:
        print("Starterdan herhangi bir başlangıç verisi alınamadı.")
    else:
        if update == "update":
            print("Bağlanan client güncel.")
            bilgi = starter.recv(1024).decode("utf8")
            if not bilgi:
                print("Kullanıcının giriş türü ile ilgili bir bilgi alamadık.")
            else:
                if bilgi == "yenigiris":
                    print("Yeni giriş yapılacak.")
                    newuser,addresss2 = s1.accept()
                    a = newuser.recv(2048)
                    if not a:
                        print("Kullanıcı giriş verileri alınamadı.")
                    else:
                        data = pickle.loads(a)
                        print(data)
                        kullaniciadi = data[2]
                        print("Kullanıcı giriş verileri alındı.")
                        print(kullaniciadi)
                        baglantılar.append(kullaniciadi)
                        print(baglantılar)
                        print("Kullanıcı profili listesine kullanıcı adı yazıldı.")
                        clientCalisiyor = True
                        print("Kullanıcı ana programı çalışıyor.")
                        client,address3 = s3.accept()
                        roomclient,address4 = s4.accept()
                        usernclient,address5 = s5.accept()
                        app["anaoda"][kullaniciadi] = client
                        anaodadamı = True
                        threading.Thread(target = hall, args = (client, kullaniciadi, app, clientCalisiyor)).start()
                        roomnumberthread = threading.Thread(target = roomnumbersend, args = (roomclient, app, clientCalisiyor))
                        roomnumberthread.start()
                        usernumberthread = threading.Thread(target = kullanicinumber, args = (usernclient, app, clientCalisiyor, anaodadamı, False))
                        usernumberthread.start()
                elif bilgi == "otogiris":
                    olduser,addresss2 = s1.accept()
                    print("Otogiriş için bağlantı kuruldu.")
                    a2 = olduser.recv(2048)
                    if not a2:
                        print("Kullanıcı giriş verileri alınamadı.")
                    else:
                        data = pickle.loads(a2)
                        print(data)
                        kullaniciadi = data[2]
                        print("Kullanıcı giriş verileri alındı.")
                        print(kullaniciadi)
                        baglantılar.append(kullaniciadi)
                        print(baglantılar)
                        print("Kullanıcı profili listesine kullanıcı adı yazıldı.")
                        clientCalisiyor = True
                        print("Kullanıcı ana programı çalışıyor.")
                        client,address3 = s3.accept()
                        roomclient,address4 = s4.accept()
                        usernclient,address5 = s5.accept()
                        app["anaoda"][kullaniciadi] = client
                        anaodadamı = True
                        threading.Thread(target = hall, args = (client, kullaniciadi, app, clientCalisiyor)).start()
                        roomnumberthread = threading.Thread(target = roomnumbersend, args = (roomclient, app, clientCalisiyor))
                        roomnumberthread.start()
                        usernumberthread = threading.Thread(target = kullanicinumber, args = (usernclient, app, clientCalisiyor, anaodadamı, False))
                        usernumberthread.start()
                else:
                    print("Giriş bilgisi yanlış.")
        elif update == "outofdate":
            #update ile ilgili veri gönderilecek.
            pass

        else:
            print("Böyle bir client yok veya değiştirilmiş.")
            pass

        
        


                    


