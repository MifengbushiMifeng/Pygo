# coding=utf-8

# function oriented
stud1 = {'name': 'Michael', 'score': 98}
stud2 = {'name': 'Bob', 'score': 81}


def print_score(std):
    print '%s: %s' % (std['name'], std['score'])


print_score(stud1)
print_score(stud2)


# object oriented
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print '%s: %s' % (self.name, self.score)


bart = Student('Bart Simpson', 60)
lisa = Student('Lisa Simpson', 87)

bart.print_score()
lisa.print_score()
