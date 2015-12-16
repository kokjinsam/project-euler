import time
import math

# Functions
def makePentagonNum(i):
  return (i * (3 * i -1))/2

def makePentagonSeries (startpoint = None, endpoint = None):
  # the 0th number
  if startpoint is None:
    startpoint = 0
  
  # the 100th number 
  if endpoint is None:
    endpoint = 100
  
  # construct series
  series = []
  for num in range(startpoint, endpoint):
    temp = makePentagonNum(num)
    series.append(temp)
    
  return series

def checkPentagonal (num):
  return isWhole((math.sqrt(24 * num + 1) + 1)/6)
  
def isWhole(x):
  if x % 1 == 0:
    return True
  else:
    return False

# not complete
def findPair ():
  startpoint = 0
  endpoint = 100
  series = makePentagonSeries(startpoint, endpoint)
  
# result
start = time.time()

elapsed = time.time() - start
print("%s found in %s seconds") % (result,elapsed)
