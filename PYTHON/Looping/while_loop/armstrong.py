"""
Armstrong number
"""

# num = int(input("Enter a number:"))
# org_num = num
# count = 0

# while num!=0:

#     digit = num%10
#     count+=1
#     num = num//10

# org_num = num
# sum = 0

# while org_num!=0:

#     digit = org_num%10
#     exponent = digit**count
#     sum = sum+exponent
#     org_num = org_num//10

# if org_num == sum:
#     print("It is an armstrong number")

# else:
#     print("It is not an armstrong number")

# OR

num = int(input("Enter a number:"))
org_num = num
count = len(str(num))
sum = 0

while num>0:

    digit = num%10
    exponent = digit**count
    sum = sum+exponent
    num = num//10

print(f"sum = {sum}")

if sum == org_num:
    print("It is an armstrong number")

else:
    print("Not an armstrong number")