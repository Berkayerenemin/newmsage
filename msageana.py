from PyQt5 import QtWidgets, uic, QtGui, QtCore
from PyQt5.QtWidgets import QApplication
import sys
import os
import time
import socket
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QFileDialog, QInputDialog
from PyQt5.QtCore import Qt
import pickle

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('msageana2.ui', self)
        self.satir = self.findChild(QtWidgets.QLineEdit, "lineEdit")
        self.ortamesaj = self.findChild(QtWidgets.QListWidget, "listWidget")
        self.kisilerlist = self.findChild(QtWidgets.QListWidget, "listWidget_3")
        self.odalarlist = self.findChild(QtWidgets.QListWidget, "listWidget_2")
        self.odaacklama = self.findChild(QtWidgets.QLabel, "label")
        self.logo = self.findChild(QtWidgets.QLabel, "label_2")
        self.odaekle = self.findChild(QtWidgets.QPushButton, "pushButton")
        self.cikis = self.findChild(QtWidgets.QPushButton, "pushButton_3")
        self.profile = self.findChild(QtWidgets.QPushButton, "pushButton_4")
        self.addbuton = self.findChild(QtWidgets.QPushButton, "pushButton_2")
        self.buyutme = self.findChild(QtWidgets.QPushButton, "pushButton_5")
        self.cikis.clicked.connect(self.kapat)

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setFocus()
        self.show()

        host = "127.0.0.1"
        port = 25568
        portrroom = 12255
        ADDR = (host,port)
        ADDR2 = (host, portrroom)
        self.client = socket(AF_INET, SOCK_STREAM)
        self.client.connect(ADDR)
        print("25565 numaralı porttan bağlantı sağlandı.")
        self.clientroom = socket(AF_INET, SOCK_STREAM)
        self.clientroom.connect(ADDR2)
        print("12255 numaralı porttan bağlantı sağlandı.")

        receive_thread = Thread(target=self.receive)
        receive_thread.start()
        print("Receive, thread ile bağlantı kurdu.")
        room_thread = Thread(target= self.roomnumber)
        room_thread.start()
        print("Roomnumber, thread ile bağlantı kurdu.")

    def kapat(self):
        print("Kapatma işlemi başlatıldı.")
        self.close()
        quit()

    def photo(self):
        pixmap = QPixmap('msagelogo.png')
        pixmap_resized = pixmap.scaled(600, 1500, QtCore.Qt.KeepAspectRatio)
        self.logo.setPixmap(pixmap_resized)

    def receive(self):

        while True:
            try:
                self.roommsg = self.client.recv(2048).decode("utf8")
                b = 150
                z = 0
                a = len(self.roommsg)
                t = int(round(a/b))
                if t>1:
                    for _ in range(t+1):
                        self.msgnew= self.roommsg[z:b]
                        self.ortamesaj.addItem(self.msgnew)
                        z = b
                        b += 150
                else:
                    self.ortamesaj.addItem(self.roommsg)
            except:
                print("x")

    """def profiledef(self):
        os.system('python msageprofile.py')"""

    def send(self):
        self.msg = self.satir.text()
        self.satir.setText("")
        self.client.send(bytes(self.msg, "utf8"))
        print(self.msg)

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Return:
            self.send()
            print("Enter tuşuna basıldı ve gönderme işlemi başlatıldı.")
    
    def roomnumber(self):
        while True:
            try:
                self.odasayisi = self.clientroom.recv(2048).decode("utf8")
                self.odalarlist.addItem(self.odasayisi)
            except:
                print("Oda listesi alınamadı.")
                #Socket veya uygulama kapatılacak.


app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()