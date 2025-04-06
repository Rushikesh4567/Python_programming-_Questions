#problem 14
def add(x,y):
    return x+y
    
def sub(x,y):
    return x-y

def mul(x,y):
    return x*y
    
def div(x,y):
    return x/y
while True:
    print("\nChoose any 1 Operation\n\n1.Addition\n2.Subtraction,\n3.Multiplication\n4.Divide\n5.Exit.\n")
    
    ch=int(input("Enter choice "))
    
    if ch==1:
        x=int(input("Enter 1st number "))
        y=int(input("Enter 2nd number "))
        print("The addition is ",add(x,y))
    elif ch==2:
        x=int(input("Enter 1st number "))
        y=int(input("Enter 2nd number "))
        print("The subtraction is ",sub(x,y))
    elif ch==3:
        x=int(input("Enter 1st number "))
        y=int(input("Enter 2nd number "))
        print("The Multiplication is ",mul(x,y))
    elif ch==4:
        x=int(input("Enter 1st number "))
        y=int(input("Enter 2nd number "))
        print("The dividation is ",div(x,y))
    elif ch==5:
        print("exit ")
        break