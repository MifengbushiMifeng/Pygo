# !/usr/bin/env python
# encoding=utf-8

class Duck():
    def quack(self):
        print 'Quaaaaaaaack'


class Bird():
    def quack(self):
        print 'bird imitate duck'


class Doge():
    def quack(self):
        print 'doge imiate duck'


def in_the_forest(duck):
    duck.quack()


duck = Duck()
bird = Bird()
doge = Doge()

for item in [duck, bird, doge]:
    in_the_forest(item)
