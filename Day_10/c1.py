from datetime import datetime

now = datetime.now()
timer = now.time()

time1 = now.strftime("%A %d, %B %Y")

time_ong = datetime.strptime("235757","%H%M%S")

print(timer)
print(time1)
print(time_ong)