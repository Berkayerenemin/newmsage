from PyQt5 import QtWidgets, uic, QtGui, QtCore
from PyQt5.QtWidgets import QApplication
import sys
import os
import time
import socket
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import pickle

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('starter.ui', self)
        self.giflabel = self.findChild(QtWidgets.QLabel, "label")
        #self.progressbar = self.findChild(QtWidgets.QProgressBar, "progressBar")
        self.logolabel = self.findChild(QtWidgets.QLabel, "label_2")
        self.uptlabel = self.findChild(QtWidgets.QLabel, "label_8")
        self.start = 0
        #self.progressbar.setValue(self.start)
        self.version = "v1a"
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setFocus()
        #self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.show()
        print("Widgetlar oluşturuldu.")
        self.movie()
        print("Gif çalışması başlatıldı.")
        self.progress()
        print("Progress bar başlatıldı.")
        self.baslat()
        print("Bağlantı kurulma izni verildi.")

        
    def movie(self):
        self.movie = QtGui.QMovie("shodaw.gif")
        size = QtCore.QSize(150, 150)
        self.movie.setScaledSize(size)
        self.giflabel.setMovie(self.movie)
        QApplication.processEvents()
        self.movie.start()
        print("Gif sorunsuz çalışmakta.")

    def progress(self):
        self.completed = 0
        while self.completed < 10:
            QApplication.processEvents()
            self.completed += 0.0005
            print(self.completed)
        print("Progress bar tammalandı.")


    def baslat(self):
        host = "127.0.0.1"
        port = 25565
        print("Starter için adresler belirlendi.")
        addr = (host, port)
        c2 = socket(AF_INET, SOCK_STREAM)
        c2.connect(addr)
        print("Starter gerekli adrese bağlandı.")
        data = c2.recv(2048).decode("utf8")
        print(data)
        if data > "1":
            time.sleep(2)
            print("Versiyon eski, yeni dosya alınacak.")
            c2.send("outofdate".encode("utf"))
            pass
            #updater yapıldıktan sonra yazılacaktır.
        else:
            print("Versiyon güncel.")
            c2.send("update".encode("utf8"))
            try:
                otologin = open("oto.txt", "r")
                print("Otomatik login için giriş bilgilerini kaydettiği dosyayı aramakta.")
            except FileNotFoundError:
                print("Öyle bir dosya yok.")
                c2.send("yenigiris".encode("utf8"))
                print("Sunucuya yeni bir kullanıcı girişi olduğu belirtildi.")
                self.close()
                print("GUI kapatıldı.")
                c2.close()
                print("Starter'ın bağlantı soketi kapatıldı.")
                os.system('python newuser.py')
                quit()
                #Yeni kullanıcı için gerekli sayfa açılıyor.

            c2.send("otogiris".encode("utf8"))
            port2 = 25566
            addr2 = (host, port2)
            c = socket(AF_INET, SOCK_STREAM)
            c.connect(addr2)
            print("Otogiriş bilgileri gönderilmesi için yeni bir porta bağlanıldı.")
            login = otologin.read() 
            print("Otogiriş dosyası okunuyor.")
            uye = login.split(",")
            uye.pop()
            print(uye)
            self.dataprofil = pickle.dumps(uye)
            c.send(self.dataprofil)
            print("Kullanıcı bilgileri sunucuya gönderildi.")
            self.close()
            os.system('python msageana.py')


app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()
