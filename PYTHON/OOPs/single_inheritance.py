"""
inheritance is the mechanism that child class access the methods and properties of parent class
"""

"""
Single level inheritance
"""

class Parent:

    def house(self):

        print("Parent class house method")

class Child(Parent):

    def insta_account(self):

        print("Child has insta account")

class_instance1 = Child()
class_instance1.insta_account()
class_instance1.house()