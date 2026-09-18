"""
first repeating character in a string

input => s="ababbc"
output => a
"""

s = "ababbc"

repeating_list = []

for ch in s:

    if ch not in repeating_list:
        repeating_list.append(ch)

    else:
        print(f"first repeating character = {ch}")
        break

