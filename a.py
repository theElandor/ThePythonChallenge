import datetime
import time

start_time = datetime.datetime(2029, 10, 31, 0, 0, 0)
while datetime.datetime.now() < start_time:
    time.sleep(1)
