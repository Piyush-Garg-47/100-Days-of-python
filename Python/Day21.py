def average(a,b=5):
    print("average of two number is" ,((a+b)/2))

average(10,20)

#default argument 

def name(fname , mname = "singh" , lname = "rajput"):
    print("Hello my name is " ,fname , mname , lname)

name("piyush")

#keyword argument 

average(b=5 , a = 15)

#required function 

average(10)

#value length argument 
def mean(*number):
   sum = 0 
   for i in number:
      sum = sum + i 
   print(" mean of the number is " , sum / len(number))

mean(3,4,5,6)

def name(**name):
   print( "Hello my name is " ,name["fname"] , name["mname"] , name["lname"])

name(mname="Singh" , fname = "Piyush " , lname ="Rajput")