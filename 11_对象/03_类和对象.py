"""
事务由属性和行为
类描述现实世界食物
基于类创建对象

"""

class Clock:
    id = None#序列化
    price = None#价格

    def ring(self):
        import winsound
        winsound.Beep(2000,3000)

clock1 = Clock()
clock1.id = '003032'
clock1.price = 19.99
print(f"闹钟Id:{clock1.id}, 价格:{clock1.price}")
clock1.ring()