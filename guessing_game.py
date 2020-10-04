"""
****guessing game****
Ask for user name
ask for user guess
give user certain amount of guess's
determine if the guess is >, <, = to or != to random number.
print out results to user
Ask user if they want to play again
"""
import random

yes = True
user_name = input("please enter you first name: ")
print("Hello " + user_name + " and welcome to my number guessing game. "
                             "You will be given 6 tries to guess a secret number. "
                             "Please only enter numbers and not letters")

while yes:
    def guessing_game():
        num = random.randint(0, 10)
        guess = 0
        for x in range(0, 5 + 1):
            guess = int(input("Please enter your guess: "))
            if guess > num:
                print("Sorry that number is to high")

            elif guess < num:
                print("Sorry your guess is to low")

            elif guess == num:
                print("That is correct")
                break

        if guess != num:
            print("Sorry you didn't guess correctly the number was " + str(num))


    guessing_game()

    play_again = input("do you want to play again? \n[]yes \n[]no\n: ")
    if play_again.lower() == "yes":
        continue
    else:
        yes = False
