# Level 1 — Python Theory

Level 1 focuses on the basic Python concepts used to build simple command-line games.

The goal is not only to play the games, but also to understand how the Python code works.

---

## 1. Variables

A variable is used to store a value so that the program can use it later.

Example:

```python
attempts = 0
```

The variable `attempts` starts with a value of `0`.

The value can then be changed:

```python
attempts += 1
```

This increases `attempts` by 1.

### Used in

**Number Guessing Game**

```python
attempts = 0

attempts += 1
```

The program uses `attempts` to keep track of how many guesses the player has made.

---

## 2. User Input

Python's `input()` function allows a program to receive information from the user.

Example:

```python
guess = input("Enter your guess: ")
```

The value returned by `input()` is a string.

If the program expects a number, the input can be converted using `int()`:

```python
guess = int(input("Enter your guess: "))
```

### Used in

The games use `input()` to allow the player to interact with the program.

For example:

```python
player = input("Choose rock, paper, or scissors: ").lower()
```

---

## 3. Conditional Statements

Conditional statements allow a program to make decisions.

The basic structure is:

```python
if condition:
    # code
elif another_condition:
    # code
else:
    # code
```

For example:

```python
if guess < number:
    print("Too low!")
elif guess > number:
    print("Too high!")
else:
    print("Correct!")
```

The program checks different conditions and executes the appropriate block of code.

### Used in

**Number Guessing Game**

The program checks whether the player's guess is:

* Lower than the target number
* Higher than the target number
* Equal to the target number

**Rock Paper Scissors**

Conditional statements determine whether the player wins, loses, or ties.

---

## 4. Loops

Loops allow a section of code to run repeatedly.

### `while` loop

A `while` loop continues running while its condition is true.

Example:

```python
while True:
    print("This keeps running")
```

Because `True` never becomes false, the loop continues until something stops it.

A `break` statement can be used to exit the loop:

```python
while True:
    answer = input("Continue? ")

    if answer == "n":
        break
```

### Used in

The games use `while` loops when the player is allowed to continue playing.

For example:

```python
while True:
    # game logic

    again = input("Play again? (y/n): ").lower()

    if again != "y":
        break
```

---

## 5. `for` Loops

A `for` loop is useful when something needs to be repeated a specific number of times.

Example:

```python
for _ in range(5):
    print("Hello")
```

This prints `Hello` five times.

The `_` is commonly used when the loop variable itself is not needed.

### Used in

**Dice Roller**

```python
for _ in range(number_of_dice):
    rolls.append(random.randint(1, 6))
```

The loop runs once for every die the player wants to roll.

For example, if the player enters `3`, the loop runs three times.

---

## 6. Lists

A list stores multiple values in a single variable.

Example:

```python
choices = ["rock", "paper", "scissors"]
```

A list can contain multiple related values.

Individual elements can be accessed using an index:

```python
print(choices[0])
```

This prints:

```text
rock
```

Python lists start counting from index `0`.

### Used in

**Rock Paper Scissors**

```python
choices = ["rock", "paper", "scissors"]
```

The list stores the possible choices.

**Dice Roller**

```python
rolls = []
```

The program starts with an empty list and adds each dice result:

```python
rolls.append(random.randint(1, 6))
```

---

## 7. Random Numbers

Python provides the `random` module for generating random values.

First, import the module:

```python
import random
```

A random integer can be generated using:

```python
random.randint(1, 100)
```

This generates a random integer between 1 and 100, including both 1 and 100.

### Used in

**Number Guessing Game**

```python
number = random.randint(1, 100)
```

The computer randomly chooses the number the player needs to guess.

**Dice Roller**

```python
random.randint(1, 6)
```

This simulates a six-sided die.

**Coin Flip**

```python
random.choice(["heads", "tails"])
```

This randomly selects either `heads` or `tails`.

**Rock Paper Scissors**

```python
random.choice(choices)
```

This allows the computer to randomly choose rock, paper, or scissors.

---

## 8. Functions

A function is a reusable block of code that performs a particular task.

Example:

```python
def play():
    print("Starting game")
```

The function can then be called:

```python
play()
```

Functions make programs easier to organize and understand.

Instead of putting all the game code directly in the main program, the game logic can be placed inside a function.

### Used in

All Level 1 games use a `play()` function.

For example:

```python
def play():
    # game logic
```

---

## 9. Input Validation

Input validation checks whether the user entered something that the program can accept.

For example:

