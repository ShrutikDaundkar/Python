class Salesemployee:
    def __init__(self ,first_name,last_name,daily_wages=300,insentive=100,salestarget=5,working_days=25):
        self.first_name =first_name
        self.last_name = last_name
        self.daily_wages =daily_wages
        self.insentive = insentive
        self.salestarget =salestarget
        self.working_days = working_days
        
    def Salary(self):
        basic_salary =self.daily_wages*self.working_days
        if self.salestarget>10:
            salary_insentive=basic_salary+self.insentive
            
            
            print("Salary with incentive",salary_insentive)
        print("Basic salary",basic_salary)
        
emp1=Salesemployee("ram","sharma",500,100,5,25)
print(f"Full Name:{emp1.first_name} {emp1.last_name} ")
emp1.Salary()

emp2=Salesemployee("sham","kumar",1000,200,11,25)
print(f"Full Name:{emp1.first_name}    {emp1.last_name}")
emp2.Salary()
