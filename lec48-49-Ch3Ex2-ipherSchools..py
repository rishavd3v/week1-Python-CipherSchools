# Exercise - Watch COCO 
# ask user's name and age
# if name starts with ('a' or 'A') and age is above 10 then
# print "you can watch"
# else print "sorry, you cannot watch COCO"

name = input("Enter your name: ")
age = int(input("Enter your name: "))
if age>10 and (name[0] == "a" or name[0]=="A"):
    print("You can watch Coco")
else: 
    print("sorry, you cannot watch Coco")