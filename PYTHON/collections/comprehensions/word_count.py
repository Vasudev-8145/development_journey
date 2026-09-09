"""
create a new dict with count of words
"""

words = ["hello","hai","hello","wow","silent","active","hello"]

wc = {w:words.count(w) for w in words}
print(wc)