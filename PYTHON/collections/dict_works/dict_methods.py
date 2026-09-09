"""
==>  DICTIONARY METHODS

1.keys()    --> to print all keys in the dictionary
2.values()  --> to print all values in the dictionary
3.items()   --> to print keys and values in the dictionary
4.get(key)  --> to get values from dictionary.none will print if the key does not exist


"""

daily_calorie = {"mon":2000,
                 "tue":2100,
                 "wed":2000,
                 "thur":3200,
                 "fri":1000,
                 }

# keys()
# for k in daily_calorie.keys():
#     print(k)

# values()
# for v in daily_calorie.values():
#     print(v)

# items()
# for k,v in daily_calorie.items():
#     print(k,v)

# get()
# print(daily_calorie.get("tue"))
# print(daily_calorie.get("total",0))   #o kodkunath aa key ilenkil 0 print akan ann, 0 kodthilenkil none print akum
                                 