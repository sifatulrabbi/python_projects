import random


def main() -> None:
    low: int = int(input("What is the lowest number: "))
    high: int = int(input("What is the highest number: "))

    user_input = ""

    guess = low

    while user_input != "c" and low != high:
        guess = random.randint(low, high)

        user_input = input(
            f"Is your number {guess}??\n (C) correct / (H) high / (L) low: "
        ).lower()

        if user_input == "h":
            high = guess - 1

        elif user_input == "l":
            low = guess + 1

    print(f"Your number is: {guess}")


main()
