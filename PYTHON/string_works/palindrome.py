"""
function is_palindrome
"""


def is_palindrome(word):

    reversed_word = word[::-1]

    print(reversed_word == word)

is_palindrome("madam")
is_palindrome("racecar")
is_palindrome("messi")