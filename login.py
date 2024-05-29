# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.11.2

# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMessageBox
from socket import *


class Ui_MainWindow(object):

    def tcp_start(self):
        # address = '127.0.0.1'
        # address = '192.168.31.142'
        address = '192.168.31.90'
        # address = '192.168.31.103'
        port = 8000
        self.buffsize = 1024
        self.s = socket(AF_INET, SOCK_STREAM)
        self.s.connect((address, port))

    def setupUi(self, MainWindow):
        self.MainWindow=MainWindow
        self.MainWindow.setObjectName("MainWindow")
        self.MainWindow.resize(360, 340)
        self.MainWindow.setMinimumSize(QtCore.QSize(360, 340))
        self.MainWindow.setMaximumSize(QtCore.QSize(360, 340))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("image/QQicon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        #normal当用户没有与图标交互，但图标所表示的功能可用时，显示像素图
        #off表示当小部件处于“关闭”状态时显示像素图
        self.MainWindow.setWindowIcon(icon)

        self.MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.accountLine = QtWidgets.QLineEdit(self.centralwidget)
        self.accountLine.setGeometry(QtCore.QRect(100, 160, 191, 30))
        self.accountLine.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.accountLine.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.accountLine.setText("")
        self.accountLine.setMaxLength(32767)
        self.accountLine.setObjectName("lineEdit")
        self.passwordLine = QtWidgets.QLineEdit(self.centralwidget)
        self.passwordLine.setGeometry(QtCore.QRect(100, 210, 191, 31))
        self.passwordLine.setInputMask("")
        self.passwordLine.setText("")
        self.passwordLine.setMaxLength(32767)
        self.passwordLine.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordLine.setCursorPosition(0)
        self.passwordLine.setObjectName("lineEdit_2")
        self.signInButton = QtWidgets.QPushButton(self.centralwidget)
        self.signInButton.setGeometry(QtCore.QRect(70, 260, 221, 41))
        self.signInButton.setStyleSheet("background-color: rgb(7, 85, 240);\n""color: rgb(255, 255, 255);")
        self.signInButton.setObjectName("pushButton")
        self.signInButton.clicked.connect(self.login)

        self.formFrame = QtWidgets.QFrame(self.centralwidget)
        self.formFrame.setGeometry(QtCore.QRect(0, -1, 361, 151))
        self.formFrame.setStyleSheet("border-color: rgb(0, 85, 255);\n""background-image: url(image/loginicon.jpg);")
        self.formFrame.setObjectName("formFrame")
        self.formLayout = QtWidgets.QFormLayout(self.formFrame)
        self.formLayout.setObjectName("formLayout")
        self.accountLabel = QtWidgets.QLabel(self.centralwidget)
        self.accountLabel.setGeometry(QtCore.QRect(45, 170, 41, 16))
        self.accountLabel.setObjectName("label")
        self.passwordLabel = QtWidgets.QLabel(self.centralwidget)
        self.passwordLabel.setGeometry(QtCore.QRect(45, 220, 41, 16))
        self.passwordLabel.setObjectName("label_2")



        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")


        _translate = QtCore.QCoreApplication.translate
        self.MainWindow.setWindowTitle(_translate("MainWindow", "QQ登录"))
        self.signInButton.setText(_translate("MainWindow", "登录"))
        self.accountLabel.setText(_translate("MainWindow", "账号："))
        self.passwordLabel.setText(_translate("MainWindow", "密码："))
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def login(self):
        login_info=['login']
        self.user=self.accountLine.text()
        password=self.passwordLine.text()
        user_l=len(str(self.user))
        if self.user=='':
            QMessageBox.information(self.MainWindow, '提示', 'QQ账号不能为空!', QMessageBox.Ok | QMessageBox.Close, QMessageBox.Close)
        elif user_l<5 or user_l>10:
            QMessageBox.information(self.MainWindow, '提示', 'QQ账号长度不对!', QMessageBox.Ok | QMessageBox.Close, QMessageBox.Close)
        else:
            if password=='':
                QMessageBox.information(self.MainWindow, '提示', '密码不能为空!', QMessageBox.Ok | QMessageBox.Close, QMessageBox.Close)
            else:
                login_info.append(self.user)
                login_info.append(password)
                login_info='$%'.join(login_info)
                print(login_info)
                self.s.send(str(login_info).encode())
                self.login_recv()

    def login_recv(self):
        recv_info=self.s.recv(self.buffsize).decode('utf-8')
        print(recv_info)
        if str(recv_info) == 'true':
            QMessageBox.information(self.MainWindow, '登录成功', '登录成功!', QMessageBox.Ok | QMessageBox.Close, QMessageBox.Close)
            login_ui.hide()
            QQmain_ui.show()
            ui1.label.setText(self.user)
        elif str(recv_info) == 'false-id/pw':
            QMessageBox.information(self.MainWindow, '失败', '登录失败，账号或密码错误!!', QMessageBox.Ok | QMessageBox.Close,QMessageBox.Close)
        elif str(recv_info)=='false-login':
            QMessageBox.information(self.MainWindow, '失败', '此账号已登录!', QMessageBox.Ok | QMessageBox.Close,QMessageBox.Close)



if __name__ == "__main__":

    import sys
    app = QtWidgets.QApplication(sys.argv)
    login_ui = QtWidgets.QWidget()
    ui = Ui_MainWindow()        # 登录界面
    ui.setupUi(login_ui)
    ui.tcp_start()
    login_ui.show()
    print('tcp connect!')
    import QQ
    QQmain_ui = QtWidgets.QWidget()
    ui1 = QQ.Ui_MainWindowt(ui.s)
    ui1.setupUit(QQmain_ui)

    sys.exit(app.exec_())


