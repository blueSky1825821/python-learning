"""
转换
排序
"""
my_list = [1, 2, 3, 4, 5]
my_tuple = (1, 2, 3, 4, 5)
my_str = "hello world"
my_set = {1, 2, 3, 4, 5}
my_dict = {"key1": 1, "key2": 2, "key3": 3}

# len元素个数
print(f"my_list 元素个数: {len(my_list)}")
print(f"my_tuple 元素个数: {len(my_tuple)}")
print(f"my_str 元素个数: {len(my_str)}")
print(f"my_set 元素个数: {len(my_set)}")
print(f"my_dict 元素个数: {len(my_dict)}")

# max最大元素
print(f"my_list 最大元素: {max(my_list)}")
print(f"my_tuple 最大元素: {max(my_tuple)}")
print(f"my_str 最大元素: {max(my_str)}")
print(f"my_set 最大元素: {max(my_set)}")
print(f"my_dict 键最大元素: {max(my_dict)}")
print(f"my_dict 值最大元素: {max(my_dict.values())}")

# min最小元素
print(f"my_list 最小元素: {min(my_list)}")
print(f"my_tuple 最小元素: {min(my_tuple)}")
print(f"my_str 最小元素: {min(my_str)}")
print(f"my_set 最小元素: {min(my_set)}")
print(f"my_dict 键最小元素: {min(my_dict)}")
print(f"my_dict 值最小元素: {min(my_dict.values())}")

# 类型转换：容器转列表
print(f"列表转列表的结果: {list(my_list)}")
print(f"元组转列表的结果: {list(my_tuple)}")
print(f"字符串转列表的结果: {list(my_str)}")
print(f"集合转列表的结果: {list(my_set)}")
print(f"字典转列表的结果: {list(my_dict)}")

#类型转换：容器转元组
print(f"列表转元组的结果: {tuple(my_list)}")
print(f"元组转元组的结果: {tuple(my_tuple)}")
print(f"字符串转元组结果: {tuple(my_str)}")
print(f"集合转元组的结果: {tuple(my_set)}")
print(f"字典转元组的结果: {tuple(my_dict)}")

# 类型转换：容器转字符串
print(f"列表转字符串的结果: {str(my_list)}")
print(f"元组转字符串的结果: {str(my_tuple)}")
print(f"字符串转字符串的结果: {str(my_str)}")
print(f"集合转字符串的结果: {str(my_set)}")
print(f"字典转字符串的结果: {str(my_dict)}")

#  类型转换：容器转集合
print(f"列表转集合的结果: {set(my_list)}")
print(f"元组转集合的结果: {set(my_tuple)}")
print(f"字符串转集合 无序 的结果: {set(my_str)}")
print(f"集合转集合的结果: {set(my_set)}")
print(f"字典转集合的结果: {set(my_dict)}")


# 容器排序-正向
print(f"列表对象的排序结果: {sorted(my_list)}")
print(f"元组对象的排序结果: {sorted(my_tuple)}")
print(f"字符串对象的排序结果: {sorted(my_str)}")
print(f"集合对象的排序结果: {sorted(my_set)}")
print(f"字典对象的排序结果: {sorted(my_dict)}")

# 容器排序-反向
print(f"列表对象的排序结果: {sorted(my_list, reverse=True)}")
print(f"元组对象的排序结果: {sorted(my_tuple, reverse=True)}")
print(f"字符串对象的排序结果: {sorted(my_str, reverse=True)}")
print(f"集合对象的排序结果: {sorted(my_set, reverse=True)}")
print(f"字典对象的排序结果: {sorted(my_dict, reverse=True)}")