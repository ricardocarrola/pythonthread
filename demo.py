#!/usr/bin/python3

import _thread
import time

# Define a function for the thread
def hello_world( threadName, delay):
   count = 0
   while count < 5:
      time.sleep(delay)
      count += 1
      print("%s: %s" % ( threadName, time.ctime(time.time()) ))


try:
   _thread.start_new_thread( hello_world, ("Thread-1", 2, ) )
   _thread.start_new_thread( hello_world, ("Thread-2", 4, ) )
except:
   print("Error: unable to start thread")

while 1:
   pass
