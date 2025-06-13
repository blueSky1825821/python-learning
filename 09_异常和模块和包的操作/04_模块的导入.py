"""
模块：.py文件，可以认为是一个工具包
    [from 模块名] import [模块 | 类 | 变量 | 函数 | *] [as 别名]
"""

# 使用import导入time模块
import time  # 导入python内置的time模块(time.py这个代码文件)

# . 确认层级关系
time.sleep(2)

# from 导入time的sleep功能
from time import sleep

sleep(2)

# 使用 * 导入time模块的所有功能
from time import *

sleep(2)

#  使用as给模块起别名
import time as tt

tt.sleep(2)

from time import sleep as sl

sl(2)
