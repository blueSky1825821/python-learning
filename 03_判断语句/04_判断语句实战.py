"""

"""
import random

num = random.randint(1, 10)
guess_num = int(input("请输入数字："))
if guess_num == num:
    print("恭喜你猜对了")
else:
    if guess_num > num:
        print("你猜的数字太大了")
    elif  guess_num < num:
        print("你猜的数字太小了")
    guess_num = int(input("请输入数字："))
    if  guess_num == num:
        print("恭喜你猜对了")
    else:
        print("你猜的数字不对")
print("程序结束")
