import time

def fibo (num):
  # construct fibonacci sequence
  arr = [1,2]
  total = 0
  while total < num:
    total = arr[len(arr)-1] + arr[len(arr)-2]
    if total <= num:
        arr.append(total)
  
  # sum of the even-valued terms
  sum = 0
  for j in range(len(arr)):
    if arr[j] % 2 == 0:
      sum += arr[j]
    
  return sum

# result
start = time.time()
x = 4000000
result = fibo(x)
elapsed = time.time() - start
print("%s found in %s seconds") % (result,elapsed)
