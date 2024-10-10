a = 9 
b = 8
gmean1 =(a+b) / (a*b)

print(gmean1)

if(a>b):
    print("first number is grater !")
else:
    print("Second number is grater !")

c =5
d=6
gmean2 =(c+d)/(c/d)

if(a>b):
    print("first number is grater !")
else:
    print("Second number is grater !")


print(gmean2)

def calculategmean(a,b):
    mean= (a+b) / (a*b)
    print(mean)

def isgrater(a,b):
    if(a>b):
     print("first number is grater !")
    else:
     print("Second number is grater !")



calculategmean(a,b)
calculategmean(c,d)
isgrater(a,b)
isgrater(c,d)
