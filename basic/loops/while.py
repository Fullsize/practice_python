'''
Author: Fullsize
Date: 2021-07-15 10:53:20
LastEditors: Fullsize
LastEditTime: 2021-07-15 10:55:09
FilePath: /practice_python/basic/loops/while.py
'''
while True:
    line = input('> ')
    if line == 'done':
        break
    print(line, line == 'done')
print('Done!')
