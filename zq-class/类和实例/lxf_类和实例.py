class Student(object):
    def __init__(self, name, score=19):  # 创建实例时，必须传入与__init__方法匹配的参数，参数与函数定义类似，也可传入默认参数、可变参数、关键字参数、命名关键字参数 这些参数称为 类的属性
        self.name = name
        self.score = score

    def print_score(self):  # 在类的内部定义的访问数据的函数，称为 类的方法
        print('%s: %s' % (self.name, self.score))

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        if self.score >= 60:
            return 'B'
        if self.score:
            return 'C'


bart = Student('Bart Simpson')
print(Student)
print(bart)
print()
print(bart.name)
print(bart.score)
print()
bart.print_score()  # 类的方法
print(bart.get_grade())
