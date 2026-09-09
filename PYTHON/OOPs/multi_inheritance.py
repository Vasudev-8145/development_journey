"""
Multi level inheritance
"""

class Grandparent:

    def properties(self):
        print("2 acre land...")

class Parent(Grandparent):

    def home(self):
        print("1500sqft home")

class Child(Parent):

    def insta_acnt(self):
        print("Insta account")

child_instance = Child()
child_instance.insta_acnt()
child_instance.home()
child_instance.properties()