'''
Author: Fullsize
Date: 2021-07-27 11:07:50
LastEditors: Fullsize
LastEditTime: 2021-07-27 11:10:55
FilePath: /practice_python/basic/dictionaries/ex_1.py
'''
counts = dict()
line = input('请输入词语: ')
words = line.split()
for word in words:
    counts[word] = counts.get(word, 0)+1
print(counts)
