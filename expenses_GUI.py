import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
from collections import defaultdict
from datetime import datetime

# Data structure to store expenses
expenses = []

def add_expense():
    amount = amount_entry.get()
    category = category_var.get().strip()
    description = description_entry.get()
    date_str = date_entry.get().strip()
    
    try:
        amount = float(amount)
    except ValueError:
        messagebox.showerror("Error", "Enter a valid amount!")
        return
    
    if not category:
        category = "Others"
    
    if not description:
        description="Not applicable"
    
    if not date_str:
        date = datetime.today().strftime('%Y-%m-%d')
    else:
        try:
            datetime.strptime(date_str, '%Y-%m-%d')
            date = date_str
        except ValueError:
            messagebox.showerror("Error", "Enter a valid date in YYYY-MM-DD format!")
            return
    
    expenses.append((amount, category, description, date))
    messagebox.showinfo("Success", "Expense added successfully!")
    update_expense_table()

def update_expense_table():
    for row in expense_table.get_children():
        expense_table.delete(row)
    for expense in expenses:
        expense_table.insert("", "end", values=expense)

def show_monthly_expenses():
    monthly_data = defaultdict(list)
    for expense in expenses:
        month = datetime.strptime(expense[3], '%Y-%m-%d').strftime('%B %Y')
        monthly_data[month].append(expense)
    
    monthly_window = tk.Toplevel(root)
    monthly_window.title("Monthly Expenses")
    
    for month, expenses_list in monthly_data.items():
        tk.Label(monthly_window, text=f"Expenses for {month}", font=("Arial", 12, "bold")).pack()
        for expense in expenses_list:
            tk.Label(monthly_window, text=f"Date: {expense[3]}, Amount: {expense[0]}, Category: {expense[1]}, Description: {expense[2]}").pack()

def analyze_expenses():
    data = defaultdict(float)
    for amount, category, _, _ in expenses:
        data[category] += amount
    
    if not data:
        messagebox.showinfo("Info", "No data to analyze!")
        return
    
    categories = list(data.keys())
    amounts = list(data.values())
    plt.figure(figsize=(6,6))
    plt.pie(amounts, labels=categories, autopct="%.2f%%", startangle=90)
    plt.title("Expense Distribution")
    plt.show()

root = tk.Tk()
root.title("Expense Tracker")
root.geometry("500x500")

tk.Label(root, text="Amount").pack()
amount_entry = tk.Entry(root)
amount_entry.pack()

tk.Label(root, text="Category").pack()
category_var = tk.StringVar()
category_dropdown = ttk.Combobox(root, textvariable=category_var, values=["Food", "Transport", "Entertainment", "Bills", "Others"])
category_dropdown.pack()
category_dropdown.current(0)

tk.Label(root, text="Description").pack()
description_entry = tk.Entry(root)
description_entry.pack()

tk.Label(root, text="Date (YYYY-MM-DD)").pack()
date_entry = tk.Entry(root)
date_entry.pack()

tk.Button(root, text="Add Expense", command=add_expense).pack()
tk.Button(root, text="Show Monthly Expenses", command=show_monthly_expenses).pack()
tk.Button(root, text="Analyze Expenses", command=analyze_expenses).pack()

expense_table = ttk.Treeview(root, columns=("Amount", "Category", "Description", "Date"), show="headings")
expense_table.heading("Amount", text="Amount")
expense_table.heading("Category", text="Category")
expense_table.heading("Description", text="Description")
expense_table.heading("Date", text="Date")
expense_table.pack()

update_expense_table()
root.mainloop()
