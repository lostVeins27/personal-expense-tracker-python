import customtkinter as ctk
from tkcalendar import Calendar
from datetime import date
from tkinter import filedialog

app = ctk.CTk()

app.title("Personal Expense Tracker")

app.geometry("400x300")

app.resizable(False, False)
app.columnconfigure((0, 1, 2, 3), weight=1)
app.rowconfigure(2, weight= 1)

def balance_dialog():

    """Balance dialog to input current balance"""

    dialog = ctk.CTkInputDialog(text="Input your current balance", title="Balance")
    balance = dialog.get_input()

    if balance is None:
        return

    balance_label.configure(text= f"BALANCE: {balance}")

def expense_window():

    """Expense window after add expense window is pressed"""

    window = ctk.CTkToplevel(app)
    window.geometry("400x370")
    window.title("Expense")
    window.resizable(False,False)

    window.transient(app)
    window.lift()
    window.focus_force()

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

    def open_calendar():
        calendar_window = ctk.CTkToplevel(window)
        calendar_window.geometry("300x300")
        calendar_window.resizable(False,False)

        calendar_window.columnconfigure((0, 1), weight = 1)
        calendar_window.rowconfigure((0, 1), weight = 1)

        cal = Calendar(calendar_window, selectmode = "day", date_pattern="yyyy-mm-dd")
        cal.grid(row = 0, column = 0, columnspan = 2, padx = 10, pady = (15, 10), sticky = "nsew")

        def select_date():
            date_cb.set(cal.get_date())
            calendar_window.destroy()

        ctk.CTkButton(calendar_window, text="Select", command= select_date).grid(row = 1, column = 0, padx = (10, 0), pady= (0, 10), sticky = "nsew")
        ctk.CTkButton(calendar_window, text="Cancel", command= calendar_window.destroy).grid(row = 1, column = 1, padx = (5, 10), pady = (0, 10), sticky = "nsew")

    def date_option(choice):
        if choice == "Today":
            date_cb.set(date.today().strftime("%Y-%m-%d"))
        
        elif choice == "Pick Date":
            open_calendar()

    def attach_file():
        file_path = filedialog.askopenfilename(title= "import reciept image", filetypes= [ ("Images", "*.png *.jpg *.jpeg"), ("All files", "*.*") ])

        if file_path is None or file_path == "":
            print("no attachment")
            return
        
        view_image_button = ctk.CTkButton(window, text="View Image")
        view_image_button.grid(row = 6 , column = 1, padx = (10, 0), pady = (0, 10), sticky = "ew")
        reciept_image.grid(row = 6, column = 2, padx = (0, 10), pady = (0, 10), sticky = "ew")

    window.columnconfigure((1, 2), weight= 1)
    window.rowconfigure((0, 1, 2, 3, 4, 5, 6, 7), weight= 1)
    
    # Amount
    ctk.CTkLabel(window, text="Amount:").grid(row = 0, column = 0, padx = 10, pady = (10, 5))
    amount_entry = ctk.CTkEntry(window)
    amount_entry.grid(row = 0, column = 1, padx = 10, columnspan = 2,  pady = (10, 5), sticky = "ew")

    # Category
    ctk.CTkLabel(window, text="Category:").grid(row = 1, column = 0, padx = 10, pady = (0, 5))
    category_cb = ctk.CTkComboBox(window, values = category_options, state="readonly")
    category_cb.grid(row = 1, column = 1, padx = 10, pady = (0,5), columnspan = 2, sticky = "ew")

    # Account
    ctk.CTkLabel(window, text="Account:").grid(row = 2, column = 0, padx = 10, pady = (0, 5))
    account_cb = ctk.CTkComboBox(window, values=account_options, state="readonly")
    account_cb.grid(row = 2, column = 1, padx = 10, pady = (0,5), columnspan = 2, sticky = "ew")

    # Date
    ctk.CTkLabel(window, text="Date:").grid(row = 3, column = 0, padx = 10, pady= (0,5))
    date_cb = ctk.CTkComboBox(window, values = ["Today", "Pick Date"], state="readonly", command = date_option)
    date_cb.grid(row = 3, column = 1, padx = 10, pady = (0,5), columnspan = 2, sticky = "ew")

    # Merchant
    ctk.CTkLabel(window, text="Merchant:").grid(row = 4, column = 0, padx = 10, pady = (0,5))
    merchant_entry = ctk.CTkEntry(window)
    merchant_entry.grid(row = 4, column = 1, padx = 10, pady = (0,5), columnspan = 2, sticky = "ew")

    # Notes
    ctk.CTkLabel(window, text="Notes:").grid(row = 5, column = 0, padx = 10, pady = (0,5))
    notes_tb = ctk.CTkTextbox(window, width= 100, height = 100 )
    notes_tb.grid(row = 5, column = 1, padx = 10, pady = (0,5), columnspan = 2, sticky = "ew")

    # Reciept
    ctk.CTkLabel(window, text="Reciept:").grid(row = 6, column = 0, padx = 10, pady = (0, 10))
    reciept_image = ctk.CTkButton(window, text="Attach Image", command= attach_file)
    reciept_image.grid(row = 6, column = 1, padx = 10, pady = (0, 10), columnspan = 2, sticky = "ew")

    button_frame = ctk.CTkFrame(window, fg_color="transparent")
    button_frame.grid(row =  7, column = 0, columnspan = 3, padx = 10, pady = (0, 10), sticky = "ew")
    button_frame.columnconfigure((0, 1), weight= 1)

    save_button = ctk.CTkButton(button_frame, text = "Save")
    save_button.grid(row = 0, column = 0, padx = (0, 5), sticky = "ew")

    cancel_button = ctk.CTkButton(button_frame, text = "Cancel", command= window.destroy)
    cancel_button.grid(row = 0, column = 1, sticky = "ew")


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