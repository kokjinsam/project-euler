import datetime
import time

# startDate and endDate has to be in this format: DDMMYYYY  
def countSunday (startDate, endDate):
  start = datetime.datetime.strptime(startDate, '%d%m%Y').date()
  end = datetime.datetime.strptime(endDate, '%d%m%Y').date()
  sundays = 0
  
  for year in range(start.year, end.year + 1):
    for month in range( 1, 13):
      day = datetime.date(year, month, 1).weekday() == 6
      if(day.weekday() == 6):
        sundays += 1
  
  return sundays
  
# result
start = time.time()
total = countSunday('01011901', '31122000')
elapsed = time.time() - start
print("%s found in %s seconds") % (total,elapsed)
