from PyQt5 import QtCore, QtGui, QtWidgets
import chatroom_ui
from chatroom_ui import connect_to_mysql
import personal_ui
from Dialog_add import Ui_Dialog

class Ui_MainWindowt(object):
    def __init__(self, s):
        self.s = s
        self.buffsize = 1024
        self.db=connect_to_mysql()
    def setupUit(self, MainWindow):
        self.MainWindow = MainWindow
        self.MainWindow.setObjectName("MainWindow")
        self.MainWindow.resize(326, 627)
        self.MainWindow.setMinimumSize(QtCore.QSize(326, 627))
        self.MainWindow.setMaximumSize(QtCore.QSize(326, 627))

        self.menu_ui_add_group = QtWidgets.QWidget()
        self.add_relationship_ui = Ui_Dialog()
        self.add_relationship_ui.setupUi(self.menu_ui_add_group)
        self.menu_ui_add_group.setWindowTitle("添加分组")
        self.add_relationship_ui.friendname.setText("新组名：")

        self.menu_ui_add_friend = QtWidgets.QWidget()
        self.add_friend_ui = Ui_Dialog()
        self.add_friend_ui.setupUi(self.menu_ui_add_friend)
        self.menu_ui_add_friend.setWindowTitle("添加好友")
        self.add_friend_ui.friendname.setText("好友名：")

        self.menu_ui_move = QtWidgets.QWidget()
        self.move_ui = Ui_Dialog()
        self.move_ui.setupUi(self.menu_ui_move)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("image/QQ1.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 331, 141))
        self.frame.setStyleSheet("background-color: rgb(0, 85, 255);\n")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(120, 30, 70, 65))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setStyleSheet("background-image:url(image/qq.jpeg)")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(125, 100, 91, 21))
        self.label.setStyleSheet("background-color: rgb(85, 255, 255);\n""color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 85, 255);\n")
        self.label.setObjectName("label")
        self.closeButton = QtWidgets.QPushButton(self.frame)
        self.closeButton.setGeometry(QtCore.QRect(294, 0, 31, 23))
        self.closeButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 85, 255);")
        self.closeButton.setObjectName("pushButton_3")
        self.hideButton = QtWidgets.QPushButton(self.frame)
        self.hideButton.setGeometry(QtCore.QRect(260, 0, 31, 23))
        self.hideButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 85, 255);")
        self.hideButton.setObjectName("pushButton_4")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(0, 140, 326, 35))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.friendButton = QtWidgets.QPushButton(self.frame_3)
        self.friendButton.setGeometry(QtCore.QRect(0, 2, 163, 35))
        self.friendButton.setStyleSheet("background-color: rgb(255, 239, 239);")
        self.friendButton.setIcon(icon)
        self.friendButton.setObjectName("pushButton")
        self.groupButton = QtWidgets.QPushButton(self.frame_3)
        self.groupButton.setGeometry(QtCore.QRect(160, 2, 171, 35))
        self.groupButton.setStyleSheet("background-color: rgb(255, 248, 248);")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("image/哈工程头像.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.groupButton.setIcon(icon1)
        self.groupButton.setObjectName("pushButton_2")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(0, 171, 331, 451))
        self.listWidget.setIconSize(QtCore.QSize(45, 45))

        self.treeWidget = QtWidgets.QTreeWidget(self.centralwidget)
        self.treeWidget.setGeometry(QtCore.QRect(-3, 171, 331, 441))
        self.treeWidget.setAutoScrollMargin(10)
        self.treeWidget.setIconSize(QtCore.QSize(40, 40))
        self.treeWidget.setAutoExpandDelay(-1)
        self.treeWidget.setIndentation(6)
        self.treeWidget.setColumnCount(1)
        self.treeWidget.setObjectName("treeWidget")
        font = QtGui.QFont()
        font.setPointSize(10)
        self.treeWidget.headerItem().setFont(0, font)

        self.treeWidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.treeWidget.customContextMenuRequested.connect(self.menuevent)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")

        self.closeButton.clicked.connect(self.closeMainwindow_and_changeAlive)

        self.friendButton.clicked.connect(self.listWidget.hide)
        self.groupButton.clicked.connect(self.listWidget.show)
        self.friendButton.clicked.connect(self.treeWidget.show)
        self.groupButton.clicked.connect(self.treeWidget.hide)
        self.hideButton.clicked.connect(MainWindow.showMinimized)

        self.listWidget.itemClicked.connect(self.group_req)
        self.treeWidget.itemClicked.connect(self.personal)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def closeMainwindow_and_changeAlive(self):
        self.MainWindow.close()
        self.close()
        send_list = f"close$%{self.username}$%close"
        # self.s.send(send_list.encode())

    def retranslateUi(self, MainWindow, username):
        self.username = username

        _translate = QtCore.QCoreApplication.translate
        self.MainWindow.setWindowTitle(_translate("MainWindow", "QQ"))
        self.label.setText(_translate("MainWindow", "*******************************************************"))

        self.closeButton.setText(_translate("MainWindow", "关闭"))
        self.hideButton.setText(_translate("MainWindow", "隐藏"))
        self.friendButton.setText(_translate("MainWindow", "好友"))
        self.groupButton.setText(_translate("MainWindow", "群聊"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)  # 不排序

        cursor = self.db.cursor()
        query = """
            SELECT group_name 
            FROM ast_chatsystem.groups_users_relationship AS gs
            LEFT JOIN ast_chatsystem.groups AS g 
            ON g.groupID = gs.groupID 
            WHERE gs.userID = %s
            """
        cursor.execute(query, (self.username,))
        ret = cursor.fetchall()
        if ret:
            for ele in ret:
                item = QtWidgets.QListWidgetItem()
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap("image/" + ele[0] + ".png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                item.setIcon(icon)
                item.setText(_translate("MainWindow", ele[0]))
                self.listWidget.addItem(item)
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "好友列表"))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)

        self.relationships = []
        query = "select relationship from users_relationship where userID=%s group by relationship"
        cursor.execute(query, (self.username,))
        ret = cursor.fetchall()
        if ret:
            for element in ret:
                self.relationships.append(element[0])

        font = QtGui.QFont()
        font.setPointSize(10)
        for relation in self.relationships:
            query = "select friendID from users_relationship where userID=%s and relationship=%s"
            cursor.execute(query, (self.username, relation))
            ret = cursor.fetchall()
            print("ret is", ret)
            if ret:
                item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
                item_0.setFont(0, font)
                item_0.setText(0, _translate("MainWindow", relation))
                for elem in ret:
                    item_1 = QtWidgets.QTreeWidgetItem(item_0)
                    item_1.setFont(0, font)
                    item_1.setText(0, _translate("MainWindow", elem[0]))
                    icon = QtGui.QIcon()
                    path="image/" + elem[0] + ".jpg"
                    try:
                        file=open(path,"r")
                        file.close()
                    except:
                        path="image/icon.jpg"
                    icon.addPixmap(QtGui.QPixmap(path), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                    item_1.setIcon(0, icon)
            else:
                print("nothing in his/her", relation)
        cursor.close()
        self.treeWidget.setSortingEnabled(__sortingEnabled)
    def friend_recv(self):
        recv_info = self.recv(self.buffsize).decode("utf-8")
        print(recv_info)
    def group_req(self, item):
        self.grouptitle = item.text()
        print(item.text())
        self.user = self.label.text()
        group_chat = ['wechat_req']
        group_chat.append(self.grouptitle)
        group_chat.append(self.user)
        group_chat = '$%'.join(group_chat)
        self.s.send(group_chat.encode())
        self.group_setup(item)
    def group_setup(self, item):
        self.grouptitle = item.text()
        self.user = self.label.text()

        item = QtWidgets.QListWidgetItem()
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("image/QQ1.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon1)
        item.setText(str(self.user))

        groupchat_ui = QtWidgets.QWidget()
        ui2 = chatroom_ui.Ui_MainWindow(self.s, self.grouptitle, self.user)
        ui2.setupUi(groupchat_ui)

        groupchat_ui.show()
        ui2.textBrowser.clear()
        ui2.grouplabel.setText(self.grouptitle)

        ui2.recv_thead()
        ui2.dj_send()
        ui2.dj_quit(groupchat_ui)
    def personal(self, item):
        self.user = self.label.text()
        self.personaltitle = item.text(0)
        print("in qq.py", self.user, self.personaltitle)
        socket = self.s
        if self.personaltitle not in self.relationships:
            personalchat_ui = QtWidgets.QWidget()
            ui3 = personal_ui.Ui_Dialog(socket, self.user, self.personaltitle)
            ui3.setupUi(personalchat_ui)
            personalchat_ui.show()

            ui3.perlLabel.setText(self.personaltitle)
            print('my title is: ' + self.personaltitle)
            ui3.pel_recv()
            ui3.pel_send()
            ui3.voice_chat()
            ui3.file_send()
            ui3.voice_chat_down()
            ui3.quit_window(personalchat_ui)
            ui3.textBrowser.clear()
    def menuevent(self):
        self.treetext = self.treeWidget.currentItem().text(0)

        if self.treetext in self.relationships or str(self.treetext).isdigit() == False:
            pmenu1 = QtWidgets.QMenu(self.MainWindow)
            AddGroupAct = QtWidgets.QAction("添加分组", pmenu1)
            pmenu1.addAction(AddGroupAct)
            AddGroupAct.triggered.connect(self.addrelationship)

            AddFriendAct = QtWidgets.QAction("添加好友", pmenu1)
            pmenu1.addAction(AddFriendAct)
            AddFriendAct.triggered.connect(self.addfriend)

            pmenu1.exec_(QtGui.QCursor.pos())
        else:
            pmenu2 = QtWidgets.QMenu(self.MainWindow)
            deletem = QtWidgets.QAction("删除", pmenu2)
            pmenu2.addAction(deletem)
            deletem.triggered.connect(self.deletefriend)

            movem = QtWidgets.QAction("转移联系人至", pmenu2)
            pmenu2.addAction(movem)
            movem.triggered.connect(self.movefriend)

            pmenu2.exec_(QtGui.QCursor.pos())
    def addrelationship(self):
        self.menu_ui_add_group.show()
        def gettext():
            relationship = self.add_relationship_ui.lineEdit.text()
            if relationship != '':
                if relationship not in self.relationships:
                    item = QtWidgets.QTreeWidgetItem(self.treeWidget)
                    item.setText(0, relationship)
                    self.treeWidget.addTopLevelItem(item)
                    self.menu_ui_add_group.close()
                    self.add_relationship_ui.lineEdit.clear()
                    self.relationships.append(relationship)
                else:QtWidgets.QMessageBox.information(self.MainWindow, '提示', '该分组已存在!',
                                                      QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Close,
                                                      QtWidgets.QMessageBox.Close)
            else:QtWidgets.QMessageBox.information(self.MainWindow, '提示', '组名不能为空!', QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Close,
                                                  QtWidgets.QMessageBox.Close)
        try:
            self.add_relationship_ui.submitButton.clicked.disconnect()
        except TypeError:
            pass
        self.add_relationship_ui.submitButton.clicked.connect(gettext)
    def addfriend(self):
        self.menu_ui_add_friend.show()
        def gettext():
            selectroot = self.treeWidget.currentItem()
            friendname = self.add_friend_ui.lineEdit.text()
            if friendname != '':
                cursor = self.db.cursor()
                try:
                    item = QtWidgets.QTreeWidgetItem(selectroot)
                    item.setText(0, friendname)
                    font = QtGui.QFont()
                    font.setPointSize(10)
                    item.setFont(0, font)
                    icon = QtGui.QIcon()
                    icon.addPixmap(QtGui.QPixmap("image/chatbk.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                    query = "INSERT INTO users_relationship (userID,friendID,relationship) VALUES (%s, %s,%s)"
                    cursor.execute(query, (self.username,friendname,selectroot.text(0)))
                    self.db.commit()
                    item.setIcon(0, icon)
                    self.menu_ui_add_friend.close()
                    self.add_friend_ui.lineEdit.clear()
                except Exception as e:
                    print(e)
                    QtWidgets.QMessageBox.information(self.MainWindow, '提示', '好友添加失败',
                                                      QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Close,
                                                      QtWidgets.QMessageBox.Close)
                    item.parent().removeChild(item)
                cursor.close()
            else:
                QtWidgets.QMessageBox.information(self.MainWindow, '提示', '好友名不能为空!',
                                                  QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Close,
                                                  QtWidgets.QMessageBox.Close)
        # 确保在连接前断开先前的连接
        try:
            self.add_friend_ui.submitButton.clicked.disconnect()
        except Exception:
            pass
        self.add_friend_ui.submitButton.clicked.connect(gettext)
    def deletefriend(self):
        item = self.treeWidget.currentItem()
        cursor = self.db.cursor()
        try:
            query = "DELETE FROM users_relationship WHERE userID=%s AND friendID=%s AND relationship=%s"
            cursor.execute(query, (self.username, item.text(0), item.parent().text(0)))
            self.db.commit()
            item.parent().removeChild(item)
        except Exception as e:
            QtWidgets.QMessageBox.information(self.MainWindow, '提示', '删除失败',
                                              QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Close,
                                              QtWidgets.QMessageBox.Close)
        cursor.close()
    def movefriend(self):
        self.menu_ui_move.show()
        def move():
            item = self.treeWidget.currentItem()
            target = self.move_ui.lineEdit.text()
            if target in self.relationships:
                cursor = self.db.cursor()
                try:
                    query = "DELETE FROM users_relationship WHERE userID=%s AND friendID=%s AND relationship=%s"
                    cursor.execute(query, (self.username, item.text(0), item.parent().text(0)))
                    query = "INSERT INTO users_relationship (userID,friendID,relationship) VALUES (%s, %s,%s)"
                    cursor.execute(query, (self.username, item.text(0), target))
                    self.db.commit()
                    item.parent().removeChild(item)
                    try:
                        for i in range(self.treeWidget.topLevelItemCount()):
                            root = self.treeWidget.topLevelItem(i)
                            if root.text(0)==target:
                                root.addChild(item)
                                break
                        self.menu_ui_move.close()
                    except Exception as e:
                        print(e)
                except Exception as e:
                    QtWidgets.QMessageBox.information(self.MainWindow, '提示', '移动失败',
                                                      QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Close,
                                                      QtWidgets.QMessageBox.Close)
                cursor.close()
            else:
                QtWidgets.QMessageBox.information(self.MainWindow, '提示', '分组不存在',
                                                  QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Close,
                                                  QtWidgets.QMessageBox.Close)
        try:
            self.move_ui.submitButton.clicked.disconnect()
        except Exception:
            pass
        self.move_ui.submitButton.clicked.connect(move)