"""
check wheather a string is palindrome
"""

string = input("Enter a string:")

reversed_string = string[::-1]

if reversed_string == string:
    print("Palindrome")

else:
    print("Not a palindrome")