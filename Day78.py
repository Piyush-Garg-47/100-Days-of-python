class animal:
    def __init__(self , name , species):
        self.name = name
        self.species = species

    def make_sound(self):
        print("sound made by animal !!")

class dog(animal):
    def __init__(self , name , bread):
        animal.__init__(self , name ,species="dog")
        self.bread = bread
        
    def make_sound(self):
        print("dog barks  !!")

d = animal("cow" , "diman")

d.make_sound()

b = dog("dog" , "pitter")

b.make_sound()