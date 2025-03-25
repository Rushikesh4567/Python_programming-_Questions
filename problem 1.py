#problem 1 employee salary category
salary=int(input("Enter salary of employee "))

if salary>50000:
    category="High Income"
elif 30000<salary<50000:
    category="Medium Income"
else:
    category="Low Income"

print("The employee is from category of ",category)
