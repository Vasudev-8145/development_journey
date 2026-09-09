"""
Use membership operator to check if item is in a list
"""

item=input("Enter a vegetable:")
vegetables=["carrot","cucumber","tomato","onion"]
if item in vegetables:
    print(item,"is available")
else:
    print(item,"is not available")