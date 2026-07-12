# Read two integers and store the largest one in a variable
"""
###a = int(input("Enter first integer: "))
b = int(input("Enter second integer: "))

largest = a if a > b else b
print(largest)
###
"""

age = int(input("Enter age: "))
print("Age is:", age)

if age < 13:
    result = "child (<13)"
elif 13 <= age <= 17:
    result = "Teen (13-17)"
elif age >= 18:
    result = "Adult (18+)"
else:
    result = "Invalid"

print(result)
