"""
Find the larger of two numbers.
"""

num1=int(input("Enter num1:"))
num2=int(input("Enter num2:"))
if num1>num2:
    print(num1,"is largest")
elif num2>num1:
    print(num2,"is largest")
else:
    print("Both are equal")