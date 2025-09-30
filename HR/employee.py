class Employee:
    def __init__(self,id, first_name,last_name,position,contact_no,salary,daily_wages=300):
        self.id = id
        self.name = name
        self.salary = salary
    
    def display(self):
        print("employee ID:-",self.id)
        print("Name:-", self.name)
        print("Salary:-",self.salary)
    
    

emp1=Employee(1,"Shrutik",50000)
emp2=Employee(2,"Yash",50000)

emp1.display()
emp2.display()