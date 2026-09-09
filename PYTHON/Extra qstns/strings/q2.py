"""
count vowels and consanents
"""

name = "lunnappi"
vowel_count = 0
consanent_count = 0

for i in name:

    if i in "aeiou":
        vowel_count+=1

    else:
        consanent_count+=1

print(f"vowel count in {name} = {vowel_count}")
print(f"consanent count in {name} = {consanent_count}")