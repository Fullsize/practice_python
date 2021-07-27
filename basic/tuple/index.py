'''
Author: Fullsize
Date: 2021-07-27 11:46:41
LastEditors: Fullsize
LastEditTime: 2021-07-27 14:31:40
FilePath: /practice_python/basic/tuple/tuple.py
'''

# Python 的元组与列表类似，不同之处在于元组的元素不能修改。
# 元组使用小括号 ( )，列表使用方括号 [ ]。
# 元组创建很简单，只需要在括号中添加元素，并使用逗号隔开即可。
tup1=('1','2',3)
tup2=((1,2),(3,4))
print(tup2)
print(tup1[0])
# 解构赋值 二维数组
(x,y)=(4,5)
print(x,y)

# 元组直接可以比较  逐位比较,相同则比较后面,直到比较出大小
(0,1,2)<(0,2,3)
print((0,1,2)<(0,2,3))


# 可以组成一个新的元组
tup3=tup1+tup2
print(tup3)
# 关于元组是不可变的
# 所谓元组的不可变指的是元组所指向的内存中的内容不可变。
tup = ('r', 'u', 'n', 'o', 'o', 'b')
# tup[0] = 'g'     # 不支持修改元素
print(id(tup))     # 查看内存地址
tup = (1,2,3)
print(id(tup))