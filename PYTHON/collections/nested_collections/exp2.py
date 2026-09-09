"""
name,price,avl_qty => 5 vegetables list of list
"""

vegetables = [

            ["onion",19,"50 kg"],
            ["tomato",17,"40 kg"],
            ["chilli",20,"25 kg"],
            ["garlic",25,"30 kg"],
            ["ginger",14,"20 kg"],

            ]

# display price of ginger

print(vegetables[-1][1])

# display price and avl_qty of tomato

print(vegetables[1][1:])

# display name of every vegetables

veg_names = [name[0] for name in vegetables]
print(veg_names)