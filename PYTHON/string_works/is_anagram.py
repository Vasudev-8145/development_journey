"""
function is_anagram
"""


def is_anagram(word1,word2):

    for ch in word1.lower():

        if ch not in word2.lower() or word1.count(ch)!=word2.count(ch):
            print(False)
            break

    else:
        print(True)

is_anagram("Listens","silEnt")
is_anagram("act","cat")