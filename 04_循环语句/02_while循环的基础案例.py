"""
while条件基础案例
"""
import random
num = random.randint(1, 10)

flag = True
while  flag:
    guess = int(input("请输入数字："))
    if guess == num:
        print("恭喜你猜对了")
        flag = False
    else:
        if guess > num:
            print("你猜的数字太大了")
        elif guess < num:
            print("你猜的数字太小了")