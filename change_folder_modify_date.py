import os
import time
import datetime

fileLocation = r"D:\New folder"
year = time.localtime().tm_year
month = time.localtime().tm_mon
day = time.localtime().tm_mday
hour = time.localtime().tm_hour
minute = time.localtime().tm_min
second = time.localtime().tm_sec

date = datetime.datetime(year=year, month=month, day=day, hour=hour, minute=minute, second=second)
modTime = time.mktime(date.timetuple())
os.utime(fileLocation, (modTime, modTime))
