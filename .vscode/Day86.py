numbers = [1,2,3,4,5,6]
while( n:= len(numbers)) > 0:
    print(numbers.pop())

a = True 
print(a)
print(a :=False)

foods = list()
while True :
    food = input ("whiat food do you like most ?")
    if food =="quite":
        break 
    foods.append(food)