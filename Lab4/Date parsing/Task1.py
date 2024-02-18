from datetime import datetime, timedelta

current_date = datetime.now()

subtracted_date = current_date - timedelta(days=5)

print("Current Date:", current_date.strftime("%Y-%m-%d"))
print("Subtracted Date:", subtracted_date.strftime("%Y-%m-%d"))

#Current Date: 2024-02-18
#Subtracted Date: 2024-02-13