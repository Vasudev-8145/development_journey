"""
write palindromes to palidrome.txt
"""

words = ["madam","aba","tan","sin","malayalam"]

fw = open("file_operation\\palindrome.txt","w")

for w in words:

    if w[::-1] == w:

        fw.write(w+"\n")

print("completed...")

fw.close()