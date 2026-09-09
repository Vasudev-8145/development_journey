"""
Check if two strings are anagrams.
"""

word1 = input("Enter first word:")
word2 = input("Enter second word:")

for ch in word1:

    if ch not in word2 or word1.count(ch)!=word2.count(ch):
        print("Not a anagram")
        break

else:
    print("Anagram")