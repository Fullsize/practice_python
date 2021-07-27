'''
Author: Fullsize
Date: 2021-07-27 11:29:23
LastEditors: Fullsize
LastEditTime: 2021-07-27 11:32:05
FilePath: /practice_python/basic/dictionaries/values.py
'''
# 返回value的列表视图
dicts={'a':1,'b':2,'c':3}
value_list=dicts.values()
print('values',value_list)
for i in value_list:
	print(i)