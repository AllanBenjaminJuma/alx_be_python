class BankAccount:
    def __init__(self, account_balance = 0.0):
        if not isinstance(account_balance, (int, float)):
            raise ValueError("Initial Balance must be a number, 0-9.")
        if account_balance < 0:
            raise ValueError("Initial balance cannot be a negative.")
        self.account_balance = account_balance
        
    def deposit(self, amount):
        self.account_balance += amount
        return self.account_balance
    
    def withdraw(self, amount):# pass self to use instantiated account balance and amount that will alter the balance
        if not isinstance (amount, (int, float)) or amount <= 0:#check whether amount is a float or int
            raise ValueError("Amount has to be a positive number.")
        if amount > self.account_balance:
            print("Insufficient funds.")
            return False
        self.account_balance -= amount
        print(f"Withdrew: ${amount:.2f}")
        return True
    
    def display(self):
        
        
        return self.account_balance
    
