a = input("enter the number : ")
print(f"multiplication thable of {a} is : " )


try:
 for i in range (1 , 11):
    print(f"{int(a)} X {i}  = {int(a) * i}")
except Exception as e :
  print("invalid input")

print("some important lines of code below ")

print(" Hello piyush how are you  ?")