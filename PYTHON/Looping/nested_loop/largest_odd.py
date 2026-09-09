"""
number = 3734
largest odd number
"""

num = int(input("Enter a number:"))

if num%2!=0:
    print(f"largest odd = {num}")

else:

    while num!=0:

        digit = num%10
        odd = num
        
        if odd%2!=0:
            print(f"largest odd = {odd}")
            break
        else:
            num = num//10
