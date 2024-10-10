dic={
   "name" : "piyush" ,
    "age" : 21 ,
   " Branch" :  "B.tech(ai&ml)" ,
    "course duretion" : 2022_2026 
}

print(dic)
print(dic.get("course duretion"))

for keys in dic.keys():
    print(dic[keys])

for keys , values in dic.items():
    print(keys , values)