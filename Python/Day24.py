tup1 = (1,2,3,4,5,6,7,8,9)
tup2 = ("red", "green" ,"blue" ,"yellow")

print(type(tup1) , tup1)
print(type(tup2) , tup2)

print("poaitive indexing\n ")

print(tup1[0])
print(tup1[1])
print(tup1[2])
print(tup1[3])
print(tup1[4],"\n")

print(tup2[0])
print(tup2[1])
print(tup2[2])
print(tup2[3],"\n")

print("negative indexing\n ")

print(tup1[-1])
print(tup1[-2])
print(tup1[-3])
print(tup1[-4])
print(tup1[-5],"\n")

print(tup2[-1])
print(tup2[-2])
print(tup2[-3],"\n")

if 88 in tup1:
    print("Yes this number is present in this tuple\n")
else:
    print("No this number is present in this tuple\n")

tup3 = tup1[2:6]
print("tup3 is the subset of the tup1 after slicing of tup1 :" , tup3)