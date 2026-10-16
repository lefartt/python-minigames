
import random
import tkinter as tk
from tkinter import ttk


def open_dice_roller(parent):
    """Open the Dice Roller in its own window."""

    window = tk.Toplevel(parent)
    window.title("Dice Roller")
    window.geometry("420x350")
    window.resizable(False, False)

    ttk.Label(
        window,
        text="Dice Roller",
        font=("Arial", 20, "bold")
    ).pack(pady=(20, 10))

    ttk.Label(
        window,
        text="Choose how many six-sided dice to roll:"
    ).pack(pady=5)

    dice_count = tk.StringVar(value="1")

    ttk.Combobox(
        window,
        textvariable=dice_count,
        values=["1", "2", "3", "4", "5"],
        state="readonly",
        width=8
    ).pack(pady=5)

    result_label = ttk.Label(
        window,
        text="Press Roll Dice to begin!",
        font=("Arial", 14),
        justify="center"
    )
    result_label.pack(pady=15)

    def roll_dice():
        number_of_dice = int(dice_count.get())
        results = [
            random.randint(1, 6)
            for _ in range(number_of_dice)
        ]

        total = sum(results)
        dice_display = "   ".join(
            f"[ {number} ]" for number in results
        )

        result_label.config(
            text=f"{dice_display}\n\nTotal: {total}"
        )

    def reset_results():
        result_label.config(
            text="Press Roll Dice to begin!"
        )

    ttk.Button(
        window,
        text="Roll Dice",
        command=roll_dice
    ).pack(pady=5)

    ttk.Button(
        window,
        text="Reset",
        command=reset_results
    ).pack(pady=5)
