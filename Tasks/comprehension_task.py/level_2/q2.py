"""
Extract words longer than 5 letters Input:
    words=["apple","watermelon","dog","elephant","cat"]
      Expected Output: ["watermelon","elephant"]
"""

words = ["apple","watermelon","dog","elephant","cat"]

words_lt_five = {w for w in words if len(w)>5}
print(words_lt_five)