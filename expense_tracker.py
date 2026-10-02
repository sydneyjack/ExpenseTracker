import sqlite3


def create_database():
    """Create the expense database and expenses table."""
    connection = sqlite3.connect("expenses.db")
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            description TEXT NOT NULL,
            category TEXT NOT NULL,
            amount REAL NOT NULL,
            date TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()

def add_expense():
    """Add a new expense to the database."""
    description = input("Enter expense description: ")
    category = input("Enter expense category: ")

    while True:
        try:
            amount = float(input("Enter expense amount: "))
            if amount < 0:
                print("Amount cannot be negative.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")

    date = input("Enter expense date (YYYY-MM-DD): ")

    connection = sqlite3.connect("expenses.db")
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO expenses (description, category, amount, date)
        VALUES (?, ?, ?, ?)
    """, (description, category, amount, date))

    connection.commit()
    connection.close()

    print("Expense added successfully.")


def view_expenses():
    """Display all expenses stored in the database."""
    connection = sqlite3.connect("expenses.db")
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, description, category, amount, date
        FROM expenses
    """)

    expenses = cursor.fetchall()
    connection.close()

    print("\nAll Expenses")
    print("------------")

    if not expenses:
        print("No expenses found.")
        return

    for expense in expenses:
        print(
            f"ID: {expense[0]} | "
            f"Description: {expense[1]} | "
            f"Category: {expense[2]} | "
            f"Amount: ₦{expense[3]:,.2f} | "
            f"Date: {expense[4]}"
        )


def update_expense():
    """Update an existing expense in the database."""
    expense_id = int(input("Enter the ID of the expense to update: "))

    new_description = input("Enter new description: ")
    new_category = input("Enter new category: ")
    new_amount = float(input("Enter new amount: "))
    new_date = input("Enter new date (YYYY-MM-DD): ")

    connection = sqlite3.connect("expenses.db")
    cursor = connection.cursor()

    cursor.execute("""
        UPDATE expenses
        SET description = ?, category = ?, amount = ?, date = ?
        WHERE id = ?
    """, (new_description, new_category, new_amount, new_date, expense_id))

    connection.commit()

    if cursor.rowcount > 0:
        print("Expense updated successfully.")
    else:
        print("Expense ID not found.")

    connection.close()


def delete_expense():
    """Delete an expense from the database."""
    expense_id = int(input("Enter the ID of the expense to delete: "))

    connection = sqlite3.connect("expenses.db")
    cursor = connection.cursor()

    cursor.execute("""
        DELETE FROM expenses
        WHERE id = ?
    """, (expense_id,))

    connection.commit()

    if cursor.rowcount > 0:
        print("Expense deleted successfully.")
    else:
        print("Expense ID not found.")

    connection.close()

def show_summary():
    """Calculate and display total and average expenses."""
    connection = sqlite3.connect("expenses.db")
    cursor = connection.cursor()

    cursor.execute("""
        SELECT SUM(amount), AVG(amount)
        FROM expenses
    """)

    result = cursor.fetchone()
    connection.close()

    total = result[0] or 0
    average = result[1] or 0

    print("\nExpense Summary")
    print("---------------")
    print(f"Total expenses: ₦{total:,.2f}")
    print(f"Average expense: ₦{average:,.2f}")

def main():
    """Start the Expense Tracker program."""
    create_database()

    while True:
        print("\nExpense Tracker")
        print("----------------")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Update Expense")
        print("4. Delete Expense")
        print("5. Show Summary")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            update_expense()
        elif choice == "4":
            delete_expense()
        elif choice == "5":
            show_summary()
        elif choice == "6":
            print("Thank you for using Expense Tracker.")
            break
        else:
            print("Invalid option. Please choose a number from 1 to 6.")

if __name__ == "__main__":
    main()