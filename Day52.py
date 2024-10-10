# def doubl(x):
#     return x*2

# print(doubl(5))

double =lambda x:x*2

print(double(5))

cube = lambda x:x*x*x

print(cube(2))

avg = lambda x,y,z:(x+y+z)/3

print(avg(3,5,10))

def appl(fx , value):
    return 6 +fx(value)

print(appl(cube , 2))