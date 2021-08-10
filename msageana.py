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
        uic.loadUi('msageana.ui', self)
        self.satir = self.findChild(QtWidgets.QLineEdit, "lineEdit")
        self.ortamesaj = self.findChild(QtWidgets.QListWidget, "listWidget")
        self.kisilerlist = self.findChild(QtWidgets.QListWidget, "listWidget_3")
        self.odalarlist = self.findChild(QtWidgets.QListWidget, "listWidget_2")
        self.odaacklama = self.findChild(QtWidgets.QLabel, "label")
        self.odaekle = self.findChild(QtWidgets.QPushButton, "pushButton")
        self.cikis = self.findChild(QtWidgets.QPushButton, "pushButton_3")
        self.profile = self.findChild(QtWidgets.QPushButton, "pushButton_4")
        self.addbuton = self.findChild(QtWidgets.QPushButton, "pushButton_2")
        self.odakatil = self.findChild(QtWidgets.QPushButton, "pushButton_5")
        self.profile.clicked.connect(self.profiledef)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setFocus()
        self.show()

        host = "127.0.0.1"
        port = 25565
        ADDR = (host,port)
        self.client = socket(AF_INET, SOCK_STREAM)
        self.client.connect(ADDR)

        receive_thread = Thread(target=self.receive)
        receive_thread.start()

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

    def profiledef(self):
        os.system('python msageprofile.py')

    def send(self):
        self.msg = self.satir.text()
        self.satir.setText("")
        self.client.send(bytes(self.msg, "utf8"))
        print(self.msg)

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Return:
            self.send()

app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()