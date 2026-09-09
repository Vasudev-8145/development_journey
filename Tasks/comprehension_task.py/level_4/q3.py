"""
Get first character of every word
    Input:["Python","Java","Django","React"] Output:["P","J","D","R"]
"""

words = ["Python","Java","Django","React"]

characters = [ch[0] for ch in words]
print(characters)