l= [2,3,6,7,8,9]

print(l)

print(type(l))

print(" Now we print this list in accending order ")

print(l[0])
print(l[1])
print(l[2])
print(l[3])
print(l[4])
print(l[5])


print(" Now we print this list in decending order ")


print(l[-1])
print(l[-2])
print(l[-3])
print(l[-4])
print(l[-5])

if 7 in l:
    print(" yes it is present !! ")
else:
    print(" no it is not present !!")

print(" print the l with the help of range ")
print(l)
print(l[1:-1])
print(l[1:5:2])

lst = [i*i for i  in range(10)]
print(lst)

lst = [i*i for i  in range(10) if i%2 == 0]
print(lst)

