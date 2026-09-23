import random


def play():
    print("\n=== Coin Flip ===")

    while True:
        choice = input("Heads or tails? ").lower()

        if choice not in ["heads", "tails"]:
            print("Please enter 'heads' or 'tails'.")
            continue

        result = random.choice(["heads", "tails"])

        print(f"The coin landed on: {result}")

        if choice == result:
            print("You guessed correctly!")
        else:
            print("Wrong guess!")

        again = input("Play again? (y/n): ").lower()

        if again != "y":
            break


if __name__ == "__main__":
    play()
