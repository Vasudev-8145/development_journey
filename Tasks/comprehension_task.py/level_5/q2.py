"""
Double only even numbers Input:[2,3,6,7,10] Output:[4,3,12,7,20]
"""

numbers = [2,3,6,7,10]

result = [num*2 if num%2==0 else num for num in numbers]
print(result)