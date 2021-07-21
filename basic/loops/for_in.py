'''
Author: Fullsize
Date: 2021-07-15 10:58:17
LastEditors: Fullsize
LastEditTime: 2021-07-15 11:06:17
FilePath: /practice_python/basic/loops/for_in.py
'''
for i in [5, 4, 3, 2, 1]:
    print(i)
print('Done !')

max_number = -1
print('Before',max_number)
for num in [9, 41, 12, 3, 74, 15]:
    if num > max_number:
        max_number = num
    print(max_number, num)
print('After',max_number)