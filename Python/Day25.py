countries = ("spain" , " england" , " india", "germany")

print(countries)

team = list(countries) 


team.append("russia")   #add new element after converting tuple in list
team.pop(3)                #remove the element 
team[2] ="finland"

countries = tuple(team)
print(countries)

countries2 = ("banglades", "pakistan", " japan" ,"america")

southasia = countries + countries2 

print(southasia)

element =(1,2,6,5,1,2,3,4,5,1,2,3,4,1,2,3,4)

res = element.count(1)

print(" the number in res is comes it elent is" , res ,"times !!\n ")

pos = element.index(4)

print('the integer in res is available on the position of : \n', pos )

length =len(element)

print("length of the tuple is :\n" , length)