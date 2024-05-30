# -*-coding:utf-8-*-

from socket import *
import threading
import re
# from coonect_mysql import connect_to_mysql
import mysql.connector

client_list = []  # 已登录的用户

user_list = []

alive_user = 0
group_list = []
# 已经在线的用户
user_client = []


# todo:修改数据为数据库文件
# todo:修改非服务器的接收信息处理
# todo:修改图标
# todo:阅读代码
# todo:上下线更新状态/数据库


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


def retdata():
    return user_list


def getinfo(db):
    global alive_user
    if db != None:
        cursor = db.cursor()
        cursor.execute("select * from ast_chatsystem.user")
        result = cursor.fetchall()
        for row in result:
            print("getinfo", row)
            id, password, is_alive, headpath = row
            user_list.append((id, password))
            if is_alive:
                alive_user += 1
        cursor.execute("select * from ast_chatsystem.group")
        result = cursor.fetchall()
        name_list = []
        for row in result:
            print("in getinfo result", result)
            name, id, group_headpath = row
            name_list.append(name)
        group_list.append(name_list)
        print(group_list)
    else:
        print("err")
    # print(user_list)
    # user_l = len(user_list)
    print("###", alive_user)
    return retdata()


# db.close()

def isUser(db, logindata):
    # print("in isUser")
    cursor = db.cursor()
    # print(logindata)
    ID = logindata[1]
    password = logindata[2]
    query = "select * from ast_chatsystem.user where ID=%s and password=%s"
    cursor.execute(query, (ID, password))
    result = cursor.fetchall()
    # print("isUser函数中:", result)
    return result


# 改变用户在线状态
def change_alive(db, logindata):
    try:
        cursor = db.cursor()
        ID = logindata[1]
        print(ID)
        query = "update ast_chatsystem.user set is_online=NOT is_online where ID = %s"
        cursor.execute(query, (ID,))
        db.commit()
        print("修改成功")
    except Exception as e:
        print(e)


def signup_db(regeisterdata, clientsock):
    db = connect_to_mysql()
    cursor = db.cursor()
    ID = regeisterdata[1]
    query = "select * from ast_chatsystem.user where ID=%s"
    cursor.execute(query, (ID))
    result = cursor.fetchall()
    # print("isUser函数中:", result)
    if result:
        signup_bkinfo = "false"
        clientsock.send(signup_bkinfo.encode())
    else:
        query = "INSERT INTO user (ID, password) VALUES (%s, %s)", (regeisterdata[1], regeisterdata[2])
        cursor.execute(query)
        signup_bkinfo = "true"
        clientsock.send(signup_bkinfo.encode())


def login_db(logindata, clientsock):
    db = connect_to_mysql()
    getinfo(db)
    res = isUser(db, logindata)
    # print(res[0][2])
    user_l = len(user_list)
    # 非空则代表数据库中有所查找的用户
    if res:
        # res[2]是数据库中对应user_alive属性
        if res[0][2]:
            # 在线
            login_bkinfo = 'false-login'
            clientsock.send(login_bkinfo.encode())
        else:
            # 不在线就能登录进去
            usercl = []
            usercl.append(logindata[1])
            usercl.append(clientsock)
            login_bkinfo = 'true'
            user_client.append(usercl)
            print(user_client)
            clientsock.send(login_bkinfo.encode())

            # change_alive(db, logindata)        # 修改为在线 / 暂时注释掉用于调试
            # todo 调试完成后重新打开注释
    else:
        # 数据库查不到
        login_bkinfo = 'false-id/pw'
        clientsock.send(login_bkinfo.encode())


