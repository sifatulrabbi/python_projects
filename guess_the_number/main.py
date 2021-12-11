import random


def main() -> None:
    low = 1
    high = int(input("Define the max number: "))

    number = random.randint(1, high)
    guess = 0

    while guess != number:
        guess = int(input(f"\nGuess the number between {low} to {high}: "))

        if guess < number:
            print("You guess is too low!")

        elif guess > number:
            print("Your guess is too high!")

    print(f"\nCongrats! you've guessed the number, {number}")


main()
