def func1():
    try:
      l=[1,2,3,4,5,6,]
      i=int(input(" enter the value of i : "))
      print(l[i])
    except:
     print("Some error occured !!")

    finally:
      print("I am always executed !!")

x  = func1()
print(x)
