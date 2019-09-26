#!/usr/bin/python
# -*- coding: GB18030 -*-

from ftplib import FTP
import ftplib
import os
import sys


def ftpconnect():
    ftp_server = '192.168.32.132'
    username = 'cib'
    password = 'cib'
    ftp = FTP()
    ftp.set_debuglevel(2)  # 打开调试级别2，显示详细信息
    ftp.connect(ftp_server, 21)  # 连接
    ftp.login(username, password)  # 登录，如果匿名登录则用空串代替即可
    return ftp


def downloadfile():
    remotepath = "/yycx/tmp/test/"
    ftp = ftpconnect()
    print
    ftp.getwelcome()  # 显示ftp服务器欢迎信息
    bufsize = 1024  # 设置缓冲块大小
    localpath = 'D:\\python\\ftptest\\'
    fp = open(localpath, 'wb')  # 以写模式在本地打开文件
    ftp.retrbinary('RETR ' + remotepath, fp.write, bufsize)  # 接收服务器上文件并写入本地文件
    ftp.set_debuglevel(0)  # 关闭调试
    fp.close()
    ftp.quit()  # 退出ftp服务器


def uploadfile(remotepath,localpath):
    # remotepath = "/yycx/tmp/test/tes/"
    print("目标路径：", remotepath)
    ftp = ftpconnect()
    print("登陆成功，开发发送文件")
    try:
        ftp.cwd(remotepath)
    except ftplib.error_perm:
        try:
            ftp.mkd(remotepath)
            ftp.cwd(remotepath)
        except ftplib.error_perm:
            print("you have no Permission to mkdir")
    bufsize = 1024
    # localpath = 'D:\\python\\ftptest\\'
    print("local path", localpath)
    os.chdir( localpath )
    fileList = os.listdir(localpath)
    for file in fileList:
        filePath = localpath + file
        fp = open(filePath, 'rb')
        send_cmd = 'STOR ' + file
    # ftp.storbinary('STOR ' + remotepath, fp, bufsize)  # 上传文件
        ftp.storbinary(send_cmd, fp)
        ftp.set_debuglevel(0)
        fp.close()  # 关闭文件
    ftp.quit()


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("need 2 params")
        sys.exit(1)
    # remotepath = "/yycx/tmp/test/tes/"
    remotepath = sys.argv[1]
    localpath = sys.argv[2]
    # localpath = 'D:\\python\\ftptest\\'
    uploadfile(remotepath, localpath)

