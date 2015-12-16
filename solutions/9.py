import time
import math

# result
start = time.time()
a_limit = 1000/3  # there are three variables and a has to be the smallest
b_limit = 1000/2 # to ensure that b is larger than a

result = 0
found = False

for a in range(a_limit):
  for b in range(b_limit):
    c = math.sqrt((b*b) + (a*a))
    if b > a and c > b:
      if a + b + c == 1000:
        result = a*b*c
        found = True
        break
  
  if(found):
    break
elapsed = time.time() - start
print("%s found in %s seconds") % (result,elapsed)
