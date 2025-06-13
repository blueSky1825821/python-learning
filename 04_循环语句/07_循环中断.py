"""
break:直接结束所在循环

continue：中断所在循环的当次执行，直接进入下一次


"""

i = 0
j = 0
for i in range(10):
    print(f"会执行{i}")
    continue
    print(f"不会执行...{i}")
print(j)

for i in range(10):
    print(f"会执行{i}")
    for j in range(10):
        print(f"会执行{j}")
        continue
        print(f"不会执行...{j}")
print(j)

for i in range(10):
    print(f"会执行{i}")
    break
    print(f"不会执行...{i}")
print(i)

print("===")
for i in range(3):
    print(f"会执行{i}")
    for j in range(3):
        print(f"会执行{j}")
        break
        print(f"不会执行...{i}")
print(j)