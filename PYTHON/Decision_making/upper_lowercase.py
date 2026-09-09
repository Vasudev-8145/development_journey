"""
check whethear A character is uppercase or lowercase
"""

ch = input("Enter a character:")

if ch.isupper():

    print("Character is in uppercase")

elif ch.islower():

    print("Character is in lowercase")

else:

    print("Not a character")