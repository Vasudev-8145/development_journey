"""
find the sum of numbers
"""

num1 = int(input("Enter lower limit:"))
num2 = int(input("Enter upper limit:"))
sum = 0

for i in range(num1,num2+1):

    sum = sum+i

print(f"Sum of numbers = {sum}")