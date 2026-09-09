"""
count the even and odd digits in a number
"""

num = int(input("Enter a number:"))
even_count = 0
odd_count = 0

while num>0:

    digit = num%10

    if digit%2 == 0:
        even_count+=1

    elif digit%2 != 0:
        odd_count+=1

    num = num//10

print("Number of even digits =",even_count) 
print("Number of odd digits =",odd_count) 
