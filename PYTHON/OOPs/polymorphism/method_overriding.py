"""
Method over riding
child class redefine the method that is already defined in parent class
"""

class Parent:

    def mobile(self):
        print("Iqoo neo 10r")

class Child(Parent):

    def mobile(self):
        print("Iphone 17 pro")

child_instance = Child()
child_instance.mobile()