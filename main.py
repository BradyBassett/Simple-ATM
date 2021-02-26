# Use snake cases from now on instead of camel cases when writing python
# PROTOTYPE VERSION

import random
import time


class Accounts:
    # Defining Account instance variables.
    def __init__(self, pin, balance, annualInterestRate=3.4):
        self.pin = pin
        self.balance = balance
        self.annualInterestRate = annualInterestRate

    # Class function to return the monthly interest rate.
    def getMonthlyInterestRate(self):
        return self.annualInterestRate / 12

    # class function to calculate difference between the balance and the amount withdrawn.
    def withdraw(self, amount):
        self.balance -= amount

    # class function to calculate the sum between the balance and the amount deposited.
    def deposit(self, amount):
        self.balance += amount

    # Class function to calculate the product of the balance and the annual interest rate.
    def getAnnualInterest(self):
        return self.balance * self.annualInterestRate

    # Class function to calculate the product of the balance and the monthly interest rate.
    def getMonthlyInterest(self):
        return self.balance * self.getMonthlyInterestRate()


# Revieves pin from user input and validates input.
def getAccountPin():
    while True:
        pin = input("\nEnter four digit account pin: ")
        try:
            pin = int(pin)
            if 1000 <= pin <= 9999:
                return pin
            else:
                print(f"\n{pin} is not a valid pin... Try again")
        except ValueError:
            print(f"\n{pin} is not a vaild pin... Try again")


# Recieves user input for option selection and validates selection.
def getSelection():
    while True:
        selection = input("\nEnter your selection: ")
        try:
            selection = int(selection)
            if 1 <= selection <= 4:
                return selection
            else:
                print(f"{selection} is not a valid choice... Try again")
        except ValueError:
            print(f"{selection} is not a valid choice... Try again")


# Recieves user input and validates if input is either yes, y, no, or n.
def correctAmount(amount):
    while True:
        answer = input(f"Is ${amount} the correct ammount, Yes or No? ")
        try:
            answer = answer.lower()
            if answer == "y" or answer == "yes":
                return True
            elif answer == "n" or answer == "no":
                return False
            else:
                print("Please enter a valid response")
        except AttributeError:
            print("Please enter a valid response")


# Recieves user input on amount to withdraw and validates inputed value.
def withdraw(workingAccount):
    while True:
        try:
            amount = float(input("\nEnter amount you want to withdraw: "))
            amount = round(amount, 2)
            if amount > 0 and ((workingAccount.balance) - amount) > 0:
                answer = correctAmount(amount)
                if answer == True:
                    print("Verifying withdraw")
                    time.sleep(random.randint(1, 2))
                    return amount
            elif (((workingAccount.balance) - amount) < 0):
                print("\nYour balance is less than the withdraw amount")
            elif amount == 0:
                answer = correctAmount(amount)
                if answer == True:
                    print("Canceling withdraw")
                    time.sleep(random.randint(1, 2))
                    return amount
            else:
                print("\nPlease enter an amount greater than or equal to 0")
        except (ValueError, TypeError):
            print("\nAmount entered is invalid... Try again")


# Recieves user input on amount to deposit and validates inputed value.
def deposit():
    while True:
        try:
            amount = float(input("\nEnter amount you want to deposit: "))
            amount = round(amount, 2)
            if amount > 0:
                answer = correctAmount(amount)
                if answer == True:
                    print("Verifying deposit")
                    time.sleep(random.randint(1, 2))
                    return amount
            elif amount == 0:
                answer = correctAmount(amount)
                if answer == True:
                    print("Canceling deposit")
                    time.sleep(random.randint(1, 2))
                    return amount
            else:
                print("\nPlease enter an amount greater than or equal to 0")
        except (ValueError, TypeError):
            print("\nAmount entered is invalid... Try again")


# End of program to print out account information and return false to end main loop
def exitATM(workingAccount):
    print("\nTransaction is now complete.")
    print("Transaction number: ", random.randint(10000, 1000000))
    print("Current Interest Rate: ", workingAccount.annualInterestRate)
    print("Monthly Interest Rate: ", workingAccount.annualInterestRate / 12)
    print("Thanks for using this ATM")
    return False


def main():
    # Creating all accounts possible, could be stored or read from a file/database instead for better functionality overall.
    accounts = []
    for i in range(1000, 9999):
        account = Accounts(i, 0)
        accounts.append(account)

    # ATM Processes loop
    loop = True
    while loop:
        pin = getAccountPin()
        print(pin)
        # Account session loop
        while loop:
            # Menu Selection
            print("\n1 - View Balance \t 2 - Withdraw \t 3 - Deposit \t 4 - Exit ")

            selection = getSelection()

            # Getting working account object by comparing pins
            for acc in accounts:
                # Comparing user inputted pin to pins created
                if acc.pin == pin:
                    workingAccount = acc
                    break

            # View Balance
            if selection == 1:
                print(f"\nYour balance is ${workingAccount.balance}")
            # Withdraw
            elif selection == 2:
                workingAccount.withdraw(withdraw(workingAccount))
                print(f"\nUpdated Balance: ${workingAccount.balance}")
            # Deposit
            elif selection == 3:
                workingAccount.deposit(deposit())
                print(f"\nUpdated Balance: ${workingAccount.balance}")
            # Exit
            elif selection == 4:
                loop = exitATM(workingAccount)
            # Invalid input
            else:
                print("Enter a valid choice")


if __name__ == "__main__":
    main()
