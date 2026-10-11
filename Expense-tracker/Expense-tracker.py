import json
import csv
from pathlib import Path
from datetime import datetime
from collections import defaultdict

# ==========================================
# EXPENSE TRACKER - VERSION 2.0
# ==========================================

DATA_FILE = Path("expenses.json")
BUDGET_FILE = Path("budget.json")
CSV_FILE = Path("expense_report.csv")

CATEGORIES = [
    "Food",
    "Travel",
    "Shopping",
    "Education",
    "Books",
    "Entertainment",
    "Health",
    "Bills",
    "Other"
]


# ==========================================
# FILE HANDLING
# ==========================================

def load_json(file_path, default):
    """Load JSON data safely."""
    if not file_path.exists():
        return default

    try:
        with file_path.open("r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        print(f"Warning: Could not read {file_path}. Using default data.")
        return default


def save_json(file_path, data):
    """Save data to a JSON file."""
    try:
        with file_path.open("w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
        return True
    except OSError:
        print(f"Error: Could not save data to {file_path}.")
        return False


expenses_list = load_json(DATA_FILE, [])
budget_data = load_json(BUDGET_FILE, {})


# ==========================================
# INPUT VALIDATION
# ==========================================

def get_amount(prompt):
    """Accept only positive monetary amounts."""
    while True:
        try:
            amount = float(input(prompt))

            if amount <= 0:
                print("Amount must be greater than zero.")
                continue

            if not amount < float("inf"):
                print("Please enter a valid amount.")
                continue

            return round(amount, 2)

        except ValueError:
            print("Invalid amount! Please enter a number.")


def get_date(prompt="Enter date (YYYY-MM-DD): "):
    """Validate dates."""
    while True:
        date_text = input(prompt).strip()

        try:
            datetime.strptime(date_text, "%Y-%m-%d")
            return date_text
        except ValueError:
            print("Invalid date! Use YYYY-MM-DD, for example 2026-10-11.")


def get_category():
    """Display categories and return the selected category."""
    print("\nAvailable Categories:")

    for index, category in enumerate(CATEGORIES, start=1):
        print(f"{index}. {category}")

    while True:
        try:
            choice = int(input("Select category number: "))

            if 1 <= choice <= len(CATEGORIES):
                return CATEGORIES[choice - 1]

            print("Please select a valid category number.")

        except ValueError:
            print("Please enter a number.")


def get_expense_by_id(expense_id):
    """Find an expense using its unique ID."""
    for expense in expenses_list:
        if expense["id"] == expense_id:
            return expense

    return None


def get_next_id():
    """Generate a unique expense ID."""
    return max(
        (expense.get("id", 0) for expense in expenses_list),
        default=0
    ) + 1


# ==========================================
# ADD EXPENSE
# ==========================================

def add_expense():
    print("\n========== ADD EXPENSE ==========")

    date = get_date()
    category = get_category()

    description = input("Enter description: ").strip()

    while not description:
        print("Description cannot be empty.")
        description = input("Enter description: ").strip()

    amount = get_amount("Enter amount (₹): ")

    expense = {
        "id": get_next_id(),
        "date": date,
        "category": category,
        "description": description,
        "amount": amount
    }

    expenses_list.append(expense)

    if save_json(DATA_FILE, expenses_list):
        print("\nExpense added successfully!")
        print(f"Expense ID: {expense['id']}")
        print(f"Amount: ₹{amount:.2f}")
    else:
        expenses_list.pop()
        print("Expense was not saved. Please try again.")


# ==========================================
# VIEW ALL EXPENSES
# ==========================================

def view_expenses():
    print("\n========== ALL EXPENSES ==========")

    if not expenses_list:
        print("No expenses recorded yet.")
        return

    print(
        f"{'ID':<5} {'Date':<12} {'Category':<16} "
        f"{'Amount':>12}  Description"
    )
    print("-" * 80)

    for expense in sorted(
        expenses_list,
        key=lambda item: (item["date"], item["id"])
    ):
        print(
            f"{expense['id']:<5} "
            f"{expense['date']:<12} "
            f"{expense['category']:<16} "
            f"₹{expense['amount']:>10.2f}  "
            f"{expense['description']}"
        )

    print("-" * 80)
    print(f"Total expenses: {len(expenses_list)}")


# ==========================================
# TOTAL SPENDING
# ==========================================

def view_total_spending():
    print("\n========== TOTAL SPENDING ==========")

    total = sum(expense["amount"] for expense in expenses_list)

    print(f"Total expenditure: ₹{total:.2f}")


# ==========================================
# CATEGORY-WISE SPENDING
# ==========================================

def category_summary():
    print("\n========== CATEGORY-WISE SPENDING ==========")

    if not expenses_list:
        print("No expenses recorded yet.")
        return

    category_totals = defaultdict(float)

    for expense in expenses_list:
        category_totals[expense["category"]] += expense["amount"]

    for category, total in sorted(category_totals.items()):
        print(f"{category:<20} ₹{total:.2f}")

    print("-" * 40)
    print(
        f"{'Total':<20} "
        f"₹{sum(category_totals.values()):.2f}"
    )


# ==========================================
# MONTHLY SUMMARY
# ==========================================

def monthly_summary():
    print("\n========== MONTHLY SUMMARY ==========")

    month = input("Enter month (YYYY-MM): ").strip()

    try:
        datetime.strptime(month, "%Y-%m")
    except ValueError:
        print("Invalid month! Use YYYY-MM, for example 2026-10.")
        return

    monthly_expenses = [
        expense
        for expense in expenses_list
        if expense["date"].startswith(month)
    ]

    if not monthly_expenses:
        print(f"No expenses found for {month}.")
        return

    amounts = [expense["amount"] for expense in monthly_expenses]

    total = sum(amounts)
    average = total / len(amounts)
    highest = max(amounts)

    print(f"\nMonth: {month}")
    print(f"Number of transactions: {len(monthly_expenses)}")
    print(f"Total spending: ₹{total:.2f}")
    print(f"Average expense: ₹{average:.2f}")
    print(f"Highest expense: ₹{highest:.2f}")


# ==========================================
# SEARCH EXPENSES
# ==========================================

def search_expenses():
    print("\n========== SEARCH EXPENSES ==========")
    print("1. Search by category")
    print("2. Search by date")
    print("3. Search by description")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid choice.")
        return

    if choice == 1:
        category = get_category()

        results = [
            expense for expense in expenses_list
            if expense["category"] == category
        ]

    elif choice == 2:
        date = get_date()

        results = [
            expense for expense in expenses_list
            if expense["date"] == date
        ]

    elif choice == 3:
        keyword = input("Enter description keyword: ").strip().lower()

        if not keyword:
            print("Search keyword cannot be empty.")
            return

        results = [
            expense for expense in expenses_list
            if keyword in expense["description"].lower()
        ]

    else:
        print("Invalid choice.")
        return

    if not results:
        print("No matching expenses found.")
        return

    print("\nMatching expenses:")

    for expense in results:
        print(
            f"ID: {expense['id']} | "
            f"Date: {expense['date']} | "
            f"Category: {expense['category']} | "
            f"Amount: ₹{expense['amount']:.2f} | "
            f"Description: {expense['description']}"
        )


# ==========================================
# DELETE EXPENSE
# ==========================================

def delete_expense():
    print("\n========== DELETE EXPENSE ==========")

    if not expenses_list:
        print("No expenses available to delete.")
        return

    view_expenses()

    try:
        expense_id = int(input("\nEnter expense ID to delete: "))
    except ValueError:
        print("Please enter a valid ID.")
        return

    expense = get_expense_by_id(expense_id)

    if expense is None:
        print("Expense ID not found.")
        return

    print(
        f"Selected: {expense['category']} - "
        f"₹{expense['amount']:.2f}"
    )

    confirm = input("Are you sure? (yes/no): ").strip().lower()

    if confirm != "yes":
        print("Deletion cancelled.")
        return

    expenses_list.remove(expense)

    if save_json(DATA_FILE, expenses_list):
        print("Expense deleted successfully!")
    else:
        expenses_list.append(expense)
        print("Deletion could not be saved.")


# ==========================================
# EDIT EXPENSE
# ==========================================

def edit_expense():
    print("\n========== EDIT EXPENSE ==========")

    if not expenses_list:
        print("No expenses available to edit.")
        return

    view_expenses()

    try:
        expense_id = int(input("\nEnter expense ID to edit: "))
    except ValueError:
        print("Please enter a valid ID.")
        return

    expense = get_expense_by_id(expense_id)

    if expense is None:
        print("Expense ID not found.")
        return

    print("\nPress Enter to keep the existing value.")

    new_date = input(
        f"Date [{expense['date']}]: "
    ).strip()

    if new_date:
        try:
            datetime.strptime(new_date, "%Y-%m-%d")
            expense["date"] = new_date
        except ValueError:
            print("Invalid date. Keeping the existing date.")
            
    print("\nChoose a new category or press Enter to keep the existing one.")

    for index, category in enumerate(CATEGORIES, start=1):
        print(f"{index}. {category}")

    category_choice = input(
        f"Category [{expense['category']}]: "
    ).strip()

    if category_choice:
        try:
            category_index = int(category_choice)

            if 1 <= category_index <= len(CATEGORIES):
                expense["category"] = CATEGORIES[category_index - 1]
            else:
                print("Invalid category. Keeping the existing category.")
        except ValueError:
            print("Invalid category. Keeping the existing category.")

    new_description = input(
        f"Description [{expense['description']}]: "
    ).strip()

    if new_description:
        expense["description"] = new_description

    new_amount = input(
        f"Amount [₹{expense['amount']:.2f}]: "
    ).strip()

    if new_amount:
        try:
            amount = float(new_amount)

            if 0 < amount < float("inf"):
                expense["amount"] = round(amount, 2)
            else:
                print("Invalid amount. Keeping the existing amount.")

        except ValueError:
            print("Invalid amount. Keeping the existing amount.")

    if save_json(DATA_FILE, expenses_list):
        print("Expense updated successfully!")


# ==========================================
# MONTHLY BUDGET
# ==========================================

def set_budget():
    print("\n========== SET MONTHLY BUDGET ==========")

    month = input("Enter month (YYYY-MM): ").strip()

    try:
        datetime.strptime(month, "%Y-%m")
    except ValueError:
        print("Invalid month! Use YYYY-MM.")
        return

    amount = get_amount("Enter monthly budget (₹): ")

    budget_data[month] = amount

    if save_json(BUDGET_FILE, budget_data):
        print(f"Budget for {month} set to ₹{amount:.2f}.")
    else:
        budget_data.pop(month, None)
        print("Budget could not be saved.")


def view_budget():
    print("\n========== BUDGET STATUS ==========")

    month = input("Enter month (YYYY-MM): ").strip()

    try:
        datetime.strptime(month, "%Y-%m")
    except ValueError:
        print("Invalid month! Use YYYY-MM.")
        return

    if month not in budget_data:
        print("No budget set for this month.")
        return

    budget = budget_data[month]

    total = sum(
        expense["amount"]
        for expense in expenses_list
        if expense["date"].startswith(month)
    )

    remaining = budget - total
    percentage = (total / budget) * 100

    print(f"\nMonth: {month}")
    print(f"Monthly budget: ₹{budget:.2f}")
    print(f"Total spent: ₹{total:.2f}")
    print(f"Remaining budget: ₹{remaining:.2f}")
    print(f"Budget used: {percentage:.2f}%")

    if remaining < 0:
        print("WARNING: You have exceeded your budget!")
    elif remaining == 0:
        print("You have used your entire budget.")
    else:
        print("You are within your budget.")


# ==========================================
# EXPORT EXPENSES TO CSV
# ==========================================

def export_to_csv():
    print("\n========== EXPORT EXPENSES ==========")

    if not expenses_list:
        print("No expenses available to export.")
        return

    try:
        with CSV_FILE.open(
            "w",
            newline="",
            encoding="utf-8-sig"
        ) as file:

            fieldnames = [
                "id",
                "date",
                "category",
                "description",
                "amount"
            ]

            writer = csv.DictWriter(
                file,
                fieldnames=fieldnames
            )

            writer.writeheader()
            writer.writerows(expenses_list)

        print(f"Expenses exported successfully to {CSV_FILE.resolve()}")

    except OSError:
        print("Unable to export expenses. Check file permissions.")


# ==========================================
# MAIN MENU
# ==========================================

def main():
    while True:
        print("\n" + "=" * 45)
        print("       WELCOME TO EXPENSE TRACKER")
        print("=" * 45)

        print("1.  Add Expense")
        print("2.  View All Expenses")
        print("3.  View Total Spending")
        print("4.  Category-wise Spending")
        print("5.  Monthly Summary")
        print("6.  Search Expenses")
        print("7.  Delete Expense")
        print("8.  Edit Expense")
        print("9.  Set Monthly Budget")
        print("10. View Budget Status")
        print("11. Export Expenses to CSV")
        print("12. Exit")

        try:
            choice = int(input("\nEnter your choice: "))
        except ValueError:
            print("Invalid input! Please enter a number from 1 to 12.")
            continue

        if choice == 1:
            add_expense()

        elif choice == 2:
            view_expenses()

        elif choice == 3:
            view_total_spending()

        elif choice == 4:
            category_summary()

        elif choice == 5:
            monthly_summary()

        elif choice == 6:
            search_expenses()

        elif choice == 7:
            delete_expense()

        elif choice == 8:
            edit_expense()

        elif choice == 9:
            set_budget()

        elif choice == 10:
            view_budget()

        elif choice == 11:
            export_to_csv()

        elif choice == 12:
            print("\nThank you for using Expense Tracker!")
            print("Your expenses are saved locally.")
            break

        else:
            print("Invalid choice! Please select between 1 and 12.")


# ==========================================
# PROGRAM ENTRY POINT
# ==========================================

if __name__ == "__main__":
    main()

