"""
面向对象：基于模板（类）去创建实体（对象），使用对象完成功能开发

三大特性：
封装：将现实世界事物的属性和行为封装到类中，描述为成员变量和成员方法

私有成员变量
私有成员方法
__前缀

对象不能使用私有的成员变量和方法
类内可以使用

继承
堕胎
"""


class Phone:
    IMEI = None  # 唯一标识符
    producer = None  # 生产商

    __current_voltage = 0.5  # 电池电压 私有成员变量

    def call_by_5g(self):
        if self.__current_voltage >= 1:
            print("5G通话开启")
        else:
            self.__keep_single_core()
            print("电量不足，5G通话关闭")


    # 私有成员方法
    def __keep_single_core(self):
        print("单核CPU运行节省电量")


phone = Phone()
#phone.__keep_single_core()
phone.call_by_5g()
