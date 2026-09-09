"""
pangram
"""


text = "the quick brown fox jumps over the lazy dog"
alphabets = "abcdefghijklmnopqrstuvwxyz"

for alpha in alphabets:

    if alpha not in text:
        print("Not a pangram")
        break

else:
    print("Pangram")


    