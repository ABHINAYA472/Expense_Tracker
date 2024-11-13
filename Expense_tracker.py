class ExpenseTracker:
    def __init__(self):
        self.expenses = {}

    def add_expense(self, date, category, amount, description):
        if date not in self.expenses:
            self.expenses[date] = []
        self.expenses[date].append({"category": category, "amount": amount, "description": description})

    def view_expenses(self, date=None):
        if date:
            if date in self.expenses:
                return self.expenses[date]
            else:
                return "No expenses found for this date."
        else:
            return self.expenses

    def view_categories(self):
        categories = set()
        for date, expenses in self.expenses.items():
            for expense in expenses:
                categories.add(expense["category"])
        return categories

    def view_monthly_summary(self, month, year):
        monthly_expenses = []
        for date, expenses in self.expenses.items():
            if date.startswith(f"{month}/{year}"):
                monthly_expenses.extend(expenses)
        return monthly_expenses

    def view_category_wise_expenditure(self, category):
        category_expenses = []
        for date, expenses in self.expenses.items():
            for expense in expenses:
                if expense["category"] == category:
                    category_expenses.append(expense)
        return category_expenses

def main():
    tracker = ExpenseTracker()

    while True:
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Categories")
        print("4. View Monthly Summary")
        print("5. View Category-wise Expenditure")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            date = input("Enter date (mm/dd/yyyy): ")
            category = input("Enter category: ")
            amount = float(input("Enter amount: "))
            description = input("Enter description: ")
            tracker.add_expense(date, category, amount, description)
			
        elif choice == "2":
            date = input("Enter date (mm/dd/yyyy) or leave blank for all: ")
            if date:
                expenses = tracker.view_expenses(date)
            else:
                expenses = tracker.view_expenses()
            print(expenses)
			
        elif choice == "3":
            categories = tracker.view_categories()
            print(categories)
			
        elif choice == "4":
            month = input("Enter month: ")
            year = input("Enter year: ")
            summary = tracker.view_monthly_summary(month, year)
            print(summary)
			
        elif choice == "5":
            category = input("Enter category: ")
            expenditure = tracker.view_category_wise_expenditure(category)
            print(expenditure)
			
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
	