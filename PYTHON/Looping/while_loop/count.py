"""
count of digits in a number
"""

num = int(input("Enter a number:"))
org_num = num
count = 0

while num!=0:

    digit = num%10
    count+=1
    num = num//10

print(f"Number of digits in {org_num} = {count}")