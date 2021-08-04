'''
Author: Fullsize
Date: 2021-08-03 15:59:34
LastEditors: Fullsize
LastEditTime: 2021-08-03 16:06:49
FilePath: /practice_python/basic/class/index.py
'''


class FirstClass:
    x = 0
    b = 'a'

    def fn(self):
        self.x = self.x+1
        print(self.x)


an = FirstClass()

an.fn()  # FirstClass.fn(an)
an.fn()
an.fn()
an.fn()
print('dir', dir(an))
print('type', type(an))
