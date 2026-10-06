# Hangman — Python Theory

## 1. Overview

Hangman is a word-guessing game where the player tries to guess a hidden word one letter at a time.

In this version:

* A random word is selected from a JSON file.
* A hint is displayed.
* One letter is automatically revealed at the beginning.
* The player guesses one letter at a time.
* Correct guesses reveal the matching letters.
* Incorrect guesses increase the number of wrong guesses.
* The Hangman drawing changes after each incorrect guess.
* The player loses after 6 incorrect guesses.
* The player wins when all letters have been revealed.

This game introduces several new Python concepts compared with the Level 1 games.

---

# 2. Importing Modules

The game uses two Python modules:

```python
import random
import json
```

### `random`

The `random` module is used to randomly select a word and randomly reveal one letter.

For example:

```python
word = random.choice(list(words))
```

and:

```python
hint_index = random.randint(0, len(word) - 1)
```

### `json`

The `json` module allows Python to read data stored in a JSON file.

The game stores its words and hints in:

```text
level-2/words.json
```

---

# 3. Storing the Hangman Stages

The Hangman drawings are stored inside a list:

```python
hangman_stages = [
    "...",
    "...",
    ...
]
```

Each element represents a different stage of the Hangman drawing.

The game starts with:

```python
wrong_guesses = 0
```

Therefore:

```python
hangman_stages[wrong_guesses]
```

initially displays:

```text
hangman_stages[0]
```

After an incorrect guess:

```python
wrong_guesses += 1
```

the next stage is displayed.

This demonstrates how a variable can be used as a list index.

---

# 4. Reading JSON Data

The game loads the words from a JSON file:

```python
with open("level-2/words.json", "r") as file:
    words = json.load(file)
```

### `open()`

The `open()` function opens a file.

The `"r"` means the file is opened in **read mode**.

### `with`

The `with` statement manages the file automatically.

Once the block finishes, Python closes the file.

### `json.load()`

The `json.load()` function converts the JSON data into a Python object.

For example, the JSON file may contain:

```json
{
    "python": "A programming language",
    "router": "A device that forwards network traffic",
    "computer": "An electronic device used to process data"
}
```

Python can then access the data as a dictionary.

---

# 5. Selecting a Random Word

The game uses:

```python
word = random.choice(list(words))
```

`words` is a dictionary.

The `list(words)` converts the dictionary keys into a list.

For example:

```python
words = {
    "python": "A programming language",
    "router": "A networking device"
}
```

The keys are:

```text
python
router
```

Therefore:

```python
list(words)
```

produces something similar to:

```python
["python", "router"]
```

`random.choice()` then selects one of them randomly.

---

# 6. Getting the Hint

After selecting the word:

```python
hint = words[word]
```

The selected word is used as a dictionary key to retrieve its hint.

For example:

```python
word = "python"
```

Then:

```python
hint = words["python"]
```

might return:

```text
A programming language
```

This demonstrates how dictionaries can store related information using **key-value pairs**.

---

# 7. Creating the Hidden Word Display

The game creates a list of underscores:

```python
display = ["_"] * len(word)
```

If the word is:

```text
python
```

its length is 6.

Therefore:

```python
["_"] * 6
```

creates:

```python
["_", "_", "_", "_", "_", "_"]
```

The display represents the letters that the player has not guessed yet.

---

# 8. Randomly Revealing a Letter

The game automatically reveals one letter:

```python
hint_index = random.randint(0, len(word) - 1)
display[hint_index] = word[hint_index]
```

`random.randint()` generates a random number within the specified range.

For example, if the word has 6 letters:

```python
random.randint(0, 5)
```

could produce:

```text
3
```

Python uses zero-based indexing, so index `3` represents the fourth character.

The corresponding character is then copied into the display.

---

# 9. Lists and Indexing

The game uses lists heavily.

For example:

```python
display = ["_", "_", "_", "_", "_", "_"]
```

Each item has an index:

```text
Index:    0    1    2    3    4    5
          ↓    ↓    ↓    ↓    ↓    ↓
Display: "_"  "_"  "_"  "_"  "_"  "_"
```

A specific letter can be changed using its index:

```python
display[2] = "t"
```

The list would then become:

```python
["_", "_", "t", "_", "_", "_"]
```

This allows the game to reveal letters without replacing the entire display.

---

# 10. Tracking Guessed Letters

The game uses:

```python
guessed_letters = [word[hint_index]]
```

This creates a list containing the automatically revealed letter.

Whenever the player makes a valid guess:

```python
guessed_letters.append(guess)
```

The new letter is added to the list.

This allows the program to prevent the player from guessing the same letter multiple times.

---

# 11. The Game Loop

The main game uses:

```python
while "_" in display and wrong_guesses < max_wrong_guesses:
```

The loop continues while **both conditions** are true.

### Condition 1

```python
"_" in display
```

This means there are still letters that have not been guessed.

### Condition 2

```python
wrong_guesses < max_wrong_guesses
```

This means the player still has remaining attempts.

The game therefore ends when either:

* all letters are guessed, or
* the player reaches 6 wrong guesses.

This demonstrates how multiple conditions can be combined using the `and` operator.

---

# 12. Input Validation

The game checks whether the player's input is valid:

```python
if len(guess) != 1 or not guess.isalpha():
    print("Please enter exactly one letter.")
    continue
```

There are two checks.

### `len()`

```python
len(guess)
```

checks how many characters were entered.

The game requires exactly one character.

### `.isalpha()`

```python
guess.isalpha()
```

checks whether the input contains alphabetic characters.

For example:

```text
a      → True
z      → True
7      → False
@      → False
ab     → True
```

The length check prevents multiple letters from being entered.

---

# 13. Using `continue`

