#!usr/bin/env python3
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

if __name__ == "__main__":
    # headers = {
    #     "User-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
    #                   "(KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36"}
    # uri = str("http://seat.lib.whu.edu.cn/login")
    # res = requests.get(uri, headers=headers)
    # print(res.text)
    browser = webdriver.Android()
    browser.get("https://whu.pt/torrents.php?cat2=1&cat402=1&cat417=1&cat416=1&cat418=1")
    browser.implicitly_wait(10)
