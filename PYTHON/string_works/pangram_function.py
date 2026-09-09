"""
function is_pangram
"""


def is_pangram(text):

    pangram = "abcdefghijklmnopqrstuvwxyz"

    for ch in pangram.lower():

        if ch not in text.lower():
            print(False)
            break

    else:
        print(True)

is_pangram("The quick brown fox jumps over the lazy dog")