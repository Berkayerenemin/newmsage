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

sunucuCalısıyor = True
print("Sunucu hatasız açıldı.")

ip = "127.0.0.1"
port = 25565
port1 = 25566
port2 = 25567
port3 = 25568
print("İp ve portlar belirlendi.")

app = {}
app["anaoda"] = {}
baglantılar = []
kullaniciprofili = []

s.bind((ip, port))
s1.bind((ip,port1))
s2.bind((ip,port2))
s3.bind((ip,port3))
print("Bağlantılar dinlemeye alındı.")

with sqlite3.connect('data/quit.db') as db:
    c = db.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS msg (id INTEGER NOT NULL ,message TEXT NOT NULL);')
    c.execute('CREATE TABLE IF NOT EXISTS user (id INTEGER NOT NULL ,username TEXT NOT NULL ,email TEXT NOT NULL ,acıklama TEXT NOT NULL);')
    db.commit()
print("Database ve gerekli tablolar oluşturuldu.")

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
            bilgi = update.recv(1024).decode("utf8")
            if bilgi == "yenigiris":
                s1.listen()
                print("Bilgilerin gönderileceği soket bağlantıları dinliyor.")
                pass
            elif bilgi == "otogiris":
                s1.listen()
                print("Bilgilerin gönderileceği soket bağlantıları dinliyor.")
                pass
            else:
                pass

        else:
            #Bu kısım updater yapıldıktan sonra yazılacaktır.
            file1=open("starter.py","rb").read()
            file2=open("widgets/starter.ui", "rb").read()
            file3=open("newuser.py", "rb").read()
            file4=open("widgets/msagenewuser.ui", "rb").read()
            #update.sendall(file)
            #print("Starter için py dosyası gönderildi.")
            #time.sleep(15)
            #update.sendall(file2)
            #print(Starter için yükleme tamamlandı.)

            
    except:
        print("Bağlantı hatası.")
        break