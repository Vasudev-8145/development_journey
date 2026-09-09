"""
sales case study
"""

sales = [100000,120000,110000,115000,100000,116000]
#          0      1      2      3     4     5

# display march month sales

print(f"March month sale = {sales[2]}")

# update may month sale as 105000

sales[4] = 105000
print(f"updates sales = {sales}")

# display all sales using index

for i in range(0,len(sales)):
    print(sales[i])

# display sales>100000

print("sales>100000")
for amount in sales:

    if amount>100000:
        print(amount)

