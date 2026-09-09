"""
define a calculator function accept any numbers and operation
"""

def calculator(*args,**kwargs):

    if kwargs.get("operation")=="+":
        return sum(args)

    elif kwargs.get("operation")=="*":
        result=1
        for i in args:
            result*=i
        return result

print(calculator(10,20,operation="+"))
print(calculator(10,20,30,operation="*"))
    