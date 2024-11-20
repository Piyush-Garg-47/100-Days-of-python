#Hybrid Inheritance 
class baseclass:
    pass
class derived1(baseclass):
    pass
class derived2(baseclass):
    pass

class Hybrid(derived1 , derived2):
    pass 

# Hierarchical Inheritance 

class baseclass:
    pass

class D1(baseclass):
    pass

class D2(baseclass):
    pass

class D3(baseclass):
    pass

class D4(baseclass):
    pass

print(Hybrid.mro())