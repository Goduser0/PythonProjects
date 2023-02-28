class Animals(object):
    def run(self):
        print('Animal is running')


class Dog(Animals):
    def eat(self):
        print('Eating meat')


class Cat(Animals):
    pass


dog = Dog()
dog.run()
dog.eat()
print()
cat = Cat()
cat.run()


def run_twice(animal):
    animal.run()
    animal.run()


run_twice(Animals())
run_twice(Dog())
run_twice(Cat())
