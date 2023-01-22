import threading
import time

fg=0
class MyThreadClass(threading.Thread):
    def __init__(self,tid,nm,counter):
        threading.Thread.__init__(self)
        self.tid=tid
        self.nm=nm
        self.counter=counter
    def run(self):
        print("Strating Thread..."+self.nm)
        print_time(self.nm,self.counter,5)
        print("Exiting Thread..." + self.nm)

def print_time(tn,dl,ctr):
    while(ctr):
        if(fg):
            tn.exit()
        time.sleep(dl)
        print(tn,time.ctime(time.time()))
        ctr-=1
th1=MyThreadClass(101,"Thread1",1)
th2=MyThreadClass(102,"Thread2",2)

th1.start()
th2.start()