from main import startit
import threading

THREADS = 2
LOOPS = 1

import threading
sums = []
class SummingThread(threading.Thread):
     def __init__(self,low,high):
         super(SummingThread, self).__init__()
         self.low=low
         self.high=high
         self.total=0

     def run(self):
         for i in range(self.low,self.high):
             sums.append(startit())

thread1 = SummingThread(0, 2)
thread2 = SummingThread(0,2)
thread1.start()
thread2.start()
thread1.join()
thread2.join()


print sums

# broken
# runs identical programs not unique
# I don't get multithreads :/