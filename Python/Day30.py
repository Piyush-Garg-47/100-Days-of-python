# today we study about the recursion in python 

#fectorial by using the recurssion 
def fectorial(n):
    if(n==0 or n ==1 ):
        return 1 
    else:
        return n * fectorial(n-1)
    
print( "factorial of  n is : " ,fectorial(2))
print( "factorial of  n is : " ,fectorial(3))
print( "factorial of  n is : " ,fectorial(4))   
print( "factorial of  n is : " ,fectorial(5))

#febonachi series using the recurssion 

def febonachi(m):
    if(m==0 or m==1):
        return 1 
    else:
        return febonachi(m-1) + febonachi(m-2)
    
print("febonachi of number m is : " , febonachi(3))
print("febonachi of number m is : " , febonachi(4))
print("febonachi of number m is : " , febonachi(5))
print("febonachi of number m is : " , febonachi(6))
print("febonachi of number m is : " , febonachi(7))