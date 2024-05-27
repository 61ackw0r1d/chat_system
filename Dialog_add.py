# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Dialog_add.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(275, 175)
        Dialog.setMinimumSize(QtCore.QSize(275, 175))
        Dialog.setMaximumSize(QtCore.QSize(275, 175))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("image/QQicon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.friendname = QtWidgets.QLabel(Dialog)
        self.friendname.setGeometry(QtCore.QRect(10, 40, 54, 21))
        self.friendname.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(70, 40, 181, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.headpic = QtWidgets.QLabel(Dialog)
        self.headpic.setGeometry(QtCore.QRect(30, 110, 31, 20))
        self.headpic.setObjectName("label_2")
        self.defaultButton = QtWidgets.QRadioButton(Dialog)
        self.defaultButton.setGeometry(QtCore.QRect(90, 110, 89, 16))
        self.defaultButton.setObjectName("radioButton")
        self.submitButton = QtWidgets.QPushButton(Dialog)
        self.submitButton.setGeometry(QtCore.QRect(140, 140, 81, 23))
        self.submitButton.setStyleSheet("background-color: rgb(0, 85, 255);")
        self.submitButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "添加好友"))
        self.friendname.setText(_translate("Dialog", "好友名字："))
        self.headpic.setText(_translate("Dialog", "头像："))
        self.defaultButton.setText(_translate("Dialog", "默认"))
        self.submitButton.setText(_translate("Dialog", "确定"))

