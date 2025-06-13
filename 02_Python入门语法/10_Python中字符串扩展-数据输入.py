"""
获取键盘输入（字符串）：
input():从键盘获取输入，回车键结束
input("提示")
"""

print("请告诉我你是谁？")
name = input()
print("你是：%s" % name)

name = input("请告诉我你是谁？")
print("你是：%s" % name)

#输入数字类型
num = input("请输入数字：")
#数字类型转换
num = int(num)
print("类型：", type(num))