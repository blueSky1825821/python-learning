"""
构造方法：
在创建类对象（构造类）时，会自动执行
在创建类对象（构造类）时，将传入参数自动传递给__init__方法使用


"""
class Student:
    name = None
    age = None
    tel = None

    #参数自动传入，init自动执行
    def __init__(self, name, age, tel):
        self.name = name
        self.age = age
        self.tel = tel
        print(f"Student类创建对象成功")

stu_1 = Student("xiaowang", 18, "123456")
