"""
Find length of each word Input:
    words=["apple","cat","elephant","bat"] Output: [5,3,8,3]
"""

words = ["apple","cat","elephant","bat"]

length = [len(w) for w in words]
print(length)