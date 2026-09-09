num1 = int(input("Enter num1"))
num2 = int(input("Enter num2"))

try:

    result = num1/num2
    print(result)

except Exception as e:
    print(e)
    

print("db transaction...")
print("file writing...")