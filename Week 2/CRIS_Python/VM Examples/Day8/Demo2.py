import _thread
import threading
import time
def Perform(tname,delay):
    count=0
    while(count<5):
        time.sleep(delay)
        count+=1
        print(tname,time.ctime(time.time()))

print(threading.main_thread().name)
try:
    _thread.start_new_thread(Perform("Th1",2))
except:
    print("Error in Thread")

if (threading.main_thread().is_alive()):
    print("Alive3")