# Tic-Tac-Toe — Python Theory

## 1. Overview

Tic-Tac-Toe is a two-player game played on a 3×3 board.

This version supports two game modes:

1. **Player vs Player**
2. **Player vs AI**

The player uses `X`, while the second player or AI uses `O`.

The game demonstrates several important Python concepts:

* Lists
* Functions
* Loops
* Conditional statements
* Input validation
* List indexing
* `random.choice()`
* Game state
* Boolean values
* `all()`
* Nested loops
* Basic AI logic

---

# 2. Representing the Board

The board is stored as a Python list:

```python
board = [
    "1", "2", "3",
    "4", "5", "6",
    "7", "8", "9"
]
```

Each position on the board has an index:

```text
  1 | 2 | 3
 ---|---|---
  4 | 5 | 6
 ---|---|---
  7 | 8 | 9
```

Python lists use **zero-based indexing**, so the actual indexes are:

```text
  0 | 1 | 2
 ---|---|---
  3 | 4 | 5
 ---|---|---
  6 | 7 | 8
```

For example:

```python
board[0]
```

refers to position `1` on the game board.

---

# 3. Displaying the Board

The `display_board()` function is responsible for showing the current board.

```python
def display_board(board):
    print(f"  {board[0]}  |  {board[1]}  |  {board[2]}")
    print("_____|_____|_____")
    print(f"  {board[3]}  |  {board[4]}  |  {board[5]}")
    print("_____|_____|_____")
    print(f"  {board[6]}  |  {board[7]}  |  {board[8]}")
```

Instead of writing separate code every time the board needs to be displayed, the function can simply be called:

```python
display_board(board)
```

This demonstrates **functions** and **code reuse**.

---

# 4. Choosing a Game Mode

When the program starts, the player chooses between two modes:

```text
1. Player vs Player
2. Player vs AI
```

The program stores the selected mode:

```python
if mode == "1":
    game_mode = "pvp"

elif mode == "2":
    game_mode = "ai"
```

This is an example of using **conditional statements** to control program behaviour.

The same game logic can then be reused for both modes.

---

# 5. Player Move Input

Human players use the `get_player_move()` function.

```python
def get_player_move(board):
    while True:
        choice = input("Choose a position (1-9): ")
```

The program first checks whether the user entered a number:

```python
if not choice.isdigit():
    print("Please enter a number from 1 to 9.")
    continue
```

`.isdigit()` checks whether a string contains only digits.

For example:

```python
"5".isdigit()
```

returns:

```text
True
```

while:

```python
"hello".isdigit()
```

returns:

```text
False
```

---

# 6. Converting the Position to a List Index

The player chooses positions from `1` to `9`, but Python lists start from index `0`.

Therefore:

```python
index = position - 1
```

For example:

```text
Player input     List index

1                0
2                1
3                2
...
9                8
```

This conversion allows the player's input to correctly access the board list.

---

# 7. Checking Whether a Position Is Available

Before allowing a move, the program checks whether the position is already occupied:

```python
if board[index] in ["X", "O"]:
    print("That position is already taken.")
    continue
```

The `in` operator checks whether a value exists inside a list.

For example:

```python
"X" in ["X", "O"]
```

returns:

```text
True
```

This prevents players from replacing an existing move.

---

# 8. Winning Combinations

There are eight possible ways to win Tic-Tac-Toe:

```python
winning_combinations = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]
```

These represent:

* Three horizontal rows
* Three vertical columns
* Two diagonals

For example:

```python
[0, 1, 2]
```

represents:

```text
X | X | X
--+---+--
4 | 5 | 6
--+---+--
7 | 8 | 9
```

---

# 9. Checking for a Winner

The `check_winner()` function checks all winning combinations.

```python
for combination in winning_combinations:
    if all(board[position] == player for position in combination):
        return True
```

The `all()` function returns `True` only when every condition is true.

For example:

