import random  

top_of_range = input("enter the value: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <=0:
      print("Hey! enter the value greater than the zero next time")
      quit()
else:
    print("hey! please type a number next time ")
    quit()

random_number = random.randint(0, top_of_range)
guesses = 0

while True:
    guesses= guesses+1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("please type a number next time")
        continue

    if user_guess == random_number:
        print("correct.")
        break
    else:
        print("wrong.")
print("you got it in", guesses, "guesses")