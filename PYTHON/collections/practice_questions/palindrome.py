"""
collection off palindrome words
"""


words = ["madam","tan","ant","racecar","malayalam"]

palindrome_words = []

for w in words:

    reverse = w[::-1]

    if reverse == w:
        palindrome_words.append(w)

print(palindrome_words)