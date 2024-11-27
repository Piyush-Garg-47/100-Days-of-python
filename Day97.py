import threading
import time

def func(second):
   print(f"Sleeping for {second} seconds")
   time.sleep(second)  

time1 = time.perf_counter()
# Normal code calling
# func(4)
# func(3)
# func(2)
# func(1)
# time2 = time.perf_counter()
# print(time2-time1)

# Calling using thread
t1 =threading.Thread(target=func ,args=[4])
t2 =threading.Thread(target=func ,args=[3])
t3 =threading.Thread(target=func ,args=[2])
t4 =threading.Thread(target=func ,args=[1])

t1.start()
t2.start()
t3.start()
t4.start()

t1.join()
t2.join()
t3.join()
t4.join()

#calculating time
time2 = time.perf_counter()
print(time2-time1)