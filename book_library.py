#!usr/bin/env python3

import requests
import cv2

if __name__ == "__main__":
    # headers = {
    #     "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
    #                   "Chrome/70.0.3538.102 Safari/537.36"
    # }
    # uri = str("http://seat.lib.whu.edu.cn/history?type=SEAT")
    # res = requests.get(uri, headers=headers)
    # print(res.text)
    url = str("http://seat.lib.whu.edu.cn/")#auth/signIn
    s = requests.Session()

    s.headers['User-agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) ' \
                               'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36'
    # s.headers['Accept'] = "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8"
    # s.headers['Accept-Encoding'] = "gzip, deflate"
    # s.headers['Accept-Language'] = "zh-CN,zh;q=0.9,en;q=0.8"
    # s.headers['Connection'] = "keep-alive"
    # s.headers['Content-Type'] = "application/x-www-form-urlencoded"
    # s.headers['Cookie'] = "JSESSIONID=E6FCD358EFEE5430AA29C1BFB557BDF8"
    # s.headers['Host'] = "seat.lib.whu.edu.cn"
    # s.headers['Origin'] = "http://seat.lib.whu.edu.cn"
    # s.headers['Referer'] = "http://seat.lib.whu.edu.cn/login?targetUri=%2F"
    # s.headers['Upgrade-Insecure-Requests'] = "1"
    # s.headers['Cache-Control'] = "max-age=0"
    # s.headers['Content-Length'] = "213"

    # data = {"SYNCHRONIZER_TOKEN": "7507289d-ff86-415a-ac15-f99d87c4eb23",
    #         "SYNCHRONIZER_URI": "/login",
    #         "username": "2015301200168",
    #         "password": "304711",
    #         "authid": "-1",
    #         "appId": "a3a5c1faff9e41c2b2447a52c5bd7ea0",
    #         "appAuthKey": "a109981dd38540d5b20b4af760d7f6f1"}

    captchaUrl = url + "simpleCaptcha/captcha"
    loginUrl = url + "auth/signIn"
    data = {"username": "2015301200168",
            "password": "304711"}
    captchaImg = s.get(captchaUrl)
    # cv2.imwrite("./test.png", captchaImg.content)
    cv2.imshow("123", captchaImg.content)
    cv2.waitKey()
    print(123)
    #res = s.post(url, data=data)
    #print(res.history)
    #print(res.text)
