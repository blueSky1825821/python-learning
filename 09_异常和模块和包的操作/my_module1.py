def test(a, b):
    print(a + b)


#__main__如果是被导入的，则不会执行
if __name__ == '__main__':
    test(10, 20)
