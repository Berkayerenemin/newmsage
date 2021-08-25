from PyQt5 import QtWidgets, uic, QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QMenu, QFileDialog, QInputDialog
from PyQt5.QtCore import Qt, QEvent, QPoint, QThread, pyqtBoundSignal, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap
import sys
import os
import time
import socket
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import pickle

class Conn():
    host = "127.0.0.1"
    port = 25568
    portrroom = 12255
    userrroom = 13255
    ADDR = (host,port)
    ADDR2 = (host, portrroom)
    ADDR3 = (host, userrroom)

    client = socket(AF_INET, SOCK_STREAM)
    client.connect(ADDR)
    print("25565 numaralı porttan bağlantı sağlandı.")
    clientroom = socket(AF_INET, SOCK_STREAM)
    clientroom.connect(ADDR2)
    print("12255 numaralı porttan bağlantı sağlandı.")
    usernroom = socket(AF_INET, SOCK_STREAM)
    usernroom.connect(ADDR3)
    print("13255 numaralı porttan bağlantı sağlandı.")

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('msageana2.ui', self)
        self.Receiver = Receive()
        self.Room = RoomN()
        self.User = UserN()
        self.satir = self.findChild(QtWidgets.QLineEdit, "lineEdit")
        self.ortamesaj = self.findChild(QtWidgets.QListWidget, "listWidget")
        self.kisilerlist = self.findChild(QtWidgets.QListWidget, "listWidget_3")
        self.odalarlist = self.findChild(QtWidgets.QListWidget, "listWidget_2")
        self.kisilerlist.installEventFilter(self)
        self.odalarlist.installEventFilter(self)
        self.sayfadegistirme = self.findChild(QtWidgets.QStackedWidget, "stackedWidget")
        self.odaacklama = self.findChild(QtWidgets.QLabel, "label")
        self.logo = self.findChild(QtWidgets.QLabel, "label_2")
        self.odaekle = self.findChild(QtWidgets.QPushButton, "pushButton")
        self.cikis = self.findChild(QtWidgets.QPushButton, "pushButton_3")
        self.dahafazla = self.findChild(QtWidgets.QPushButton, "pushButton_4")
        self.addbuton = self.findChild(QtWidgets.QPushButton, "pushButton_2")
        self.buyutme = self.findChild(QtWidgets.QPushButton, "pushButton_5")

        self.Receiver.msg_signal.connect(lambda data: self.ortamesaj.addItem(str(data)))
        self.Room.msg_signal_2.connect(lambda data2: self.odalarlist.addItem(str(data2)))
        self.User.msg_signal_3.connect(lambda data3: self.kisilerlist.addItem(str(data3)))

        self.cikis.clicked.connect(self.kapat)
        self.dahafazla.clicked.connect(self.sfdeg)
        print(self.sayfadegistirme.currentIndex())
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.Receiver.start()
        self.Room.start()
        self.User.start()

        self.client = Conn.client

        self.setFocus()
        self.show()

    def eventFilter(self, source, event):
        if event.type() == QEvent.ContextMenu and source is self.odalarlist:
            menu = QMenu()
            menu.addAction("Odaya Katıl")

            #Eğer herhangi bir odada ise odadan çık komutu eklenecek.

            if menu.exec_(event.globalPos()):
                print("Basıldı")
        
            return True
        return super().eventFilter(source, event)

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint (event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Return:
            self.send()
            print("Enter tuşuna basıldı ve gönderme işlemi başlatıldı.")
    
    def send(self):
        self.msg = self.satir.text()
        self.satir.setText("")
        self.client.send(bytes(self.msg, "utf8"))

    def sfdeg(self):
        self.sayfadegistirme.setCurrentWidget(self.page_2)
        if self.sayfadegistirme.currentIndex() == 1:
            self.dahafazla.setText("Ana Sayfa")
            #Tekrardan ana sayfaya dönmek gerekecek.
        else:
            pass

    def kapat(self):
        print("Kapatma işlemi başlatıldı.")
        self.close()
        quit()

    def photo(self):
        pixmap = QPixmap('msagelogo.png')
        pixmap_resized = pixmap.scaled(600, 1500, QtCore.Qt.KeepAspectRatio)
        self.logo.setPixmap(pixmap_resized)
        



class Receive(QThread):

    msg_signal = pyqtSignal(str)

    def __init__(self):
        QThread.__init__(self)
        self.client = Conn.client

    def run(self):
        while True:
            self.msg = self.client.recv(2048).decode("utf8")
            if not self.msg:
                print("Mesaj alınamadı.")
            else:
                #self.ortamesaj.addItem(self.msg)
                self.msg_signal.emit(self.msg)

    def stop(self):
        print('Stopping thread...')
        self.terminate()




class RoomN(QThread):

    msg_signal_2 = pyqtSignal(str)

    def __init__(self):
        QThread.__init__(self)
        self.clientnroom = Conn.clientroom

    def run(self):
        while True:
            try:
                self.odasayisi = self.clientnroom.recv(2048).decode("utf8")
                print(self.odasayisi)
                #self.odalarlist.addItem(self.odasayisi)
                self.msg_signal_2.emit(self.odasayisi)
            except:
                print("Oda listesi alınamadı.")
                #Socket veya uygulama kapatılacak.

    def stop(self):
        print('Stopping thread...')
        self.terminate()




class UserN(QThread):

    msg_signal_3 = pyqtSignal(str)

    def __init__(self):
        QThread.__init__(self)
        self.usernroom = Conn.usernroom

    def run(self):
        while True:
            try:
                self.kullanicisayisi = self.usernroom.recv(2048).decode("utf8")
                print(self.kullanicisayisi)
                #self.kisilerlist.addItem(self.kullanicisayisi)
                self.msg_signal_3.emit(self.kullanicisayisi)
            except:
                print("Kişi listesi alınamadı.")
                #Socket veya uygulama kapatılacak.

    def stop(self):
        print('Stopping thread...')
        self.terminate()



app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()