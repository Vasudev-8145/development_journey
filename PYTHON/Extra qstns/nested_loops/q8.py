"""
print floyd's traingle
"""

count = 1

for r in range(1,5):

    for c in range(1,r+1):

        print(count,end=" ")
        count+=1

    print()