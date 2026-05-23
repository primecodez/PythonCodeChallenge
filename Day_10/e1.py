#Using datetime module

from datetime import datetime

now = datetime.now()
year = now.year
month = now.month
date = now.date()
timestamp = now.timestamp()

time = now.strftime("%d %A %Y , %H:%M:%S")
print("time:",time)