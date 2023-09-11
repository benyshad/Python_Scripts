import random
import sys

def main():
    guess()

def guess():
    
    level = 0
    # prompt user for desired level
    while True:
        level = input("Please choose a level: ")
        # check to confirm input is a digit
        try:
            level = int(level)
            # check if input is a positive number
            if level > 0:
                break
            else:
                print("Please input a number greater than 0.")
        except ValueError:
            print("Please input a number.")

    # genarate random integer between 1 and the value of level.
    num = random.randint(0, level)
    # promt the user to guess a number
    while True:
        users_guess = input("Please guess a number: ")
        try:
            users_guess = int(users_guess)
            if users_guess > num:
                print("Too Large! ")
            elif users_guess < num:
                print("Too small")
            else:
                sys.exit("Just right!")
        except ValueError:
            pass

if __name__ == "__main__":
    main()