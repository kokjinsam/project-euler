import time
 
 
max_a = 1000
max_b = 1000
 
def getCoeffTotal(a, b):
  longest = 39
  
  for coef_a in range(39, a):
    for coef_b in range(39, b):
      for n in range(longest):
        test = (n * n) + (coef_a * n) + coef_b
        
 
start = time.time()
result = getCoeffTotal(max_a, max_b)
elapsed = time.time() - start
 
print "result %s found in %s seconds" % (result, elapsed)
