# coding=utf-8

# the 'object' in here means the extend class / parent class
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif 80 <= self.score < 90:
            return 'B'
        elif 60 <= self.score < 80:
            return 'C'
        else:
            return 'D'


# bart = Student()
# print bart
# print Student

# bart.name = 'Bart Simpson'
# print bart.name

bart = Student('Bart Simpson', 60)
print bart.name, ':', bart.score
print bart.get_grade()

bart.age = 9

lisa = Student('Lisa simpson', 90)

print bart.age
# print lisa.age  # will got an exception
