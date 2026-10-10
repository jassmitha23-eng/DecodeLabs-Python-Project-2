
# DecodeLabs Project 2: Expense Tracker

total = 0.0
count = 0

print("================================")
print("       EXPENSE TRACKER")
print("================================")
print("Enter your expense amounts.")
print("Type 'done' to calculate total.\n")

while True:
    expense = input("Enter expense amount (₹): ")

    if expense.lower() == "done":
        break

    try:
        amount = float(expense)

        if amount <= 0:
            print("Please enter an amount greater than zero.")
            continue

        total = total + amount
        count = count + 1

        print("Expense added successfully!")
        print(f"Current total: ₹{total:.2f}\n")

    except ValueError:
        print("Invalid input. Enter a number or type 'done'.")

print("\n================================")
print("          SUMMARY")
print("================================")
print(f"Number of expenses: {count}")
print(f"Total Spent: ₹{total:.2f}")
print("Thank you for using Expense Tracker!")
