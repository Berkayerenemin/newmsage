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
        self.progressbar = self.findChild(QtWidgets.QProgressBar, "progressBar")
        self.start = 0
        self.progressbar.setValue(self.start)
        self.version = "v1a"
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
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
        size = QtCore.QSize(200, 161)
        self.movie.setScaledSize(size)
        self.giflabel.setMovie(self.movie)
        QApplication.processEvents()
        self.movie.start()
        print("Gif sorunsuz çalışmakta.")

    def progress(self):
        self.completed = 0
        while self.completed < 100:
            QApplication.processEvents()
            self.completed += 0.0005
            self.progressbar.setValue(self.completed)
        print("Progress bar tammalandı.")


    def baslat(self):
        host = "127.0.0.1"
        port = 25565
        print("Starter için adresler belirlendi.")
        addr = (host, port)
        c2 = socket(AF_INET, SOCK_STREAM)
        c2.connect(addr)
        print("Starter gerekli adrese bağlandı.")
        c2.send(self.version.encode("utf8"))
        data = c2.recv(2048).decode("utf8")
        print(data)
        if data > "1":
            time.sleep(2)
            print("Versiyon eski, yeni dosya alınacak.")
        else:
            print("Versiyon güncel.")
            try:
                otologin = open("oto.txt", "r")
                print("Otomatik login için giriş bilgilerini kaydettiği dosyayı aramakta.")
            except FileNotFoundError:
                print("Öyle bir dosya yok.")
                #c2.send("yenigiris".encode("utf8"))
                print("Sunucuya yeni bir kullanıcı girişi olduğu belirtildi.")
                self.close()
                os.system('python newuser.py')
            c2.send("Otogiris".encode("utf8"))
            port = 25565
            addr2 = (host, port)
            c = socket(AF_INET, SOCK_STREAM)
            c.connect(addr2)
            login = otologin.read()
            uye = login.split(",")
            uye.pop()
            print(uye)
            self.dataprofil = pickle.dumps(uye)
            c.send(self.dataprofil)
            self.close()
            os.system('python msageana.py')


app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()