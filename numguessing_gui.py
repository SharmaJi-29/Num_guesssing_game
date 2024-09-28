import tkinter as tk
from tkinter import messagebox
import random

class NumberGuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game")


        self.number_to_guess = random.randint(1, 100)
        self.attempts = 0


        self.create_widgets()

    def create_widgets(self):

        self.root.geometry("400x500")


        self.entry_label = tk.Label(self.root, text="Enter your guess (1-100):", font = ('verdana', 20, 'bold'))
        self.entry_label.pack(pady=60)

        self.entry = tk.Entry(self.root)
        self.entry.pack(pady=10)


        self.submit_button = tk.Button(self.root, text="Submit", command=self.check_guess)
        self.submit_button.pack(pady=10)


        self.result_label = tk.Label(self.root, text="")
        self.result_label.pack(pady=10)


        self.attempts_label = tk.Label(self.root, text="Attempts: 0", font = ('verdana', 15, 'bold'))
        self.attempts_label.pack(pady=50)

    def check_guess(self):
        try:

            guess = int(self.entry.get())
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter a valid integer.")
            return

        self.attempts += 1
        self.attempts_label.config(text=f"Attempts: {self.attempts}")

        # Check the guess
        if guess < self.number_to_guess:
            self.result_label.config(text="Too low! Try again.")
        elif guess > self.number_to_guess:
            self.result_label.config(text="Too high! Try again.")
        else:
            self.result_label.config(text=f"Congratulations! You guessed it in {self.attempts} attempts.")

            self.entry.config(state=tk.DISABLED)
            self.submit_button.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    game = NumberGuessingGame(root)
    root.mainloop()
