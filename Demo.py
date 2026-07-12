# Read two integers and store the largest one in a variable

a = int(input("Enter first integer: "))
b = int(input("Enter second integer: "))

largest = a if a > b else b
print(largest)


