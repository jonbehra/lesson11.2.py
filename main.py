import datetime
current_datetime = datetime.datetime.now()

print(current_datetime)

print("Year:", current_datetime.year)
print("Month:", current_datetime.month)
print("Day:", current_datetime.day)
print("Hour:", current_datetime.hour)
print("Minute:", current_datetime.minute)
print("Second:", current_datetime.second)
print("Microsecond:", current_datetime.microsecond)

current_datetime1 = datetime.datetime.now().date()
print(current_datetime1)
current_datetime1 = datetime.datetime.now().time()
print(current_datetime1)

time_object = datetime.time(12, 30, 45, 123456)
print(time_object)

time_object = datetime.date(2024, 12, 15)
print(time_object)

duration = datetime.timedelta(days=15, hours=3)
print(duration)

new_date = current_datetime + duration
print(new_date)

birthday = datetime.timedelta(days=5950, hours=4)
previous_date = current_datetime - birthday
print(previous_date)