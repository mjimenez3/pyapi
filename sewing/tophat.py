#!/usr/bin/python3
""" Naming threads and pids || rzfeeser@alta3.com
Helpful notes:
  - os.getpid() function will return ID of current process
  - threading.main_thread() returns the main thread object.
    Typically the main thread is the thread from which Python was
    started.
  - threading.current_thread() returns the current thread object.
"""        


import threading 
import os 
import time

def task1():
    print("Task 1 assigned to thread: {}".format(threading.current_thread().name))
    print("ID of process running task 1: {}".format(os.getpid())) 


def task2(): 
    print("Task 2 assigned to thread: {}".format(threading.current_thread().name))            
    print("ID of process running task 2: {}".format(os.getpid())) 

def task3():
    for i in range(5, -1, -1):
         print(i)
         

def main():
    # print ID of current process 
    print("ID of process running main program: {}".format(os.getpid())) 
  
    # print name of main thread 
    print("Main thread name: {}".format(threading.main_thread().name)) 
  
    # creating threads 
    t1 = threading.Thread(target=task1, name='t1') 
    t2 = threading.Thread(target=task2, name='t2')   
    t3 = threading.Thread(target=task3, name='t3')
    # starting threads 
    t3.start()
    t1.start() 
    
    t2.start() 
    
    # wait until all threads finish 
    t1.join() 
    t2.join() 

if __name__ == "__main__":
    main()





