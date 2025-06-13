"""
数据容器：一种可以容纳多分数据的数据类型，容纳的每一份数据称之为一个元素


"""


def test_a():
    num = 10
    print(num)


test_a()
# 局部变量报错 print(num)

num = 100


def test_a():
    print(f"test_a:{num}")
def test_b():
    print(f"test_b:{num}")
test_a()
test_b()
print(f"全局变量:{num}")

num = 100
def test_a():
    print(f"test_a:{num}")
def test_b():
    #局部变量
    num = 200
    print(f"test_b:{num}")
test_a()
test_b()
print(f"全局变量:{num}")


num = 100
def test_a():
    print(f"test_a:{num}")
def test_b():
    #设置内部定义的变量为全局变量
    global num
    num = 200
    print(f"test_b:{num}")
test_a()
test_b()
print(f"全局变量:{num}")