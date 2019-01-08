# coding:utf-8
import requests
import json
import signal
import os
from sys import exit

path = "./download_image\\"


def download(src, id):
    """
    download img
    :param src: image source(url)
    :param id: image id
    :return:
    """
    pic = None
    dir = path + str(id) + '.jpg'
    try:
        pic = requests.get(src, timeout=10)
    except requests.exceptions.ConnectionError:
        # print 'error, %d 当前图片无法下载', %id
        print('图片无法下载')
    if pic:
        fp = open(dir, 'wb')
        fp.write(pic.content)
        fp.close()


if __name__ == "__main__":
    if not os.path.exists(path):
        os.makedirs(path)
    print("请输入明星姓名：")
    query = input()
    url = 'https://www.douban.com/j/search_photo?q=' + query + '&limit=20&start=0'
    html = requests.get(url).text  # 得到返回结果
    response = json.loads(html, encoding='utf-8')  # 将 JSON 格式转换成 Python 对象
    total_amount = response["total"]
    print(total_amount)

    def finish(signum, frame):
        print('Program stop...')
        exit()

    signal.signal(signal.SIGINT, finish)
    signal.signal(signal.SIGTERM, finish)
    ''' for 循环 请求全部的 url '''
    for i in range(0, total_amount, 20):
        url = 'https://www.douban.com/j/search_photo?q=' + query + '&limit=20&start=' + str(i)
        html = requests.get(url).text  # 得到返回结果
        response = json.loads(html, encoding='utf-8')  # 将 JSON 格式转换成 Python 对象
        for image in response['images']:
            image['src'] = image['src'].replace('thumb', 'l')
            print(image['src'])  # 查看当前下载的图片网址
            download(image['src'], image['id'])  # 下载一张图片
