"""
Take two numbers as input, store them, and swap them.
"""

num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
print("Before swapping")
print(f"First number={num1} and second number={num2}")
temp=num1
num1=num2
num2=temp
print("After swapping")
print(f"First number={num1} and second number={num2}")
