from .Account import Account

class CurrentAccount(Account):
    def __init__(self, account_no, account_holder, balance,overdraft=1000):
        super().__init__(account_no, account_holder, balance)
    
    def withdrawal(self, amount):
        if amount<self.balance+1000:
            self.balance-=amount
            
            print("balance after withdrawal in current account:-",self.balance)
       