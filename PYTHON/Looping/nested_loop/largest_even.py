"""
largest even number
"""

num = int(input("Enter a number:"))

while num!=0:

    digit = num%10

    if digit%2==0:
        print(f"Largest even number = {num}")
        break

    else:
        num = num//10