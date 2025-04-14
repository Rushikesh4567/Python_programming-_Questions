# Base class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

# Subclass: Student
class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

    def display_info(self):
        super().display_info()
        print(f"Grade: {self.grade}")

# Subclass: Teacher
class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def display_info(self):
        super().display_info()
        print(f"Subject: {self.subject}")

# Example 
student1 = Student("Alice", 16, "10th Grade")
teacher1 = Teacher("Mr. John", 40, "Mathematics")

print("Student Info:")
student1.display_info()

print("\nTeacher Info:")
teacher1.display_info()
