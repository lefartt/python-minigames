import tkinter as tk
from tkinter import messagebox

from coin_flip_gui import open_coin_flip


# =========================
# Placeholder
# =========================

def not_connected(game_name):
    messagebox.showinfo(
        game_name,
        f"{game_name} will be connected here next!"
    )


# =========================
# Main Window
# =========================

root = tk.Tk()

root.title("Python Mini Games")
root.geometry("600x750")
root.resizable(False, False)


# =========================
# Header
# =========================

title = tk.Label(
    root,
    text="Python Mini Games",
    font=("Arial", 28, "bold")
)
title.pack(pady=(30, 5))


subtitle = tk.Label(
    root,
    text="Choose a game to play",
    font=("Arial", 14)
)
subtitle.pack(pady=(0, 20))


# =========================
# Level 1
# =========================

level1_frame = tk.LabelFrame(
    root,
    text="Level 1",
    font=("Arial", 16, "bold"),
    padx=20,
    pady=15
)

level1_frame.pack(
    fill="x",
    padx=60,
    pady=10
)


coin_button = tk.Button(
    level1_frame,
    text="Coin Flip",
    font=("Arial", 13),
    width=25,
    height=2,
    command=lambda: open_coin_flip(root)
)
coin_button.pack(pady=5)


dice_button = tk.Button(
    level1_frame,
    text="Dice Roller",
    font=("Arial", 13),
    width=25,
    height=2,
    command=lambda: not_connected("Dice Roller")
)
dice_button.pack(pady=5)


guess_button = tk.Button(
    level1_frame,
    text="Number Guess",
    font=("Arial", 13),
    width=25,
    height=2,
    command=lambda: not_connected("Number Guess")
)
guess_button.pack(pady=5)


rps_button = tk.Button(
    level1_frame,
    text="Rock Paper Scissors",
    font=("Arial", 13),
    width=25,
    height=2,
    command=lambda: not_connected("Rock Paper Scissors")
)
rps_button.pack(pady=5)


# =========================
# Level 2
# =========================

level2_frame = tk.LabelFrame(
    root,
    text="Level 2",
    font=("Arial", 16, "bold"),
    padx=20,
    pady=15
)

level2_frame.pack(
    fill="x",
    padx=60,
    pady=10
)


blackjack_button = tk.Button(
    level2_frame,
    text="Blackjack",
    font=("Arial", 13),
    width=25,
    height=2,
    command=lambda: not_connected("Blackjack")
)
blackjack_button.pack(pady=5)


hangman_button = tk.Button(
    level2_frame,
    text="Hangman",
    font=("Arial", 13),
    width=25,
    height=2,
    command=lambda: not_connected("Hangman")
)
hangman_button.pack(pady=5)


tictactoe_button = tk.Button(
    level2_frame,
    text="Tic-Tac-Toe",
    font=("Arial", 13),
    width=25,
    height=2,
    command=lambda: not_connected("Tic-Tac-Toe")
)
tictactoe_button.pack(pady=5)


# =========================
# Exit
# =========================

exit_button = tk.Button(
    root,
    text="Exit",
    font=("Arial", 13, "bold"),
    width=15,
    height=2,
    command=root.destroy
)

exit_button.pack(pady=20)


# =========================
# Start GUI
# =========================

root.mainloop()
