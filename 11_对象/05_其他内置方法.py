"""
内置方法:魔术方法


"""


class Student:
    name = None
    age = None
    tel = None

    # 参数自动传入，init自动执行
    def __init__(self, name, age, tel):
        self.name = name
        self.age = age
        self.tel = tel
        print(f"Student类创建对象成功")

    # 重写后，打印字符串
    def __str__(self):
        return f"Student类对象信息：name:{self.name}, age:{self.age}, tel:{self.tel}"

    # lt 小于符号比较，不包含等于,other是另外一个对象
    def __lt__(self, other):
        return self.age < other.age

    # le 小于等于符号比较，包含等于
    def __le__(self, other):
        return self.age <= other.age
    # eq 等于符号比较
    def __eq__(self, other):
        return self.age == other.age


stu_1 = Student("xiaowang", 18, "123456")
# 内存地址
print(stu_1)
print(str(stu_1))

stu_2 = Student("xiaozhang", 20, "123")
print(stu_1 <= stu_2)
# 默认比较内存地址
print(stu_1 == stu_2)
