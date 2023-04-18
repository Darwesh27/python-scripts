import random


def guess_number():
    """A number guessing game"""
    secret_number = random.randint(1, 100)
    num_guesses = 0

    while True:
        try:
            guess = int(input("Guess a number between 1 and 100: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        num_guesses += 1

        if guess == secret_number:
            print(f"Congratulations! You guessed the number in {num_guesses} guesses.")
            break
        elif guess < secret_number:
            print("Too low. Guess again.")
        else:
            print("Too high. Guess again.")


if __name__ == "__main__":
    guess_number()
