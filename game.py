import random


def main() -> None:
    print("Welcome to Number Guess!")
    print("I'm thinking of a number between 1 and 20.")

    secret = random.randint(1, 20)
    attempts = 0

    while True:
        guess_raw = input("Enter your guess: ").strip()

        if not guess_raw.isdigit():
            print("Please enter a whole number.")
            continue

        guess = int(guess_raw)
        attempts += 1

        if guess < secret:
            print("Too low.")
        elif guess > secret:
            print("Too high.")
        else:
            print(f"You got it in {attempts} attempt(s)! The number was {secret}.")
            break


if __name__ == "__main__":
    main()
