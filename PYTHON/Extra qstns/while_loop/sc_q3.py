"""
3. Water Tank Filling

A water tank can hold 500 liters.

The user enters the amount of water added each time.

Keep accepting input until the tank is full or exceeds its capacity.

Display the final amount of water in the tank
"""

max_fill = 0
user_fill = int(input("Enter amount of water added (press 0 to stop):"))

while user_fill!=0 and max_fill<500:

    max_fill = max_fill+user_fill

    if user_fill==500:
        print("Tank is full")
    
    elif user_fill>500:
        print("Above tank capacity")

    else:
        print(f"Amount of water in tank = {max_fill}")
    
    if max_fill<500:
        user_fill = int(input("Enter amount of water added:"))

print(f"Final amount of water in the tank = {max_fill}")
print("Thank you !")
