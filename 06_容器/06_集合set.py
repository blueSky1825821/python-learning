"""
集合
{元素,元素...}

变量名称 = set()

集合无序，不重复，不支持下标索引

支持for，不支持while
"""

my_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}
my_set_empty = set()
print(f"my_set = {my_set}, type: {type(my_set)}")
print(f"my_set_empty = {my_set_empty}, type: {type(my_set_empty)}")

my_set.add(10)
my_set.add("黑马")
print(f"添加后结果my_set = {my_set}")

# 移除元素
my_set.remove(10)
print(f"删除后结果my_set = {my_set}")

# 随机取出元素
element = my_set.pop()
print(f"随机取出元素为：{element}")
print(f"取出后结果my_set = {my_set}")

# 清空集合
my_set.clear()
print(f"清空集合后结果my_set = {my_set}")

# 取出2个集合的差集
set1 = {1, 2, 3}
set2 = {2, 3, 4}
set3 = set1.difference(set2)
print(f"取出2个集合的差集为：{set3}")
print(f"set1：{set1}")

# 消除2个集合的差集，集合1删除集合2的元素，会修改已有集合
set1.difference_update(set2)
print(f"消除2个集合的差集，集合1删除集合2的元素为：{set1}")

# 2个集合合并，不会修改已有集合
set1 = {1, 2, 3}
set2 = {2, 3, 4}
set3 = set1.union(set2)
print(f"2个集合合并为：{set3}")

# 统计集合长度，不统计重复的元素
set1 = {1, 2, 3, 5, 1, 2}
num = len(set1)
print(f"集合长度为：{num}")

# 遍历集合
for e in set1:
    print(f"集合元素为：{e}")