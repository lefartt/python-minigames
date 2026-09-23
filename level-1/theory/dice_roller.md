# Dice Roller — Theory

The Dice Roller game builds on the concepts learned from the previous games.

The main new concept in this game is using a `for` loop to repeat an action a specific number of times.

The game also introduces lists, `append()`, and `sum()`.

---

## What This Game Teaches

* `for` loops
* `range()`
* Lists
* `append()`
* `sum()`
* Multiple random values
* `try` / `except`
* `ValueError`
* Input validation
* Processing multiple pieces of data

---

## 1. Getting the Number of Dice

The player chooses how many dice they want to roll:

```python
number_of_dice = int(input("How many dice do you want to roll? "))
```

For example, if the player enters:

```text
3
```

then:

```python
number_of_dice
```

contains:

```text
3
```

The program can then use this number to determine how many times it should roll a die.

---

## 2. The `for` Loop

A `for` loop is useful when you know how many times you want something to happen.

For example:

```python
for _ in range(number_of_dice):
    print("Rolling...")
```

If:

```python
number_of_dice = 3
```

then the loop runs three times.

The flow is:

```text
Loop 1 → Rolling...
Loop 2 → Rolling...
Loop 3 → Rolling...
```

This is different from a `while` loop.

### `while` loop

A `while` loop continues while a condition is true:

```python
while True:
    ...
```

### `for` loop

A `for` loop is commonly used when iterating over a collection or repeating something a known number of times:

```python
for _ in range(3):
    ...
```

---

## 3. Understanding `range()`

The `range()` function generates a sequence of numbers.

For example:

```python
range(3)
```

represents:

```text
0
1
2
```

Therefore:

```python
for _ in range(3):
```

runs three times.

Notice that Python starts counting from `0`.

So:

```python
range(5)
```

produces:

```text
0
1
2
3
4
```

There are still five values.

---

## 4. What Does `_` Mean?

The game uses:

```python
for _ in range(number_of_dice):
```

The underscore `_` is commonly used when the loop variable itself isn't needed.

For example:

```python
for _ in range(3):
    print("Hello")
```

prints:

```text
Hello
Hello
Hello
```

We don't care whether the loop is currently on `0`, `1`, or `2`.

We only care that the loop runs three times.

---

## 5. Creating a List

The game creates an empty list:

```python
rolls = []
```

A list can store multiple values.

For example:

```python
rolls = [3, 6, 2]
```

The list contains three dice results.

At the beginning of the game, however, we don't know what the results will be, so we start with:

```python
rolls = []
```

---

## 6. Adding Values With `append()`

The `append()` method adds an item to the end of a list.

The game uses:

```python
rolls.append(random.randint(1, 6))
```

First:

```python
random.randint(1, 6)
```

generates a random number between 1 and 6.

Then:

```python
rolls.append(...)
```

adds that number to the list.

For example:

```text
First roll → 4
Second roll → 2
Third roll → 6
```

The list becomes:

```python
[4, 2, 6]
```

---

## 7. Combining `for`, `random`, and `append()`

This is one of the most important parts of the game:

```python
rolls = []

for _ in range(number_of_dice):
    rolls.append(random.randint(1, 6))
```

Suppose:

```python
number_of_dice = 3
```

The loop runs three times.

### First iteration

```python
random.randint(1, 6)
```

might generate:

```text
4
```

The list becomes:

```python
[4]
```

### Second iteration

It might generate:

```text
2
```

The list becomes:

```python
[4, 2]
```

### Third iteration

It might generate:

```text
6
```

The final list becomes:

```python
[4, 2, 6]
```

---

## 8. Calculating the Total

The game uses Python's built-in `sum()` function:

```python
sum(rolls)
```

If:

```python
rolls = [4, 2, 6]
```

then:

```python
sum(rolls)
```

returns:

```text
12
```

So the program can display:

```python
print(f"Total: {sum(rolls)}")
```

Output:

```text
Total: 12
```

---

## 9. Why Use a List?

You might wonder why we don't just store the total.

The list lets us keep the individual results.

For example:

```python
rolls = [4, 2, 6]
```

allows us to display:

```text
You rolled: [4, 2, 6]
```

and calculate:

```python
sum(rolls)
```

