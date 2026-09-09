"""
ransome note
"""

note = "hen"
megazine = "chicken"

for ch in note:

    if ch not in megazine:
        print("Not a ransome note")
        break

else:
    print("Ransome note")