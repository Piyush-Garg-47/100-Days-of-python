class employee:
    def __init__(self , name ,id):
        self.name = name
        self.id =id

    def showdetails(self):
        print(f"the name of employee : {self.id} is {self.name}")
       
class programmer(employee):
 def showlanguage(self):
  print("the default languages is python :")
e =employee("piyush garg " , 111)
e.showdetails()

e1 =employee("Aman kumar  " , 131)
e1.showdetails()

e2 = programmer("shivam garg" , 121)

e2.showlanguage()