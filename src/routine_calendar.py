import calendar
from datetime import datetime


class Period():
    def __init__(self):
        pass
    

actual_year = datetime.now().year
actual_month = datetime.now().month
actual_day = datetime.now().day

#print(calendar.month(actual_year, actual_month))
print(calendar.week(5, 5))
