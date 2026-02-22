from datetime import timedelta, datetime

current_date = datetime.now()
five_days_ago = current_date - timedelta(days=5)
print("Current date:", current_date)
print("Date 5 days ago:", five_days_ago, "\n")