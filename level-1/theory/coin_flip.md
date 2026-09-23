# Coin Flip — Theory

The Coin Flip game builds on the basic Python concepts introduced in Number Guessing.

The main purpose of this game is to practice random choices, strings, input validation, loops, and comparing user input with a randomly generated result.

---

## What This Game Teaches

* `random.choice()`
* Lists
* Strings
* `.lower()`
* Input validation
* `while` loops
* Comparing values
* Boolean conditions
* Repeating a game with a loop

---

## 1. Using Lists

The game stores the possible coin results in a list:

```python
["heads", "tails"]
```

A list is a collection of values.

For example:

```python
choices = ["heads", "tails"]
```

The list contains two strings:

```text
heads
tails
```

Lists are useful when a program has multiple possible values to choose from.

---

## 2. Random Choice

Instead of generating a random number, the Coin Flip game randomly selects an item from a list.

Python's `random` module provides:

```python
random.choice()
```

For example:

```python
result = random.choice(["heads", "tails"])
```

Python randomly selects one item from the list.

The result will therefore be either:

```text
heads
```

or:

```text
tails
```

This is different from:

```python
random.randint(1, 100)
```

which generates a random integer.

### Comparison

```python
random.randint(1, 100)
```

Generates a number.

```python
random.choice(["heads", "tails"])
```

Chooses an item from a collection.

---

## 3. Strings

A string is text stored inside a Python program.

Examples:

```python
"heads"
"tails"
"hello"
"python"
```

The player enters text:

```python
choice = input("Heads or tails? ")
```

The user's answer is stored as a string.

For example, if the user enters:

```text
Heads
```

the value is:

```python
"Heads"
```

---

## 4. Converting Input to Lowercase

Users might enter:

```text
Heads
HEADS
heads
HeAdS
```

We want all of these to be treated as the same choice.

The `.lower()` string method converts text to lowercase:

```python
choice = input("Heads or tails? ").lower()
```

For example:

```python
"HeAds".lower()
```

becomes:

```text
heads
```

This makes input comparison easier.

---

## 5. Input Validation

The game checks whether the user entered a valid choice:

```python
if choice not in ["heads", "tails"]:
    print("Please enter 'heads' or 'tails'.")
    continue
```

The expression:

```python
choice not in ["heads", "tails"]
```

asks:

> Is the user's choice NOT inside the list?

If the user enters:

```text
banana
```

then the condition is `True`, because `"banana"` is not a valid choice.

The program displays an error message and asks again.

---

## 6. The `in` Operator

Python's `in` operator checks whether a value exists inside a collection.

Example:

```python
"heads" in ["heads", "tails"]
```

This produces:

```text
True
```

But:

```python
"banana" in ["heads", "tails"]
```

produces:

```text
False
```

The game uses the opposite:

```python
not in
```

For example:

```python
choice not in ["heads", "tails"]
```

---

## 7. Comparing the Player and Computer

After generating the random result, the game compares it with the player's choice:

```python
if choice == result:
    print("You guessed correctly!")
else:
    print("Wrong guess!")
```

The `==` operator checks whether two values are equal.

For example:

```python
"heads" == "heads"
```

is:

```text
True
```

But:

```python
"heads" == "tails"
```

is:

```text
False
```

---

## 8. Repeating the Game

The game uses a `while` loop:

```python
while True:
```

This allows the player to play repeatedly.

At the end of each round:

```python
again = input("Play again? (y/n): ").lower()
```

The program asks whether another round should be played.

If the player doesn't enter `"y"`:

```python
if again != "y":
    break
```

the loop stops.

---

## 9. `continue` vs `break`

The Coin Flip game uses both `continue` and `break`.

### `continue`

```python
if choice not in ["heads", "tails"]:
    print("Please enter 'heads' or 'tails'.")
    continue
```

`continue` skips the rest of the current loop iteration and starts the next iteration.

In this game, it means:

> The input was invalid, so ask the player again.

### `break`

```python
if again != "y":
    break
```

`break` completely exits the loop.

In this case:

> The player doesn't want another round, so end the game.

### Simple difference

```text
continue → restart the loop
break    → stop the loop
```

---

## 10. Functions

The game is contained inside:

```python
def play():
```

This keeps the game logic organized inside one function.

The program then uses:

```python
if __name__ == "__main__":
    play()
```

to start the game when the file is executed directly.

---

## How Everything Works Together

The basic flow is:

```text
Start
  ↓
Ask player for heads/tails
  ↓
Is the input valid?
  ↓
No ──→ Ask again
  ↓ Yes
Randomly choose heads/tails
  ↓
```
