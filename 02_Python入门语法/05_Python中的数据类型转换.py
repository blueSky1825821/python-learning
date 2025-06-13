"""
int(x) float(x) str(x)

任何类型都可以转换成字符串
字符串不能随意转换成数字
"""
#将数字类型转换成字符串
num_str = str(123)
print(type(num_str), num_str)

#将字符串类型转换成数字类型
num = int("11")
print(type(num), num)

#将浮点数类型转换成整数类型,会丢失精度
float_int = int(11.1)
print(type(float_int), float_int)

#错误示例，字符串转数字，必须要求字符串内的内容都是数字
num = int("黑马")
print(type(num), num)