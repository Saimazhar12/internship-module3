import json
import os

FILE_NAME = "expenses.json"

# Load expenses from file
def load_expenses():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

# Save expenses to file
def save_expenses(expenses):
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)

# Add expense
def add_expense(expenses):
    amount = float(input("Enter amount: "))
    category = input("Enter category (Food, Travel, etc): ")
    description = input("Enter description: ")

    expense = {
        "amount": amount,
        "category": category,
        "description": description
    }

    expenses.append(expense)
    save_expenses(expenses)
    print("Expense added successfully!")

# View expenses
def view_expenses(expenses):
    if not expenses:
        print("No expenses found.")
        return

    print("\nAll Expenses:")
    for i, exp in enumerate(expenses, 1):
        print(f"{i}. {exp['amount']} - {exp['category']} - {exp['description']}")

# Show total expense
def total_expense(expenses):
    total = sum(exp["amount"] for exp in expenses)
    print(f"\nTotal Expense: {total}")

# Menu
def main():
    expenses = load_expenses()

    while True:
        print("\n==== Expense Tracker ====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expense")
        print("4. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            total_expense(expenses)
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()

