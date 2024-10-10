class employee:
    def __init__(self , name):
        self.name = name 
        self.raise_amount = 0.2
    
    def showdetails(self):
        print(f"thhe name of employee is {self.name} is the raised amount is {self.raise_amount}")


emp1 = employee("piyush")
emp1.raise_amount =2000
emp2 = employee("aman")
emp1.showdetails()
emp2.showdetails()
employee.showdetails(emp1)
employee.showdetails(emp2)