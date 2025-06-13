"""
文件读取：
1、打开 open(name,mode,encoding) mode读、写、追加
2、读写
    read() 读取所有
    read(num) 读取指定字节
    readlines() 行的方式把整个文件的内容进行一次性读取，返回的是一个列表，每一行为一个元素
    readline()
3、关闭
    close
    with open() as f 创建文件对象，自动关闭文件
"""

# 打开文件
f = open('E:/study/py/code/python-learning/README.md', 'r', encoding='utf-8')
print(f"文件类型：{type(f)}")

#  读取文件 - read
#  多次调用会继续后面的内容读取
# print(f"读取10个字节：{f.read(10)}")
# print(f"读取所有：{f.read()}")
print("----------------------")

# 读取readLines()
line1 = f.readline()
print(f"line1:{line1}")
line2 = f.readline()
print(f"line2:{line2}")
lines = f.readlines()
print(f"lines对象的类型：{type(lines)}")
print(f"lines对象的内容：{lines}")

# for循环读取文件行
for line in f:
    print(f"line:{line}")

# 文件关闭
f.close()

# with open() as f 创建文件对象，自动关闭文件
with open('E:/study/py/code/python-learning/README.md', 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        print(f"line:{line}")
