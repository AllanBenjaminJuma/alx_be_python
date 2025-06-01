import random

secret_number = random.randint(1,10)
guess = int(input("Enter a random number between 1 and 10: "))

def play():
    if guess == secret_number:
        print("You've won!", secret_number, guess)
    else :
        print(secret_number, guess)

play_on = input("Do you still want to play on ?")

if play_on == "y":
    play()
else:
    print("Thank you!")

# def number_guesser():
#     match guess:
#         case _ if guess == secret_number:
#             print("Congratulations, you guessed it!")
#         case _ if guess > 10:
#             print("Oops, your guess is a bit high. Try again")
#         case _ if guess < 1:
#             print("Nope, your guess is a bit low. Give it another shot!")
#         # case _:
#         #     print("Oops, your guess is a bit high. Try again")

# play_again = input("If you want to play again, type yes: ")

# if play_again == "yes":
#     number_guesser()
# else :
#     print("you are exiting the game!")
#     exit()