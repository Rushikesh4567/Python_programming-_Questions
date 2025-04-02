#problem 9

grades = (
    float(input("Enter grade for subject 1: ")), 
    float(input("Enter grade for subject 2: ")), 
    float(input("Enter grade for subject 3: ")), 
    float(input("Enter grade for subject 4: ")), 
    float(input("Enter grade for subject 5: "))
)

print("\nStudent Grades Summary:")
print(f"Highest Grade: {max(grades)}")
print(f"Lowest Grade: {min(grades)}")
print(f"Average Grade: {sum(grades) / 5:.2f}")

