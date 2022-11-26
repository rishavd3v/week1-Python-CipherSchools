# # center method
# name = "rishav"
# # **rishav** len ----> 10
# print(name.center(10,"*"))

# output ----> ****Rishav****
name = input("Enter your name: ")
print(name.center(len(name)+8,"*"))