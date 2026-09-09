"""
 Add 100 to every salary Input: salary=[1200,1800,1500,2200] Output:
    [1300,1900,1600,2300]
"""

salary = [1200,1800,1500,2200]

salary_add = [sal+100 for sal in salary]
print(salary_add)