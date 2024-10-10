class employee:
    company = "apple"
    def show(self):
        print(f"the name of employee is {self.name} is belongs to {self.company} company")
    @classmethod
    def changecompany(cls , newcompany):
        cls.company = newcompany


e1 = employee()

e1.name = "piyush"

e1.show()

e1.changecompany("tesla")

e1.show()

print(employee.company)