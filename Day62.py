class studdent:
    def __init__(self , age ,name ):
        self.__age = age 
        self.name =name

obj =studdent("piyush" , 21)

print(obj.name)
print(obj._studdent__age)

print(obj.__dir__())