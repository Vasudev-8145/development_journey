"""
 Label numbers Input:[50,120,80,200,95]
    Output:["Low","High","Low","High","Low"]
"""

numbers = [50,120,80,200,95]

result = ["Low" if num<100 else "High" for num in numbers]
print(result)