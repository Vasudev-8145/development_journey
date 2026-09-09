"""
Capitalize every word Input:["john","alice","bob","emma"]
    Output:["John","Alice","Bob","Emma"]
"""

words = ["john","alice","bob","emma"]

result = [w[0].upper()+w[1:] for w in words]
print(result)