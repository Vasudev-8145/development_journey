"""
Pass or Fail Input:[35,70,90,48,55]
    Output:["Fail","Pass","Pass","Fail","Pass"]
"""

numbers = [35,70,90,48,55]

result = ["fail" if num<50 else "pass" for num in numbers]
print(result)