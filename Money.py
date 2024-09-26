# add money to account
# subtract money from account
# do taxes for adding money to account
# tax rate = 0.025
# record loans

class account():
    def __init__(self, balance):
        self.balance = balance


    def __len__(self):
        return self.balance
    
    def deposit(self, amount):
        amount = amount - (amount * 0.0025)
        self.balance = self.balance + amount
        return self.balance

store = account(1000)