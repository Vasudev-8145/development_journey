"""
find the GCD of two numbers
"""

first_num = int(input("Enter first number:"))
second_num = int(input("Enter second number:"))

while second_num!=0:

    rem = first_num%second_num
    first_num = second_num
    second_num = rem

print("GCD =",first_num)