'''
Author: Fullsize
Date: 2021-07-27 10:52:32
LastEditors: Fullsize
LastEditTime: 2021-07-27 11:27:03
FilePath: /practice_python/basic/dictionaries/dictionaries.py
'''
# 和js的json差不多,key:value形式; value可以是任何形式数据
p = dict()
p['a'] = 1
print(p)
p['b'] = 2
p['c'] = 3
print(p)
# 也可以这样声明同js的json 字面量声明
p2 = {}
p2['d'] = 1
print(p2)
p2['e'] = 2
p2['f'] = 3

print(p2)
for i in p2:
    print(i, p2[i])
# 检查字典是否存在某个key
print('d是否存在于p2', 'd' in p2)
print('g是否存在于p2', 'g' in p2)

# 转为str
p2_str=str(p2)
p2['g'] = 3
print(p2_str,type(p2_str))

# 再转为dictionary
p3=eval(p2_str)
print(p3,type(p3))
print(p2)