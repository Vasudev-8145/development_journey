"""
index of first non recursive character

input: s="loveleetcode"
output:2
"""

s = "loveleetcode"

for ch in s:

    if s.count(ch) == 1:

        index = s.find(ch)
        print(f"index of first non recursive character = {index}")
        break

else:
    print("All are repeating character")