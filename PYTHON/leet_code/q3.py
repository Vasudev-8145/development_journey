"""
least positive missing integer

arr = [1,2,3,5]
output:4
"""

arr = [1,2,4,5]

sum_arr = sum(arr)
total = 0

for num in range(min(arr),max(arr)+1):

    total+=num

missing_num = total-sum_arr

print(f"missing number = {missing_num}")

"""
sliding window technique
"""


# arr = [1,3,2,5,4,7]
# arr.sort() #list internaly sort avum vere variable ilot edtha none kanikum

# l = 0

# while(l<len(arr)-1):

#     r = l+1

#     difference = arr[r] - arr[l]

#     if difference!=1:

#         print(arr[l]+1,"is missing")
#         break

#     l=l+1