'''
Author: Fullsize
Date: 2021-07-22 16:32:36
LastEditors: Fullsize
LastEditTime: 2021-07-23 10:15:13
FilePath: /practice_python/basic/list/sort.py
'''
# sort排序会改变原数据


# key -- 主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序。
# reverse -- 排序规则，reverse = True 降序， reverse = False 升序（默认）。
ls = [1, 2, 3, 4, 5]
# 默认 sort(key=None, reverse=False)
ls.sort()
#
# ls.sort(reverse=True)
ls.sort(reverse=True)
print(ls)

ls_test = [{'level': 5, 'oder': 1}, {'level': 4, 'oder': 2}, {
    'level': 3, 'oder': 3}, {'level': 2, 'oder': 4}, {'level': 1, 'oder': 5}]


def sortLevel(elem):
    return elem['level']


# 根据数据的level进行排序
ls_test.sort(key=sortLevel)
print(ls_test)

