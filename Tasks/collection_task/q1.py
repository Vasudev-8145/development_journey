"""
word="python programming is simple"
    write a program to print character count
"""

word = "python programming is simple"

word_set = set(word)
ch_count = {}

for w in word_set:

    ch_count[w] = word.count(w)

print(ch_count)
