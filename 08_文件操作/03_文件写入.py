"""
文件写入
open
write 写入内存
flush 内存刷新到硬盘
"""
# 打开文件 不存在的文件 r w覆盖写入 a追加写入
f = open('E:/study/py/code/python-learning/testfile.txt', 'w', encoding='utf-8')

# 写入 文件写入到内存中
f.write('hello world')
f.write('\n')
# 刷新 内存中的数据到硬盘中
f.flush()
# 关闭 会刷新文件
f.close()
