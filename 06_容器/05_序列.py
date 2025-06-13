"""
序列：内容连续、有序，可使用下标索引的一类数据容器
列表、元组、字符串

支持切片，从一个序列中取出一个子序列
序列[其实下标:结束下标:步长]
"""
# 对list切片
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#步长默认1
result1 = my_list[0:5]
print(f"结果:{result1}")

#对tuple切片
my_tuple = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
result2 = my_tuple[0:5]
print(f"结果:{result2}")

#对字符串切片
my_str = "hello world"
result3 = my_str[0:5]
print(f"结果:{result3}")

#对列表切片，，从3开始到1结束，步长-1
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result4 = my_list[3:1:-1]
print(f"结果:{result4}")
result4 = my_list[8:1:-2]
print(f"结果:{result4}")
result4 = my_list[1:8:-2]
print(f"结果:{result4}")

#对tuple切片，从头开始到尾结束，步长-2
my_tuple = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
result5 = my_tuple[::-2]
print(f"结果:{result5}")
