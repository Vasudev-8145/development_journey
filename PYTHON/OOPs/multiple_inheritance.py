"""
Multiple level inheritance
"""

class Father:

    def football_skill(self):
        print("Father has football skill")

class Mother:

    def dancing_skill(self):
        print("Mother has dancing skill")

class Child(Father,Mother):

    def coding_skill(self):
        print("Child has coding skill")

child_instance = Child()

child_instance.coding_skill()
child_instance.dancing_skill()
child_instance.football_skill()