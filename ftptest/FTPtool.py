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
    ftp.set_debuglevel(2)  # �򿪵��Լ���2����ʾ��ϸ��Ϣ
    ftp.connect(ftp_server, 21)  # ����
    ftp.login(username, password)  # ��¼�����������¼���ÿմ����漴��
    return ftp


def downloadfile():
    remotepath = "/yycx/tmp/test/"
    ftp = ftpconnect()
    print
    ftp.getwelcome()  # ��ʾftp��������ӭ��Ϣ
    bufsize = 1024  # ���û�����С
    localpath = 'D:\\python\\ftptest\\'
    fp = open(localpath, 'wb')  # ��дģʽ�ڱ��ش��ļ�
    ftp.retrbinary('RETR ' + remotepath, fp.write, bufsize)  # ���շ��������ļ���д�뱾���ļ�
    ftp.set_debuglevel(0)  # �رյ���
    fp.close()
    ftp.quit()  # �˳�ftp������


def uploadfile(remotepath,localpath):
    # remotepath = "/yycx/tmp/test/tes/"
    print("Ŀ��·����", remotepath)
    ftp = ftpconnect()
    print("��½�ɹ������������ļ�")
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
    # ftp.storbinary('STOR ' + remotepath, fp, bufsize)  # �ϴ��ļ�
        ftp.storbinary(send_cmd, fp)
        ftp.set_debuglevel(0)
        fp.close()  # �ر��ļ�
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

