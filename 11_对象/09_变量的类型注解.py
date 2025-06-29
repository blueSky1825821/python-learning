"""
变量的类型注解：
函数（方法）形参列表和返回值的类型注解

基础语法：  变量: 类型
var_1: int = 10
stu: Student = Student()
my_list: list = []
my_list: list[int] = [1, 2, 3]
my_tuple: tuple[int, str] = [1, '2']


#type: 类型


函数方法类型注解：提示性
def 函数方法名(形参名: 类型, 。。。) [-> 返回值类型]:
    pass

Union类型
Union[类型,...]
表混合类型
"""
import json
import random
from typing import Union

# 基础数据类型注解
var_1: int = 10
var_2: float = 10.1
var_3: str = "hello world"
var_4: bool = True


# 类对象类型注解
class Student:
    pass


stu: Student = Student()

# 容器类型注解
my_list: list = []
my_list_a: list[int] = [1, 2, 3]
my_tuple: tuple[int, str] = (1, "2")

# type: 类型
# 注释进行类型注解
var_5 = random.randint(1, 100)  # type: int
var_6 = json.loads('{}')  # type: dict[str, str]


# 函数返回值类型注解
def func():
    return 10



var_7 = func()  # type: int

#类型注解限制 类型不一致不会报错
var_8: int = "10"


#形参类型注解
def func2(a: int, b: str) -> int:
    return a + len(b)


my_union_list: list[Union[int, str]] = [1, "2", 3, "4", 5, "6", 7, "8", 9, "10"]
my_union_dict: dict[str, Union[int, str]] = {"key1": 1, "key2": "2", "key3": 3, "key4": "4", "key5": 5, "key6": "6",
                                           "key7": 7, "key8": "8", "key9": 9, "key10": "10"}

def func_union(a: Union[int, str], b: Union[int, str]) -> Union[int, str]:
    return a + b