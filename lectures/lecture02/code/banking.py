from __future__ import print_function

class bank_account:
    
    def __init__(self, initial_balance=0.0, initial_debt=0.0):
        self.balance = initial_balance
        self.debt = initial_debt
    
    def withdraw(self, ammount):
        self.balance -= ammount
        self.print_balance()
    
    def deposit(self, ammount):
        self.balance += ammount
        self.print_balance()
        
    def get_loan(self, ammount):
        self.balance += ammount
        self.debt += ammount
        self.print_balance()

    def pay_debt(self, ammount):
        self.balance -= ammount
        self.debt -= ammount
        self.print_balance()
        
    def print_balance(self):
        print('Your account balance is', self.balance, '\n You own the bank', self.debt)

    
john = bank_account(100.0,10)
john.withdraw(2.77)
john.deposit(10.00)
john.get_loan(1000.0)
john.pay_debt(723.0)