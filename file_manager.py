import csv
import os
from expense import Expense

FILE_NAME = 'expenses.csv'

def load_expenses():
    expenses = []
    if not os.path.exists(FILE_NAME):
        return expenses

    with open(FILE_NAME, 'r', newline='') as file:
        reader = csv.reader(file)
        next(reader, None)
        for row in reader:
            if len(row) == 4:
                expenses.append(Expense(row[2], row[1], row[0], row[3]))
    return expenses

def save_expenses(expenses):
    with open(FILE_NAME, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Date', 'Category', 'Amount', 'Description'])
        for exp in expenses:
            writer.writerow(exp.to_list())

def backup_data():
    import shutil
    if os.path.exists(FILE_NAME):
        shutil.copy(FILE_NAME, 'backup_expenses.csv')
        print("Backup created successfully!")
