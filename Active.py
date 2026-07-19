# Taking input
age = int(input('Enter the age:'))

# Write your code here
if (age<13):
    result = "child(<13)"
elif (age>=13 and age <=17):
    result = "Teen (13-17)"
elif (age>18):
    result = "Adult(18+)"
else:
    result = "Invalid"    
# Print the output
print(result)