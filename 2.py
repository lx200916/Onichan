import os
import json
import requests
import time
import subprocess
name='欧尼酱SAMA'
url ="https://v1.hitokoto.cn/?c=a&encode=json"
greet=""
file=open('1.ps1','w')

json1=requests.get(url).text
json = json.loads(json1)
time=time.localtime(time.time()).tm_hour
time_table = [('0',"凌晨"),
        ('5',"早晨"),
        ('8',"上午"),
        ('11',"中午"),
        ('13',"下午"),
        ('16',"傍晚"),
        ('19',"晚上")
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
title=date_mark+"好,"+name+"!"
words=json['hitokoto']+"--"+json['from']
print('$text1 = New-BTText -Content '+'\''+title+'\'\n$text2=New-BTText -Content '+'\''+words+'\'\n'+'$image3 = New-BTImage -Source \'C:\Windows\System32'+'\\'+'221.jpg\' -HeroImage\n$binding1 = New-BTBinding -Children $text1,$text2 -HeroImage $image3\n$visual1 = New-BTVisual -BindingGeneric $binding1\n$content1 = New-BTContent -Visual $visual1\nSubmit-BTNotification -Content $content1',file=file)
file.close()

args = [r"C:\WINDOWS\system32\WindowsPowerShell\v1.0\powershell.exe","-ExecutionPolicy","Unrestricted",r"C:\\Users\Administrator\PycharmProjects\\untitled\\venv\\1.ps1"]
ps = subprocess.Popen(args,stdout=subprocess.PIPE)
psReturn = ps.stdout.read()
