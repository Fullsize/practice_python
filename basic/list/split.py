'''
Author: Fullsize
Date: 2021-07-22 17:30:47
LastEditors: Fullsize
LastEditTime: 2021-07-27 10:39:01
FilePath: /practice_python/basic/list/split.py
'''
# 和js的split差不多,但存在第二参数,代表分割次数
# str.split(str="", num=string.count(str))
# str -- 分隔符，默认为所有的空字符，包括空格、换行(\n)、制表符(\t)等。
# num -- 分割次数。默认为 -1, 即分隔所有。
str1 = 'a b c'
str2 = 'a,b,c'
print(str1.split())
print(str2.split())
print(str2.split(','))
print('分割次数一次', str2.split(',', 1))
print('分割次数二次', str2.split(',', 2))
print('分割次数负一次(所有)', str2.split(',', -1))