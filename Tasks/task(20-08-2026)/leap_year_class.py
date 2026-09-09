"""
leap year programme using class
"""

class LeapYear:

    def solution(self,year):

        if (year%100==0 and year%400==0) or (year%100!=0 and year%4==0):
            return ("Leap year")

        else:
            return ("Not a leap year")

leap_year_instance = LeapYear()

print(leap_year_instance.solution(2024))
print(leap_year_instance.solution(2026))