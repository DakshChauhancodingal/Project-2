import random
import tkinter as tk

options = ["Rock", "Paper", "Scissors"]
beats = {"Rock": "Scissors", "Paper": "Rock", "Scissors": "Paper"}


def play(choice):
    computer = random.choice(options)
    result = (
        "It's a Tie!" if choice == computer
        else "You Win!" if beats[choice] == computer
        else "Computer Wins!"
    )
    choice_label.config(text=f"Your Choice: {choice}\nComputer's Choice: {computer}")
    result_label.config(text=result)


root = tk.Tk()
root.geometry("400x400")
root.title("Length Converter App")
tk.Label(root, text="Rock, Paper, Scissors", font=("Arial", 16, "bold")).pack(pady=15)
tk.Label(root, text="Click a button to make your choice:", font=("Arial", 11)).pack(pady=5)

button_frame = tk.Frame(root)
button_frame.pack(pady=15)
for column, choice in enumerate(options):
    tk.Button(
        button_frame, text=choice, width=10, command=lambda choice=choice: play(choice)
    ).grid(row=0, column=column, padx=5)

choice_label = tk.Label(root, text="", font=("Arial", 12))
choice_label.pack(pady=15)
result_label = tk.Label(root, text="", font=("Arial", 14, "bold"), fg="blue")
result_label.pack(pady=10)

root.mainloop()