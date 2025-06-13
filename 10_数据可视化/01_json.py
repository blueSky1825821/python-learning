"""
json 同python dict
"""

# 导入json模块
import json

#list转为json
data = [{
    "name": "Bob",
    "age": 20,
    "city": "北京"
}, {
    "name": "Alice",
    "age": 18,
    "city": "上海"
}]
# 将python对象转换成json字符串
json_str = json.dumps(data, ensure_ascii=False)
print(f"json_str type: {type(json_str)}")
print(f"json_str: {json_str}")

#dict 转 json
data = {
    "name": "Bob",
    "age": 20,
    "city": "北京"
}
json_str = json.dumps(data, ensure_ascii=False)
print(f"json_str type: {type(json_str)}")
print(f"json_str: {json_str}")

# str 转 json {k:v,k:v}
json_str = '{"name": "Bob", "age": 20, "city": "北京"}'
data = json.loads(json_str)
print(f"data type: {type(data)}")
print(f"data: {data}")

# str 转 json [{},{}]
json_str = '[{"name": "Bob", "age": 20, "city": "北京"}, {"name": "Alice", "age": 18, "city": "上海"}]'
data = json.loads(json_str)
print(f"data type: {type(data)}")
print(f"data: {data}")

