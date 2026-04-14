from expense import Expense
from file_manager import load_expenses, save_expenses, backup_data
from utils import validate_amount, validate_date
import reports

def menu():
    expenses = load_expenses()

    while True:
        print("""
==============================
 PERSONAL FINANCE MANAGER
==============================
1. Add Expense
2. View Expenses
3. Category Summary
4. Monthly Report
5. Backup Data
6. Exit
""")

        choice = input("Enter choice: ")

        if choice == '1':
            amount = input("Enter amount: ")
            if not validate_amount(amount):
                print("Invalid amount!")
                continue

            category = input("Enter category: ")
            date = input("Enter date (YYYY-MM-DD): ")
            if not validate_date(date):
                print("Invalid date!")
                continue

            desc = input("Enter description: ")

            exp = Expense(amount, category, date, desc)
            expenses.append(exp)
            save_expenses(expenses)

            print("Expense added successfully!")

        elif choice == '2':
            for exp in expenses:
                print(exp)

        elif choice == '3':
            summary = reports.category_summary(expenses)
            for cat, amt in summary.items():
                print(f"{cat}: ₹{amt}")

        elif choice == '4':
            month = input("Enter month (YYYY-MM): ")
            data = reports.monthly_report(expenses, month)
            for exp in data:
                print(exp)
            print(f"Total: ₹{reports.total_expense(data)}")

        elif choice == '5':
            backup_data()

        elif choice == '6':
            break

        else:
            print("Invalid choice!")
