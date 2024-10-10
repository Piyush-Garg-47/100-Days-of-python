l = [11,42,6,4,1,1,1,1,1,5,3,]
print(l)

l.append(7)

print(l) 
l.sort()
print(l)

l.sort(reverse = True)
print(l)

l.reverse()
print("this is reverse side " ,l)

print(l.index(6))

print(l.count(1))

m=l.copy()

m[0]=0
print(m)

l.insert(2,15)
print(l)

m=[600,700,800,900]
l.extend(m)

print(l)