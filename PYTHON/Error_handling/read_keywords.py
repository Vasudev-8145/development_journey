
try:

    fr = open("Error_handling\\ey_words.txt")

    for line in fr:
        print(line)

except Exception as e:

    print(e)

finally:

    print("db commit...")