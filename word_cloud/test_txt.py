# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 18:37:07 2018

@author: 刘斯齐
"""

#txt_fname = './test.txt'
#file_obj = open(txt_fname,'r')
#
#all_content = file_obj.read()
#all_content = all_content.replace('\n','')
#print(all_content)
import jieba.analyse
import wordcloud
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
#import os
###---------读取文件夹中的文件-------------###
#path = "./wd" #文件夹目录
#files= os.listdir(path) #得到文件夹下的所有文件名称
#s = []
#for file in files: #遍历文件夹
#     if not os.path.isdir(file): #判断是否是文件夹，不是文件夹才打开
#          f = open(path+"/"+file); #打开文件
#          iter_f = iter(f); #创建迭代器
#          str = ""
#          for line in iter_f: #遍历文件，一行行遍历，读取文本
#              str = str + line
#          s.append(str) #每个文件的文本存到list中
#print(s) #打印结果
###------------------------------------###
# 停用词表按照行进行存储，每一行只有一个词语
## 创建停用词list
#def stopwordslist(filepath):
#    stopwords = [line.strip() for line in open(filepath, 'r', encoding='utf-8').readlines()]
#    return stopwords
## 对句子进行分词
#def seg_sentence(sentence):
#    sentence_seged = jieba.cut(sentence.strip())
#    stopwords = stopwordslist('./stopword/中文停用词表.txt')  # 这里加载停用词的路径
#    outstr = ''
#    for word in sentence_seged:
#        if word not in stopwords:
#            if word != '\t':
#                outstr += word
#                outstr += " "
#    return outstr
text = open('E:\Python\word_cloud\词云.txt','r')
content = text.read()
word = jieba.cut(content)  #此处可以增加一个去掉停用词的 

word_count = Counter(word)

mask = np.array(Image.open('alice_color.png'))

wc = wordcloud.WordCloud(background_color="white",font_path=r'C:\Users\Sakura\AppData\Local\Microsoft\Windows\Fonts\HanYi.ttf',
                         mask = mask, 
                         max_words=2000,
                         max_font_size=80)
wc.generate_from_frequencies(word_count)
image_colors = wordcloud.ImageColorGenerator(mask)
wc.recolor(color_func = image_colors)
plt.imshow(wc)
plt.axis('off')
plt.show()
