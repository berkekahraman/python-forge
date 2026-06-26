import json

FILE_NAME = "expenses.json"


def load_expenses():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_expenses(expenses):
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)


def show_menu():
    print("\nExpense Tracker")
    print("1. Add expense")
    print("2. View expenses")
    print("3. Show total spending")
    print("4. Delete expense")
    print("5. Filter by category")
    print("6. Category summary")
    print("7. Exit")


def add_expense(expenses):
    name = input("Expense name: ")
    while True:
        try:
            amount = float(input("Amount: "))
            break
        except ValueError:
            print("Please enter a valid number.")
    category = input("Category: ")

    expense = {
        "name": name,
        "amount": amount,
        "category": category
    }

    expenses.append(expense)
    save_expenses(expenses)

    print("Expense added successfully!")


def view_expenses(expenses):
    if not expenses:
        print("No expenses found.")
        return

    print("\nExpenses:")
    for index, expense in enumerate(expenses, start=1):
        print(
            f"{index}. {expense['name']} - ${expense['amount']} ({expense['category']})"
        )


def show_total(expenses):
    total = 0

    for expense in expenses:
        total += expense["amount"]

    print(f"\nTotal spending: ${total:.2f}")


def delete_expense(expenses):
    view_expenses(expenses)

    if not expenses:
        return

    try:
        index = int(input("Enter expense number to delete: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    if index < 1 or index > len(expenses):
        print("Invalid expense number.")
        return

    removed_expense = expenses.pop(index - 1)
    save_expenses(expenses)

    print(f"Deleted: {removed_expense['name']}")

def filter_by_category(expenses):
    category = input("Enter category: ").lower()

    found_expenses = []

    for expense in expenses:
        if expense["category"].lower() == category:
            found_expenses.append(expense)

    if not found_expenses:
        print("No expenses found in this category.")
        return

    view_expenses(found_expenses)


def show_category_summary(expenses):
    if not expenses:
        print("No expenses found.")
        return

    summary = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        if category in summary:
            summary[category] += amount
        else:
            summary[category] = amount

    print("\nCategory Summary:")
    for category, total in summary.items():
        print(f"{category}: ${total:.2f}")


def main():
    expenses = load_expenses()

    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            show_total(expenses)
        elif choice == "4":
            delete_expense(expenses)
        elif choice == "5":
            filter_by_category(expenses)
        elif choice == "6":
            show_category_summary(expenses)
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()