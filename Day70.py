class employee:
    def __init__(self , name , sallery):
        self.name = name 
        self.sallery = sallery
    
    @classmethod
    def fromStr(cls , string):
        return cls(string.split("-")[0] , string.split("-")[1])

e = employee("piyush" , 120000)

print(e.name)
print(e.sallery)

string ="shivam-12000"

e1 = employee.fromStr(string)

print(e1.name)
print(e1.sallery)