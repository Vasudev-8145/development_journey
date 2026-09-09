"""
create a new list that containes palindrome
"""

words = ["madam","pop","push","dad"]

palindrome = [w for w in words if w == w[::-1]]
print(palindrome)