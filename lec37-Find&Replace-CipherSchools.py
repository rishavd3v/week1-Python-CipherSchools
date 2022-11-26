# replace() method
# find() method

string = "she is beautiful and she is a good dancer"
print(string.replace(" ","_"))

print(string.find("is"))
print(string.find("is",5))

is_pos1 = string.find("is")
is_pos2 = string.find("is",is_pos1+1)
print(is_pos2)