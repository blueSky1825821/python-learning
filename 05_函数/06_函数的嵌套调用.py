"""
函数的嵌套调用：
一个函数里又调用了另外一个函数

执行流程：a调用b，先执行a，在调用b执行完后a才能执行完

"""

def func_a():
    print("func_a")
    func_b()
    print("func_a end")

def func_b():
    print("func_b")

func_a()
