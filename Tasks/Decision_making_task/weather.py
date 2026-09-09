"""
**Weather Conditions**:
   - Above 30: Hot
   - 20 to 30: Warm
   - Below 20: Cold
"""

weather = int(input("Enter weather temperature:"))

if weather<=20:

    print("cold weather")

elif weather<=30:

    print("warm weather")

else:

    print("Hot weather")