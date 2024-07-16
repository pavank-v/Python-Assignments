class BankAccount:
    
    def __init__(self, account_no: int, account_holder_name: str, account_type: str):
        self.account_no = account_no
        self.account_holder_name = account_holder_name
        self.account_type = account_type
        self.balance = 0
        self.transaction_history = []  # List to store transaction history
        
    def deposit_funds(self, amount: int):
        """Deposit funds into the account."""
        self.balance += amount
        self.transaction_history.append(f"Deposited ${amount}")
        return f"Deposited ${amount}. Current Balance: ${self.balance}"
    
    def withdraw_funds(self, amount: int): 
        """Withdraw funds from the account if sufficient balance is available."""
        if self.balance >= amount:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew ${amount}")
            return f"Withdrew ${amount}. Current Balance: ${self.balance}"
        else:
            return "Insufficient funds for withdrawal."
    
    def get_account_details(self):
        """Get account details such as account number, holder name, and type."""
        return f"Account Number: {self.account_no}\nAccount Holder: {self.account_holder_name}\nAccount Type: {self.account_type}"
    
    def check_balance_status(self):
        """Check if the account balance is above the minimum required."""
        if self.balance < 1000:
            return "Balance is below the minimum amount."
        else:
            return "Account has sufficient balance."
    
    def calculate_interest(self, amount):
        """Calculate interest based on the given amount."""
        try:   
            interest = amount * 0.07  # Assuming annual interest rate of 7%
            return f"Interest per year: ${interest}"
        except TypeError:
            return "Invalid amount for interest calculation."
        
    def get_account_type(self, option):
        """Get the type of account based on the option provided."""
        account_types = {1: "Savings Account", 2: "Business Account"}
        return account_types.get(option, "Not a valid option.")
    
    def transfer_funds(self, amount: int, recipient_account):
        """Transfer funds from this account to another account."""
        if self.balance >= amount:
            self.balance -= amount
            recipient_account.balance += amount
            self.transaction_history.append(f"Transferred ${amount} to Account {recipient_account.account_no}")
            return f"Transferred ${amount} to Account {recipient_account.account_no}. Your current balance: ${self.balance}"
        else:
            return "Insufficient funds for transfer."
    
    def view_transaction_history(self):
        """View the transaction history of the account."""
        return "\n".join(self.transaction_history)
    
    def update_account_info(self, new_name: str, new_type: str):
        """Update the account holder's name and account type."""
        self.account_holder_name = new_name
        self.account_type = new_type
        return "Account information updated successfully."


# Create two BankAccount instances for testing
person_1 = BankAccount(140231, 'John', 'Savings')
person_2 = BankAccount(245689, 'Alice', 'Business')

# Demonstrate various functionalities
print(person_1.get_account_details())
print()
print(person_1.deposit_funds(20000))
print()
print(person_1.transfer_funds(5000, person_2))
print()
print(person_1.view_transaction_history())
print()
print(person_1.update_account_info("Joe Shmoe", "Joint Account"))
print()
print(person_1.get_account_details())