```python
choices = ["rock", "paper", "scissors"]

if player not in choices:
    print("Invalid choice.")
```

The program checks whether the player's input exists in the list of valid choices.

Without validation, unexpected input could cause the program to behave incorrectly.

### Used in

**Rock Paper Scissors**

```python
if player not in choices:
    print("Invalid choice. Please try again.")
    continue
```

**Coin Flip**

```python
if choice not in ["heads", "tails"]:
    print("Please enter 'heads' or 'tails'.")
    continue
```

---

## 10. Error Handling with `try` and `except`

Sometimes a user enters something that Python cannot convert into the expected data type.

For example:

```python
number = int(input("Enter a number: "))
```

If the user enters:

```text
hello
```

Python cannot convert `"hello"` into an integer.

This causes a `ValueError`.

We can handle this using `try` and `except`:

```python
try:
    number = int(input("Enter a number: "))
except ValueError:
    print("Please enter a whole number.")
```

This allows the program to handle invalid input instead of crashing.

### Used in

**Dice Roller**

```python
try:
    number_of_dice = int(input("How many dice do you want to roll? "))

except ValueError:
    print("Please enter a whole number.")
```

---

## 11. Boolean Logic

Boolean logic deals with values that are either:

```text
True
False
```

Python provides operators such as:

* `and`
* `or`
* `not`

For example:

```python
if age >= 18 and has_id:
    print("Allowed")
```

Both conditions must be true because `and` is being used.

### Used in

**Rock Paper Scissors**

The program uses multiple conditions to determine the winner:

```python
(player == "rock" and computer == "scissors")
```

This condition is true only when:

* The player chose rock
* The computer chose scissors

---

## 12. String Methods

Strings are pieces of text.

Python provides methods that can be used to manipulate strings.

One example is `.lower()`:

```python
choice = input("Heads or tails? ").lower()
```

If the player enters:

```text
HEADS
```

`.lower()` converts it to:

```text
heads
```

This makes input validation easier because the program does not need separate checks for uppercase and lowercase input.

### Used in

All games that receive text input can use string methods such as `.lower()`.

---

## 13. `append()`

The `append()` method adds an item to the end of a list.

Example:

```python
rolls = []

rolls.append(5)
rolls.append(2)
```

The list becomes:

```python
[5, 2]
```

### Used in

**Dice Roller**

```python
rolls.append(random.randint(1, 6))
```

Each dice result is added to the `rolls` list.

---

## 14. `sum()`

Python provides the `sum()` function to calculate the total of numbers in an iterable such as a list.

Example:

```python
numbers = [5, 4, 3]

total = sum(numbers)
```

The result is:

```text
12
```

### Used in

**Dice Roller**

```python
print(f"Total: {sum(rolls)}")
```

This calculates the total value of all the dice that were rolled.

---

## 15. `__name__ == "__main__"`

You may notice this at the bottom of the game files:

```python
if __name__ == "__main__":
    play()
```

Python gives every file a special variable called `__name__`.

When the file is run directly, Python sets:

```python
__name__ == "__main__"
```

Therefore:

```python
if __name__ == "__main__":
    play()
```

means:

> Run `play()` when this file is executed directly.

This becomes especially useful when programs start being split into multiple files and modules.

---

# How the Concepts Work Together

The individual concepts become more useful when combined.

For example, the Number Guessing Game uses:

```text
random
   ↓
Generate a number

input()
   ↓
Get player's guess

int()
   ↓
Convert input to a number

if / elif / else
   ↓
Compare the guess

while
   ↓
Allow repeated guesses

variable
   ↓
Track the number of attempts

function
   ↓
Organize the game
```

The Rock Paper Scissors game combines several concepts:

```text
list
   ↓
Store possible choices

input()
   ↓
Get player's choice

random.choice()
   ↓
Choose the computer's move

if / elif / else
   ↓
Determine the result

while
   ↓
Allow multiple rounds

input validation
   ↓
Handle invalid choices
```

---

# Level 1 Learning Goals

After completing Level 1, you should be comfortable with:

* Creating and using variables
* Getting input from users
* Converting data types
* Using `if`, `elif`, and `else`
* Using `while` and `for` loops
* Creating functions
* Working with lists
* Using the `random` module
* Validating user input
* Handling basic errors with `try` and `except`
* Using Boolean logic
* Understanding how a simple Python program is structured

These concepts form the foundation for the more advanced games and projects in later levels.