If we only stored:

```python
total = 12
```

we would no longer know what each individual die rolled.

Keeping the list gives the program more information to work with.

---

## 10. Input Validation With `try` and `except`

The player is expected to enter a whole number.

However, they might enter:

```text
hello
```

If the program tries:

```python
int("hello")
```

Python cannot convert it into an integer.

This causes a `ValueError`.

To prevent the program from crashing, we use:

```python
try:
    number_of_dice = int(input("How many dice do you want to roll? "))

except ValueError:
    print("Please enter a whole number.")
```

The `try` block contains code that might cause an error.

The `except` block handles the error if it occurs.

---

## 11. Why `ValueError`?

Python raises different types of errors for different problems.

In this game:

```python
int("hello")
```

causes:

```text
ValueError
```

because Python received a value that cannot be converted into an integer.

For example:

```python
int("5")
```

works.

But:

```python
int("hello")
```

does not.

---

## 12. Validating the Number

The player could also enter:

```text
0
```

or:

```text
-5
```

These are valid integers, but they don't make sense for the game.

So the program checks:

```python
if number_of_dice <= 0:
    print("Please enter a number greater than 0.")
    continue
```

This is an example of **logical input validation**.

The input has the correct data type, but the value itself isn't acceptable.

---

## 13. `continue` in This Game

The game uses:

```python
continue
```

when invalid input is detected.

For example:

```python
if number_of_dice <= 0:
    print("Please enter a number greater than 0.")
    continue
```

`continue` skips the rest of the current loop iteration and starts the next iteration.

So instead of trying to roll zero or negative dice, the program asks again.

---

## 14. The Difference Between Invalid Types and Invalid Values

There are two different problems the game handles.

### Invalid type

The player enters:

```text
hello
```

This cannot be converted into an integer.

The `except ValueError` handles it.

### Invalid value

The player enters:

```text
-2
```

This is a valid integer, but it isn't useful for the game.

The `if` statement handles it.

```python
if number_of_dice <= 0:
```

This distinction is important in many real programs.

---

## How Everything Works Together

The game flow is:

```text
Start
  ↓
Ask how many dice
  ↓
Convert input to integer
  ↓
Valid integer?
  ↓
No ──→ Show error → Ask again
  ↓ Yes
Is number greater than 0?
  ↓
No ──→ Show error → Ask again
  ↓ Yes
Create empty list
  ↓
Repeat for each die
  ↓
Generate random number 1–6
  ↓
Add result to list
  ↓
Display all rolls
  ↓
Calculate total
  ↓
Ask to roll again
```

---

## Example

Suppose the player enters:

```text
How many dice do you want to roll? 4
```

The program creates:

```python
rolls = []
```

Then the `for` loop runs four times.

Possible results:

```text
5
2
6
3
```

The list becomes:

```python
[5, 2, 6, 3]
```

Then:

```python
sum(rolls)
```

calculates:

```text
16
```

The output becomes:

```text
You rolled: [5, 2, 6, 3]
Total: 16
```

---

## Key Concepts From This Game

The most important new concept is the `for` loop:

```python
for _ in range(number_of_dice):
```

It allows the program to repeat an action a specific number of times.

Another important combination is:

```python
rolls.append(random.randint(1, 6))
```

This:

1. Generates a random number.
2. Adds it to a list.

Finally:

```python
sum(rolls)
```

allows the program to process all the values stored in the list.

---

## Practice Questions

### Question 1

If:

```python
number_of_dice = 5
```

how many times does this loop run?

```python
for _ in range(number_of_dice):
```

### Question 2

What does `append()` do?

### Question 3

What would this return?

```python
sum([2, 5, 3])
```

### Question 4

Why do we use `try` and `except`?

### Question 5

What's the difference between:

```text
"hello"
```

and:

```text
-5
```

when validating the number of dice?

---

## Mini Challenge

Try modifying the game yourself.

Ideas:

1. Allow the player to choose the number of sides on the dice.
2. Add a 20-sided dice option.
3. Display the highest roll.
4. Display the lowest roll.
5. Calculate the average roll.
6. Count how many times a 6 was rolled.
7. Add a maximum number of dice.

Try implementing these yourself before looking for a solution.
