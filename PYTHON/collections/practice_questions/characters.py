"""
display vowels, consonansts, special characters, digits
"""

text = "hello$world#12"

vowels = []
consanents = []
digits = []
specials = []

for ch in text:

    if ch.lower() in "aeiou":
        vowels.append(ch)

    elif ch.isalpha():
        consanents.append(ch)

    elif ch.isdigit:
        digits.append(ch)

    else:
        specials.append(ch)

print(f"vowels = {vowels}")
print(f"consanents = {consanents}")
print(f"digits = {digits}")
print(f"specials = {specials}")