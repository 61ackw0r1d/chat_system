# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QQchating.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from threading_end import *
import mysql.connector
def connect_to_mysql():
    try:
        # 创建数据库连接
        db = mysql.connector.connect(
            host="192.168.31.90",  # MySQL 服务器地址
            user="chat",  # 用户名
            password="123456",  # 密码
            database="ast_chatsystem"  # 数据库名称
        )
        # 创建游标对象，用于执行 SQL 查询
        print("数据库连接成功！")
        return db
    except mysql.connector.Error as err:
        print(f"数据库连接失败：{err}")
        return None
class Ui_MainWindow(object):
    def __init__(self, s, wename, user):
        self.s = s
        self.wename = wename
        self.user = user

    def recv_thead(self):
        buffsize = 1024
        def recv():
            while True:
                recvdata =self.s.recv(buffsize).decode('utf-8')
                self.textBrowser.append(recvdata + "\n" + "\n")
        self.re = threading.Thread(target=recv)  # 创建线程
        self.re.start()

    def setupUi(self, MainWindow):
        self.GroupChat = MainWindow
        self.GroupChat.setObjectName("MainWindow")
        self.GroupChat.resize(771, 588)
        self.GroupChat.setMinimumSize(QtCore.QSize(771, 585))
        self.GroupChat.setMaximumSize(QtCore.QSize(771, 588))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("image/QQicon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.GroupChat.setWindowIcon(icon)
        self.GroupChat.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 241, 571))
        self.frame.setStyleSheet("background-image: url(image/qqchatbk.jpg);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.listWidget = QtWidgets.QListWidget(self.frame)
        self.listWidget.setGeometry(QtCore.QRect(0, 50, 241, 521))
        self.listWidget.setIconSize(QtCore.QSize(40, 40))
        self.listWidget.setGridSize(QtCore.QSize(40, 40))
        self.listWidget.setObjectName("listWidget")
        _translate = QtCore.QCoreApplication.translate

        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(True)

        db = connect_to_mysql()
        cursor = db.cursor()
        query = """
                    SELECT userID
                    FROM ast_chatsystem.groups_users_relationship AS gs
                    LEFT JOIN ast_chatsystem.groups AS g
                    ON g.groupID = gs.groupID
                    WHERE g.group_name = %s
                """
        print(self.wename)
        cursor.execute(query, (str(self.wename),))
        ret = cursor.fetchall()
        if ret:
            for ele in ret:
                item = QtWidgets.QListWidgetItem()
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap("image/" + ele[0] + ".jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                item.setIcon(icon)
                item.setText(_translate("MainWindow", ele[0]))
                self.listWidget.addItem(item)
        cursor.close()
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(0, 10, 241, 31))
        self.label.setObjectName("label")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(240, 49, 531, 531))
        self.frame_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.frame_2)
        self.textBrowser.setGeometry(QtCore.QRect(10, 11, 511, 311))
        self.textBrowser.setObjectName("textBrowser")
        self.textEdit = QtWidgets.QTextEdit(self.frame_2)
        self.textEdit.setGeometry(QtCore.QRect(10, 340, 511, 131))
        self.textEdit.setObjectName("textEdit")
        self.sendButton = QtWidgets.QPushButton(self.frame_2)
        self.sendButton.setGeometry(QtCore.QRect(354, 482, 91, 31))
        self.sendButton.setStyleSheet("background-color: rgb(255, 170, 127);")
        self.sendButton.setObjectName("pushButton")

        self.cancelButton = QtWidgets.QPushButton(self.frame_2)
        self.cancelButton.setGeometry(QtCore.QRect(60, 480, 81, 31))
        self.cancelButton.setStyleSheet("background-color: rgb(255, 170, 127);")
        self.cancelButton.setObjectName("pushButton_2")

        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(240, 0, 531, 51))
        self.frame_3.setStyleSheet("background-color: rgb(255, 170, 127);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.grouplabel = QtWidgets.QLabel(self.frame_3)
        self.grouplabel.setGeometry(QtCore.QRect(220, 15, 101, 21))
        self.grouplabel.setStyleSheet("color: rgb(255, 255, 255);")
        self.grouplabel.setObjectName("label_2")

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.GroupChat.setWindowTitle(_translate("MainWindow", "QQ群聊"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(True)

        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.label.setText(_translate("MainWindow", "群聊人员："))
        self.sendButton.setText(_translate("MainWindow", "发送"))
        self.cancelButton.setText(_translate("MainWindow", "关闭"))

    def dj_send(self):
        def send():
            we_text=['wechat']
            we_text.append(self.wename)
            we_text.append(self.user)
            text=self.textEdit.toPlainText()
            if text!='':
                we_text.append(text)
                we_text='$%'.join(we_text)
                print(we_text)
                self.s.send(we_text.encode())
            else:
                # QtWidgets.QMessageBox.information(self.MainWindow, '警告', '输入消息为空！', QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Close, QtWidgets.QMessageBox.Close)
                pass
            self.textEdit.clear()

        self.sendButton.clicked.connect(send)

    def dj_quit(self, ui2):
        def quit():
            we_text = ['wechat_quit']
            we_text.append(self.wename)
            we_text.append(self.user)
            print('we_text is : ' + str(we_text))
            send_text = we_text[0] + '$%' + we_text[1] + '$%' +we_text[2]
            self.s.send(str(send_text).encode())
            ui2.close()
            stop_thread(self.re)
        self.cancelButton.clicked.connect(quit)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QWidget()
    ui = Ui_MainWindow()
    ui.setupUi(widget)
    widget.show()
    #ui.tcp_start()

    sys.exit(app.exec_())
