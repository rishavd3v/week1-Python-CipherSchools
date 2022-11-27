# exercise 
# Number guessing game
# ask user to guess number.
# if user guessed number correctly then print "You Win!"
# if user didn't guessed correctly then:
#      if user guessed lower than actual number then print "Too low"
#      if user guessed higher than actual number than actual number then print "too high"

# Solution

winning_num = 13
user_input = int(input("Guess a number b/w 1 and 100: "))
if user_input == winning_num:
    print("You Win!")
else:
    if user_input>winning_num:
        print("Too High")
    else:
        print("Too Low")