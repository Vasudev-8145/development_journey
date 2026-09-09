"""
first recursive character in a string
"""

text = "abcaba"

char_count = {}

for ch in text:

    if ch in char_count:
        print(ch,"first recursive character")
        break

    else:
        char_count[ch]=1


"""
or with list
"""

# unique_words = []

# for ch in text:

#     if ch in unique_words:

#         print(ch,"is the first recursive character")
#         break

#     else:
#         unique_words.append(ch)

