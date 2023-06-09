# Datetime module

import datetime


now = datetime.datetime.now()
now = datetime.datetime.utcnow()
dt = datetime.datetime(2023, 3, 27, 9, 30, 0)

print(type(now))
print(now)
print(dt)

# Convert to string

str_now = now.strftime("%Y-%m-%d %H:%M:%S")
print(type(str_now))
print(str_now)

# Time diff between two dates

start_time = datetime.datetime(2023, 3, 27, 9, 30, 0)
end_time = datetime.datetime(2023, 3, 27, 10, 0, 0)

time_diff = end_time - start_time
print(time_diff)


# Time delta

td = datetime.timedelta(hours=2)
time1 = datetime.datetime(2023, 3, 27, 10, 30)
new_time = time1 + td
print(new_time)
