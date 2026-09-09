"""
Create usernames Input:["John","Alice","Bob","Emma"]
    Output:["john@gmail.com","alice@gmail.com","bob@gmail.com","emma@gmail.com"]
"""

names = ["John","Alice","Bob","Emma"]

username = [n.lower()+"@gmail.com" for n in names]
print(username)