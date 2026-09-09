"""
 Add ".com" to each website name
    Input:["google","amazon","github","openai"]
    Output:["google.com","amazon.com","github.com","openai.com"
"""

domain = ["google","amazon","github","openai"]

result = [d+".com" for d in domain]
print(result)