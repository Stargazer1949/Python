'''
以下代码在MSSQL中运行创建库
create database books
on primary
(name='books',filename='d:\books\books.mdf')
LOG on
(name ='books_log',filename = 'd:\books\books_log.ldf')
use books

create table admin(
aid nchar(4) primary key,
pw nvarchar(20))

create table book(
bookid nchar(4)primary key,
bookname nvarchar(20),
author nvarchar(20),
publisher nvarchar(20),
pubdate date,
price float,
summary nvarchar(50)
quantity nchar（1）)

create table rtype(
rtype nchar(2)primary key ,
rtname nvarchar(20),
rtbooks tinyint,
rtdays tinyint)

create table reader(
rid nchar(4)primary key,
rname nvarchar(20),
rsex nvarchar(4),
runit nvarchar(20),
rtel nvarchar(13),
rtype nchar(2),
rmoney float,
pw nvarchar(20)
foreign key (rtype) references rtype(rtype))

create table borrow(
id int identity(1,1) primary key,
bookid nchar(4),
rid nchar(4),
bdate date,
rdate date,
rm float
foreign key(bookid)references book(bookid),
foreign key(rid)references reader(rid))
'''

import os
import pymssql

def createdb():
    conn = pymssql.connect(host='.', database='master', user='sa', password='1234')
    cur = conn.cursor()
    conn.autocommit(True)
    sql = '''
    create database books
    on primary 
    (name='books',filename='d:\books\books.mdf')
    LOG on 
    (name ='books_log',filename = 'd:\books\books_log.ldf')

    '''
    cur.execute(sql)
    print('数据库建立完毕')

def first():
    print('===图书管理系统===')
    conn = pymssql.connect(host='.', database='master', user='sa', password='1234')
    cur = conn.cursor()
    sql = "select name from sys.databases where name ='books'"
    cur.execute(sql)
    data = cur.fetchall()
    if len(data) == 0:
        ch = input('第一次启动程序，是否新建数据库（Y/N）：')
        if ch == 'y' or ch == 'Y':
            createdb()
        else:
            print('退出系统')
            os.system('pause')
            exit()

def adminlogin():   #管理员登录
    os.system("cls")
    print("===管理员登录===")
    id=input("请输入管理员编号：")
    pw=input("请输入管理员密码：")
    #连接数据库BOOKS
    conn=pymssql.connect(host='.',database='BOOKS',user='sa',password='1234')
    cur=conn.cursor()
    sql="SELECT * FROM admin WHERE aid='"+id+"' and pw='"+pw+"'"
    cur.execute(sql)
    data=cur.fetchall()
    if len(data)==0:
        print("编号或密码错误")
        os.system("pause")
    else:
        adminmain()
    conn.close()

def adminmain():    #管理员界面
    while True:
        os.system("cls")
        print("===图书管理系统(管理员)===")
        print("1、借阅管理")
        print("2、图书管理")
        print("3、读者管理")
        print("9、管理员管理")
        print("0、退出系统")
        ch=input("请选择操作：")
        if ch=='1':
            borrowm()
        elif ch=='2':
            bookm()
        elif ch=='3':
            readerm()
        elif ch=='9':
            adminm()
        elif ch=='0':
            exit()

def bookm():  # 图书管理
    while True:
        os.system("cls")
        print("===图书管理===")
        print("1、添加图书")
        print("2、删除图书")
        print("3、查询图书")
        print("4、修改图书")
        print("0、回到上层菜单")
        ch = input("请选择操作：")
        if ch == '1':
            booki()
        elif ch == '2':
            bookd()
        elif ch == '3':
            books()
        elif ch == '4':
            booku()
        elif ch == '0':
            break

def booki():  # 图书插入
    os.system("cls")
    print("===添加图书===")
    print("请输入图书信息：")
    bookid = input("图书编号：")
    bookname = input("书名：")
    author = input("作者：")
    publisher = input("出版社：")
    pubdate = input("出版日期：")
    price = input("价格：")
    summary = input("简介：")
    quantity = input("是否被借阅：")
    conn = pymssql.connect(host='.', database='BOOKS', user='sa', password='1234')
    cur = conn.cursor()
    sql = "INSERT INTO book VALUES('" + bookid + \
          "','" + bookname + \
          "','" + author + \
          "','" + publisher + \
          "','" + pubdate + \
          "','" + price + \
          "','" + summary + \
          "','" + quantity + \
          "')"
    cur.execute(sql)
    conn.commit()
    conn.close()
    print("图书添加成功")
    os.system("pause")

