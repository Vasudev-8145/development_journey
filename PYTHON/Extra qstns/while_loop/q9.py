"""
check whethear a number is an armstrong number
"""

num = int(input("Enter a number:"))
org_num = num
sum = 0
count = 0 

while num>0: 
    
    num = num//10 
    count+=1 

org_num = num
sum = 0

while org_num>0:

    digit = org_num%10
    sum = sum+(digit**count)

if sum == org_num:

    print("Armstrong number!!")

else:

    print("Not an armstrong number")