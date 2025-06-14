import csv
import os
from datetime import datetime

CSV_FILE = 'expenses.csv'
FIELDNAMES = ['date', 'category', 'description', 'amount']

def init_csv():
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
            writer.writeheader()

def log_expense(category, description, amount):
    with open(CSV_FILE, 'a', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writerow({
            'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'category': category,
            'description': description,
            'amount': f"{float(amount):.2f}"
        })

def show_expenses():
    if not os.path.exists(CSV_FILE):
        print("No expenses logged yet.")
        return
    with open(CSV_FILE, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            print(row)

def main():
    init_csv()
    while True:
        print("\n1. Log Expense\n2. Show Expenses\n3. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            category = input("Category: ")
            description = input("Description: ")
            amount = input("Amount: ")
            log_expense(category, description, amount)
            print("Expense logged.")
        elif choice == '2':
            show_expenses()
        elif choice == '3':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()