class employee:
    def __init__(self , name):
        self.name = name 
    def show(self):
        print(f"thee name is {self.name }")

class dancer:
    def __init__(self , dance ):
        self.dance = dance

    def show(self):
        print(f"thee dance is {self.dance }")

class danceremployee(employee , dancer):
    def __init__(self , dance ,name ):
        self.dance = dance
        self.name = name 

o = danceremployee("kathak" , "shivani")
print(o.name)
print(o.dance)

o.show()

print(danceremployee.mro())