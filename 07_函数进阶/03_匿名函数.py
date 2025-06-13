"""
匿名函数
1、函数作为参数传递：计算逻辑的传递，非传入数据
2、lambda匿名函数：
    1、只能使用一次
    2、lambda 传入参数: 函数体(一行代码)
"""


# 函数作为参数传递
def test_func(data_compute):
    result = data_compute(1, 2)  # 确定compute是函数
    print(f"data_compute的参数类型：{type(data_compute)}")
    print(f"result:{result}")


def compute(x, y):
    return x + y


test_func(compute)


# lambda
def test_lambda_func(lambda_compute):
    result = lambda_compute(1, 2)
    print(f"lambda_compute的参数类型：{type(lambda_compute)}")
    print(f"result:{result}")


test_lambda_func(lambda x, y: x + y)
