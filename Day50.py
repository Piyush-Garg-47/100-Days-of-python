a=5
b=76
print(a+b)

f =open('myfile.txt' ,'r')
while True:
    line=f.readline()
    if not line:
        break
    print(line)
