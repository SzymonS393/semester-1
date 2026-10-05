# Worksheet 1.2: Task 1 Solution
import sys
try:
    grade = int(input("Enter a grade between 0 and 100: "))
except:
    sys.exit("Invalid input")
if grade < 0 or grade > 100:
    sys.exit("Invalid input")
elif grade >= 0 and grade <= 39:
    result = "Fail"
elif grade >= 40 and grade <= 69:
    result = "Pass"
else:
    result = "Distinction"
print(int(grade), "is a", result)
