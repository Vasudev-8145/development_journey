"""
Replace empty strings with "Unknown"
    Input:["John","","Alice","","David"]
    Output:["John","Unknown","Alice","Unknown","David"]
"""

names = ["John","","Alice","","David"]

replaced_string = ["Unknown" if w=="" else w for w in names]
print(replaced_string)