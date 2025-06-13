"""
位置参数
关键字参数：键-值，无序
缺省参数
不定长传参：
    位置不定长 *args:所有传参都被args变量收集，合并成tuple，位置传递
    关键字不定长 **kwargs，键值对 任意传递
"""


def user_info(name, age, gender):
    print(f"姓名:{name}, 年龄:{age}, 性别:{gender}")


# 参数位置顺序必须一致
user_info('张三', 18, '男')
# 关键字参数
user_info(name='张三', age=18, gender='男')
user_info(gender='男', age=19, name="李四")


# 缺省参数（默认值必须在最后）
def user_info(name, age, gender='男'):
    print(f"姓名:{name}, 年龄:{age}, 性别:{gender}")


user_info(name='小王', age=18)


# 参数不定长
def user_info(*args):
    print(f"kwargs:{args}, 类型:{type(args)}")


user_info('小王', 18, '男')


# 关键字传递，任意传递 参数类型字典
def user_info(**kwargs):
    print(f"kwargs:{kwargs}, 类型:{type(kwargs)}")


user_info(age=18, name='小王', gender='男')
