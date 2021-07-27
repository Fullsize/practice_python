'''
Author: Fullsize
Date: 2021-07-22 17:23:54
LastEditors: Fullsize
LastEditTime: 2021-07-23 10:09:09
FilePath: /practice_python/basic/list/sorted.py
'''
# sorted 不会改变原数据,支持任何类型数据排序
ls_one=['fagew','eferewq','weeee'];
print(sorted(ls_one))


def sortA(value):
		return value['oder']
ls_test = [{'level': 5,'oder':1}, {'level': 4,'oder':2}, {
    'level': 3,'oder':3}, {'level': 2,'oder':4}, {'level': 1,'oder':5}]
print(sorted(ls_test,key=sortA,reverse=True))