x = (1,2,3,4)

print(dir(x))

#x.reverse()

print(x)

class person:
    def __init__(self , name , age):
        self.name= name 
        self.age = age 
        
p = person("piyush garg" , 21)

print(p.__dict__)

print(help(person))