# Expense Tracker

This project is a simple expense tracking program built with Python and SQLite. It allows users to add, view, update, and delete expense records stored in a relational database.

## Description

The Expense Tracker uses Python to interact with a SQLite relational database. The program creates an `expenses` table and uses SQL commands to manage expense information.

The program allows the user to:

* Add an expense
* View all expenses
* Update an expense
* Delete an expense
* View the total and average expense amounts
* Exit the program

## Technologies Used

* Python
* SQLite
* SQL
* VS Code
* Git and GitHub

## Database

The program creates a SQLite database named:

`expenses.db`

The database contains an `expenses` table with the following columns:

| Column      | Type    | Description                |
| ----------- | ------- | -------------------------- |
| id          | INTEGER | Unique ID for each expense |
| description | TEXT    | Description of the expense |
| category    | TEXT    | Expense category           |
| amount      | REAL    | Amount spent               |
| date        | TEXT    | Date of the expense        |

The `id` column is the primary key.

## SQL Requirements Demonstrated

### Create a Database and Table

The program creates the SQLite database and the `expenses` table when it starts.

### Insert Data

The program uses an SQL `INSERT` statement to add new expenses.

### Retrieve Data

The program uses an SQL `SELECT` statement to retrieve and display expenses.

### Modify Data

The program uses an SQL `UPDATE` statement to modify an existing expense.

### Delete Data

The program uses an SQL `DELETE` statement to remove an expense.

### Aggregate Functions

The program uses two SQL aggregate functions:

* `SUM()` to calculate the total amount of expenses.
* `AVG()` to calculate the average expense amount.

## How to Run

1. Make sure Python is installed.
2. Clone or download this repository.
3. Open the project folder in VS Code.
4. Open the terminal.
5. Run:

```text
python expense_tracker.py
```

6. Use the menu to select an option.

## Example Menu

```text
Expense Tracker
----------------
1. Add Expense
2. View Expenses
3. Update Expense
4. Delete Expense
5. Show Summary
6. Exit
```

## Video

Video demonstration and code walkthrough:

**Video link:** Add your YouTube video link here after recording.

## Author

Sobomabo Boma Sydney

CSE 310 - Applied Programming

Module 2 - SQL Relational Databases
