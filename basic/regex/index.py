'''
Author: Fullsize
Date: 2021-07-27 14:39:00
LastEditors: Fullsize
LastEditTime: 2021-07-27 15:48:47
FilePath: /practice_python/basic/regex/index.py
'''
# 正则同js正则,需要先引入正则模块
import re
phone_number=input('请输入手机号: ')
print(phone_number)
if re.match(r"1[358]\d{9}",phone_number):
	print('正确的手机号')
else:
	print('错误的手机号')