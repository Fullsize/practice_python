'''
Author: Fullsize
Date: 2021-07-27 11:14:27
LastEditors: Fullsize
LastEditTime: 2021-07-27 11:29:09
FilePath: /practice_python/basic/dictionaries/keys.py
'''
# 返回key的列表视图
dicts={'a':1,'b':2,'c':3}
key_list=dicts.keys()
print('keys',key_list)
for i in key_list:
	print(i)