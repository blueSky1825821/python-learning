"""
类的定义和使用
class 类名称:
    类的属性（成员变量）
    类的行为（方法）
对象 = 类名称()

self 必填，表示类对象自身；
    使用类对象调用方法时，self会自动被python传入
    在方法内部，使用self访问成员变量
def 方法名(self, 形参1,...)
    方法体
"""


class Student:
    name = None
    age = None

    def say_hi(self):
        print(f"Hello, {self.name}")

    def say_msg(self, msg):
        print(f"Hello, {self.name} {msg}")

stu = Student()
stu.name = "xiaowang"
stu.age = 18
stu.say_hi()
stu.say_msg("honey")
