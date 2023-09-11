import threading 
import random 
import time
import math


class myThread(threading.Thread):
    def __init__(self, threadId, name, count):
        threading.Thread.__init__(self)
        self.threadId = threadId
        self.name = name
        self.count = count

    def run(self):
        print("Starting: " + self.name + "\n")
        threadLock.acquire()
        print_time(self.name, 1,self.count)
        threadLock.release()
        print("Exiting: " + self.name + "\n")


def print_time(name, delay, count):
    while count:
        def generate_random_int_array():
            arr = [random.randint(0, 10) for i in range(10)]
            return arr
        def sort_array(arr):
            arr.sort()
        my_array = generate_random_int_array()
        sort_array(my_array)
        print(my_array)
        time.sleep(delay)
        print ("%s: %s %s" % (name, time.ctime(time.time()), count) + "\n")
        count -= 1


threadLock = threading.Lock()
print("Thread test start")
thread1 = myThread(1, "Thread 1", 10)
thread2 = myThread(2, "Thread 2", 10)


thread1.start()
thread1.join()
thread2.start()
thread2.join()
print("thread test")
