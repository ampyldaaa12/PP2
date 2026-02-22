from datetime import datetime

dt = datetime.now()
dt_no_micro = dt.replace(microsecond=0)

print("Datetime with microseconds:", dt)
print("Datetime without microseconds:", dt_no_micro)