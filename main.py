# main.py - Your first working version
def main():
    print("=== Personal Expense Tracker ===")
    expenses = []  # Start simple - list of dictionaries
    
    while True:
        print("\n1. Add Expense")
        print("2. View Expenses") 
        print("3. Show Total")
        print("4. Exit")
        
        choice = input("Choose option: ")
        
        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            show_total(expenses)
        elif choice == "4":
            break
        else:
            print("Invalid choice!")

def add_expense(expenses):
    # We'll build this together
    pass

def view_expenses(expenses):
    # We'll build this together  
    pass

def show_total(expenses):
    # We'll build this together
    pass

if __name__ == "__main__":
    main()