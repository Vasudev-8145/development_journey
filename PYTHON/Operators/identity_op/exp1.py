#in case of string

# p1="jain"
# p2="jain"
p1=["jain"] #ivde string mati list akyapo output mari 
p2=["jain"]

print(p1==p2) #True
print(p1 is p2) #True(string il) #false(list il)

#in case of list(not string)

p1_fav_food=["idly","dosa"]
p2_fav_food=["idly","dosa"]
print(p1_fav_food==p2_fav_food) #True
print(p1_fav_food is p2_fav_food) #False

