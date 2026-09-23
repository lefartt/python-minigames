import random

def play():
    number = random.randint(1, 100)
    attempts = 0

    print("\n=== Number Guessing Game ===")
    print("I'm thinking of a number between 1 and 100.")

    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print(f"Correct! You got it in {attempts} attempts.")
            break

if __name__ == "__main__":
    play()
