import random
import json


hangman_stages = [
    """
     +---+
     |   |
         |
         |
         |
         |
    ========
    """,
    """
     +---+
     |   |
     O   |
         |
         |
         |
    ========
    """,
    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    ========
    """,
    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    ========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    ========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    ========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    ========
    """
]


with open("words.json", "r") as file:
    words = json.load(file)


word = random.choice(list(words))
hint = words[word]

print(f"Hint: {hint}")

display = ["_"] * len(word)

hint_index = random.randint(0, len(word) - 1)
display[hint_index] = word[hint_index]

guessed_letters = [word[hint_index]]

wrong_guesses = 0
max_wrong_guesses = 6


print("=== Hangman ===")
print()
print(hangman_stages[wrong_guesses])
print(" ".join(display))


while "_" in display and wrong_guesses < max_wrong_guesses:

    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter exactly one letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct!")

        for index, letter in enumerate(word):
            if letter == guess:
                display[index] = guess

    else:
        wrong_guesses += 1
        print("Wrong!")
        print(f"Wrong guesses: {wrong_guesses}/{max_wrong_guesses}")

    print(hangman_stages[wrong_guesses])
    print(" ".join(display))


if "_" not in display:
    print("You guessed the word!")
else:
    print("You lost!")
    print(f"The word was: {word}")

