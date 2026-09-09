"""
Price increases from 1200 to 1500. Find increase amount and percentage.
"""

inc_from=1200
inc_to=1500
inc_amnt=inc_to-inc_from
per=(inc_amnt/inc_from)*100
print(f"Increase amount is Rs.{inc_amnt}")
print(f"Increase percentage is {per}%")