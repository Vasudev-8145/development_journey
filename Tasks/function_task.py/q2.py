"""
w.a function for sum_of_digits(number)
"""

def sum_of_digits(num):

    sum = 0
    org_num = num

    while num != 0:
        digit = num%10
        sum = sum+digit
        num = num//10

    print(f"sum of digits of {org_num} = {sum}")

num = int(input("Enter a number:"))

sum_of_digits(num)