"""
function check wheather a string is palindrome
"""

def palindrome(string):

    if string == string[::-1]:
        print("palindrome")

    else:
        print("Not palindrome")

palindrome("dad")