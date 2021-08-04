'''
Author: Fullsize
Date: 2021-07-29 11:56:07
LastEditors: Fullsize
LastEditTime: 2021-07-29 11:56:08
FilePath: /practice_python/urllib/web_ crawler.py
'''
import urllib.error
import urllib.parse
import urllib.request

http_url = input('请输入抓取的链接地址: ')


def main():
    global http_url
    fhand = urllib.request.urlopen(http_url)
    file1 = open("test.html", mode='w')
    print(fhand.read().decode('utf-8'))
    file1.write(fhand.read().decode('utf-8'))


if __name__ == '__main__':
    main()
