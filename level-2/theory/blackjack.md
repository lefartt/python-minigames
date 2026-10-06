# Blackjack — Python Theory

## Overview

The Blackjack game is a Level 2 project designed to introduce more Python programming concepts than the Level 1 games.

The game uses:

* Lists
* Dictionaries / values
* Functions
* Loops
* Conditionals
* Randomisation
* String slicing
* Input validation
* Game state
* Basic game logic

The objective is to get a score as close to **21** as possible without going over.

---

## 1. Creating the Deck

The game stores the suits and ranks in lists:

```python
SUITS = ["♠", "♥", "♦", "♣"]

RANKS = [
    "2", "3", "4", "5", "6", "7", "8", "9", "10",
    "J", "Q", "K", "A"
]
```

A function creates the deck:

```python
def create_deck():
    deck = []

    for suit in SUITS:
        for rank in RANKS:
            deck.append(f"{rank}{suit}")

    return deck
```

The nested `for` loops combine every rank with every suit.

For example:

```text
2♠
3♠
...
A♠
2♥
3♥
...
A♥
```

This produces a standard **52-card deck**.

---

## 2. Randomising the Deck

The `random` module is used to shuffle the cards:

```python
import random

random.shuffle(deck)
```

`random.shuffle()` changes the order of the cards randomly.

This means every new round starts with a different deck order.

---

## 3. Dealing Cards

Cards are removed from the deck using:

```python
def deal_card(deck):
    return deck.pop()
```

The `pop()` function removes and returns the last item in a list.

For example:

```python
deck = ["2♠", "3♠", "4♠"]

card = deck.pop()
```

The result is:

```text
card = "4♠"
```

The deck now contains:

```text
["2♠", "3♠"]
```

This prevents the same physical card from being dealt twice during the same round.

---

## 4. Player and Dealer Hands

The player and dealer each have their own list:

```python
player_hand = [deal_card(deck), deal_card(deck)]
dealer_hand = [deal_card(deck), deal_card(deck)]
```

For example:

```text
Player:
["K♠", "7♥"]

Dealer:
["9♦", "A♣"]
```

Lists are useful because more cards can be added during the game.

For example:

```python
player_hand.append(new_card)
```

---

## 5. Calculating the Score

The game uses a function to calculate the value of a hand:

```python
def calculate_score(hand):
```

The function checks every card in the hand.

```python
for card in hand:
```

The rank is extracted using:

```python
rank = card[:-1]
```

For example:

```text
"K♠" → "K"
"10♥" → "10"
"A♦" → "A"
```

`[:-1]` means to take everything except the final character.

The final character is the suit.

---

## 6. Face Cards

Jack, Queen and King are worth 10 points.

```python
if rank in ["J", "Q", "K"]:
    score += 10
```

The `in` operator checks whether the rank exists inside the list.

For example:

```python
"K" in ["J", "Q", "K"]
```

returns:

```text
True
```

---

## 7. Number Cards

Number cards use their actual value:

```python
else:
    score += int(rank)
```

For example:

```text
"2" → 2
"7" → 7
"10" → 10
```

`int()` converts a string into an integer.

For example:

```python
int("7")
```

becomes:

```text
7
```

---

## 8. Handling Aces

The Ace is special because it can be worth either:

```text
11 points
```

or:

```text
1 point
```

The program initially treats an Ace as 11:

```python
elif rank == "A":
    score += 11
    aces += 1
```

The number of Aces is tracked using:

```python
aces += 1
```

If the score becomes greater than 21, the program changes an Ace from 11 to 1:

```python
while score > 21 and aces:
    score -= 10
    aces -= 1
```

Why subtract 10?

Because:

```text
11 - 10 = 1
```

For example:

```text
A + 9
```

Initially:

```text
11 + 9 = 20
```

No adjustment is needed.

But:

```text
A + 9 + 5
```

would initially be:

```text
11 + 9 + 5 = 25
```

The program changes the Ace from 11 to 1:

```text
25 - 10 = 15
```

So the final score becomes:

```text
15
```

This prevents the player from unnecessarily busting.

---

## 9. Detecting Blackjack

Blackjack normally occurs when a player has exactly two cards with a score of 21.

The game checks this using:

```python
def is_blackjack(hand):
    return len(hand) == 2 and calculate_score(hand) == 21
```

Two conditions must be true:

```python
len(hand) == 2
```

and:

```python
calculate_score(hand) == 21
```

The `and` operator requires both conditions to be true.

For example:

```text
A♠ + K♥
```

has:

```text
2 cards
21 points
```

Therefore, it is Blackjack.

---

## 10. Player's Turn

The player can choose between:

```text
Hit
Stand
```

The program repeatedly asks for input:

```python
while player_score < 21:
```

If the player chooses Hit:

```python
if choice == "h":
```

A new card is dealt:

```python
new_card = deal_card(deck)
player_hand.append(new_card)
```

The score is then recalculated:

```python
player_score = calculate_score(player_hand)
```

If the score goes above 21:

```python
if player_score > 21:
    print("\nYou bust!")
    break
```

The player loses because they have busted.

---

## 11. Input Validation

The game checks whether the player entered a valid choice:

