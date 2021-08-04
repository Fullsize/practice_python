'''
Author: Fullsize
Date: 2021-08-03 16:58:54
LastEditors: Fullsize
LastEditTime: 2021-08-03 17:13:09
FilePath: /practice_python/basic/class/__init__.py
'''


class PartyA:
    x = 0
    # 构造函数

    def __init__(self, name) -> None:
        print('constructed')
        self.name = name

    def party(self):
        self.x = self.x+1
        print(self.x)

    def __del__(self) -> None:
        print('结束', self.x)


an = PartyA('andi')
an.party()
print(an.name, an.x)
a = PartyA('jon')
print(a.name, a.x)
# an.party()
# an.party()
