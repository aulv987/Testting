myStr="hello new"
print(dir(myStr))

print("my name is "+ myStr)
print(f"my name is {myStr}")
print("my name is {0}".format(myStr))



print(myStr.upper())
print(myStr.lower())
print(myStr.swapcase())
print(myStr.capitalize())
print(myStr.replace("hello","bye").upper())
print(myStr.count("l"))

print(myStr.startswith("hello"))
print(myStr.endswith("new"))
print(myStr.split("l"))
print(myStr.find("l"))