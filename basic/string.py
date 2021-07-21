'''
Author: Fullsize
Date: 2021-07-15 11:17:47
LastEditors: Fullsize
LastEditTime: 2021-07-15 12:08:56
FilePath: /practice_python/basic/string.py
'''
# 字符串数组?
user_name='benming'
print(user_name[0])
print(user_name[3-1])
# len 获取数据长度
print(len('123'))
print(len([1,2,3]))
print(len({'a':1,'b':2}))
# 可以for in
for i in user_name:
	print(i)
# 切片 substring
print(user_name[0:2])
print(user_name[:2])
# 字符是否存在于字符串中
print('i' in user_name)
print('ing' in user_name)
print('a' in user_name)
# 转换小写
a='AWD'
print(a.lower())
print('AAAAA'.lower())
# 转为大写
print(a.upper())
print('aaaaa'.lower())
print('AAAAA'.lower())
# 替换
print('abc'.replace('a','d'))

# 去除空格

# 左侧
print('  hello word'.lstrip())
# 右侧
print('hello word  '.rstrip())
# 两侧
print('   hello word    '.strip())
