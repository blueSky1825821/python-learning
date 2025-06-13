"""
后导入会覆盖之前的
"""
#导入自定义模块
from my_module1 import test
from my_module2 import test

test(1, 2)

# __main__变量
from my_module1 import test
test(5, 10)

#__all__变量 *使用的范围
from my_module3 import *
test_a(5, 10)
# test_b(5, 10) 使用不了
