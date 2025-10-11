from bank import Account,SavingAccount,FixedDeposite,CurrentAccount

baseacc = Account(1235,"sahil",12345)
baseacc.deposite(19000)
baseacc.withdrawal(300)
baseacc.getdetails()

acc1 =SavingAccount(1234,"shrutik",12345,6)
acc1.addInterest() 

acc2 = CurrentAccount(1245,"yash",12345,2000)
acc2.withdrawal(2000)

acc3 = FixedDeposite(1265,"sumit",12345)
acc3.calculate_maturity_amount()