```python
if choice == "h":
```

or:

```python
elif choice == "s":
```

If neither is entered:

```python
else:
    print("Invalid choice. Please enter 'h' or 's'.")
```

This prevents unexpected input from breaking the game.

The `.lower()` function is also used:

```python
input(...).lower()
```

This allows the player to enter:

```text
H
h
S
s
```

without causing a problem.

---

## 12. Standing

If the player chooses Stand:

```python
elif choice == "s":
    print("\nYou stand.")
    break
```

The `break` statement exits the player's turn loop.

The game then moves to the dealer's turn.

---

## 13. Dealer's Turn

After the player finishes, the dealer reveals the hidden card:

```python
print("Dealer reveals:", dealer_hand)
```

The dealer must follow a simple rule:

```text
Hit if score < 17
Stand if score >= 17
```

This is implemented using:

```python
while dealer_score < 17:
```

If the dealer's score is below 17, another card is drawn:

```python
new_card = deal_card(deck)
dealer_hand.append(new_card)
```

The score is then recalculated.

The dealer continues drawing cards until the score reaches at least 17.

---

## 14. Game State

The game needs to remember several values while the round is running:

```python
deck
player_hand
dealer_hand
player_score
dealer_score
```

These variables represent the current **game state**.

For example:

```text
Deck → remaining cards
Player hand → player's cards
Dealer hand → dealer's cards
Player score → player's current score
Dealer score → dealer's current score
```

The game updates these values as cards are drawn.

---

## 15. Functions

The game is divided into functions:

```python
create_deck()
deal_card()
calculate_score()
is_blackjack()
play_round()
```

Using functions makes the program easier to understand and maintain.

For example:

```python
calculate_score(player_hand)
```

can be reused whenever the player's score needs to be updated.

The main round is contained inside:

```python
def play_round():
```

This makes it possible to start another round without duplicating the entire game code.

---

## 16. Replay System

After a round finishes, the program asks:

```text
Play again? (y/n):
```

The replay system uses a loop:

```python
while True:
```

If the player enters:

```text
y
```

another round starts.

If the player enters:

```text
n
```

the program exits.

Invalid input produces an error message:

```text
Invalid choice. Please enter 'y' or 'n'.
```

This is another example of input validation.

---

## 17. Overall Game Flow

The Blackjack program follows this general process:

```text
Start
  ↓
Create deck
  ↓
Shuffle deck
  ↓
Deal 2 cards to player
  ↓
Deal 2 cards to dealer
  ↓
Check for Blackjack
  ↓
Player chooses Hit or Stand
  ↓
Player busts?
  ├── Yes → Lose
  └── No
       ↓
Dealer reveals cards
       ↓
Dealer score < 17?
  ├── Yes → Hit
  └── No → Stand
       ↓
Compare scores
       ↓
Display result
       ↓
Play again?
  ├── Yes → New round
  └── No → Exit
```

---

## 18. Python Concepts Learned

This project introduces several important Python concepts.

### Lists

Used for:

* Suits
* Ranks
* Deck
* Player hand
* Dealer hand

Example:

```python
player_hand = []
```

### Functions

Used to separate different parts of the program:

```python
def deal_card(deck):
```

### Loops

Used for:

* Creating the deck
* Player turns
* Dealer turns
* Replay

Examples:

```python
for card in hand:
```

and:

```python
while player_score < 21:
```

### Conditionals

Used to make decisions:

```python
if player_score > 21:
```

### Randomisation

Used to shuffle the deck:

```python
random.shuffle(deck)
```

### String Slicing

Used to extract card ranks:

```python
rank = card[:-1]
```

### Input Validation

Used to make sure the player enters valid choices.

### Game State

Variables such as `player_hand`, `dealer_hand`, and `player_score` store the current state of the game.

---

## 19. What Makes This a Level 2 Game?

Compared with the Level 1 games, Blackjack requires more interaction between different parts of the program.

The program needs to:

1. Create a complete deck.
2. Shuffle the deck.
3. Deal cards.
4. Track multiple hands.
5. Calculate changing scores.
6. Handle special Ace behaviour.
7. Detect Blackjack.
8. Handle player decisions.
9. Automatically control the dealer.
10. Compare the final scores.
11. Allow the game to restart.

This makes Blackjack a useful step towards larger Python programs where multiple functions and pieces of state work together.

---

## 20. Possible Future Improvements

The current Blackjack game can be expanded in the future.

Possible improvements include:

* Better card graphics
* Cleaner card display
* Betting system
* Chips / virtual money
* Multiple players
* Split hands
* Double down
* Insurance
* Dealer rules for soft 17
* Statistics and win/loss tracking
* Save player statistics to a file
* GUI version

These features can be added later as the project becomes more advanced.

---

## Summary

The Blackjack project builds on the Python concepts learned in Level 1 and introduces more complex game logic.

The most important concepts learned are:

* Lists
* Functions
* Loops
* Conditionals
* Randomisation
* String slicing
* Input validation
* Game state
* Score calculation
* Handling special cases such as Aces

The main goal is not only to create a playable Blackjack game, but also to understand how Python can be used to manage a program with multiple interacting components.

