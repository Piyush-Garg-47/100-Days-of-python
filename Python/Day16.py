x = int (input("zenter the value of x :"))

match x:
    case 0:
        print(" x is zero")
    case 1:
        print("x is one ")
    case 2:
        print(" x is two")
    case 3:
        print(" x is three")
    case 4:
        print("x is four ")
    case _ if x%2 ==0:
        print(" x is positive and even number ")
    case _ if x%2 !=0:
        print(" x is positive and odd number ")

