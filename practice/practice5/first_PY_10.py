# coding=utf-8

class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print '%s: %s' % (self.__name, self.__score)

    def get_name(self):
        return self.__name

    def get_scour(self):
        return self.__score

    def set_score(self, score):
        self.__score = score


bart = Student('Bart Simpson', 98)

# print bart.__name # Will got an exception
