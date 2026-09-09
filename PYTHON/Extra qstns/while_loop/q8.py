"""
check whethear a number is palindrome or not
"""

num = int(input("Enter a number:"))
org_num = num
palindrome = 0

while num>0:

    last_digit = num%10
    palindrome = palindrome*10+last_digit
    num = num//10

if palindrome == org_num:
    print(f"{org_num} is a palindrome")

else:
    print(f"{org_num} is not a palindrome")