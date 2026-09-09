"""
create a function to count vowels in a string
"""

def vowel_count(string):

    count = 0

    for ch in string:

        if ch.lower() in "aeiou":
            count+=1

    print(f"vowel count = {count}")

vowel_count("vasudev")
