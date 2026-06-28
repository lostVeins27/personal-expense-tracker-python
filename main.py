import customtkinter as ctk

app = ctk.CTk()

app.title("Personal Expense Tracker")

app.geometry("350x300")


app.resizable(False,False)
app.columnconfigure((0, 1, 2), weight=1)

def balance_window():
    new_window = ctk.CTkToplevel(app)
    new_window.geometry("250x100")
    new_window.title("Set Balance")
    new_window.resizable(False,False)

    new_window.transient(app)
    new_window.after(10, new_window.lift)
    new_window.after(10, new_window.focus_force)

    ctk.CTkLabel(new_window, text="Enter your balance").pack(pady= (10, 10))

    balance_entry = ctk.CTkEntry(new_window)
    balance_entry.pack()

    def submit(event):
        balance = balance_entry.get()
        balance_label.configure(text = f"BALANCE: {balance}")
        new_window.destroy()

    balance_entry.bind("<Return>", submit)


balance_label = ctk.CTkLabel(app, text="BALANCE:", font=("Arial", 24))
balance_label.grid(row = 0, column = 0, columnspan = 3, padx = 10, pady = (20, 20), sticky = "w")

add_expense_button = ctk.CTkButton(app, text="Add Expense")
add_expense_button.grid(row = 1, column = 0, padx = (10, 3), sticky="nsew")

history_button = ctk.CTkButton(app, text="History")
history_button.grid(row = 1, column = 1, sticky = "nsew")

set_balance_button = ctk.CTkButton(app, text="Set Balance", command= balance_window)
set_balance_button.grid(row = 1, column = 2, padx = (3, 10), sticky = "nsew")


app.mainloop()