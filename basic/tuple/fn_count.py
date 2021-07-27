'''
Author: Fullsize
Date: 2021-07-27 14:24:36
LastEditors: Fullsize
LastEditTime: 2021-07-27 14:34:23
FilePath: /practice_python/basic/tuple/fn_count.py
'''
# 返回 指定值在元祖的次数(注意数据类型)
tup1=(1,2,3)
tup2=(1,2,3,1)
print('int 1在tup1的数量',tup1.count(1))
print('int 1在tup2的数量',tup2.count(1))
print('str 1在tup1的数量',tup2.count('1'))
print('str 1在tup2的数量',tup2.count('1'))