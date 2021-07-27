'''
Author: Fullsize
Date: 2021-07-27 15:49:25
LastEditors: Fullsize
LastEditTime: 2021-07-27 16:09:18
FilePath: /practice_python/basic/regex/findall.py
'''
# findall 以列表的形式返回能匹配的子串|	 返回符合条件的数据 数组形式
import re
x = 'woeewe 1 ewewe we weqeq fqrqr 5 qeqeqeq 6'
y = re.findall(r'[0-9]+', x)
print(y)
y = re.findall(r'[ABCD]+', x)
print(y)