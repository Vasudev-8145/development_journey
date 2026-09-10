"""
pangram
"""


text = "the quick brown fox jumps over the lazy dog"
alphabets = "abcdefghijklmnopqrstuvwxyz"

for ch in alphabets:

    if ch not in text:
        print("Not pangram")
        break

else:
    print("pangram")


    