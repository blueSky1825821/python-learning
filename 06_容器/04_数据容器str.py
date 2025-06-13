"""
字符串是字符的容器


"""
my_str = "hello world"
#通过下标索引取值
value = my_str[0]
print(f"从字符串中取出第一个字符为：{value}")
value = my_str[-2]
print(f"从字符串中取出倒数第二个字符为：{value}")

#字符串不可变
# my_str[0] = "a"

#index方法
value = my_str.index("world")
print(f"字符串中world字符的索引为：{value}")

#replace方法
new_str = my_str.replace("world", "python")
print(f"字符串中world替换为python后的结果为：{new_str}")

#split分割字符串
list_str = my_str.split(" ")
print(f"字符串通过空格分割后的结果为：{list_str}")

#字符串规整操作 去除前后空格 strip
my_str = "   hello world   "
new_str = my_str.strip()
print(f"字符串去除前后空格后的结果为：{new_str}")
my_str  = "hello world"
#会将 h d拆分成两个字符
new_str = my_str.strip("hd")
print(f"字符串去除前后指定字符后的结果为：{new_str}")

#统计字符串某字符出现的次数 count
my_str = "hello world"
count = my_str.count("l")
print(f"字符串中l出现的次数为：{count}")

#统计字符串的长度 len
length = len(my_str)
print(f"字符串的长度为：{length}")
