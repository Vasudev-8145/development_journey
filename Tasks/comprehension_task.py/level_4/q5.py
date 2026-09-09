"""
Replace spaces with underscores Input:["Python Basics","Learn
    Django","React Course"]
    Output:["Python_Basics","Learn_Django","React_Course"]
"""

words = ["Python Basics","Learn Django","React Course"]

replaced_words = [w.replace(" ","_")for w in words]
print(replaced_words)