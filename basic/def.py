'''
Author: Fullsize
Date: 2021-07-09 14:50:02
LastEditors: Fullsize
LastEditTime: 2021-07-09 17:47:46
FilePath: /practice_python/basic/def.py
'''
# 不同于js的函数声明,py用def来声明function,调用方式都是一样的:fnName()
# 不存在js的变量提升


from typing import Tuple


def callFn() -> str:
    return 'call'


def thing(a: str, b) -> str:
    return 'this is function'+a+b()


# 函数调用
print(thing('1', callFn))
print('default')
print(thing('2', callFn))


def isStr(a) -> bool:
    return type(a) == str


def defaultF():
    pass


def toInt(a):
    try:
        return int(a)
    except:
        return False


print(defaultF, toInt('1.2a'))
x = 5


def concat(a, *b):
    x = a
    for c in b:
        x = x+c
    return x


print(concat(1, 2, 3, 4, 5, 6, 7, 8, 9))


def chain(**kwargs):
    return kwargs


print(chain(a=1, b=2))
