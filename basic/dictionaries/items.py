'''
Author: Fullsize
Date: 2021-07-27 11:32:37
LastEditors: Fullsize
LastEditTime: 2021-07-27 12:15:19
FilePath: /practice_python/basic/dictionaries/items.py
'''
# 返回一个[(key:value)]的列表 每一项是元组
dicts = {'a': 1, 'b': 2, 'c': 3}
# [('a', 1), ('b', 2), ('c', 3)]
item_list = dicts.items()
print('items', item_list)
for a, b in item_list:
    print(a, b)
