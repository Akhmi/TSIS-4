from datetime import datetime

current_datetime = datetime.now()

current_datetime_without_microseconds = current_datetime.replace(microsecond=0)

print("Datetime without microseconds:", current_datetime_without_microseconds)

#Datetime without microseconds: 2024-02-18 23:11:49