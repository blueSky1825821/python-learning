"""
if(条件):
    do thing
else:
    do other
"""

age = 18
print(f"今年我已经{age}岁了")
if int(input("你的身高是多少：")) > 120:
    print("身高超出限制，不可以免费")
    print("但是，如果vip级别大于3可以免费")
    if int(input("你的vip级别是几：")) > 3:
        print("可以免费")
    else:
        print("不可以免费")
else:
    print("可以免费")
print("程序结束")
