"""
多态：多种状态，即完成某个行为时，使用不同的对象会得到不同的状态

抽象类：顶层设计，对子类的约束，必须复写父类的一些方法
"""


class Animal:
    """抽象方法，子类实现"""

    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        print("汪汪汪")


class Cat(Animal):
    def speak(self):
        print("喵喵喵")


def make_noise(animal: Animal):
    """传入Animal对象"""
    animal.speak()


dog = Dog()
make_noise(dog)
cat = Cat()
make_noise(cat)


# 抽象类
class AC:
    def cool_wind(self):
        """制冷"""
        pass

    def heat_wind(self):
        """制热"""
        pass

    def swing_l_r(self):
        """左右摆风"""
        pass


class MideaAC(AC):
    def cool_wind(self):
        print("美的空调制冷")

    def heat_wind(self):
        print("美的空调制热")

    def swing_l_r(self):
        print("美的空调左右摆风")


class GreeAC(AC):
    def cool_wind(self):
        print("格力空调制冷")
    def heat_wind(self):
        print("格力空调制热")
    def swing_l_r(self):
        print("格力空调左右摆风")

def make_cool(ac : AC):
    ac.cool_wind()

midea_ac = MideaAC()
make_cool(midea_ac)
gree_ac = GreeAC()
make_cool(gree_ac)