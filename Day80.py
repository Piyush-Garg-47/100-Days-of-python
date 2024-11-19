class animal:
    def __init__(self , name , species):
        self.name = name 
        self.species = species 
    
    def show_details(self):
        print(f"Name : {self.name}")
        print(f" Species : {self.species}")

class dog(animal):
    def __init__(self , name , bread):
        animal.__init__(self,name , species="Dog")
        self.bread = bread 

    def show_details(self):
        animal.show_details(self)
        print(f" Bread : {self.bread}")

class goldenretriver(dog):
    def __init__(self , name , color):
      dog.__init__(self ,name , bread="Goldenretriver")
      self.color = color 
    
    def show_details(self):
        dog.show_details(self)
        print(f" Color : {self.color}")

o = goldenretriver("tommy" , "black")
o.show_details()

print(goldenretriver.mro())