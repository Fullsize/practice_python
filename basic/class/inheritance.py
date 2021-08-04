'''
Author: Fullsize
Date: 2021-08-03 17:23:30
LastEditors: Fullsize
LastEditTime: 2021-08-03 17:28:49
FilePath: /practice_python/basic/class/inheritance.py
'''


class A:
    x = 0

    def __init__(self, name) -> None:
        self.name = name
        print('name', self.name)

    def add(self):
        self.x += 1
        print(self.x)


class B(A):
    y = 0

    def touchdown(self):
        self.y += 7
        self.add()
        print(self.name, 'y', self.y)


a = A('a')
a.add()
b = B('b')
b.add()
b.touchdown()