"""

===>  LIST METHODS

==> ADD

    1.append(value)        --> appends object at end of the list
    2.insert(index,value)  --> add object at specified index

==> REMOVE

    3.pop(index)    --> removes the element at specified index.
                      if index not mentioned default -1 will be taken(last index value)
    4.remove(value) --> remove the specified value element.
                       first occurence of the value will be removed.Error if the value not in list

5.index(value)  --> returns index position of first occurence of value
6.count(value)  --> return frequency of value
7.reverse()     --> reverse the list in place
8.sort()        --> sort according to ascending order
                    (if alphabets=alphabetical order) (if numbers=numerical order).
                    to reverse order --> variable.sort(reverse=True)
9.copy()        --> copy one list to another.create new object

"""

colors = ["red","green","blue","red","violet","purple"]
#           0      1       2      3      4       5

# (append)
# colors.append("white")
# print(colors)

# (insert)
# colors.insert(2,"orange")
# print(colors)

# (pop)
# colors.pop()
# print(colors)
# colors.pop(4)
# print(colors)

# (remove)
# colors.remove("red")
# print(colors)

# (index)
# blue_index = colors.index("blue")
# print(blue_index)

# (count)
# red_count = colors.count("red")
# print(red_count)

# (reverse)
# colors.reverse()
# print(colors)

# sort()
# colors.sort()  # sort in ascending order of alphabets
# print(colors)
# colors.sort(reverse=True)  # sort in descending order of alphabets
# print(colors)

# copy()
# messi_fav_food = ["egg","chicken","tea"]
# vasu_fav_food = messi_fav_food.copy()
# vasu_fav_food[2] = "coffee"
# print("messi",messi_fav_food)
# print("vasu",vasu_fav_food)