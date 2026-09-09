"""
find the LCM of two numbers
"""

num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))
org_num1 = num1
org_num2 = num2

while num2!=0:

    rem = num1%num2
    num1 = num2
    num2 = rem

lcm = (org_num1*org_num2)//num1

print("LCM =",lcm)