def tcplink(clientsock, clientaddress):
    group_l = len(group_list)
    while True:
        recvdata = clientsock.recv(1024).decode('utf-8')
        recvdata_list = recvdata.split('$%')  # 信息间隔符为空格
        print(recvdata_list)
        if str(recvdata_list[0]) == 'login':  # 处理登录消息
            login_db(recvdata_list, clientsock)
        elif str(recvdata_list[0]) == 'signup':
            signup_db(recvdata_list, clientsock)
        elif str(recvdata_list[0]) == 'wechat_req':  # 处理群聊消息
            for y in range(0, group_l):
                if str(group_list[y][0]) == str(recvdata_list[1]):
                    requser = str(recvdata_list[2]) + ' ' + '加入群聊'
                    group_list[y].append(clientsock)
                    # print('my clientsock is : ' + str(clientsock))
                    print(group_list[y])
                    groupl = len(group_list[y])
                    print(groupl)
                    if True:  # groupl>2
                        for h in range(1, groupl):
                            group_list[y][h].send(requser.encode())
                    break
        elif str(recvdata_list[0]) == 'wechat_quit':  # 处理群聊消息
            for y in range(0, group_l):
                if str(group_list[y][0]) == str(recvdata_list[1]):
                    requser = str(recvdata_list[2]) + ' ' + '退出群聊'
                    group_list[y].remove(clientsock)
                    print(group_list[y])
                    groupl = len(group_list[y])
                    if True:
                        for h in range(1, groupl):
                            group_list[y][h].send(requser.encode())
                    else:
                        clientsock.send(requser.encode())
                    break
        elif str(recvdata_list[0]) == 'wechat':
            for wl in range(0, group_l):
                if str(group_list[wl][0]) == str(recvdata_list[1]):  ###
                    senddata = str(recvdata_list[2]) + ":" + str(recvdata_list[3])
                    l = len(group_list[wl])
                    try:
                        if l >= 2:
                            for x in range(1, l):
                                group_list[wl][x].send(senddata.encode())
                        else:
                            clientsock.send(senddata.encode())
                            break
                        print("群聊信息" + str(senddata) + str(clientaddress))
                    except ValueError:
                        break
        elif str(recvdata_list[0]) == 'personal':  # 处理私聊消息
            user_cl = len(user_client)
            send_info = str(recvdata_list[1]) + ":" + str(recvdata_list[3])
            z = 1
            for pl in range(0, user_cl):
                if user_client[pl][0] == recvdata_list[2]:
                    for ql in range(0, user_cl):
                        if user_client[ql][0] == recvdata_list[1]:
                            user_client[ql][1].send(send_info.encode())
                    user_client[pl][1].send(send_info.encode())
                    print(clientaddress)
                    break
                elif z == user_cl:
                    back = str(recvdata_list[2]) + '不在线'
                    backtext = 'personal$%' + recvdata_list[1] + '$%' + recvdata_list[2] + '$%' + back
                    print('sendback text is: ' + backtext)
                    clientsock.send(back.encode())
                z = z + 1
        elif str(recvdata_list[0]) == 'voicechat':  # 处理语音聊天消息
            length = len(recvdata_list)
            if str(recvdata_list[length - 2]) == 'end':
                user_cl = len(user_client)  # list[1] sender  list[2] receiver
                # send_info = str(recvdata_list[1])+":"+str(recvdata_list[3])
                length = len(recvdata_list)
                z = 1
                for pl in range(0, user_cl):
                    if user_client[pl][0] == recvdata_list[2]:
                        p1 = re.compile(r'[(](.*?)[)]', re.S)  # 正则表达式提取客户端的地址
                        list = re.findall(p1, str(user_client[pl][1]))
                        list1 = list[1].split(',')
                        result = ''.join(list1)
                        result = result + '$%' + 'ignore' + '$%' + 'voicechat_accept'  # 发送给发起方
                        print(list1)

                        for ql in range(0, user_cl):
                            if user_client[ql][0] == recvdata_list[1]:
                                p1 = re.compile(r'[(](.*?)[)]', re.S)  # 正则表达式提取客户端的地址
                                list = re.findall(p1, str(user_client[ql][1]))
                                list1 = list[1].split(',')
                                send_info = ''.join(list1)
                                if recvdata_list[length - 2] == 'end':
                                    send_info = ''.join('end')
                                send_info = send_info + '$%' + 'voicechat_request'  # 发送给接收方
                                print('send_info is:' + send_info)
                                user_client[pl][1].send(send_info.encode())
                                # user_client[ql][1].send(result.encode())
                        print(clientaddress)

                        break
                    elif z == user_cl:
                        back = str(recvdata_list[2]) + '不在线'
                        clientsock.send(back.encode())
                    z = z + 1
            else:
                user_cl = len(user_client)  # list[1] sender  list[2] receiver
                # send_info = str(recvdata_list[1])+":"+str(recvdata_list[3])
                length = len(recvdata_list)
                z = 1
                for pl in range(0, user_cl):
                    if user_client[pl][0] == recvdata_list[2]:
                        p1 = re.compile(r'[(](.*?)[)]', re.S)  # 正则表达式提取客户端的地址
                        list = re.findall(p1, str(user_client[pl][1]))
                        list1 = list[1].split(',')
                        result = ''.join(list1)
                        result = result + '$%' + 'voicechat_accept'  # 发送给发起方
                        print(list1)

                        for ql in range(0, user_cl):
                            if user_client[ql][0] == recvdata_list[1]:
                                p1 = re.compile(r'[(](.*?)[)]', re.S)  # 正则表达式提取客户端的地址
                                list = re.findall(p1, str(user_client[ql][1]))
                                list1 = list[1].split(',')
                                send_info = ''.join(list1)
                                if recvdata_list[length - 2] == 'end':
                                    send_info = ''.join('end')
                                send_info = send_info + '$%' + 'voicechat_request'  # 发送给接收方
                                print('send_info is:' + send_info)
                                user_client[pl][1].send(send_info.encode())
                                user_client[ql][1].send(result.encode())
                        print(clientaddress)

                        break
                    elif z == user_cl:
                        back = str(recvdata_list[2]) + '不在线'
                        clientsock.send(back.encode())
                    z = z + 1
        elif str(recvdata_list[0]) == 'filesend':  # 处理文件传输
            user_cl = len(user_client)  # list[1] sender  list[2] receiver
            # send_info = str(recvdata_list[1])+":"+str(recvdata_list[3])
            z = 1
            for pl in range(0, user_cl):
                if user_client[pl][0] == recvdata_list[2]:
                    p1 = re.compile(r'[(](.*?)[)]', re.S)  # 正则表达式提取客户端的地址
                    list = re.findall(p1, str(user_client[pl][1]))
                    list1 = list[1].split(',')
                    result = ''.join(list1)
                    result = result + '$%' + 'filesend_accept'
                    print(list1)

                    for ql in range(0, user_cl):
                        if user_client[ql][0] == recvdata_list[1]:
                            p1 = re.compile(r'[(](.*?)[)]', re.S)  # 正则表达式提取客户端的地址
                            list = re.findall(p1, str(user_client[ql][1]))
                            list1 = list[1].split(',')
                            send_info = ''.join(list1)
                            send_info = send_info + '$%' + 'filesend_request'
                            print('send_info is:' + send_info)
                            user_client[pl][1].send(send_info.encode())
                            user_client[ql][1].send(result.encode())
                    print(clientaddress)

                    break
                elif z == user_cl:
                    back = str(recvdata_list[2]) + '不在线'
                    clientsock.send(back.encode())
                z = z + 1
        else:
            print('无法识别：')
            print(recvdata_list[0])
            break

    clientsock.close()
    del client_list[-1]


if __name__ == "__main__":
    from netifaces import interfaces, ifaddresses, AF_INET

    ifaceName = interfaces()[2]
    # address = [i['addr'] for i in ifaddresses(ifaceName).setdefault(AF_INET, [{'addr': 'No IP addr'}])][0]

    # address='127.0.0.1'
    # address='192.168.31.142'
    # address = '192.168.31.90'
    s = socket(AF_INET, SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    address = s.getsockname()[0]
    port = 8000
    s = socket(AF_INET, SOCK_STREAM)
    s.bind((address, port))
    s.listen(10)  # 最大连接数

    while True:
        clientsock, clientaddress = s.accept()
        client_list.append(clientsock)
        print('connect from:', clientaddress)  # clientaddress 包含IP与端口
        t = threading.Thread(target=tcplink, args=(clientsock, clientaddress))  # 新创建的线程
        t.start()
    # s.close()
