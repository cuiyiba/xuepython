'''
    r:读取
    w：写入
    +:可读可写
    a:附加

    b:字节：mp3,mp4,图片
'''
import time

f1 = open (file="baidu_x_system.log", mode="r", encoding="utf-8")
# f2 = open(file="古诗.txt",mode="w",encoding="utf-8")
# coding:utf-8
# with True:
aa = []
p = 0
a = 0
b = 0
c = 0
d = ""

with f1 as f:
    for line in f.readlines ():
        data = line.split ('\n\t')
        for str in data:
            sub_str = str.split (' ')
        if sub_str:
            aa.append (sub_str)
    for i in aa:
        # print(i[0])
        if i[0] == "10.155.24.132":
            p = p + 1
        print ("10.155.24.132", "出现了", p, "次")
        if i[0] == "16.155.34.132":
            a = a + 1
            print ("16.155.34.132", "出现了", a, "次")
        if i[0] == "56.78.35.131":
            b = b + 1
            print ("56.78.35.131", "出现了", b, "次")
        if i[0] == "46.76.185.36":
            c = c + 1
            print ("46.76.185.36", "出现了", c, "次")
    time.sleep (3)
