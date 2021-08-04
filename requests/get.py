'''
Author: Fullsize
Date: 2021-07-29 17:53:18
LastEditors: Fullsize
LastEditTime: 2021-07-29 17:53:18
FilePath: /practice_python/requests/ex_1.py
'''
import requests
r = requests.get('https://www.wanmen.org')
r.encoding = 'utf-8'
file1 = open("test.html", mode='w')
file1.write(r.text)
print(r.text, r.encoding)
