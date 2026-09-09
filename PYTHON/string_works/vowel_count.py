"""
display vowel count
"""

word = "supErcalifragilisticexpialidocious"
vowel_count = 0

for ch in word:

    if ch.lower() in "aeiou":
        vowel_count+=1

print(f"vowel count = {vowel_count}")