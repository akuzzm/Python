from time import time

def multy(x, k):
  start_time = time()
  
  res = x ** k
  
  end_time = time()
  time_stamp = end_time - start_time
  print "Time is: ", time_stamp
  
  return res
  
multy (1000, 1000)  
