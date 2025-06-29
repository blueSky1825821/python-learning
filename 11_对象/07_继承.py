"""
面向对象：基于模板（类）去创建实体（对象），使用对象完成功能开发

三大特性：
封装：将现实世界事物的属性和行为封装到类中，描述为成员变量和成员方法
继承：单继承
    class 类名(父类名):
        类内容体
    多继承:重名时使用第一个
    class 类名(父类名1，...):
        类内容体
堕胎
"""


class Phone:
    IMEI = None  # 唯一标识符
    producer = "test"  # 生产商

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


class Phone2025(Phone):
    face_id = True#面部识别

    def call_by_5g(self):
        print("2025最新5G通话开启")


phone = Phone2025()
#phone.__keep_single_core()
phone.call_by_5g()
print(phone.face_id)
print(phone.producer)
print(phone.IMEI)


#多继承
class NFCReader:
    producer = "nfc"
    def read_nfc(self):
        print("NFC读卡")
    def write_nfc(self):
        print("NFC写卡")
class RemoteControl:
    def control(self):
        print("远程控制")


class MyPhone(Phone, NFCReader, RemoteControl):
    #补全语法，表示空的
    pass

phone = MyPhone()
phone.call_by_5g()
phone.read_nfc()
phone.write_nfc()
phone.control()
print(phone.producer)