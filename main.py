import customtkinter as ctk

app = ctk.CTk()

app.title("Personal Expense Tracker")

app.geometry("400x300")


app.resizable(False, False)
app.columnconfigure((0, 1, 2, 3), weight=1)
app.rowconfigure(2, weight= 1)

history = []

def balance_dialog():

    dialog = ctk.CTkInputDialog(text="Input your current balance", title="Balance")
    balance = dialog.get_input()

    if balance is None:
        return

    balance_label.configure(text= f"BALANCE: {balance}")


balance_label = ctk.CTkLabel(app, text="BALANCE: 0", font=("Arial", 24))
balance_label.grid(row = 0, column = 0, columnspan = 4, padx = 10, pady = (20, 20), sticky = "w")

add_expense_button = ctk.CTkButton(app, text="Add Expense")
add_expense_button.grid(row = 1, column = 0, padx = (10, 3), sticky="nsew")

history_button = ctk.CTkButton(app, text="History")
history_button.grid(row = 1, column = 1, sticky = "nsew")

set_balance_button = ctk.CTkButton(app, text="Set Balance", command= balance_dialog)
set_balance_button.grid(row = 1, column = 2, padx = (3, 0), sticky = "nsew")

transaction_button = ctk.CTkButton(app, text="Transaction")
transaction_button.grid(row = 1, column = 3, padx = (3 , 10), sticky = "nsew")

history_scrollableframe = ctk.CTkScrollableFrame(app)
history_scrollableframe.grid(row = 2, column = 0, columnspan = 4, padx = 10, pady = 10, sticky = "nsew")


app.mainloop()