'''
Author: Fullsize
Date: 2021-07-21 17:13:47
LastEditors: Fullsize
LastEditTime: 2021-07-21 17:50:12
FilePath: /practice_python/basic/open.py
'''
# 没有相对路径
stra = 'Hello\nWorld!'
fhand = open('file/1.txt')
a = fhand.read()
print('a',a)
print('上面完毕')
for i in fhand:
    print(i)
def main():
	fname=input('请输入文件名称: ')
	try:
		fhand=open('file/'+fname)
	except:
		print('文件不存在!',fname)
		quit()
	count=0
	for i in fhand:
		count=count+1
		print(i)
	print('行数为',count)
main()