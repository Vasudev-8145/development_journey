"""
sum of digits
"""

num = int(input("Enter a number:"))
org_num = num
sum = 0

while num!=0:

    digit = num%10
    sum = sum+digit
    num = num//10

print(f"sum of digits {org_num} = {sum}")