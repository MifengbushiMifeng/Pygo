# encoding=utf-8
class Student(object):
    __slots__ = ('name', 'age')


s = Student()

s.name = 'Michael'
s.age = 27
print s.name, s.age


# s.score = 99 Will got an exception

# '__slots__' does not on child-class
class GraduateStudent(Student):
    pass


g = GraduateStudent()
g.score = 99

print g.score
