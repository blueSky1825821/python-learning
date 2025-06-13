"""
while for遍历

"""

def list_while_func():
    """
    使用while遍历
    :return: None
    """
    list_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    index = 0
    while index < len(list_data):
        print(list_data[index])
        index += 1

def list_for_func():
    """
    使用for遍历
    :return: None
    """
    list_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for item in list_data:
        print(item)

list_for_func()
list_while_func()