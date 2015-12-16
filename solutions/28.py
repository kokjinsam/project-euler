import time

size = 1001

def getDiagonalSum(size):
  current_step = 2
  next_step = current_step + 2
  arr = []
  
  while(current_step < size):
    next_step = current_step + 2
    a = current_step * next_step + 1
    b = a - current_step
    c = b - current_step
    d = c - current_step
    
    arr.append(a)
    arr.append(b)
    arr.append(c)
    arr.append(d)
    current_step = next_step
    
  return sum(arr) + 1
 
start = time.time()
result = getDiagonalSum(size)
elapsed = time.time() - start
 
print "result %s found in %s seconds" % (result, elapsed)
