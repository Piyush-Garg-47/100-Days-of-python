import time 

print(time.time())

print(4)
time.sleep(3)
print("this is printed after 3 seconds !!")

t = time.localtime()
formatted_time = time.strftime("%y %m  %d  - %H %M %S" , t )

print("current date and time : " , formatted_time)