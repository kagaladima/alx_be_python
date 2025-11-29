class BankAccount:
    def __init__(self, initial_balance=0):
        self.account_balance = initial_balance

    def deposit(self, amount):
        """Adds money to the account balance."""
        self.account_balance += amount

    def withdraw(self, amount):
        """Withdraws money if funds are sufficient. Returns True/False."""
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        return False

    def display_balance(self):
        """Prints the current account balance."""
        print(f"Current Balance: ${self.account_balance}")
        