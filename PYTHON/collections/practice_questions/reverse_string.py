"""
create a new collection of reversed version of all words
"""


words = ["run","car","madam","dam","tight"]

reversed_words = []

for w in words:

    reverse = w[::-1]

    reversed_words.append(reverse)

print(reversed_words)