#threading

import _thread
import time

def print_time(threadname,delay):
    count=0
    while(count<5):
        time.sleep(delay)
        count+=1
        print(threadname,time.ctime(time.time()))

try:
    _thread.start_new_thread(print_time("Th1",1))
except:
    print("Error In Created Thread")

while 1:
    pass