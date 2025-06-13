"""
for循环的嵌套作用
for 循环 或 while 循环:
    do1
    do2
    ...
    for 循环 或 while 循环:
        do1
        do2
        ...

"""

i = 0
j = 0
for i in range(10):
    print(i)
    for j in range(9):
        print(j)
print(i)
print(j)