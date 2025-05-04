#import tkinter GUI library
import tkinter as tk

#set global constant to $1,000, user will start with that much in the bank
balance = 1000.0

#this function allows user to check the balance.
def check_balance():
    message_label.config(text=f"Balance: ${balance:.2f}")

#this functiona allows user to deposit funds.  The global constant is called, the amount of the deposit is called from the .get method from the entry box in GUI
def deposit():
    global balance
    amount = float(amount_entry.get())
    #new balance is updated
    balance += amount
    balance_label.config(text=f"Balance: ${balance:.2f}")
    message_label.config(text=f"Deposited ${amount:.2f}")
#withdraw function allows user to withdraw funds
def withdraw():
    #calls global constant again
    global balance
    #checks to see what amount user inputted in the entry box and gets that value
    amount = float(amount_entry.get())
    #withdraw amount subtracted from balance
    balance -= amount
    balance_label.config(text=f"Balance: ${balance:.2f}")
    message_label.config(text=f"Withdrew ${amount:.2f}")

#sets main window for program
mainwindow = tk.Tk()
#sets title
mainwindow.title("ATM App")
#sets dimensions
mainwindow.geometry("300x250")

#sets the balance label, with appropriate parameters
balance_label = tk.Label(mainwindow, text=f"Balance: ${balance:.2f}", font=("Arial", 14))
#packs the label
balance_label.pack(pady=10)

#entry box is created with .Entry method, within mainwindow
amount_entry = tk.Entry(mainwindow, font=("Arial", 12))
#packs the entry
amount_entry.pack(pady=5)

#creates the buttons for deposit, withdraw, and check balance.  Each of these buttons has the corresponding text, and also
#has the command equal to the above functions that reflect that behavior.
tk.Button(mainwindow, text="Deposit", command=deposit).pack(pady=5)
tk.Button(mainwindow, text="Withdraw", command=withdraw).pack(pady=5)
tk.Button(mainwindow, text="Check Balance", command=check_balance).pack(pady=5)
#creates, packs message label
message_label = tk.Label(mainwindow, text="", font=("Arial", 10))
message_label.pack(pady=10)
#initiates GUI
mainwindow.mainloop()
