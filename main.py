import customtkinter as ctk

app = ctk.CTk()

app.title("Personal Expense Tracker")

app.geometry("400x300")

app.resizable(False, False)
app.columnconfigure((0, 1, 2, 3), weight=1)
app.rowconfigure(2, weight= 1)

def balance_dialog():

    dialog = ctk.CTkInputDialog(text="Input your current balance", title="Balance")
    balance = dialog.get_input()

    if balance is None:
        return

    balance_label.configure(text= f"BALANCE: {balance}")

def expense_window():
    window = ctk.CTkToplevel(app)
    window.geometry("400x350")
    window.title("Expense")
    window.resizable(False,False)

    window.columnconfigure((1), weight= 1)
    window.rowconfigure((0, 1, 2, 3, 4, 5, 6), weight= 1)

    account_options = (
        "Cash Wallet",
        "Bank Account",
        "Credit Card",
        "PayPal",
        "GCash",
        "Maya",
        "Others"
    )

    category_options = (
        "Food",
        "Transportation",
        "Bills",
        "Shopping",
        "Entertainment",
        "Healthcare",
        "Education",
        "Travel",
        "Rent",
        "Savings",
        "Others"
    )

    ctk.CTkLabel(window, text="Amount:").grid(row = 0, column = 0, padx = 10, pady = (10, 5))
    amount_entry = ctk.CTkEntry(window)
    amount_entry.grid(row = 0, column = 1, padx = 10, pady = (10, 5), sticky = "ew")

    ctk.CTkLabel(window, text="Category:").grid(row = 1, column = 0, padx = 10, pady = (0, 5))
    category_cb = ctk.CTkComboBox(window, values = category_options, state="readonly")
    category_cb.grid(row = 1, column = 1, padx = 10, pady = (0,5), sticky = "ew")

    ctk.CTkLabel(window, text="Account:").grid(row = 2, column = 0, padx = 10, pady = (0, 5))
    account_cb = ctk.CTkComboBox(window, values=account_options, state="readonly")
    account_cb.grid(row = 2, column = 1, padx = 10, pady = (0,5), sticky = "ew")

    ctk.CTkLabel(window, text="Date:").grid(row = 3, column = 0, padx = 10, pady= (0,5))
    date = ctk.CTkComboBox(window)
    date.grid(row = 3, column = 1, padx = 10, pady = (0,5), sticky = "ew")

    ctk.CTkLabel(window, text="Merchant:").grid(row = 4, column = 0, padx = 10, pady = (0,5))
    merchant_entry = ctk.CTkEntry(window)
    merchant_entry.grid(row = 4, column = 1, padx = 10, pady = (0,5), sticky = "ew")

    ctk.CTkLabel(window, text="Notes:").grid(row = 5, column = 0, padx = 10, pady = (0,5))
    notes_tb = ctk.CTkTextbox(window, width= 100, height = 100 )
    notes_tb.grid(row = 5, column = 1, padx = 10, pady = (0,5), sticky = "ew")

    ctk.CTkLabel(window, text="Reciept:").grid(row = 6, column = 0, padx = 10, pady = (0, 10))
    reciept_image = ctk.CTkButton(window, text="Attach Image")
    reciept_image.grid(row = 6, column = 1, padx = 10, pady = (0, 10), sticky = "ew")


balance_label = ctk.CTkLabel(app, text="BALANCE: 0", font=("Arial", 24))
balance_label.grid(row = 0, column = 0, columnspan = 4, padx = 10, pady = (20, 20), sticky = "w")

add_expense_button = ctk.CTkButton(app, text="Add Expense", command=expense_window)
add_expense_button.grid(row = 1, column = 0, padx = (10, 3), sticky="nsew")

history_button = ctk.CTkButton(app, text="History")
history_button.grid(row = 1, column = 1, sticky = "nsew")

set_balance_button = ctk.CTkButton(app, text="Set Balance", command= balance_dialog)
set_balance_button.grid(row = 1, column = 2, padx = (3, 0), sticky = "nsew")

transaction_button = ctk.CTkButton(app, text="Transactions")
transaction_button.grid(row = 1, column = 3, padx = (3 , 10), sticky = "nsew")

history_scrollableframe = ctk.CTkScrollableFrame(app)
history_scrollableframe.grid(row = 2, column = 0, columnspan = 4, padx = 10, pady = 10, sticky = "nsew")


app.mainloop()