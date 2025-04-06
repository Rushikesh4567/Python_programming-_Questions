#problem 13

def read_mark():
    marks = int(input("Enter the marks of student: "))
    return marks
    
def Grades():
    marks=read_mark()
    if marks >= 90 and marks <= 100:
        grade = "A Grade"
    elif marks >= 80 and marks <= 89:
        grade = "B Grade"
    elif marks >= 70 and marks <= 79:
        grade = "C Grade"
    elif marks >= 60 and marks <= 69:
        grade = "D Grade"
    else:
        grade = "F"
    return grade  



print("The grade is:", Grades())  
