"""
w.a function for last_digit_number(number)
"""

def last_digit(num):

    while num!=0:
        digit = num%10
        break

    print(f"Last digit of {num} = {digit}")

num = int(input("Enter a number:"))

last_digit(num)