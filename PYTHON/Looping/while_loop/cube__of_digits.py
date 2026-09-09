"""
cube of digit in a number
"""

num = int(input("Enter a number:"))

while num!=0:

    digit = num%10
    cube = digit**3
    print(f"cube of {digit} = {cube}")
    num = num//10