"""
1.string_obeject.upper() --> convert string object to upper case
2.string_obeject.lower() --> convert string object to lower case
"""

# greetings = "good morning"               #original string does not get modified
# print(greetings.upper())


# text = "HELLO THERE"
# print(text.lower())


"""
3.string_obeject.isalpha()  --> returns true if string object is full alphabets
4.string_obeject.isdigit()  --> returns true if string object is full digits
5.string_obeject.isalnum()  --> returns true if string object is mix of alphabets and digits
"""

# passord = "password@123"

# if passord.isalpha():
#     print("Password is an alphabet")

# elif passord.isdigit():
#     print("Password is digit")

# elif passord.isalnum():
#     print("Password is alphanumeric")

# else:
#     print("Special character")


"""
6.string_obeject.count(value)  --> return frequency of value. return 0 if the value does not exist
7.string_obeject.find(value)   --> return first index of value. return -1 if the value does not exist
8.string_obeject.index(value)   --> return first index of value. return error if the value does not exist
9.string_obeject.rfind(value)   --> return last index of value. return -1 if the value does not exist
"""

text = "helloworld"

# print(text.count("l"))
# print(text.count("ll"))
# print(text.count("wo"))
# print(text.count("hai"))

# print(text.find("l"))
# print(text.find("w"))
# print(text.find("v"))

# print(text.rfind("l"))
# print(text.rfind("o"))

# print(text.index("e"))
# print(text.index("r"))


"""
10.string_obeject.startswith(substr)  --> return true if string object starts with substr otherwsie false
11.string_obeject.endswith(substr)  --> return true if string object ends with substr otherwsie false
"""

# text = "python"

# print(text.startswith("py"))
# print(text.endswith("n"))


"""
12.string_obeject.replace(old,new)  --> replace old string with new
"""

# text = "i hate python"
# new_text1 = text.replace("hate","love")
# new_text2 = text.replace("i","you")
# print(new_text1)
# print(new_text2)


"""
13.string_obeject.strip(value)      --> remove value from both end
14.string_obeject.lstrip(value)      --> remove value from left end
15.string_obeject.rstrip(value)      --> remove value from right end
"""

# text = "@hel@lo@"
# print(text.strip("@"))
# print(text.lstrip("@"))
# print(text.rstrip("@"))