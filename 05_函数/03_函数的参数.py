"""
函数的定义：
def 函数名(形式参数1,形式参数2...):
    函数体
    return 返回值

函数名(实际参数1,实际参数2...)
"""


def add():
    a = 1
    b = 2
    return a + b


print(add())


def add(a, b):
    return a + b
print(f"a+b={add(1, 2)}")