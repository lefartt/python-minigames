# Rock Paper Scissors — Theory

Rock Paper Scissors is the final game in Level 1.

It combines many of the concepts learned in the previous games and introduces more complex Boolean logic.

The game also demonstrates how multiple conditions can be combined to represent game rules.

---

## What This Game Teaches

* Lists
* `random.choice()`
* String methods
* Input validation
* `if`, `elif`, and `else`
* Boolean logic
* `and`
* `or`
* Comparing strings
* Functions
* Loops
* Combining multiple conditions

---

## 1. Storing Choices in a List

The game starts with:

```python
choices = ["rock", "paper", "scissors"]
```

The list stores all possible choices.

Instead of writing:

```python
rock
paper
scissors
```

separately throughout the program, we keep them together in one list.

This makes the choices easier to work with.

---

## 2. Randomly Selecting the Computer's Choice

The computer needs to make its choice randomly.

The game uses:

```python
computer = random.choice(choices)
```

`random.choice()` selects one item from the list.

For example, if:

```python
choices = ["rock", "paper", "scissors"]
```

the computer could randomly select:

```text
rock
```

or:

```text
paper
```

or:

```text
scissors
```

This is the same `random.choice()` concept introduced in the Coin Flip game.

---

## 3. Getting the Player's Choice

The player enters their choice:

```python
player = input("Choose rock, paper, or scissors: ").lower()
```

There are two important parts here.

### `input()`

Gets the player's answer.

### `.lower()`

Converts the answer to lowercase.

So:

```text
Rock
ROCK
rOcK
```

all become:

```text
rock
```

This makes it easier to compare the player's input with the choices in the list.

---

## 4. Input Validation

Before playing the round, the program checks whether the player entered a valid choice:

```python
if player not in choices:
    print("Invalid choice. Please try again.")
    continue
```

The `in` operator checks whether a value exists inside a collection.

For example:

```python
"rock" in choices
```

returns:

```text
True
```

while:

```python
"banana" in choices
```

returns:

```text
False
```

Therefore:

```python
player not in choices
```

means:

> The player's choice is not one of the valid choices.

---

## 5. Comparing Strings

The game compares the player's choice and the computer's choice.

For example:

```python
if player == computer:
```

The `==` operator checks whether two values are equal.

If both players choose:

```text
rock
```

then:

```python
"rock" == "rock"
```

is:

```text
True
```

Therefore, the game produces:

```text
It's a tie!
```

---

# 6. Boolean Logic

The most important new concept in this game is **Boolean logic**.

A Boolean value can be either:

```text
True
```

or:

```text
False
```

Python uses Boolean expressions to make decisions.

For example:

```python
player == computer
```

produces either `True` or `False`.

---

## 7. The `and` Operator

The `and` operator requires **both conditions** to be true.

For example:

```python
age >= 18 and has_id
```

This is only `True` when:

```text
age >= 18 → True
has_id    → True
```

If either condition is false, the entire expression becomes false.

---

## 8. The `or` Operator

The `or` operator requires **at least one condition** to be true.

For example:

```python
choice == "rock" or choice == "paper"
```

This is true if the choice is either:

```text
rock
```

or:

```text
paper
```

---

# 9. Representing the Game Rules

The Rock Paper Scissors rules are:

```text
Rock beats Scissors
Scissors beats Paper
Paper beats Rock
```

We can represent these rules using Boolean expressions.

The game uses:

```python
elif (
    (player == "rock" and computer == "scissors")
    or (player == "paper" and computer == "rock")
    or (player == "scissors" and computer == "paper")
):
    print("You win!")
```

This looks complicated at first, but it can be broken down.

---

## 10. First Winning Condition

```python
player == "rock" and computer == "scissors"
```

This checks:

> Did the player choose rock AND the computer choose scissors?

If both are true, the player wins.

---

## 11. Second Winning Condition

```python
player == "paper" and computer == "rock"
```

This checks:

> Did the player choose paper AND the computer choose rock?

If both are true, the player wins.

---

## 12. Third Winning Condition

```python
player == "scissors" and computer == "paper"
```

This checks:

> Did the player choose scissors AND the computer choose paper?

If both are true, the player wins.

---

## 13. Combining the Conditions

The three winning conditions are connected using `or`:

```python
(
    condition_1
    or condition_2
    or condition_3
)
```

This means:

> If ANY of the three winning situations occurs, the player wins.

The logic can be visualized as:

```text
                    Player wins?
                         │
            ┌────────────┼────────────┐
            ↓            ↓            ↓
      Rock vs Scissors  Paper vs Rock  Scissors vs Paper
            │            │            │
            └────────────┼────────────┘
                         ↓
                      You win!
```

