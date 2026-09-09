"""
create a new list that containing only consanents
"""

text = "a man a canal panama"

consanents = {ch for ch in text if ch.lower() not in "aeiou" and ch.isalpha()}
print(consanents)