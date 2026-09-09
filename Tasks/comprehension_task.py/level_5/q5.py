"""
 Classify temperatures Input:[18,22,35,28,15]
    Output:["Cold","Warm","Hot","Warm","Cold"]
"""

temparature = [18,22,35,28,15]

result = ["cold" if t<=20 else "warm" if t<=30 else "Hot" for t in temparature]
print(result)