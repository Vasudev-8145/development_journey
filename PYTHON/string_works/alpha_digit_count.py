"""
display alphabet_count,digit_count
"""

text = "england won by 3 wickets with 3 balls remaining. england leads the series with 2-1"

alphabet_count = 0
digit_count = 0
special_char =0

for ch in text:

    if ch.isalpha():
        alphabet_count+=1

    elif ch.isdigit():
        digit_count+=1

    else:
        special_char+=1

print(f"Alphabet count = {alphabet_count}")
print(f"Digit count = {digit_count}")
print(f"Special character count = {special_char}")

