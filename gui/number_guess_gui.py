
import random
import tkinter as tk
from tkinter import ttk


def open_number_guess(parent):
    """Open a GUI version of the Number Guess game."""

    window = tk.Toplevel(parent)
    window.title("Number Guess")
    window.geometry("420x400")
    window.resizable(False, False)

    # Game settings
    minimum = 1
    maximum = 100
    secret_number = random.randint(minimum, maximum)
    attempts = 0
    game_over = False

    # Heading
    tk.Label(
        window,
        text="Number Guess",
        font=("Arial", 22, "bold")
    ).pack(pady=(20, 5))

    tk.Label(
        window,
        text=f"Guess the secret number from {minimum} to {maximum}.",
        font=("Arial", 11)
    ).pack(pady=5)

    # Guess input
    tk.Label(
        window,
        text="Enter your guess:",
        font=("Arial", 12)
    ).pack(pady=(15, 5))

    guess_entry = ttk.Entry(
        window,
        font=("Arial", 14),
        justify="center",
        width=15
    )
    guess_entry.pack(pady=5)
    guess_entry.focus_set()

    # Feedback
    feedback_label = tk.Label(
        window,
        text="Good luck!",
        font=("Arial", 12),
        wraplength=350
    )
    feedback_label.pack(pady=10)

    attempts_label = tk.Label(
        window,
        text="Attempts: 0",
        font=("Arial", 11)
    )
    attempts_label.pack(pady=5)

    def make_guess(event=None):
        nonlocal attempts, game_over

        if game_over:
            feedback_label.config(
                text="You have finished this round. Start a new game!"
            )
            return

        raw_guess = guess_entry.get().strip()

        # Check that the input is a whole number.
        try:
            guess = int(raw_guess)
        except ValueError:
            feedback_label.config(
                text="Please enter a whole number, such as 25."
            )
            return

        # Check the allowed range.
        if not minimum <= guess <= maximum:
            feedback_label.config(
                text=f"Your guess must be between {minimum} and {maximum}."
            )
            return

        attempts += 1
        attempts_label.config(text=f"Attempts: {attempts}")

        if guess < secret_number:
            feedback_label.config(text="Too low! Try a higher number.")
        elif guess > secret_number:
            feedback_label.config(text="Too high! Try a lower number.")
        else:
            feedback_label.config(
                text=f"Correct! You found {secret_number} in {attempts} "
                     f"{'attempt' if attempts == 1 else 'attempts'}!"
            )
            game_over = True
            guess_entry.config(state="disabled")
            guess_button.config(state="disabled")

        if not game_over:
            guess_entry.delete(0, tk.END)
            guess_entry.focus_set()

    def new_game():
        nonlocal secret_number, attempts, game_over

        secret_number = random.randint(minimum, maximum)
        attempts = 0
        game_over = False

        guess_entry.config(state="normal")
        guess_entry.delete(0, tk.END)
        guess_button.config(state="normal")

        feedback_label.config(text="New number generated. Good luck!")
        attempts_label.config(text="Attempts: 0")
        guess_entry.focus_set()

    # Buttons
    button_frame = ttk.Frame(window)
    button_frame.pack(pady=15)

    guess_button = ttk.Button(
        button_frame,
        text="Guess",
        command=make_guess
    )
    guess_button.pack(side="left", padx=5)

    new_game_button = ttk.Button(
        button_frame,
        text="New Game",
        command=new_game
    )
    new_game_button.pack(side="left", padx=5)

    # Press Enter to submit a guess.
    guess_entry.bind("<Return>", make_guess)
