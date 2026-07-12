# Read two integers and store the largest one in a variable
"""
###a = int(input("Enter first integer: "))
b = int(input("Enter second integer: "))

largest = a if a > b else b
print(largest)
###
"""

# Taking input
age = int(input())

# Write your code here
if (age<13):
    result = print("child(<13)")
elif (age>=13 and age <=17):
    result = print("Teen (13-17)")
elif (age>18):
    result = print ("Adult(18+)")
else:
    result = print("Invalid")    
# Print the output
print(result)

