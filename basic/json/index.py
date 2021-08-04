'''
Author: Fullsize
Date: 2021-08-03 15:21:30
LastEditors: Fullsize
LastEditTime: 2021-08-03 15:24:52
FilePath: /practice_python/basic/json/index.py
'''
import json
json_a = '''{
		"a":"1",
		"b":"2"
}
'''
info=json.loads(json_a)  # 转为字典
print(info)