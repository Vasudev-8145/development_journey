print("Welcome to number guessing game...😍")
print("You have 5 attempts")

from random import randint

secret_number = randint(1,11)

for i in range(1,6):

    num = int(input("Guess a number (Between 1 to 10):"))

    if num == secret_number:
        print("You won..👾")
        print(f"You won in {i} attempts")

        break

    elif num<secret_number:
        print("Too low..🤔")

    elif num>secret_number:
        print("Too high..😤")

else:
    print("Bad luck...🙌")