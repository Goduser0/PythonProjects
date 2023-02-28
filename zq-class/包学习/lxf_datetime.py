from datetime import datetime as dt
import time

now = dt.now()
print(now)
print(now.timestamp())

time1 = dt(2015, 6, 12, 15, 24, 3)
print(time1)

time2 = time1.timestamp()
print(time2)

now1 = dt.now()
time.sleep(2)
now2 = dt.now()
print(now2-now1)
