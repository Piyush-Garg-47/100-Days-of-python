import time
timestamp =time.strftime(('%H:%M:%S'))
print(timestamp)

if(timestamp > '12:00:00'):
    print("Good Afternoon")
else:
    print("Good Morning")