def bookd():  # 图书删除
    os.system("cls")
    print("===删除图书===")
    print("请输入欲删除图书编号：")
    bookid = input("图书编号：")
    conn = pymssql.connect(host='.', database='BOOKS', user='sa', password='1234')
    cur = conn.cursor()
    sql = "SELECT bookid FROM book WHERE bookid='" + bookid + "'"
    cur.execute(sql)
    data = cur.fetchall()
    if len(data) == 0:
        print("没有该书编号")
    else:
        ch = input("请确认删除（Y/N）：")
        if ch == 'y' or ch == 'Y':
            sql = "DELETE book WHERE bookid='" + bookid + "'"
            cur.execute(sql)
            conn.commit()
            print("图书删除成功")
    conn.close()
    os.system("pause")

def books():  # 图书查询
    os.system("cls")
    print("===查询图书===")
    print("请输入你想查找的图书编号：")
    bookid = input("图书编号")
    conn = pymssql.connect(host='.', database='BOOKS', user='sa', password='1234')
    cur = conn.cursor()
    sql = "SELECT bookid FROM book WHERE bookid='" + bookid + "'"
    cur.execute(sql)
    data = cur.fetchall()
    if len(data)==0:
        print("没有该书编号")
    else:
        sql="SELECT * FROM book WHERE bookid='"+bookid+"'"
        cur.execute(sql)
        conn.close()
        print("图书查询成功")
    os.system("pause")

def booku():  # 图书修改
    os.system("cls")
    print("===修改图书===")
    print("请输入你想修改的图书编号：")
    bookid = input("图书编号")
    conn = pymssql.connect(host='.', database='BOOKS', user='sa', password='1234')
    cur = conn.cursor()
    sql = "SELECT bookid FROM book WHERE bookid='" + bookid + "'"
    cur.execute(sql)
    data = cur.fetchall()
    if len(data)==0:
        print("没有该书编号")
    else:
        bookname = input("书名：")
        author = input("作者：")
        publisher = input("出版社：")
        pubdate = input("出版日期：")
        price = input("价格：")
        summary = input("简介：")
        sql="UPDATE book SET bookname=bookname+%s,author=author+%s,publisher=publisher+%s,pubdate=pubdate+%s,\
        price=price+%s,summary=summary+%s WHERE bookid='"+bookid+"'" %(bookname,author,publisher,pubdate,price,summary)
        cur.execute(sql)
        conn.commit()
        conn.close()
        print("图书修改成功")
    os.system("pause")

def borrowm():  # 借阅管理
    while True:
        os.system("cls")
        print("===借阅管理===")
        print("1、借阅图书")
        print("2、归还图书")
        print("0、回到上层菜单")
        ch = input("请选择操作：")
        if ch == '1':
            borrow_book()
        elif ch == '2':
            return_book()
        elif ch == '0':
            break

def borrow_book():  # 图书借阅
    os.system("cls")
    print("===借阅图书===")
    print("请输入你想借阅的图书编号：")
    bookid = input("图书编号")
    conn = pymssql.connect(host='.', database='BOOKS', user='sa', password='1234')
    cur = conn.cursor()
    sql = "SELECT bookid FROM book WHERE bookid='" + bookid + "'"
    cur.execute(sql)
    data = cur.fetchall()
    if len(data) == 0:
        print("没有该书编号")
    else:
        sql = "SELECT quantity FROM book WHERE bookid='" + bookid + "'"
        cur.execute(sql)
        quantity = cur.fetchone()
        if quantity == 0:
            print("此书已被借阅，借阅信息如下：")
            sql = "SELECT * FROM borrow WHERE bookid='" + bookid + "'"
            cur.execute(sql)
        else:
            print("请输入借阅者的读者编号：")
            rid = input("读者编号")
            date = input("借书日期")
            rdate = input("归还日期")
            rm = input("逾期金额")
            sql = "INSERT INTO borrow VALUES('" + bookid + \
                  "','" + rid + \
                  "','" + date + \
                  "','" + rdate + \
                  "','" + rm + \
                  "')"
            cur.execute(sql)
            sql = "UPDATE book SET quantity=0 WHERE quantity='" + bookid + "'"
            cur.execute(sql)
        conn.close()
        print("图书借阅成功")
    os.system("pause")

def return_book():   # 图书归还
    os.system("cls")
    print("===归还图书===")
    print("请输入你想归还的图书编号：")
    bookid = input("图书编号")
    conn = pymssql.connect(host='.', database='BOOKS', user='sa', password='1234')
    cur = conn.cursor()
    sql = "SELECT bookid FROM borrow WHERE bookid='" + bookid + "'"
    cur.execute(sql)
    data = cur.fetchall()
    if len(data) == 0:
        print("没有该书编号")
    else:
        ch = input("请确认归还（Y/N）：")
        if ch == 'y' or ch == 'Y':
            sql = "DELETE borrow WHERE bookid='" + bookid + "'"
            cur.execute(sql)
            conn.commit()
            print("图书归还成功")
            sql = "UPDATE book SET quantity=1 WHERE quantity='" + bookid + "'"
            cur.execute(sql)
        conn.close()
    os.system("pause")

