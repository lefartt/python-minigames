import random


def play():
    print("\n=== Dice Roller ===")

    while True:
        try:
            number_of_dice = int(input("How many dice do you want to roll? "))

            if number_of_dice <= 0:
                print("Please enter a number greater than 0.")
                continue

        except ValueError:
            print("Please enter a whole number.")
            continue

        rolls = []

        for _ in range(number_of_dice):
            rolls.append(random.randint(1, 6))

        print(f"You rolled: {rolls}")
        print(f"Total: {sum(rolls)}")

        again = input("Roll again? (y/n): ").lower()

        if again != "y":
            break


if __name__ == "__main__":
    play()
