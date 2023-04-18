import random


# function to check if guess is close or not
def is_close(guess, actual):
    if abs(guess - actual) <= 5:
        return True
    else:
        return False


# function for easy difficulty level
def easy_mode(secret_number):
    print("Guess a number between 1 and 20. You have 6 attempts.")
    for i in range(1, 7):
        guess = int(input("Guess #" + str(i) + ": "))
        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
        else:
            print("You guessed it!")
            return
    print("Sorry, you ran out of attempts. The secret number was " + str(secret_number))


# function for difficult difficulty level
def difficult_mode(secret_number):
    print("Guess a number between 1 and 100.")
    num_attempts = 0
    while num_attempts < 30:
        guess = int(input("Guess: "))
        if guess == secret_number:
            print("Congratulations, you guessed the number!")
            print("Total attempsts: ", num_attempts)
            return
        elif is_close(guess, secret_number):
            print("Close!")
        else:
            print("Not close!")
        num_attempts += 1
    print("Sorry, you have used all your attempts. The secret number was:", secret_number)


def guess_number():
    # get difficulty level from user
    print("Select difficulty level:")
    print("1. Easy")
    print("2. Difficult")
    difficulty = int(input("Enter difficulty level (1 or 2): "))

    # generate secret number
    secret_number = random.randint(1, 20) if difficulty == 1 else random.randint(1, 100)

    # run appropriate game mode
    if difficulty == 1:
        easy_mode(secret_number)
    else:
        difficult_mode(secret_number)
