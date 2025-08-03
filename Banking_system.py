import json
import os
from datetime import datetime

# File to store data
BANK_DATA_FILE = "bank_data.json"

# Load data
def load_data():
    if os.path.exists(BANK_DATA_FILE):
        with open(BANK_DATA_FILE, "r") as file:
            return json.load(file)
    return {}

# Save data
def save_data(data):
    with open(BANK_DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

# Create account
def create_account(data):
    acc_num = input("Enter new account number: ")
    if acc_num in data:
        print("Account already exists!")
        return
    name = input("Enter account holder name: ")
    data[acc_num] = {"name": name, "balance": 0, "transactions": []}
    print("Account created successfully.")

# Deposit
def deposit(data):
    acc_num = input("Enter account number: ")
    if acc_num not in data:
        print("Account not found.")
        return
    amount = float(input("Enter amount to deposit: "))
    data[acc_num]["balance"] += amount
    data[acc_num]["transactions"].append(
        {"type": "Deposit", "amount": amount, "date": str(datetime.now())}
    )
    print("Deposit successful.")

# Withdraw
def withdraw(data):
    acc_num = input("Enter account number: ")
    if acc_num not in data:
        print("Account not found.")
        return
    amount = float(input("Enter amount to withdraw: "))
    if data[acc_num]["balance"] >= amount:
        data[acc_num]["balance"] -= amount
        data[acc_num]["transactions"].append(
            {"type": "Withdrawal", "amount": amount, "date": str(datetime.now())}
        )
        print("Withdrawal successful.")
    else:
        print("Insufficient balance.")

# Check balance
def check_balance(data):
    acc_num = input("Enter account number: ")
    if acc_num in data:
        print(f"Account Holder: {data[acc_num]['name']}")
        print(f"Current Balance: ₹{data[acc_num]['balance']}")
    else:
        print("Account not found.")

# Show transactions
def show_transactions(data):
    acc_num = input("Enter account number: ")
    if acc_num in data:
        print(f"Transaction History for {data[acc_num]['name']}:")
        for tx in data[acc_num]["transactions"]:
            print(f"{tx['date']} - {tx['type']}: ₹{tx['amount']}")
    else:
        print("Account not found.")

# Menu
def main():
    data = load_data()
    while True:
        print("\n--- Online Banking System ---")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Transaction History")
        print("6. Exit")

        choice = input("Enter choice: ")
        if choice == "1":
            create_account(data)
        elif choice == "2":
            deposit(data)
        elif choice == "3":
            withdraw(data)
        elif choice == "4":
            check_balance(data)
        elif choice == "5":
            show_transactions(data)
        elif choice == "6":
            save_data(data)
            print("Thank you for using the banking system!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