def readerm():  # 读者管理
    while True:
        os.system("cls")
        print("===读者管理===")
        print("1、添加读者")
        print("2、删除读者")
        print("3、查询读者")
        print("4、修改读者")
        print("0、回到上层菜单")
        ch = input("请选择操作：")
        if ch == '1':
            readeri()
        elif ch == '2':
            readerd()
        elif ch == '3':
            readers()
        elif ch == '4':
            readeru()
        elif ch == '0':
            break

def readeri():  # 读者插入
    os.system("cls")
    print("==读者===")
    print("请输入读者信息：")
    rid = input("读者编号：")
    rname = input("姓名：")
    rsex = input("性别：")
    runit = input("单位：")
    rtel = input("电话：")
    rtype = input("类型号：")
    rmoney = input("余额：")
    pw = input("密码：")
    conn = pymssql.connect(host='.', database='BOOKS', user='sa', password='1234')
    cur = conn.cursor()
    sql = "INSERT INTO reader VALUES('" + rid + \
          "','" + rname + \
          "','" + rsex + \
          "','" + runit + \
          "','" + rtel + \
          "','" + rtype + \
          "','" + rmoney + \
          "','" + pw + \
          "')"
    cur.execute(sql)
    conn.commit()
    conn.close()
    print("读者添加成功")
    os.system("pause")

def readerd():  # 读者删除
    os.system("cls")
    print("===删除读者===")
    print("请输入删除读者编号：")
    rid = input("读者编号：")
    conn = pymssql.connect(host='.', database='BOOKS', user='sa', password='1234')
    cur = conn.cursor()
    sql = "SELECT rid FROM reader WHERE rid='" + rid + "'"
    cur.execute(sql)
    data = cur.fetchall()
    if len(data) == 0:
        print("没有该读者编号")
    else:
        ch = input("请确认删除（Y/N）：")
        if ch == 'y' or ch == 'Y':
            sql = "DELETE reader WHERE rid='" + rid + "'"
            cur.execute(sql)
            conn.commit()
            print("读者删除成功")
    conn.close()
    os.system("pause")

def readers():  # 读者查询
    os.system("cls")
    print("===查询读者===")
    print("请输入你想查找的读者编号：")
    rid = input("读者编号")
    conn = pymssql.connect(host='.', database='BOOKS', user='sa', password='1234')
    cur = conn.cursor()
    sql = "SELECT rid FROM reader WHERE rid='" + rid + "'"
    cur.execute(sql)
    data = cur.fetchall()
    if len(data)==0:
        print("没有该读者编号")
    else:
        sql="SELECT * FROM reader WHERE rid='"+rid+"'"
        cur.execute(sql)
        conn.close()
        print("读者查询成功")
    os.system("pause")

def readeru():  # 读者修改
    os.system("cls")
    print("===修改读者===")
    print("请输入你想修改的读者编号：")
    rid = input("读者编号")
    conn = pymssql.connect(host='.', database='BOOKS', user='sa', password='1234')
    cur = conn.cursor()
    sql = "SELECT rid FROM reader WHERE rid='" + rid + "'"
    cur.execute(sql)
    data = cur.fetchall()
    if len(data)==0:
        print("没有该读者编号")
    else:
        rname = input("姓名：")
        rsex = input("性别：")
        runit = input("单位：")
        rtel = input("电话：")
        rtype = input("类型号：")
        rmoney = input("余额：")
        pw = input("密码：")
        sql="UPDATE reader SET rname=rname+%s,rsex=rsex+%s,runit=runit+%s,rtel=rtel+%s,rtype=rtype+%s,\
        rmoney=rmoney+%s,pw=pw+%s WHERE rid='"+rid+"'" %(rname,rsex,runit,rtel,rtype,rmoney,pw)
        cur.execute(sql)
        conn.commit()
        conn.close()
        print("读者修改成功")
    os.system("pause")

def adminm():  # 管理员管理
    while True:
        os.system("cls")
        print("===管理员管理===")
        print("1、添加管理员")
        print("2、删除管理员")
        print("3、修改管理员")
        print("0、回到上层菜单")
        ch = input("请选择操作：")
        if ch == '1':
            admini()
        elif ch == '2':
            admind()
        elif ch == '3':
            adminu()
        elif ch == '0':
            break

