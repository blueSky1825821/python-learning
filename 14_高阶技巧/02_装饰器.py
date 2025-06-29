"""
装饰器：也是一种闭包，功能是在不被破坏目标函数原有的代码和功能的前提下，为目标函数增加新功能

"""
from functools import wraps


def sleep(x: int):
    import time
    print("sleeping...")
    time.sleep(x)

def outer(func):
    @wraps(func)
    def inner(*args, **kwargs):
        print(f"outer start {args}, {kwargs}")
        func(*args, **kwargs)
        print(f"outer end {args}, {kwargs}")
    return inner


f = outer(sleep)
f(1)

#类装饰器语法塘
def outer_annotation(func):
    @wraps(func)
    def inner(*args, **kwargs):
        print(f"outer start {args}, {kwargs}")
        func(*args, **kwargs)
        print(f"outer end {args}, {kwargs}")
    return inner

@outer_annotation
def sleep_annotation(x: int):
    import time
    print("sleeping...")
    time.sleep(x)
#直接使用
sleep_annotation(1)