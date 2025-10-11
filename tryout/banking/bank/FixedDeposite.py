from .Account import Account

class FixedDeposite(Account):
    def __init__(self,account_no, account_holder,balance,time=10,interest=6):
       super().__init__(account_no, account_holder, balance)
       self.time =time
       self.interest =interest
    
    def calculate_maturity_amount(self):
        interestAmount=(self.balance *self.interest*self.time)/100
        self.balance+= interestAmount
        print("the amount in fixed account is :-",self.balance)
       
  
        