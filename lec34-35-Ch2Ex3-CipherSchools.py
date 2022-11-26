name, chr = input("Enter comma seperated name and character: ").split(",")

print(f"length of your name is {len(name)}")

print(f"character count: {name.strip().lower().count(chr.strip().lower())}")   #case sensitive

# Rishav - rishav
# A - a
# "   a  " -----> "a"
# "  rishav " -----> "rishav"
