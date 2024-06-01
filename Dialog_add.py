# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(275, 100)
        Dialog.setMinimumSize(QtCore.QSize(275, 100))
        Dialog.setMaximumSize(QtCore.QSize(275, 100))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("image/QQicon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.friendname = QtWidgets.QLabel(Dialog)
        self.friendname.setGeometry(QtCore.QRect(10, 20, 60, 30))
        self.friendname.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(70, 20, 180, 30))
        self.lineEdit.setObjectName("lineEdit")
        self.submitButton = QtWidgets.QPushButton(Dialog)
        self.submitButton.setGeometry(QtCore.QRect(98, 70, 80, 20))
        self.submitButton.setStyleSheet("background-color: rgb(0, 85, 255);")
        self.submitButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "转移分组"))
        self.friendname.setText(_translate("Dialog", "转移至:"))
        self.submitButton.setText(_translate("Dialog", "确定"))