```python
all([True, True, True])
```

returns:

```text
True
```

But:

```python
all([True, False, True])
```

returns:

```text
False
```

This makes `all()` useful for checking whether all three positions contain the same player's symbol.

---

# 10. Checking for a Draw

The game also needs to detect when the board is full.

```python
def board_full(board):
    return all(position in ["X", "O"] for position in board)
```

Every position is checked to see whether it contains either:

```text
X
```

or:

```text
O
```

If every position is occupied, the game ends in a draw.

---

# 11. Player vs Player Mode

In Player vs Player mode, both players enter their own moves.

The current player is stored using:

```python
current_player = "X"
```

After each turn, the program switches players:

```python
if current_player == "X":
    current_player = "O"
else:
    current_player = "X"
```

This creates a simple game state:

```text
X → O → X → O → X
```

The same logic is used throughout the game until somebody wins or the board becomes full.

---

# 12. Player vs AI Mode

The second game mode allows the user to play against a simple AI.

In this version:

```text
Player = X
AI = O
```

When it is the AI's turn, the program does not ask for keyboard input.

Instead, it calls:

```python
get_ai_move(board)
```

---

# 13. Finding Available Moves

The AI needs to know which positions are still available.

The program creates a list:

```python
available_positions = []
```

It then checks every board position:

```python
for index in range(len(board)):
    if board[index] not in ["X", "O"]:
        available_positions.append(index)
```

If a position does not contain `X` or `O`, it is still available.

For example:

```text
Board:

X | 2 | O
---------
4 | X | 6
---------
7 | 8 | 9
```

The available positions are:

```text
1, 3, 5, 6, 7, 8
```

Their corresponding Python indexes are:

```text
1, 3, 5, 6, 7, 8
```

---

# 14. Random AI

After finding the available positions, the AI randomly chooses one:

```python
return random.choice(available_positions)
```

The program imports the `random` module:

```python
import random
```

`random.choice()` selects one item randomly from a list.

For example:

```python
random.choice([1, 3, 5, 6])
```

might return:

```text
5
```

The AI then places `O` in that position.

---

# 15. Why This Is an AI

This is a very simple form of game AI.

The AI:

1. Looks at the current game state.
2. Finds legal moves.
3. Chooses one available move.
4. Makes the move.

However, it does **not** analyse which move is best.

The AI is therefore essentially a **random-move AI**.

For example, it may fail to block the player even when the player is about to win.

This is intentional because the project is designed to gradually introduce more advanced programming concepts.

---

# 16. AI Turn Logic

The game checks whether it is the AI's turn:

```python
if game_mode == "ai" and current_player == "O":
```

If both conditions are true:

* The selected mode is Player vs AI.
* The current player is `O`.

The AI makes its move:

```python
index = get_ai_move(board)
board[index] = "O"
```

Otherwise, the program asks a human player for input.

This allows the same game loop to support both game modes.

---

# 17. Game State

The game state is represented by variables such as:

```python
board
current_player
game_mode
```

For example:

```text
game_mode = "ai"
current_player = "X"
```

means:

```text
Player vs AI
Player's turn
```

Later:

```text
game_mode = "ai"
current_player = "O"
```

means:

```text
Player vs AI
AI's turn
```

Managing this state is an important concept in game programming.

---

# 18. The Main Game Loop

The game runs inside:

```python
while True:
```

This keeps the game running until one of these conditions occurs:

* Player X wins
* Player O wins
* The game is a draw

After every move, the program checks:

```python
if check_winner(board, current_player):
```

and:

```python
if board_full(board):
```

This creates the main game flow:

```text
Start game
     ↓
Display board
     ↓
Choose move
     ↓
Update board
     ↓
Check winner
     ↓
Check draw
     ↓
Switch player
     ↓
Repeat
```

---

# 19. Input Validation

Input validation prevents the program from crashing or accepting invalid moves.

The program checks:

