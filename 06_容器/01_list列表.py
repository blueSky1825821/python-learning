"""
基础语法
列表：[元素1,元素2...]
元素内容没有任何限制

列表的下标(索引)
正向:从前向后0开始
反向：从后向前-1开始

列表的常用操作
插入
删除
清空
修改
统计
"""

name_list = ['itheima', 'itcast', 'python']
#不同类型的元素
my_list = ['itheima', 666, True]
print(my_list)
print(type(my_list))

#嵌套的列表
my_list = [['itheima', 'itcast'], ['python', 'java']]
print(my_list)
print(type(my_list))

#访问列表元素-正向
print(name_list[0])
print(name_list[1])
print(name_list[2])
#访问列表元素-反向
print(name_list[-1])
print(name_list[-2])
print(name_list[-3])
#访问嵌套列表
print(my_list[0][0])
print(my_list[1][1])
#错误释放，不要超出范围
#print(name_list[3])

#查找某元素的下标
index = name_list.index('itheima')
print(index)
#查找不存在的元素 报错
# index = name_list.index('itheima1')
#修改特定下标索引值
name_list[0] = 'itheima1'
print(f"修改后结果值为：{name_list}")

#指定下标位置插入新元素
name_list.insert(0,'itheima2')
print(f"插入后结果值为：{name_list}")

#追加元素
name_list.append('itheima3')
print(f"追加后结果值为：{name_list}")

#追加一批元素
list2 = ['itheima4', 'itheima5']
name_list.extend(list2)
print(f"追加一批元素后结果值为：{name_list}")

#删除列表下标
del name_list[0]
print(f"删除列表下标后结果值为：{name_list}")

#删除列表元素 pop 下标
element = name_list.pop(0)
print(f"pop取出的元素值为：{element},列表值为：{name_list}")

#删除某元素在列表的第一个元素，不存在报错
name_list.remove('itheima3')
print(f"remove删除元素后结果值为：{name_list}")
# name_list.remove('itheima3')
# print(f"remove删除元素后结果值为：{name_list}")

#清空列表
name_list.clear()
print(f"清空列表后结果值为：{name_list}")

#统计列表元素个数
name_list = ['itheima', 'itcast', 'python', 'python', 'python']
count = name_list.count('python')
print(f"统计列表元素个数：{count}")

#统计列表长度
length = len(name_list)
print(f"统计列表长度：{length}")
