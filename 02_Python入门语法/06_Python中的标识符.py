"""
标识符：
用户编写代码时，对变量、类、方法等编写的名字

命名规则：
内容限定：中文、英文、下划线，不能以数字开头
大小写敏感
不可使用关键字

变量命名规范：
见面知意
下划线命名规范，多个单词组合下划线分割
英文字符全小写
"""

#规则1：内容限定，只能使用：中文、英文、下划线，不能以数字开头
#错误示例：1_name = "wang"
name_ = "wang"
_name = "wang"
name_1 = "wang"

#规则2：大小写敏感
Itheima = "Itheima"
itheima = "itheima"
print(Itheima, itheima)

#规则3：不能使用关键字
#错误示例：if = "wang"
If = "wang"
print(If)