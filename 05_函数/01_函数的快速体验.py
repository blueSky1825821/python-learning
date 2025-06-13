"""
函数：组织好的，可重复使用的，用来实现特定功能的代码段

好处：
功能封装，随时使用
提高复用
"""

str1 = "itheima"
str2 = "itcast"
str3 = "python"

count = 0
for i in str1:
    count +=1
print(f"字符串{str1}的长度为：{count}")


def my_len(data):
    count = 0
    for _ in data:
        count +=1
    return count
print(f"字符串{str2}的长度为：{my_len(str2)}")