def admini():  # 管理员插入
    os.system("cls")
    print("==管理员===")
    print("请输入管理员信息：")
    aid = input("管理员编号：")
    pw = input("密码：")
    conn = pymssql.connect(host='.', database='BOOKS', user='sa', password='1234')
    cur = conn.cursor()
    sql = "INSERT INTO admin VALUES('" + aid + \
          "','" + pw + \
          "')"
    cur.execute(sql)
    conn.commit()
    conn.close()
    print("管理员添加成功")
    os.system("pause")

def admind():  # 管理员删除
    os.system("cls")
    print("===删除管理员===")
    print("请输入删除管理员编号：")
    aid = input("管理员编号：")
    conn = pymssql.connect(host='.', database='BOOKS', user='sa', password='1234')
    cur = conn.cursor()
    sql = "SELECT aid FROM admin WHERE aid='" + aid + "'"
    cur.execute(sql)
    data = cur.fetchall()
    if len(data) == 0:
        print("没有该管理员编号")
    else:
        ch = input("请确认删除（Y/N）：")
        if ch == 'y' or ch == 'Y':
            sql = "DELETE admin WHERE aid='" + aid + "'"
            cur.execute(sql)
            conn.commit()
            print("管理员删除成功")
    conn.close()
    os.system("pause")

def adminu():  # 管理员修改
    os.system("cls")
    print("===修改管理员===")
    print("请输入你想修改的管理员编号：")
    aid = input("管理员编号")
    conn = pymssql.connect(host='.', database='BOOKS', user='sa', password='1234')
    cur = conn.cursor()
    sql = "SELECT aid FROM admin WHERE aid='" + aid + "'"
    cur.execute(sql)
    data = cur.fetchall()
    if len(data)==0:
        print("没有该管理员编号")
    else:
        pw = input("密码：")
        sql="UPDATE admin SET pw=pw+%s WHERE aid='"+aid+"'" %(pw)
        cur.execute(sql)
        conn.commit()
        conn.close()
        print("管理员修改成功")
    os.system("pause")

def readerlogin():  #读者登录
    os.system("cls")
    print("===读者登录===")
    global uniqueid
    uniqueid = input("请输入读者编号：")
    pw = input("请输入读者密码：")
    # 连接数据库BOOKS
    conn = pymssql.connect(host='.', database='BOOKS', user='sa', password='1234')
    cur = conn.cursor()
    sql = "SELECT * FROM reader WHERE rid='" + uniqueid + "' and pw='" + pw + "'"
    cur.execute(sql)
    data = cur.fetchall()
    if len(data) == 0:
        print("编号或密码错误")
        os.system("pause")
    else:
        readermain()
    conn.close()

def readermain():  # 读者界面
    while True:
        os.system("cls")
        print("===图书管理系统(读者)===")
        print("1、图书查询")
        print("2、借阅查询")
        print("0、退出系统")
        ch = input("请选择操作：")
        if ch == '1':
            booksearch()
        elif ch == '2':
            borrowsearch()
        elif ch == '0':
            exit()

def booksearch():  # 查询图书界面
    os.system("cls")
    print("===查询图书===")
    print("请输入你想查找的图书编号：")
    bookid = input("图书编号")
    conn = pymssql.connect(host='.', database='BOOKS', user='sa', password='1234')
    cur = conn.cursor()
    sql = "SELECT bookid FROM book WHERE bookid='" + bookid + "'"
    cur.execute(sql)
    data = cur.fetchall()
    if len(data) == 0:
        print("没有该书编号")
    else:
        sql = "SELECT * FROM book WHERE bookid='" + bookid + "'"
        cur.execute(sql)
        conn.close()
        print("图书查询成功")
    os.system("pause")

def borrowsearch():  # 查询借阅界面
    os.system("cls")
    print("===查询借阅===")
    conn = pymssql.connect(host='.', database='BOOKS', user='sa', password='1234')
    cur = conn.cursor()
    sql = "SELECT * FROM borrow WHERE rid='" + uniqueid + "'"
    cur.execute(sql)
    conn.close()
    os.system("pause")

first()
#system("color DF")	改变屏幕背景颜色和文字颜色
#0黑 1蓝 2绿 3湖蓝 4红 5紫 6黄 7白 8灰 9淡蓝 A淡绿 B淡浅绿 C淡红 D淡紫 E淡黄 F亮白
os.system("color F0")
while True:
    os.system("cls")
    print("===图书管理系统===")
    print("1、管理员登录")
    print("2、读者登录")
    print("0、退出系统")
    ch=input("请选择操作：")
    if ch=='1':
        adminlogin()
    elif ch=='2':
        readerlogin()
    elif ch=='0':
        exit()
#os.system("pause")