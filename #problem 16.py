#problem 16

class Student:
    def __init__(self,marks,name):
        self.marks=marks
        self.name=name

    def check_marks(self):
        if self.marks>=40:
            print("Student is passed ")
        else:
            print("fail")


marks=int(input("Enter the marks of student "))
name = input("Enter student's name: ")
s=Student(marks,name)
s.check_marks()