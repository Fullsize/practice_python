'''
Author: Fullsize
Date: 2021-07-29 09:59:14
LastEditors: Fullsize
LastEditTime: 2021-07-29 09:59:16
FilePath: /practice_python/urllib/index.py
'''
'''
Author: Fullsize
Date: 2021-07-29 09:59:14
LastEditors: Fullsize
LastEditTime: 2021-07-29 09:59:15
FilePath: /practice_python/urllib/index.py
'''
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
fhand = urllib.request.urlopen('https://www.baidu.com/')
for i in fhand:
    print(i.decode().strip())
