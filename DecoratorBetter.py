from time import time

def check_time (function_to_decorate):
  def the_wrapper(*args, **kwargs):
    start_time = time()
    
    function_to_decorate(*args, **kwargs)
    
    end_time = time()
    time_stamp = end_time - start_time
    print "Time is: ", time_stamp
    
    return the_wrapper()
    
@check_time
def multy(x, k):
  res = x ** k
  return res
  
multy(1000, 1000)  
