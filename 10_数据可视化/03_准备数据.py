"""

"""


# 设计一个类
class Student:
    name = None  # 姓名
    gender = None  # 性别
    nationality = None  # 国籍
    native_place = None  # 籍贯
    age = None  # 年龄

#创建对象
stu_1 = Student()

#赋值
stu_1.name = 'xiaowang'
stu_1.gender = '男'
stu_1.nationality = '中国'
stu_1.native_place = '北京'
stu_1.age = 18

#获取对象信息
print(f"姓名：{stu_1.name}")
