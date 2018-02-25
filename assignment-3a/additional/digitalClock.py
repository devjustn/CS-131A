import time

for hour in range(24): 
  for minute in range(60):
    for second in range(60): 
      print("%02d" % hour, end=":")
      print("%02d" % minute, end=":")
      print("%02d" % second, end="\r") # in pycharm use \n instead of \r during development
      time.sleep(1) # sleep for 1 second