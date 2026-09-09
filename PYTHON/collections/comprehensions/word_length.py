"""
create a dict with number of characters in each word
"""

words = ["hello","hai","python","program"]

wl = {w:len(w) for w in words}
print(wl)