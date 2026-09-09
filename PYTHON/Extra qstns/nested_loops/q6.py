"""
Find all pairs that sum to 10 from 1-9
"""
 
for i in range(1,10):

    for j in range(1,10):

        if i+j == 10:
            sum = i+j
            print(f"({i}+{j}) = {sum}")

            

