#problem 6

n=int(input("Enter number= "))

rev=0

while n!=0:
    digit=n%10
    rev=rev*10+digit
    n=n//10

print("The reversed number is ",rev)