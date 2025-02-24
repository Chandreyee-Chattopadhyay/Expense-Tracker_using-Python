import matplotlib.pyplot as plt
from collections import defaultdict
from datetime import datetime

# Data structure to store expenses
expenses = []

# Function to add expense
def add_expense():
    amount = input("Enter amount: ")
    category = input("Enter category (leave blank for 'Others'): ").strip()
    description = input("Enter description: ")
    date_str = input("Enter date (YYYY-MM-DD, leave blank for today): ").strip()
    
    try:
        amount = float(amount)
    except ValueError:
        print("Error: Enter a valid amount!")
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
            print("Error: Enter a valid date in YYYY-MM-DD format!")
            return
    
    expenses.append((amount, category, description, date))
    print("Expense added successfully!")

# Function to show all expenses
def show_all_expenses():
    if not expenses:
        print("No expenses recorded.")
        return
    
    print("\nAll Recorded Expenses:")
    for expense in expenses:
        print(f"Date: {expense[3]}, Amount: {expense[0]}, Category: {expense[1]}, Description: {expense[2]}")

# Function to show monthly expenses
def show_monthly_expenses():
    if not expenses:
        print("No expenses recorded.")
        return
    
    monthly_data = defaultdict(list)
    for expense in expenses:
        month = datetime.strptime(expense[3], '%Y-%m-%d').strftime('%B %Y')
        monthly_data[month].append(expense)
    
    for month, expenses_list in monthly_data.items():
        print(f"\nExpenses for {month}:")
        for expense in expenses_list:
            print(f"Date: {expense[3]}, Amount: {expense[0]}, Category: {expense[1]}, Description: {expense[2]}")

# Function to analyze expenses
def analyze_expenses():
    data = defaultdict(float)
    for amount, category, _, _ in expenses:
        data[category] += amount
    
    if not data:
        print("No data to analyze!")
        return
    
    categories = list(data.keys())
    amounts = list(data.values())
    plt.figure(figsize=(6,6))
    plt.pie(amounts, labels=categories, autopct="%.2f%%", startangle=90)
    plt.title("Expense Distribution")
    plt.show()

# Menu-based system
def main():
    while True:
        print("\nExpense Tracker Menu")
        print("1. Add Expense")
        print("2. Show All Expenses")
        print("3. Show Monthly Expenses")
        print("4. Analyze Expenses")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_expense()
        elif choice == "2":
            show_all_expenses()
        elif choice == "3":
            show_monthly_expenses()
        elif choice == "4":
            analyze_expenses()
        elif choice == "5":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
