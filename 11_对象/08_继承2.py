"""
复写：对父类的成员属性或成员方法进行重新定义

调用父类成员：
使用成员变量：父类名.成员变量         super().成员变量
使用成员方法：父类名.成员方法(self)   super().成员方法


"""


class Phone:
    IMEI = None  # 唯一标识符
    producer = "test"  # 生产商

    __current_voltage = 0.5  # 电池电压 私有成员变量

    def call_by_5g(self):
        print("父类5G通话开启")


class MyPhone(Phone):
    producer = "myTest"  # 生产商

    def call_by_5g(self):
        #调用父类方法
        super().call_by_5g()
        #调用父类方法
        Phone.call_by_5g(self)
        print("子类5G通话开启")


phone = MyPhone()
phone.call_by_5g()
print(f"producer:{phone.producer}")
