"""
while嵌套循环
"""
i = 1
while i <= 100:
    print(f"今天是第{i}天，准备表白...")

    j = 1
    while j <= 10:
        print(f"送给小美第{j}支玫瑰花")
        j += 1
    i += 1
    print("表白...")
print("结束...")