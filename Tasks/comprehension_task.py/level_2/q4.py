"""
Extract names starting with "A" Input:
    names=["Alice","Bob","Andrew","Emma","Alex"] Expected Output:
    ["Alice","Andrew","Alex"]

"""

names = ["Alice","Bob","Andrew","Emma","Alex"]

words_a = [w for w in names if w[0]=="A"]
print(words_a)