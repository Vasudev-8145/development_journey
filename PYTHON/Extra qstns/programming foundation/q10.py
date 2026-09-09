"""
Swap two numbers and print before and after.
"""

num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))

print("Before swapping")
print("First number is",num1)
print("second number is",num2)

temp=num1
num1=num2
num2=temp

print("After swapping")
print("First number is",num1) 
print("second number is",num2) 
