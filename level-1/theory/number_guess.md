# Number Guessing — Theory

The Number Guessing game is the first game in Level 1.

It introduces some of the most basic Python concepts, including variables, user input, loops, conditional statements, random numbers, and counters.

---

## What This Game Teaches

* Variables
* User input
* Converting strings to integers
* Random numbers
* `while` loops
* `if`, `elif`, and `else`
* Comparison operators
* Counters
* `break`
* Functions
* Basic program structure

---

## 1. Variables

A variable is a name used to store a value.

For example:

```python
number = random.randint(1, 100)
attempts = 0
```

Here:

* `number` stores the randomly generated number.
* `attempts` stores how many guesses the player has made.

Variables allow the program to store information and use it later.

---

## 2. Random Numbers

Python provides the `random` module for generating random values.

First, import it:

```python
import random
```

Then:

```python
number = random.randint(1, 100)
```

`random.randint(1, 100)` generates a random integer between **1 and 100**, including both 1 and 100.

The generated number is stored in the `number` variable.

---

## 3. User Input

The `input()` function allows the program to receive information from the user.

```python
guess = input("Enter your guess: ")
```

However, `input()` always returns the user's input as a **string**.

For example, if the user enters:

```text
50
```

Python receives:

```python
"50"
```

not:

```python
50
```

Since we need to compare the guess with a number, we convert it into an integer:

```python
guess = int(input("Enter your guess: "))
```

---

## 4. While Loops

A `while` loop repeatedly executes code as long as its condition is `True`.

Example:

```python
while True:
    guess = int(input("Enter your guess: "))
```

Because `True` is always true, the loop continues indefinitely until something stops it.

In this game, the loop stops when the player correctly guesses the number.

---

## 5. Conditional Statements

Conditional statements allow the program to make decisions.

The game uses:

```python
if guess < number:
    print("Too low!")
elif guess > number:
    print("Too high!")
else:
    print("Correct!")
```

The program checks the player's guess against the secret number.

### If

```python
if guess < number:
```

If the guess is smaller than the secret number, the program tells the player:

```text
Too low!
```

### Elif

```python
elif guess > number:
```

If the first condition wasn't true, Python checks this condition.

If the guess is larger than the secret number:

```text
Too high!
```

### Else

```python
else:
```

If neither condition is true, the guess must equal the secret number.

Therefore:

```text
Correct!
```

---

## 6. Comparison Operators

The game uses comparison operators to compare values.

| Operator | Meaning                  |
| -------- | ------------------------ |
| `<`      | Less than                |
| `>`      | Greater than             |
| `==`     | Equal to                 |
| `!=`     | Not equal to             |
| `<=`     | Less than or equal to    |
| `>=`     | Greater than or equal to |

For example:

```python
guess < number
```

asks:

> Is the guess smaller than the secret number?

While:

```python
guess == number
```

asks:

> Is the guess equal to the secret number?

---

## 7. Counters

The game keeps track of how many attempts the player makes.

First:

```python
attempts = 0
```

Every time the player makes a guess:

```python
attempts += 1
```

This is shorthand for:

```python
attempts = attempts + 1
```

So the value changes like this:

```text
0
↓
1
↓
2
↓
3
```

The counter allows the program to tell the player how many attempts were needed.

---

## 8. Break

The `break` statement immediately exits a loop.

In the game:

```python
else:
    print(f"Correct! You got it in {attempts} attempts.")
    break
```

Once the player guesses correctly, `break` stops the `while` loop.

Without `break`, the game would continue asking for guesses even after the correct answer.

---

## 9. Functions

The game is placed inside a function:

```python
def play():
```

A function is a reusable block of code.

The game is then started with:

```python
play()
```

The program actually uses:

```python
if __name__ == "__main__":
    play()
```

This means the `play()` function is called when the file is run directly.

---

## 10. How Everything Works Together

The overall game flow is:

```text
Start program
      ↓
Generate random number
      ↓
Set attempts to 0
      ↓
Ask player for a guess
      ↓
Increase attempts
      ↓
Compare guess with number
      ↓
 ┌────┴─────┐
 ↓          ↓
Too low   Too high
      \      /
       \    /
        ↓  ↓
      Correct?
          ↓
        Yes
          ↓
      End game
```

The important part is that the concepts are not working independently.

For example:

```python
guess = int(input("Enter your guess: "))
```

combines:

* `input()` → gets information from the user
* `int()` → converts the input into an integer
* `guess` → stores the result in a variable

Then:

```python
if guess < number:
```

uses the variable together with a comparison operator and conditional statement.

---

## Practice Questions

Try answering these without looking at the code.

### Question 1

What does this do?

```python
random.randint(1, 100)
```

### Question 2

Why do we use `int()` around `input()`?

### Question 3

What would happen if we removed:

```python
attempts += 1
```

### Question 4

Why is `break` needed?

### Question 5

What is the difference between:

```python
=
```

and:

```python
==
```

---

## Mini Challenge

Try modifying the game yourself.

Ideas:

1. Change the range from `1–100` to `1–500`.
2. Give the player a maximum number of attempts.
3. Tell the player how close their guess was.
4. Add a "Play again?" option.
5. Add input validation so letters don't crash the program.

The goal is to modify the program yourself and understand **why** your changes work.

