from datetime import datetime

date_format = "%Y-%m-%d %H:%M:%S"
date_str1 = input("Enter the first date in format 'YYYY-MM-DD HH:MM:SS': ")
date_str2 = input("Enter the second date in format 'YYYY-MM-DD HH:MM:SS': ")


date1 = datetime.strptime(date_str1, date_format)
date2 = datetime.strptime(date_str2, date_format)

difference = date2 - date1
seconds_difference = difference.total_seconds()

print("Date Difference in Seconds:", seconds_difference)

