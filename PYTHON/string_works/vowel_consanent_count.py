"""
vowel count, consanent count
"""

word = "pneumonoultramicroscopicsilicovolcanoconiosis"

v_count = 0
c_count = 0

for ch in word:

    if ch.lower() in "aeiou":
        v_count+=1

    else:
        c_count+=1

print(f"Vowel count = {v_count}")
print(f"Consonant count = {c_count}")