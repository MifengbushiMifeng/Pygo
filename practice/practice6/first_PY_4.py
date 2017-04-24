# encoding=utf-8
# practice Mixin in python
from SocketServer import UDPServer


class Runnable(object):
    def run(self):
        print 'Running...'


class Flyable(object):
    def fly(self):
        print 'Flying...'


class Animal(object):
    pass


class Mammal(Animal):
    pass


class Bird(Animal):
    pass


class Dog(Mammal, Runnable):
    pass


class Bat(Mammal, Flyable):
    pass


class Parrot(Bird, Flyable):
    pass


class Ostrich(Bird, Flyable):
    pass

# define a multi-thread TCP server
# class MyTCPServer(UDPServer, ForkingMixin):
#     pass
