'''
Author: Fullsize
Date: 2021-08-04 11:13:14
LastEditors: Fullsize
LastEditTime: 2021-08-04 12:17:03
FilePath: /practice_python/demo/BMI.py
'''
import math
height = float(input("输入身高(m):"))  # 输入身高
weight = float(input("输入体重(kg):"))  # 输入体重
bmi= weight/height**2
# bmi = weight/math.pow(height, 2)  # 计算BMI指数  BMI=体重÷身高2 （体重单位：千克；身高单位：米。）
# 判断身材是否合理
if bmi < 18.5:
    # 下面 2 行同属于 if 分支语句中包含的代码，因此属于同一作用域
    print("BMI指数为:"+str(bmi))  # 输出BMI指数
    print("体重过轻")
if bmi >= 18.5 and bmi < 24.9:
    print("BMI指数为:"+str(bmi))  # 输出BMI指数
    print("正常范围，注意保持")
if bmi >= 24.9 and bmi < 29.9:
    print("BMI指数为:"+str(bmi))  # 输出BMI指数
    print("体重过重")
if bmi >= 29.9:
    print("BMI指数为:" + str(bmi))  # 输出BMI指数
    print("肥胖")
