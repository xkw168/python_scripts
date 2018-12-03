#!/usr/bin/env python3

import os
import email


def download_attachment(mailname, datapath):
    """
    download the attachment of .eml file
    :param mailname: path of .eml path
    :param datapath: path of the attachment file
    :return: None
    """
    fp = open(mailname, "r", encoding='gbk')
    msg = email.message_from_file(fp)

    for par in msg.walk():
        if not par.is_multipart():
            name = par.get_param("name")

            if name:
                h = email.header.Header(name)

                data = par.get_payload(decode=True)

                data_name = str(h).replace('/', '_')
                f = open(datapath + '\\' + data_name, 'wb')
                f.write(data)
                f.close()


if __name__ == '__main__':
    dir = "C:\\Users\\xkw\\Desktop\\srcData\\"    #邮件存放路径
    datapath = "C:\\Users\\xkw\\Desktop\\destData"   #附件存放路径
    count = 0

    for filename in os.listdir(dir):
        filename = dir + filename #由于邮件名出现中文，所以统一用utf8编码，便于读取
        print(filename)
        count += 1
        filename.encode('gbk')
        datapath.encode('gbk')
        download_attachment(filename, datapath)
