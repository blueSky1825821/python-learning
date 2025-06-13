"""
异常捕获
1、因为bug停止运行
2、对bug提醒，程序继续运行
"""
try:
    f = open("test.txt", "r")
# 捕获所有异常
except:
    print("文件不存在")

try:
    f = open("test.txt", "r")
    # 捕获所有异常
except Exception as e:
    print("文件不存在")

# 捕获指定异常
try:
    print(name)
    1 / 0
except NameError as e:
    print("出现了变量未定义的异常")

#  捕获多个异常
try:
    print(1 / 0)
except (NameError, ZeroDivisionError) as e:
    print("出现了变量未定义的异常或除以0的异常")

# else
try:
    print("hello world")
    # print(1 / 0)
except Exception as e:
    print("出现了异常")
else:
    print("没有异常")

# 一定要执行的
try:
    f = open("test.txt", "r")
except Exception as e:
    print("出现了异常")
else:
    print("没有异常")
finally:
    print("一定要执行的代码")
    f.close()
