import random
import tkinter as tk


def open_coin_flip(parent):
    coin_window = tk.Toplevel(parent)
    coin_window.title("Coin Flip")
    coin_window.geometry("400x350")
    coin_window.resizable(False, False)

    title = tk.Label(
        coin_window,
        text="Coin Flip",
        font=("Arial", 24, "bold")
    )
    title.pack(pady=(25, 15))

    instruction = tk.Label(
        coin_window,
        text="Choose Heads or Tails",
        font=("Arial", 14)
    )
    instruction.pack(pady=5)

    result_label = tk.Label(
        coin_window,
        text="",
        font=("Arial", 14, "bold")
    )
    result_label.pack(pady=20)

    def flip_coin(choice):
        result = random.choice(["heads", "tails"])

        if choice == result:
            result_label.config(
                text=f"Coin landed on: {result.title()}\n\n"
                     "You guessed correctly!"
            )
        else:
            result_label.config(
                text=f"Coin landed on: {result.title()}\n\n"
                     "Wrong guess!"
            )

    button_frame = tk.Frame(coin_window)
    button_frame.pack(pady=10)

    heads_button = tk.Button(
        button_frame,
        text="Heads",
        font=("Arial", 13),
        width=10,
        height=2,
        command=lambda: flip_coin("heads")
    )
    heads_button.grid(row=0, column=0, padx=10)

    tails_button = tk.Button(
        button_frame,
        text="Tails",
        font=("Arial", 13),
        width=10,
        height=2,
        command=lambda: flip_coin("tails")
    )
    tails_button.grid(row=0, column=1, padx=10)


if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()

    open_coin_flip(root)

    root.mainloop()
