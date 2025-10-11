class Account:
    def __init__(self,account_no, account_holder,balance):
        self.account_no =account_no
        self.account_holder =account_holder
        self.balance = balance
    
    def deposite(self, amount):
        self.amount = amount
        
        self.balance+= amount
        print("total balance in the account after deposite :-", self.balance)
        
    def withdrawal(self, amount):
        self.amount = amount
        
        self.balance -= amount
        print("total amount in the account after withdrawal:-",self.balance)
        
    def getdetails(self):
        print(self.account_holder,self.account_no,self.balance)
    
