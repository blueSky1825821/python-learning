"""
正则表达式：使用单个字符串描述、匹配某个句法规则的使用
match
search

元字符匹配
"""
import re

#match 开头匹配 第一个
s = "python itheina"
result = re.match("python", s)
print(result)
print(result.span())
print(result.group())

#search 全局匹配第一个
s = "python itheima"
result = re.search("thon", s)
print(result)
print(result.span())
print(result.group())

#findall 全局寻找 全部
s = "python itheima python1"
result = re.findall("thon", s)
print(result)

