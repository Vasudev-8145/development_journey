"""
Number guessing game
"""

from random import randint
secret_num = randint(1,11)

for i in range(1,6):

    num = int(input("Guess a number (Between 1 and 10):"))

    if num == secret_num:

        print("Congratz..👌")
        break

else:
    print("Bad luck...😢")   #ivdthe else for loop nte ann if nte ala # if il break kodtha else work avila 
