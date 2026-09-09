
wishes = ["Good morning","Good afternoon","Good evening","Good night"]

fw = open("file_operation\\greeting.txt","w")
for w in wishes:

    fw.write(w+"\n")

print("write completed....")