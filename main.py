import customtkinter as ctk

app = ctk.CTk()

app.title("Personal Expense Tracker")

app.geometry("350x300")

app.columnconfigure((0, 1, 2), weight=1)


balance_label = ctk.CTkLabel(app, text="BALANCE:", font=("Arial", 24))
balance_label.grid(row = 0, column = 0, columnspan = 3, padx = 10, pady = (20, 20), sticky = "w")

add_expense_button = ctk.CTkButton(app, text="Add Expense")
add_expense_button.grid(row = 1, column = 0, padx = (10, 3), sticky="nsew")

history_button = ctk.CTkButton(app, text="History")
history_button.grid(row = 1, column = 1, sticky = "nsew")

set_balance_button = ctk.CTkButton(app, text="Set Balance")
set_balance_button.grid(row = 1, column = 2, padx = (3, 10), sticky = "nsew")


app.resizable(False,False)


app.mainloop()