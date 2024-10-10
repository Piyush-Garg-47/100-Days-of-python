s1={1,2,4,5,6,7}

s2={3,4,6,8,9}

print(s1.union(s2))

s1.update(s2)

print(s1 , s2)

cities ={"tokyo" , "mumbai" , "kabul" , "london" , "delhi" } 

cities2 = {"delhi" , "mumbai" , "tokyo" , "madrin"} 

cities3 = cities.union(cities2)

print(cities3)

cities4 =cities.intersection(cities2)

cities.intersection_update(cities2)

print(cities)

print(cities4)

cities5 = cities.difference(cities2)

print(cities5)
