# coding=utf-8

def run_twice(animal):
    animal.run()
    animal.run()


class Animal(object):
    def run(self):
        print 'Amimal is running'


class Dog(Animal):
    def run(self):
        print 'Dog is running'


class Cat(Animal):
    def run(self):
        print 'Cat is running'


dog = Dog()
cat = Cat()

print dog.run()
print cat.run()

run_twice(dog)
