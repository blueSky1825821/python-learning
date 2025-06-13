"""
字典
{key: value, key:value.....}

变量名称 = dict()

字典无序，不重复，不支持下标索引

字典key value可以为任意类型(key不可为字典)

支持for，不支持while
"""

my_dict = {"wang": 18, "zhang": 19, "li": 20}
my_dict2 = {}
my_dict3 = dict()
print(f"字典my_dict:{my_dict}, 类型:{type(my_dict)}")
print(f"字典my_dict2:{my_dict2}, 类型:{type(my_dict2)}")
print(f"字典my_dict3:{my_dict3}, 类型:{type(my_dict3)}")

# 定义重复的key
my_dict = {"wang": 18, "zhang": 19, "wang": 20}
print(f"重复字典my_dict:{my_dict}")

# 字典key获取value
my_dict = {"wang": 18, "zhang": 19, "li": 20}
age = my_dict.get("wang")
print(f"字典my_dict的key为wang的value为:{age}")

wang_score_dict = {"语文": 98, "数学": 100, "英语": 100}
stu_score_dict = {"wang": wang_score_dict,
                  "zhang": {"语文": 98, "数学": 100, "英语": 100},
                  "li": {"语文": 98, "数学": 100, "英语": 100}}
print(f"字典stu_score_dict的key为wang的value为:{stu_score_dict['wang']}, "
      f"类型为：{type(stu_score_dict['wang'])}")

# 嵌套字典获取数据
score = stu_score_dict.get("wang").get("语文")
print(f"wang的语文成绩为：{score}")
score = stu_score_dict["zhang"]["语文"]
print(f"zhang的语文成绩为：{score}")

# 新增元素
stu_score_dict["zhang"]["体育"] = 100
print(f"新增元素后字典为：{stu_score_dict}")

# 更新元素
stu_score_dict["zhang"]["语文"] = 90
print(f"更新元素后字典为：{stu_score_dict}")

# 删除元素
stu_score_dict.pop("zhang")
print(f"删除元素后字典为：{stu_score_dict}")

stu_score_copy_dict = stu_score_dict.copy()
print(f"复制后的字典为：{stu_score_copy_dict}")

# 清空元素
stu_score_dict.clear()
print(f"清空元素后字典为：{stu_score_dict}")
print(f"复制后的字典为：{stu_score_copy_dict}")

# 获取全部key
keys = stu_score_copy_dict.keys()
print(f"获取全部key为：{keys}")
#遍历字典
for key in stu_score_copy_dict:
    print(f"key: {key}, value: {stu_score_copy_dict[key]}")

for (key, value) in stu_score_copy_dict.items():
    print(f"key: {key}, value: {value}")

#获取全部value
values = stu_score_copy_dict.values()

#统计元素数量
num = len(stu_score_copy_dict)
print(f"字典元素数量为：{num}")

