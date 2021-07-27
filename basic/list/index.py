'''
Author: Fullsize
Date: 2021-07-21 18:07:00
LastEditors: Fullsize
LastEditTime: 2021-07-21 18:20:21
FilePath: /practice_python/basic/list/list.py
'''
#
ls = ['1', '2', '3', '4']
alphabet=['A','B','C','D','E','F']
for i in ls:
    print(i)
print('列表第一个', ls[0])

# 操作
print('\n\n操作')
ls[0] = 5
print(ls)
print('列表第一个', ls[0])

# 长度 range
print('\n\n长度')
strA='aaaaaa'
print(len(strA))
print(len(ls))
print(range(len(alphabet)))