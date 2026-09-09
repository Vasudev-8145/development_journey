"""
anagram
"""

word1 = input("Enter first word:")
word2 = input("Enter second word:")

for ch in word1:

    if ch not in word2 and word1.count(ch)!=word2.count(ch):
        print("Not anagram")
        break

else:
    print("Anagram")