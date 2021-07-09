'''
Author: Fullsize
Date: 2021-07-09 14:13:11
LastEditors: Fullsize
LastEditTime: 2021-07-09 14:16:56
FilePath: /practice_python/try_except.py
'''
str = 'hello Fullsize'
try:
    isStr = int(str)
except:
    isStr = False
print(isStr)
str = '123'
try:
    isStr = int(str)
except:
    isStr = False
print(isStr)
