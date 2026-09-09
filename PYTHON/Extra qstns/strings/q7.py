"""
count alphabets, digits, special characters
"""

string = input("Enter a sentence:")
alphabets_count = 0
digit_count = 0
special_count = 0

for i in string:

    if i.isalpha():
        alphabets_count+=1

    elif i.isdigit():
        digit_count+=1

    else:
        special_count+=1

print(f"Number of alphabets = {alphabets_count}")
print(f"Number of digits = {digit_count}")
print(f"Number of special characters = {special_count}")