#!/usr/bin/python3


class ATM:
    def __init__(self):
        self.balance = 1000  # Initial balance

    def display_menu(self):
        print("\n=== ATM Menu ===")
        print("1. Check balance")
        print("2. Withdraw funds")
        print("3. Deposit funds")
        print("4. Exit")

    def check_balance(self):
        print(f"Your current balance is ${self.balance}")

    def withdraw_funds(self):
        amount = float(input("Enter the amount to withdraw: "))
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(
                f"Withdrawal successful. Your new balance is ${self.balance}")

    def deposit_funds(self):
        amount = float(input("Enter the amount to deposit: "))
        self.balance += amount
        print(f"Deposit successful. Your new balance is ${self.balance}")

    def run(self):
        print("Welcome to the ATM!")
        while True:
            pin = input("Please enter your 4-digit PIN: ")
            if pin == "1234":
                break
            else:
                print("Incorrect PIN. Please try again.")

        while True:
            self.display_menu()
            choice = input("Enter your choice (1-4): ")
            if choice == "1":
                self.check_balance()
            elif choice == "2":
                self.withdraw_funds()
            elif choice == "3":
                self.deposit_funds()
            elif choice == "4":
                print("Thank you for using the ATM. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")


# Run the ATM program
atm = ATM()
atm.run()
