import customtkinter as ctk

app = ctk.CTk()

app.title("Personal Expense Tracker")

app.geometry("350x300")

balance_label = ctk.CTkLabel(app, text="BALANCE: ")
balance_label.pack()

Add_Expense_Button = ctk.CTkButton(app, text="Add Expense")
Add_Expense_Button.pack()

history_button = ctk.CTkButton(app, text="History")
history_button.pack()


app.resizable(False,False)


app.mainloop()