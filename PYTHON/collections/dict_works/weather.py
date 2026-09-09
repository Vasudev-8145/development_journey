"""
store last one week weather
"""

weather = {"mon":20.1,
           "tue":21.2,
           "wed":28.7,
           "thur":30,
           "fri":28.7,
           "sat":10,
           "sun":23.3
           }

print(weather["sat"])

weather["sat"] = 29
print(weather)