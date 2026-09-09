"""
sum of cube of digits
"""

num = int(input("Enter a number:"))
org_num = num
sum = 0

while num!=0:

    digit = num%10
    cube = digit**3
    sum = sum+cube

    print(f"cube of {digit} = {cube}")
    
    num = num//10

print(f"sum of cubes of digits of {org_num} = {sum}")