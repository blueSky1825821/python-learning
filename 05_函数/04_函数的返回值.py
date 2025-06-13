"""
特殊字面量None
使用场景：
函数返回值
if中None等价于False
定义变量，暂时不需要变量有具体值，用None代替
"""

def say_hi():
    print("hello world")
    #函数返回值

result = say_hi()
print(f"无返回值函数，返回的内容:{result}")
print(f"无返回值函数，返回的内容类型:{type(result)}")


def say_hi_none():
    print("hello world")
    #函数返回值
    return None
print(f"无返回值函数，返回的内容:{result}")
print(f"无返回值函数，返回的内容类型:{type(result)}")

#if中None等价于False
if say_hi_none():
    print("say_hi_none()返回了非None值")

#暂时不需要变量有具体值
name = None