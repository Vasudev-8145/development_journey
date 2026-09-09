"""
 Extract names whose age >=18
Input:[("John",18),("Alice",22),("Bob",16),("Emma",25)]
Output:["John","Alice","Emma"]
"""

names = [("John",18),("Alice",22),("Bob",16),("Emma",25)]

result = [n[0] for n in names if n[1]>=18]
print(result)