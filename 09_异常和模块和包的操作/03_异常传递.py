"""
异常具有传递性
"""


# 定义一个异常的方法
def func1():
    print("func1开始执行")
    num = 1 / 0
    print("func1结束执行")

def  func2():
    print("func2开始执行")
    func1()
    print("func2结束执行")

def main():
    print("main开始执行")
    try:
        func2()
    except  Exception as e:
        print(f"出现了异常,{e}")

if __name__ == '__main__':
    main()