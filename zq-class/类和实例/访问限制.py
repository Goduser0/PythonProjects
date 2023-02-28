class Student1(object):
    def __init__(self, name, score=19):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        if self.score >= 60:
            return 'B'
        if self.score:
            return 'C'


a = Student1('a', 98)
print(a.score)

a.score = 89
print(a.score)  # 此处内部属性可以被外部改变


class Student2(object):
    def __init__(self, name, score=19):
        self.__name = name  # 在属性名称前加 __ ，则实例变量变为私有变量，在类外部无法直接访问
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

    def get_name(self):  # 以下四个类的方法用于获取属性和修改属性
        return self.__name

    def get_score(self):
        return self.__score

    def set_name(self, name):
        self.__name = name

    def set_score(self, score):
        self.__score = score


b = Student2('b', 100)
print()
print(b.get_name())
print(b.get_score())

b.set_score(99)
b.set_name('B')
print()
print(b.get_name())
print(b.get_score())
