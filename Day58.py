class person:
    def __init__(self , n , o):
      print("hey this is a class information")

      self.name = n 
      self.occ = o 
    def info(self):
         print(f"{self.name} is a {self.occ}")

a=person("aman" , "senior developer")

b=person("sharique" , "HR")

a.info()
b.info()