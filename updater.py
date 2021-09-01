import sys
import os
import time
import socket
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import pickle
import subprocess

host = "127.0.0.1"
port = 25569
addr = (host, port)
s = socket(AF_INET, SOCK_STREAM)
s.connect(addr)

os.remove("starter.py")
os.remove("newuser.py")
os.remove("msageana.py")
bilgi = "0"

print("Dosyalar silindi.")

s.send(bytes(bilgi, "utf8"))
size = s.recv(1024)
print(int(size))

f = open("starter.py","wb")
text = "Sunucudan bazı ikramlar almaktayız."
#self.infolabel.setText(text)

datasize = 0
nowsize = 0

while True:
    data = s.recv(2048)
    print("Starter verisi alınıyor.")
    nowsize = int(len(data))
    datasize = datasize + nowsize
    print("Soketten alınan data boyutu: ", nowsize)

    if datasize <= int(size):
        f.write(data)
        print("Yazıdırılan data boyutu: ", datasize)
        print("Dosya hala alınacak.")
        pass

    if int(datasize) == int(size):
        print("Dosya tammalandı.")
        print(datasize)
        break

f.close()

text = "İkramları afiyetle yedik."
#self.infolabel.setText(text)
#time.sleep(15)

print("Starter için gereken veriler alındı.")

bilgi = "1"
s.send(bytes(bilgi, "utf8"))

size = s.recv(1024)
print(int(size))

f = open("newuser.py","wb")
datasize = 0
nowsize = 0
text = "Sunucudaki odaları gezioruz."

#self.infolabel.setText(text)
while True:
    data2 = s.recv(2048)
    print("Yeni kullanıcı sayfası verisi alınıyor.")
    nowsize = int(len(data2))
    datasize = datasize + nowsize
    print("Soketten alınan data boyutu: ", nowsize)

    if datasize <= int(size):
        f.write(data2)
        print("Yazıdırılan data boyutu: ", datasize)
        print("Dosya hala alınacak.")
        pass

    if int(datasize) == int(size):
        print("Dosya tammalandı.")
        print(datasize)
        break

f.close()

text = "Gezmekten yorulduk."
#self.infolabel.setText(text)
#time.sleep(10)

print("Yeni giriş sayfası için gerekli bilgiler alındı.")
bilgi = "2"

s.send(bytes(bilgi, "utf8"))
size = s.recv(1024)
print(int(size))

f = open("msageana.py","wb")
datasize = 0
nowsize = 0

text = "Manzara eşliğinde yemek yiyoruz."
#self.infolabel.setText(text)

while True:
    data3 = s.recv(4096)
    print("Ana giriş verisi alınıyor.")
    nowsize = int(len(data3))
    datasize = datasize + nowsize
    print("Soketten alınan data boyutu: ", nowsize)

    if datasize <= int(size):
        f.write(data3)
        print("Yazıdırılan data boyutu: ", datasize)
        print("Dosya hala alınacak.")
        pass

    if int(datasize) == int(size):
        print("Dosya tammalandı.")
        print(datasize)
        break

f.close()
text = "Karınlarımızı doldurduk ve geri dönüyoruz."
#self.infolabel.setText(text)
#time.sleep(10)
bilgi = "3"
s.send(bytes(bilgi, "utf8"))
s.close()
subprocess.Popen("python starter.py")
quit()