"""
Employee id,name,salary,phone,department
        -setemployee(id,name,salary,phone,department)
        -getemployee()
"""

class Employee:

    id:str
    name:str
    salary:int
    phone:int
    department:str

    def __init__(self,id,name,salary,phone,department):

        self.id = id
        self.name = name
        self.salary = salary
        self.phone = phone
        self.department = department

    def get_employee(self):

        print(self.id,self.name,self.salary,self.phone,self.department)

employee1_instance = Employee("lumi_12","Sajay",75000,9845621789,"Trainer")
employee2_instance = Employee("lumi_15","Haritha",45000,9845789789,"Consultant")

employee1_instance.get_employee()
employee2_instance.get_employee()