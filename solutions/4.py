import time

# not complete
def palindrome ():
  largest = []
  for (var k = 100; k <= 999; k++)
        for (var j = 100; j <= 999; j++) 
            sum = k * j
            largest.append(sum)

  def isPalindrome(word) {
    wLength = word.length - 1
    wLengthToCompare = wLength / 2

    for (i = 0; i <= wLengthToCompare; i++) {
        if word.charAt(i) != word.charAt(wLength - i):
            return false;
    return true


  biggest = 0
  new_arr = []
  for (var i = 0; i < largest.length; i++):
    result = isPalindrome(largest[i].toString())
    if result == true:
        new_arr.push(largest[i])

        if largest[i] > biggest:
            biggest = largest[i]
  return biggest

  
# result
start = time.time()
result = palindrome()
elapsed = time.time() - start
print("%s found in %s seconds") % (result,elapsed)
