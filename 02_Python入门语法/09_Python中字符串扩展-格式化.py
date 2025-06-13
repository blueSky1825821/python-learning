"""
字符串格式化：
% 精度控制
f"{变量}"，不理会类型，不做精度控制

表达式：一条具有明确执行结果的代码语句
name = "wang"
"""

hello = "hello"
world = "world"
age = 18
hot = 36.1
message = "str: %s, %s, %s" % (hello, world, age)
print(message)
message = "{} {} {}".format(hello, world, age)
print(message)
message = "{1} {0} {2}".format(hello, world, age)
print(message)
message = "{h} {w} {a}".format(h=hello, w=world, a=age)
print(message)
# f： format
message = f"{hello} {world} {age}"
print(message)
message = "str: %s, %s, %d, %f" % (hello, world, age, hot)
print(message)

print("1*1结果，%d" % (1 * 1))
print(f"1*1结果，{1 * 1}")
print(f"字符串在python中的类型名称：{type(1 * 1)}")
