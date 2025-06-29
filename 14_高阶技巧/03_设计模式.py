"""
设计模式：编程套路
单例模式：确保某个类只有一个实例存在
工厂模式：大量创建一个类的实例
"""

from string_tool_python import str_tool


s1 = str_tool
s2 = str_tool
print(s1 is s2)
print(id(s1))
print(id(s2))

class Person:
    pass

class Worker(Person):
    pass

class Student(Person):
    pass

class Teacher(Person):
    pass

class PersonFactory:
    def create_person(self, p_type):
        if p_type == 'worker':
            return Worker()
        elif p_type == 'student':
            return Student()
        elif p_type == 'teacher':
            return Teacher()
        else:
            return Person()


pf = PersonFactory()
person = pf.create_person('worker')
