"""
闭包：在函数嵌套的前提下，内部函数使用了外部函数的变量，并且外部函数返回了内部函数，
使用外部函数变量的内部函数称为闭包

缺点：内部函数持续引用外部函数的值，导致一部分内存空间不被释放，一直占用内存

"""


def outer(logo):
    def inner(msg):
        print(f'这是内部函数,{logo}, {msg}')

    return inner


f = outer('hello')
f('world')


def outer_num(num1):
    def inner_num(num2):
        # 使用nonlocal修饰外部函数的变量才可在内部函数修改
        nonlocal num1
        num1 += num2
        print(num1)

    return inner_num


f = outer_num(10)
f(10)
f(10)
f(10)
