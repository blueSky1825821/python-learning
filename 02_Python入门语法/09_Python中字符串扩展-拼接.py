"""
字符串拼接：
使用"+"连接字符串变量和字符串变量

注意：
无法和非字符串类型进行拼接
"""

#字符串字面量之间的拼接
print("hello" + "world")

hello = "hello"
world = "world"
age = 18
#无法和非字符串类型进行拼接
print(hello + world + str(age))