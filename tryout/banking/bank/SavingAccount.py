from .Account import Account

class SavingAccount(Account):
    def __init__(self, account_no, account_holder, balance,interest=4):
        super().__init__(account_no, account_holder, balance)
        self.interest= interest
        
    def addInterest(self):
        interestAmount = (self.balance *self.interest)/100
        self.balance +=interestAmount
        print("in saving account balanace after intertest:-",self.balance)

  
  