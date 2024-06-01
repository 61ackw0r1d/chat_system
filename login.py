# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QFormLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from socket import *
import sys

class Ui_MainWindow(QWidget):

    def tcp_start(self):
        # address = '127.0.0.1'
        # address = '192.168.31.142'
        address = '192.168.31.90'
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
        self.signInButton.setGeometry(QtCore.QRect(60, 270, 110, 41))
        self.signInButton.setStyleSheet("background-color: rgb(7, 85, 240);\n""color: rgb(255, 255, 255);")
        self.signInButton.setObjectName("pushButton")
        self.signInButton.clicked.connect(self.login)
        self.signOnButton = QtWidgets.QPushButton(self.centralwidget)
        self.signOnButton.setGeometry(QtCore.QRect(180, 270, 110, 41))
        self.signOnButton.setStyleSheet("background-color: rgb(7, 85, 240);\n""color: rgb(255, 255, 255);")
        self.signOnButton.setObjectName("pushButton")
        self.signOnButton.clicked.connect(self.signon)

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
        self.signOnButton.setText(_translate("MainWindow", "注册"))
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
            # sys.sleep(2 * 1000)
            login_ui.hide()
            ui1.retranslateUi(self.MainWindow,self.accountLine.text())
            QQmain_ui.show()
            ui1.label.setText(self.user)
            # print("in login.py self.user", self.user)
        elif str(recv_info) == 'false-id/pw':
            QMessageBox.information(self.MainWindow, '失败', '登录失败，账号或密码错误!!', QMessageBox.Ok | QMessageBox.Close,QMessageBox.Close)
        elif str(recv_info)=='false-login':
            QMessageBox.information(self.MainWindow, '失败', '此账号已登录!', QMessageBox.Ok | QMessageBox.Close,QMessageBox.Close)

    def signon(self):
        self.register=RegistrationForm(self.s)
        self.register.show()

class RegistrationForm(QWidget):
    def __init__(self,socket):
        super().__init__()
        self.s = socket
        self.buffsize=1024
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('用户注册')

        layout = QFormLayout()

        self.id_label = QLabel('用户名')
        self.id_input = QLineEdit()
        layout.addRow(self.id_label, self.id_input)

        self.password_label = QLabel('密码')
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        layout.addRow(self.password_label, self.password_input)

        self.check_label = QLabel('确认')
        self.check_input = QLineEdit()
        self.check_input.setEchoMode(QLineEdit.Password)
        layout.addRow(self.check_label, self.check_input)

        self.submit_button = QPushButton('注册')
        self.submit_button.clicked.connect(self.signup_user)
        layout.addWidget(self.submit_button)

        self.setLayout(layout)

    def signup_user(self):
        user_id = self.id_input.text()
        password = self.password_input.text()
        check=self.check_input.text()
        if check==password:
            if user_id and password:
                signup_info = ['signup']
                signup_info.append(user_id)
                signup_info.append(password)
                signup_info = '$%'.join(signup_info)
                self.s.send(str(signup_info).encode())
                self.signup_recv()
            else:
                QMessageBox.warning(self, '输入错误', '请输入账号密码')
        else:QMessageBox.warning(self, '输入错误', '两次输入的密码不一致')

    def signup_recv(self):
        recv_info = self.s.recv(self.buffsize).decode('utf-8')
        print(recv_info)
        if str(recv_info) == 'true':
            print("注册成功")
            QMessageBox.information(self, '注册', '注册成功!')
            self.id_input.clear()
            self.password_input.clear()
            self.check_input.clear()
        elif str(recv_info) == 'false':
            print("注册失败")
            QMessageBox.warning(self, '失败', '此账号已注册!')

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    login_ui = QtWidgets.QWidget()
    ui = Ui_MainWindow()        # 登录界面
    ui.setupUi(login_ui)
    ui.tcp_start()
    login_ui.show()
    print('tcp connect!')
    QQmain_ui = QtWidgets.QWidget()
    import QQ
    ui1 = QQ.Ui_MainWindowt(ui.s)
    ui1.setupUit(QQmain_ui)
    sys.exit(app.exec_())
