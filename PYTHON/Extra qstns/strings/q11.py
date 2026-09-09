"""
count words in a string
"""

string = "iam vasudev"

count = 0

for w in string:

    if w.isalpha():
        count+=1

print(count)