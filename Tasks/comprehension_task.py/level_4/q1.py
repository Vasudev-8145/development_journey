"""
Remove leading and trailing spaces Input:[" John "," Alice "," Bob","Emma"] Output:["John","Alice","Bob","Emma"]
"""

names = [" John "," Alice "," Bob","Emma"]

result = [name.strip(" ") for name in names]
print(result)