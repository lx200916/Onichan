# coding=gbk
import os
import json
import requests
import time
from win10toast import ToastNotifier
toaster = ToastNotifier()

name='ŷ�ὴSAMA'
url ="https://v1.hitokoto.cn/?c=a&encode=json"
greet=""

json1=requests.get(url).text
json = json.loads(json1)
time=time.localtime(time.time()).tm_hour
time_table = [('0',"�賿"),
        ('5',"�糿"),
        ('8',"����"),
        ('11',"����"),
        ('13',"����"),
        ('16',"����"),
        ('19',"����")
        ]
date_mark = ''
hour = ''
for i in time_table:
    if int(time) > int(i[0]):
        if time_table.index(i) == 6:
            date_mark = time_table[-1][1]
            break
        continue
    else:
        if int(time)==int(i[0]):
            date_mark = i[1]
            break
        date_mark = time_table[time_table.index(i)-1][1]
        break
title=date_mark+"��,"+name+"!"
words=json['hitokoto']+"--"+json['from']
toaster.show_toast(title,
words,icon_path='favicon.ico',
duration=10)
