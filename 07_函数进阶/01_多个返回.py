"""
多个返回
"""


def test_return():
    return 1, 2


x, y = test_return()
print(f"x:{x}, y:{y}")
