# def cube(x):
#     return x*x*x

# print(cube(2))

l=[1,3,5,7,8,9]

# newl=[]

# for item in l:
#     newl.append(cube(item))

# print(newl)

newli =list(map(lambda x:x*x*x , l))

print(newli)

# FILTER FUNCTION 

def filter_function(a):
    return a>4

filtered_list = list(filter(filter_function , l))

print(filtered_list)

from functools import reduce 

number =[1,2,3,4,5,6,7]

def mysum(x,y):
    return x+y 
sum = reduce(mysum , number)


print(sum)