When invalid input is detected:

```python
continue
```

is used.

`continue` immediately skips the rest of the current loop iteration and starts the next iteration.

For example:

```python
if len(guess) != 1:
    print("Invalid input.")
    continue
```

The game asks the player for another guess without processing the invalid input.

---

# 14. Checking for Duplicate Guesses

The game checks:

```python
if guess in guessed_letters:
```

The `in` operator checks whether a value exists inside a collection.

For example:

```python
guessed_letters = ["a", "e", "r"]
```

Then:

```python
"a" in guessed_letters
```

returns:

```text
True
```

while:

```python
"z" in guessed_letters
```

returns:

```text
False
```

This prevents the same letter from being guessed repeatedly.

---

# 15. Checking Whether the Letter Exists

The game checks:

```python
if guess in word:
```

Strings can also be searched using the `in` operator.

For example:

```python
word = "python"
```

Then:

```python
"p" in word
```

is:

```text
True
```

while:

```python
"z" in word
```

is:

```text
False
```

---

# 16. Using `enumerate()`

One of the most important new concepts in this game is:

```python
for index, letter in enumerate(word):
```

`enumerate()` allows Python to provide both:

* the index
* the value

For example:

```python
word = "python"
```

could produce:

```text
0 p
1 y
2 t
3 h
4 o
5 n
```

The program can therefore find exactly where the guessed letter occurs.

---

# 17. Revealing Correct Letters

When a correct letter is guessed:

```python
for index, letter in enumerate(word):
    if letter == guess:
        display[index] = guess
```

Suppose the word is:

```text
python
```

and the player guesses:

```text
o
```

`enumerate()` finds that `"o"` is at index `4`.

The program then performs:

```python
display[4] = "o"
```

The display becomes:

```text
_ _ _ _ o _
```

If a letter appears multiple times, the loop reveals every occurrence.

For example, if the word contains two `"a"` characters, both positions will be updated.

---

# 18. Handling Wrong Guesses

If the guessed letter is not in the word:

```python
else:
    wrong_guesses += 1
    print("Wrong!")
```

The number of wrong guesses increases by one.

The Hangman drawing then changes because:

```python
hangman_stages[wrong_guesses]
```

uses the updated number as the list index.

---

# 19. Game State

The game keeps track of several pieces of information:

```python
word
hint
display
guessed_letters
wrong_guesses
max_wrong_guesses
```

Together, these variables represent the current **state of the game**.

For example:

```text
Word:              python
Hint:              Programming language
Display:           p _ t _ o _
Guessed letters:   p, t, o
Wrong guesses:     2
Maximum mistakes:  6
```

The program continuously updates this state after every guess.

---

# 20. Determining the Winner

After the loop finishes, the program checks:

```python
if "_" not in display:
    print("You guessed the word!")
else:
    print("You lost!")
```

If there are no underscores left, every letter has been revealed.

Therefore:

```python
"_" not in display
```

means the player has won.

Otherwise, the player reached the maximum number of wrong guesses and lost.

---

# 21. Why Hangman Is a Level 2 Game

Hangman is more complex than the Level 1 games because it combines several concepts together.

The game uses:

* JSON files
* dictionaries
* lists
* strings
* indexing
* random selection
* loops
* nested loops
* conditions
* `enumerate()`
* input validation
* `continue`
* list manipulation
* game state management

Instead of simply generating a result, the program must continuously maintain and update the state of the game.

---

# 22. Python Concepts Learned

By studying this game, the following Python concepts are introduced or reinforced:

| Concept            | Example                     |
| ------------------ | --------------------------- |
| Importing modules  | `import random`             |
| JSON files         | `json.load(file)`           |
| Dictionaries       | `words[word]`               |
| Lists              | `display`                   |
| List indexing      | `display[index]`            |
| String operations  | `len(word)`                 |
| Membership testing | `guess in word`             |
| Random selection   | `random.choice()`           |
| Random numbers     | `random.randint()`          |
| `while` loops      | Main game loop              |
| `for` loops        | Revealing letters           |
| `enumerate()`      | Getting index and character |
| `if/else`          | Win/loss logic              |
| `continue`         | Rejecting invalid input     |
| `.append()`        | Tracking guesses            |
| Input validation   | `isalpha()`                 |

---

# 23. Overall Program Flow

The program can be simplified into the following process:

```text
Start
  ↓
Load words from JSON
  ↓
Randomly select a word
  ↓
Get the hint
  ↓
Create hidden word display
  ↓
Reveal one random letter
  ↓
Display Hangman
  ↓
Ask player for a letter
  ↓
Validate input
  ↓
Check if letter was already guessed
  ↓
Is the letter in the word?
  ├── Yes → Reveal matching letters
  │
  └── No  → Increase wrong guesses
  ↓
Check win/loss condition
  ↓
Continue or end game
  ↓
Finish
```

---

# 24. Possible Future Improvements

The current Hangman game can be improved later by adding:

* Multiple difficulty levels
* Different categories of words
* A larger word database
* Score tracking
* Replay functionality
* Hints that can be used only once
* Better graphical presentation
* A word length indicator
* Case-insensitive word handling
* A two-player mode
* A GUI version

These improvements can be added as the project progresses.

---

# 25. Summary

The Hangman game introduces more advanced program logic than the Level 1 games.

The most important concepts are:

1. Loading structured data from JSON.
2. Using dictionaries to associate words with hints.
3. Using lists to represent the hidden word.
4. Using indexes to reveal individual letters.
5. Using `enumerate()` to obtain both indexes and values.
6. Validating user input.
7. Tracking game state.
8. Combining loops and conditions to control the game.

Hangman demonstrates how several basic Python concepts can be combined to create a more interactive program.