* Is the input a number?
* Is the number between 1 and 9?
* Is the selected position already occupied?

For example:

```python
if position < 1 or position > 9:
```

prevents positions outside the board.

The `continue` statement then returns to the beginning of the input loop so the player can try again.

---

# 20. Nested Loops

The program uses loops inside other loops.

For example, the main game uses:

```python
while True:
```

while player input also uses:

```python
while True:
```

The inner loop handles input validation, while the outer loop controls the game.

This is an example of **nested loops**.

---

# 21. Breaking Out of Loops

When a player wins or the game ends in a draw, the game uses:

```python
break
```

This exits the current game loop.

The program can then ask whether the user wants to play again.

---

# 22. Replay System

After the game ends, the player is asked:

```text
Play again? (y/n):
```

If the user enters:

```text
y
```

the program starts another game.

If the user enters:

```text
n
```

the program exits.

This allows multiple games to be played without restarting the Python program.

---

# 23. Python Concepts Used

This game introduces several useful Python concepts:

| Concept                | Example                           |
| ---------------------- | --------------------------------- |
| Lists                  | `board = [...]`                   |
| Indexing               | `board[index]`                    |
| Functions              | `def check_winner()`              |
| Loops                  | `while`, `for`                    |
| Conditional statements | `if`, `elif`, `else`              |
| Boolean values         | `True`, `False`                   |
| `all()`                | Checking winning positions        |
| `in` operator          | Checking occupied positions       |
| String methods         | `.isdigit()`, `.lower()`          |
| Input                  | `input()`                         |
| Type conversion        | `int()`                           |
| Random module          | `random.choice()`                 |
| Game state             | `current_player`, `game_mode`     |
| Nested loops           | Input validation inside game loop |

---

# 24. Why Tic-Tac-Toe Is a Level 2 Game

Tic-Tac-Toe is more complex than the Level 1 games because it requires the program to keep track of several pieces of information at once.

The program needs to manage:

* A board
* Two players
* The current turn
* Winning combinations
* Draw conditions
* User input
* Game modes
* AI decisions
* Replay functionality

The Player vs AI mode also introduces the idea of a program making decisions based on the current game state.

---

# 25. Future Improvements

The current AI chooses a random available position.

Possible future improvements include:

### Smarter AI

The AI could first check whether it can win:

```text
Can I win this turn?
        ↓
      Yes → Win
        ↓
       No
        ↓
Can I block the player?
        ↓
      Yes → Block
        ↓
       No
        ↓
Choose another move
```

### Minimax AI

A more advanced version could use the **Minimax algorithm** to analyse possible future moves.

This could eventually create an AI that is very difficult or impossible to beat.

### Other Improvements

Other possible features include:

* Letting the player choose `X` or `O`
* Choosing who goes first
* Score tracking
* Difficulty levels
* Better AI strategies
* Graphical user interface
* Two-player network multiplayer

---

# 26. Overall Program Flow

The complete program can be understood as:

```text
Start
  ↓
Choose Game Mode
  ↓
Create Board
  ↓
Player X Turn
  ↓
Human Move / AI Move
  ↓
Check Winner
  ↓
Check Draw
  ↓
Switch Player
  ↓
Repeat
  ↓
Game Ends
  ↓
Play Again?
  ↓
Yes → Choose Game Mode Again
No  → Exit
```

---

# 27. Summary

Tic-Tac-Toe introduces important programming concepts that are useful beyond simple games.

The project demonstrates how to:

* Represent a game board using a list.
* Use indexes to access board positions.
* Organise repeated logic using functions.
* Validate user input.
* Track the current game state.
* Check multiple possible winning conditions.
* Detect draws.
* Create different game modes.
* Use `random.choice()` to create a simple AI.
* Use loops to control a game.
* Build a replay system.

The AI version is intentionally simple. It provides a foundation for gradually learning more advanced game programming and decision-making algorithms.
