"""
（元素1,元素2...）
不能修改
"""

#定义元组
t1 = (1, "Hello", True)
t2 = ()
t3 = tuple()
print(f"t1的类型是:{type(t1)},内容是:{t1}")
print(f"t2的类型是:{type(t2)},内容是:{t2}")
print(f"t3的类型是:{type(t3)},内容是:{t3}")

#定义单个元素的元组
t4 = (1,)
print(f"t4的类型是:{type(t4)},内容是:{t4}")

#元组的嵌套
t5 = (1, "Hello", True, (1, 2, 3))
print(f"t5的类型是:{type(t5)},内容是:{t5}")

#下标索引取
print(t5[0])
print(t5[3][2])

#元组的操作：index查找方法
t6 = (1, "Hello", True, "Hello")
index = t6.index("Hello")
print(f"t6查找 Hello的下标{index}")

#元组的操作：count计数方法
count = t6.count("Hello")
print(f"t6中 Hello出现的次数是{count}")

#元组的长度
print(f"t6中 元组的长度是{len(t6)}")

#元组遍历
for item in t6:
    print(f"t6元素的数组有{item}")

index = 0
while index < len(t6):
    print(f"t6元素的数组有{t6[index]}")
    index += 1

#元组元素不能修改
t7 = (1, "Hello", True)
# t7[0] = "itheima"

#元组中list可以修改
t8 = (1, "Hello", [1, 2, 3])
t8[2][0] = "itheima"
print(f"t8修改后的结果是{t8}")