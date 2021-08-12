from PyQt5 import QtWidgets, uic, QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QMessageBox, QStackedWidget, QStackedLayout
import sys
import os
import time
import socket
from socket import AF_INET, socket, SOCK_STREAM
from threading import Event, Thread
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QFileDialog, QInputDialog
import pickle

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('msagenewuserpage.ui', self)
        self.ad = self.findChild(QtWidgets.QLineEdit, "lineEdit")
        self.soyad = self.findChild(QtWidgets.QLineEdit, "lineEdit_2")
        self.kullaniciadi = self.findChild(QtWidgets.QLineEdit, "lineEdit_3")
        self.stackwidget = self.findChild(QtWidgets.QStackedWidget, "stackedWidget")
        self.page1 = self.findChild(QtWidgets.QWidget, "page")
        self.page2 = self.findChild(QtWidgets.QWidget, "page_2")
        self.page3 = self.findChild(QtWidgets.QWidget, "page_3")
        self.sifre = self.findChild(QtWidgets.QLineEdit, "lineEdit_7")
        self.dogrulama = self.findChild(QtWidgets.QLineEdit, "lineEdit_8")
        self.avatarresim = self.findChild(QtWidgets.QPushButton, "pushButton")
        self.neden = self.findChild(QtWidgets.QPushButton, "pushButton_3")
        self.hakkimizda = self.findChild(QtWidgets.QPushButton, "pushButton_4")
        self.startbutton = self.findChild(QtWidgets.QPushButton, "pushButton_5")
        self.profilresmilabel = self.findChild(QtWidgets.QLabel, "label_7")
        self.closebutton = self.findChild(QtWidgets.QPushButton, "pushButton_8")
        #self.logo.setAlignment(QtCore.Qt.AlignCenter)
        self.msgBox = QMessageBox()
        self.msgBox2 = QMessageBox()
        self.msgBox3 = QMessageBox()
        self.uyedon1 = self.findChild(QtWidgets.QPushButton, "pushButton_6")
        self.uyedon2 = self.findChild(QtWidgets.QPushButton, "pushButton_7")
        self.hakkimizda.clicked.connect(lambda: self.stackwidget.setCurrentWidget(self.page2))
        self.neden.clicked.connect(lambda: self.stackwidget.setCurrentWidget(self.page3))
        self.uyedon1.clicked.connect(lambda: self.stackwidget.setCurrentWidget(self.page1))
        self.uyedon2.clicked.connect(lambda: self.stackwidget.setCurrentWidget(self.page1))
        #self.avatarresim.clicked.connect(self.avatarresimdef)
        self.startbutton.clicked.connect(self.start)
        self.closebutton.clicked.connect(self.kapat)

        self.kullanici = []
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setFocus()
        self.show()

    def dropEvent(self, event):
        if event.mimeData().hasUrls():
            event.setDropAction(QtCore.Qt.CopyAction)
            event.accept()

            links = []
            for url in event.mimeData().urls():
                # https://doc.qt.io/qt-5/qurl.html
                if url.isLocalFile():
                    links.append(str(url.toLocalFile()))
                else:
                    links.append(str(url.toString()))
            self.addItems(links)
        else:
            event.ignore()
    
    def kapat(self):
        print("Kapatma işlemi başlatıldı.")
        self.close()
        quit()
        #Soket bağlantısı da kesilecek.

    def avatarresimdef(self):
        self.profilresmilabel.setText("")
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        try:
            self.fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;jpg Files (*.jpg)", options=options)
            if self.fileName:
                print(self.fileName)
                dosya = self.fileName
                pixmap = QPixmap(dosya)
                pixmap4 = pixmap.scaled(101, 101, QtCore.Qt.KeepAspectRatio)
                self.profilresmilabel.setPixmap(pixmap4)
                print("Profil resmi eklendi.")
            else:
                self.control = "x"
                print("Profil resmi eklenemedi.")
                pass
        except:
            print("Profil resmi seçilemedi.")
            pass

    def start(self):
        host = "127.0.0.1"
        port = 25566
        addr2 = (host, port)
        c = socket(AF_INET, SOCK_STREAM)
        c.connect(addr2)
        print("Sunucu ile bağlantı kuruldu.")
        try:
            self.kullanici.append(self.ad.text())
            self.kullanici.append(self.soyad.text())
            self.kullanici.append(self.kullaniciadi.text())
            self.kullanici.append(self.sifre.text())
            print(self.avatarresim.dropEvent)
            print("Veriler alındı.")
        except:
            print("Veriler tam olarak alınamadı.")
        if self.dogrulama.text() == "4":
            print(self.kullanici)
            self.dataprofil = pickle.dumps(self.kullanici)
            print(self.dataprofil)
            c.send(self.dataprofil)
            print("Kullanıcı bilgileri sunucuya gönderildi.")
            try:
                dosya = str(self.fileName)
                log = open(dosya, "rb")
                data = log.read()
                c.sendall(data)
                print("Profil resmi karşıya gönderildi.")
            except:
                print("Seçili bir profil resmi bulunamadı.")
            otologin = open("oto.txt", "w")
            for element in self.kullanici:
                otologin.write(element)
                otologin.write(',')
                print("Otomatik giriş için bir dosya oluşturuluyor.")
            otologin.close()
            self.close()
            print("GUI kapatıldı.")
            c.close()
            print("Yeni kullanıcı sisteminin sunucu ile olan bağlantısı kapatıldı.")
            os.system('python msageana.py')
            quit()
        else:
            self.msgBox3.setIcon(QMessageBox.Information)
            self.msgBox3.setText("İnsan olduğunuzu doğrulayamadık. Lütfen güvenlik sorusunun yanıtını iyice düşünüp tekrar yazınız.")
            #self.msgBox3.setWindowTitle("Ne, yoksa sen...")
            #msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            self.msgBox3.show()



app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()