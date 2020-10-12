import datetime
import calendar


x = datetime.datetime.now()
a=x.year
year = a
b= x.strftime("%m")
month = int(b)

print(calendar.month(year,month))
