import random


def play():
    choices = ["rock", "paper", "scissors"]

    print("\n=== Rock Paper Scissors ===")

    while True:
        player = input("Choose rock, paper, or scissors: ").lower()

        if player not in choices:
            print("Invalid choice. Please try again.")
            continue

        computer = random.choice(choices)

        print(f"You chose: {player}")
        print(f"Computer chose: {computer}")

        if player == computer:
            print("It's a tie!")
        elif (
            (player == "rock" and computer == "scissors")
            or (player == "paper" and computer == "rock")
            or (player == "scissors" and computer == "paper")
        ):
            print("You win!")
        else:
            print("Computer wins!")

        again = input("Play again? (y/n): ").lower()

        if again != "y":
            break


if __name__ == "__main__":
    play()
