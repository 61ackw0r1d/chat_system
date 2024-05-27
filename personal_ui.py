# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'personal.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from threading_end import *
from thread_result import MyThread
from voice_code import Audio_Client, Audio_Server, _async_raise, stop_thread
from file_exchange_class import file_send, file_recv


class Ui_Dialog(object):
    def __init__(self, s, sendname, recvname):
        self.s = s
        self.sendname = sendname
        self.recvname = recvname
        send_list = ['personal']
        send_list.append(self.sendname)
        send_list.append(self.recvname)
        sendtext = '已建立连接'
        if sendtext != '':
            send_list.append(sendtext)
            textsend = '$%'.join(send_list)
            self.s.send(textsend.encode())
            print(textsend)

    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        self.MainWindow.setObjectName("MainWindow")
        self.MainWindow.resize(725, 756)

        self.MainWindow.setMinimumSize(QtCore.QSize(725, 656))
        self.MainWindow.setMaximumSize(QtCore.QSize(725, 656))

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("image/QQicon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.MainWindow.setWindowIcon(icon)

        self.MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame = QtWidgets.QFrame(self.MainWindow)
        self.frame.setGeometry(QtCore.QRect(0, 0, 731, 41))
        self.frame.setStyleSheet("background-color: rgb(255, 170, 127);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.perlLabel = QtWidgets.QLabel(self.frame)
        self.perlLabel.setGeometry(QtCore.QRect(200, 0, 200, 40))
        self.perlLabel.setStyleSheet("font: 12pt \"Agency FB\";\n""color: rgb(255, 255, 255);")
        self.perlLabel.setObjectName("label")

        self.textEdit = QtWidgets.QTextEdit(self.MainWindow)
        self.textEdit.setGeometry(QtCore.QRect(10, 420, 561, 91))
        self.textEdit.setObjectName("textEdit")
        self.textBrowser = QtWidgets.QTextBrowser(self.MainWindow)
        self.textBrowser.setGeometry(QtCore.QRect(10, 80, 561, 291))
        self.textBrowser.setObjectName("textBrowser")

        self.closeButton = QtWidgets.QPushButton(self.MainWindow)
        self.closeButton.setGeometry(QtCore.QRect(10, 510, 81, 31))
        self.closeButton.setStyleSheet("background-color: rgb(255, 170, 127);\n""color: rgb(255, 255, 255);")
        self.closeButton.setObjectName("pushButton")

        self.sendButton = QtWidgets.QPushButton(self.MainWindow)
        self.sendButton.setGeometry(QtCore.QRect(420, 510, 81, 31))
        self.sendButton.setStyleSheet("background-color: rgb(255, 170, 127);\n""color: rgb(255, 255, 255);")
        self.sendButton.setObjectName("pushButton_2")

        self.voiceButton = QtWidgets.QPushButton(self.MainWindow)
        self.voiceButton.setGeometry(QtCore.QRect(10, 380, 81, 31))
        self.voiceButton.setObjectName("btn1")

        self.fileButton = QtWidgets.QPushButton(self.MainWindow)
        self.fileButton.setGeometry(QtCore.QRect(120, 380, 81, 31))
        self.fileButton.setObjectName("btn2")

        self.overVoiceButton = QtWidgets.QPushButton(self.MainWindow)
        self.overVoiceButton.setGeometry(QtCore.QRect(230, 380, 81, 31))
        self.overVoiceButton.setObjectName("btn3")

        self.retranslateUi(MainWindow)
        # self.pushButton_4.clicked.connect(Dialog.showMinimized)
        # self.pushButton_3.clicked.connect(Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.MainWindow.setWindowTitle(_translate("MainWindow", "聊天"))
        self.perlLabel.setText(_translate("MainWindow", "perl"))
        self.closeButton.setText(_translate("MainWindow", "关闭"))
        self.sendButton.setText(_translate("MainWindow", "发送按钮"))
        self.voiceButton.setText(_translate("MainWindow", "语音聊天"))
        self.fileButton.setText(_translate("MainWindow", "文件传输"))
        self.overVoiceButton.setText(_translate("MainWindow", "结束语音"))


    def pel_send(self):
        print('user1 is: ' + self.sendname + '\nreceiver1 is : ' + self.recvname)
        def send():
            send_list=['personal']
            send_list.append(self.sendname)
            send_list.append(self.recvname)
            print('user2 is: ' + self.sendname + '\nreceiver2 is : ' + self.recvname)
            sendtext = self.textEdit.toPlainText()
            if sendtext != '':
                send_list.append(sendtext)
                textsend = '$%'.join(send_list)
                self.s.send(textsend.encode())
                print(textsend)
            self.textEdit.clear()
        self.sendButton.clicked.connect(send)

    def pel_recv(self):
        buffsize = 1024
        def recv():
            i = 0
            while True:
                recvtext=self.s.recv(buffsize).decode('utf-8')
                recvtext_list = recvtext.split('$%')
                length = len(recvtext_list)
                i = i + 1
                print('receive message list is:')
                print(recvtext_list)
                if recvtext_list[length-1] == 'voicechat_request':
                    if recvtext_list[length-2] != 'end':
                        text = '          对方发起语音聊天请求, 已建立连接......'
                        self.textBrowser.append(text + "\n")
                        recvtext_ip = recvtext_list[0].replace("'", "")
                        print('audio_client ready to start with:' + recvtext_ip)
                        au = Audio_Server(4568, 4)
                        au1 = Audio_Client(str(recvtext_ip[0:9]), 4567, 4)
                        self.re = threading.Thread(target=au.run)  # 创建线程
                        self.re1 = threading.Thread(target=au1.run)  # 创建线程
                        self.re.setDaemon(True)
                        self.re1.setDaemon(True)
                        self.re.start()
                        self.re1.start()
                    else:
                        text = '          对方已结束语音聊天......'
                        self.textBrowser.append(text + "\n")
                        stop_thread(self.re)
                        del au
                        del au1

                elif recvtext_list[length-1] == 'voicechat_accept':
                    text = '          语音聊天已开始......'
                    self.textBrowser.append(text + "\n")
                    recvtext_ip = recvtext_list[0].replace("'", "")
                    print('audio_client ready to start with:' + recvtext_ip[0:9])
                    self.au = Audio_Server(4567, 4)
                    self.au1 = Audio_Client(str(recvtext_ip[0:9]), 4568, 4)
                    self.re3 = threading.Thread(target=self.au.run)  # 创建线程
                    self.re4 = threading.Thread(target=self.au1.run)  # 创建线程
                    # self.re3.setDaemon(True)
                    # self.re4.setDaemon(True)
                    self.re3.start()
                    self.re4.start()

                elif recvtext_list[length-1] == 'filesend_request':
                    self.textBrowser.append('          准备接收对方发来的文件......\n')
                    recvtext_ip = recvtext_list[0].replace("'", "")
                    fl = file_recv()
                    re = MyThread(fl.server100)  # 创建线程
                    re.start()
                    re.join()
                    recv_result = re.get_result()
                    print('My sendresult is : ' + str(recv_result))
                    if recv_result == 0 :
                        self.textBrowser.append('          文件接收完毕......\n')

                elif recvtext_list[length-1] == 'filesend_accept':
                    self.textBrowser.append('          准备发送文件......\n')
                    recvtext_ip = recvtext_list[0].replace("'", "")
                    print(recvtext_ip)
                    fl = file_send(str(recvtext_ip[0:9]), 7788)
                    re1 = MyThread(fl.file_send_start)  # 创建线程
                    re1.start()
                    re1.join()
                    send_result = re1.get_result()
                    if send_result == 0 :
                        self.textBrowser.append('          文件发送完毕......\n')

                else:
                    self.textBrowser.append(recvtext + "\n")

        self.re = threading.Thread(target=recv)  # 创建线程
        self.re.start()

    def voice_chat(self):
        def chat():
            send_list = ['voicechat']
            send_list.append(self.sendname)
            send_list.append(self.recvname)
            sendtext = 'voicechat_request'
            send_list.append(sendtext)
            textsend = '$%'.join(send_list)
            print(textsend)
            self.s.send(textsend.encode())
        self.voiceButton.clicked.connect(chat)

    def voice_chat_down(self):
        def down():
            send_list = ['voicechat']
            send_list.append(self.sendname)
            send_list.append(self.recvname)
            sendtext = 'end$%voicechat_request'
            send_list.append(sendtext)
            textsend = '$%'.join(send_list)
            print(textsend)
            self.s.send(textsend.encode())
            if hasattr(self, 're3') and self.re3.is_alive():
                stop_thread(self.re3)
            if hasattr(self, 're4') and self.re4.is_alive():
                stop_thread(self.re4)
            if hasattr(self, 'au'):
                self.au.close()
                del self.au
            if hasattr(self, 'au1'):
                self.au1.close()
                del self.au1
        self.overVoiceButton.clicked.connect(down)

    def file_send(self):
        def fsend():
            send_list = ['filesend']
            send_list.append(self.sendname)
            send_list.append(self.recvname)
            sendtext = 'filesend_request'
            send_list.append(sendtext)
            textsend = '$%'.join(send_list)
            print(textsend)
            self.s.send(textsend.encode())

        self.fileButton.clicked.connect(fsend)

    def quit_window(self, Dlog):
        def quit():
            Dlog.close()
            stop_thread(self.re)
            print('stopped')
        self.closeButton.clicked.connect(quit)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QWidget()
    ui = Ui_Dialog()
    ui.setupUi(widget)
    widget.show()

    sys.exit(app.exec_())