---

# 14. Parentheses

The game uses parentheses to organize the Boolean conditions:

```python
(
    (player == "rock" and computer == "scissors")
    or (player == "paper" and computer == "rock")
    or (player == "scissors" and computer == "paper")
)
```

Parentheses make it clearer which conditions belong together.

They also help control the order in which Python evaluates expressions.

---

# 15. `if`, `elif`, and `else`

The game has three possible outcomes.

### Tie

```python
if player == computer:
    print("It's a tie!")
```

### Player wins

```python
elif (
    ...
):
    print("You win!")
```

### Computer wins

```python
else:
    print("Computer wins!")
```

The logic is:

```text
Are they equal?
      │
   Yes → Tie
      │
     No
      ↓
Is one of the winning combinations true?
      │
   Yes → Player wins
      │
     No
      ↓
Computer wins
```

Because the program has already checked for a tie and all possible player-winning combinations, the remaining situation must be a computer win.

---

# 16. Repeating the Game

The game uses:

```python
while True:
```

to allow multiple rounds.

After each round:

```python
again = input("Play again? (y/n): ").lower()
```

The player decides whether to continue.

If they don't enter `"y"`:

```python
if again != "y":
    break
```

the loop ends.

---

# 17. Reusing Functions

The entire game is contained inside:

```python
def play():
```

This keeps the game organized.

The program starts it with:

```python
if __name__ == "__main__":
    play()
```

This structure becomes increasingly useful as programs become larger.

Later, functions can be separated into different files and reused by other parts of a program.

---

# How Everything Works Together

The overall game flow is:

```text
Start
  ↓
Create list of choices
  ↓
Ask player for choice
  ↓
Convert input to lowercase
  ↓
Is the choice valid?
  │
  ├── No → Show error → Ask again
  │
  └── Yes
        ↓
  Computer randomly chooses
        ↓
  Compare player and computer
        ↓
   ┌────┼──────────────┐
   ↓    ↓              ↓
  Tie  Player wins   Computer wins
   │    │              │
   └────┴──────────────┘
            ↓
      Play again?
       │       │
      Yes      No
       │       │
       ↓       ↓
     Repeat   End
```

---

# Example Round

Suppose the player chooses:

```text
paper
```

The computer randomly chooses:

```text
rock
```

The program checks:

```python
player == computer
```

which becomes:

```python
"paper" == "rock"
```

This is `False`.

Then it checks the winning conditions.

One condition is:

```python
player == "paper" and computer == "rock"
```

Both conditions are true:

```text
player == "paper"   → True
computer == "rock"  → True
```

Therefore:

```text
True and True
```

is:

```text
True
```

The player wins.

---

# Key Concepts From This Game

Rock Paper Scissors combines many concepts learned throughout Level 1.

### Randomness

```python
random.choice(choices)
```

### Lists

```python
choices = ["rock", "paper", "scissors"]
```

### Input

```python
input(...)
```

### String methods

```python
.lower()
```

### Validation

```python
player not in choices
```

### Boolean logic

```python
and
or
```

### Conditional statements

```python
if
elif
else
```

### Loops

```python
while True
```

This makes Rock Paper Scissors a good summary of the Level 1 fundamentals.

---

# Practice Questions

### Question 1

What does this do?

```python
random.choice(choices)
```

### Question 2

What does `and` require?

### Question 3

What does `or` require?

### Question 4

Why do we use parentheses around the winning conditions?

### Question 5

Why does the final `else` represent a computer win?

### Question 6

What is the difference between:

```python
=
```

and:

```python
==
```

---

# Mini Challenges

Try modifying the game yourself.

### Challenge 1 — Score

Keep track of:

```text
Player wins
Computer wins
Ties
```

and display the score after every round.

### Challenge 2 — Best of 3

Make the game continue until either the player or computer has won three rounds.

### Challenge 3 — Input Shortcuts

Allow:

```text
r → rock
p → paper
s → scissors
```

### Challenge 4 — Rock Paper Scissors Lizard Spock

Expand the game from three choices to five choices.

This will require creating additional game rules and Boolean conditions.

---

# Level 1 Summary

After completing the four Level 1 games, you have practiced:

```text
Variables
   ↓
User Input
   ↓
Conditions
   ↓
Loops
   ↓
Functions
   ↓
Lists
   ↓
Random Numbers
   ↓
Input Validation
   ↓
Error Handling
   ↓
Boolean Logic
   ↓
String Methods
```

These concepts form the foundation for the more advanced programs introduced in Level 2.

