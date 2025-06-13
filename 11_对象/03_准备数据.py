"""
pyecharts 折线图开发
"""
import json

#处理数据
f_us = open("us.txt", "r", encoding="utf-8")
us_data = f_us.read()

#去掉不符合json的开头
us_data = us_data.replace("us_data", "")
#去掉不符合json的结尾
us_data = us_data.replace("]'", "")
#转换成json
us_dict = json.loads(us_data)
print(f"us_dict: {us_dict}")

trend_data = us_dict['data'][0]['trend']
print(f"trend_data: {trend_data}")
print(f"trend_data type: {type(trend_data)}")

x_data = trend_data['updateDate'][:314]

y_data = trend_data['list'][0]['data']
print(f"y_data: {y_data}")
#