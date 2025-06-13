"""
包：管理模块
    python模块、__init__.py
方式一：
    import package.module
    package.module.目标

第三方包：

"""
#创建一个包

#导入自定义包的模块，并使用
import my_package.my_module1
import my_package.my_module2

my_package.my_module1.info_print1()
my_package.my_module2.info_print2()

from my_package import my_module1
from my_package import my_module2
my_module1.info_print1()
my_module2.info_print2()

from my_package.my_module1 import info_print1
from my_package.my_module2 import info_print2
info_print1()
info_print2()
