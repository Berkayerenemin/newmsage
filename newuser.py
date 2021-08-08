from PyQt5 import QtWidgets, uic, QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QMessageBox
import sys
import os
import time
import socket
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QFileDialog, QInputDialog
import pickle

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('msagenewuser.ui', self)
        self.ad = self.findChild(QtWidgets.QLineEdit, "lineEdit")
        self.soyad = self.findChild(QtWidgets.QLineEdit, "lineEdit_2")
        self.kullaniciadi = self.findChild(QtWidgets.QLineEdit, "lineEdit_3")
        self.sifre = self.findChild(QtWidgets.QLineEdit, "lineEdit_7")
        self.dogrulama = self.findChild(QtWidgets.QLineEdit, "lineEdit_8")
        self.avatarresim = self.findChild(QtWidgets.QPushButton, "pushButton")
        self.neden = self.findChild(QtWidgets.QPushButton, "pushButton_3")
        self.hakkimizda = self.findChild(QtWidgets.QPushButton, "pushButton_4")
        self.startbutton = self.findChild(QtWidgets.QPushButton, "pushButton_5")
        self.profilresmilabel = self.findChild(QtWidgets.QLabel, "label_7")
        self.msgBox = QMessageBox()
        self.msgBox2 = QMessageBox()
        self.msgBox3 = QMessageBox()
        self.hakkimizda.clicked.connect(self.hakkimizdaShow)
        self.neden.clicked.connect(self.nedenShow)
        self.avatarresim.clicked.connect(self.avatarresimdef)
        self.startbutton.clicked.connect(self.start)
        self.kullanici = []
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.show()

    def avatarresimdef(self):
        self.profilresmilabel.setText("")
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;jpg Files (*.jpg)", options=options)
        if self.fileName:
            print(self.fileName)
            dosya = self.fileName
            pixmap = QPixmap(dosya)
            pixmap4 = pixmap.scaled(101, 101, QtCore.Qt.KeepAspectRatio)
            self.profilresmilabel.setPixmap(pixmap4)
        else:
            self.control = "x"

    def hakkimizdaShow(self):
        self.msgBox.setIcon(QMessageBox.Information)
        self.msgBox.setText("MSAGE, açık kaynak kodlu, kişilerin kendi sunucularını kurarak veya MSAGE'in kurulmuş sunucularında odalar kurarak mesajlaştığı bir mesajlaşma programdır.\n\nTüm kullanıcı verileri MSAGE'in kendi bünyesinde saklıdır. Daha fazlası için msage.com adresine bakabilirsiniz.")
        self.msgBox.setWindowTitle("MSAGE Hakkında...")
        #msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        #msgBox.buttonClicked.connect(msgButtonClick)
        self.msgBox.show()

    def nedenShow(self):
        self.msgBox2.setIcon(QMessageBox.Information)
        self.msgBox2.setText("MSAGE içerisinde olası acil bir durumda kullanıcılara ulaşmak, gerektiğinde özel olarak bilgi vermek amacıyla toplanan tüm veriler MSAGE'in güvenli veri tabanlarında saklanmaktadır.")
        self.msgBox2.setWindowTitle("Neden İstiyoruz?")
        #msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        #msgBox.buttonClicked.connect(msgButtonClick)
        self.msgBox2.show()

    def start(self):
        host = "127.0.0.1"
        port = 25565
        addr2 = (host, port)
        c = socket(AF_INET, SOCK_STREAM)
        c.connect(addr2)
        self.kullanici.append(self.ad.text())
        self.kullanici.append(self.soyad.text())
        self.kullanici.append(self.kullaniciadi.text())
        self.kullanici.append(self.sifre.text())
        if self.dogrulama.text() == "4":
            self.dataprofil = pickle.dumps(self.kullanici)
            c.send(self.dataprofil)
            dosya = str(self.fileName)
            log = open(dosya, "rb")
            data = log.read()
            c.sendall(data)
            otologin = open("oto.txt", "w")
            for element in self.kullanici:
                otologin.write(element)
                otologin.write(',')
            otologin.close()
            self.close()
            os.system('python msageana.py')
        else:
            self.msgBox3.setIcon(QMessageBox.Information)
            self.msgBox3.setText("İnsan olduğunuzu doğrulayamadık. Lütfen güvenlik sorusunun yanıtını iyice düşünüp tekrar yazınız.")
            self.msgBox3.setWindowTitle("Ne, yoksa sen...")
            #msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            #msgBox.buttonClicked.connect(msgButtonClick)
            self.msgBox3.show()



app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()