import tkinter as tk

balance = 1000.0

def check_balance():
    message_label.config(text=f"Balance: ${balance:.2f}")

def deposit():
    global balance
    amount = float(amount_entry.get())
    balance += amount
    balance_label.config(text=f"Balance: ${balance:.2f}")
    message_label.config(text=f"Deposited ${amount:.2f}")

def withdraw():
    global balance
    amount = float(amount_entry.get())
    balance -= amount
    balance_label.config(text=f"Balance: ${balance:.2f}")
    message_label.config(text=f"Withdrew ${amount:.2f}")

mainwindow = tk.Tk()
mainwindow.title("ATM App")
mainwindow.geometry("300x250")

balance_label = tk.Label(mainwindow, text=f"Balance: ${balance:.2f}", font=("Arial", 14))
balance_label.pack(pady=10)

amount_entry = tk.Entry(mainwindow, font=("Arial", 12))
amount_entry.pack(pady=5)

tk.Button(mainwindow, text="Deposit", command=deposit).pack(pady=5)
tk.Button(mainwindow, text="Withdraw", command=withdraw).pack(pady=5)
tk.Button(mainwindow, text="Check Balance", command=check_balance).pack(pady=5)

message_label = tk.Label(mainwindow, text="", font=("Arial", 10))
message_label.pack(pady=10)

mainwindow.mainloop()
