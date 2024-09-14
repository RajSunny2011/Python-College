import datetime
import calendar as cal
x = cal.calendar(2024)
y = cal.month(2004,11)
print(x)
print(y)
c = datetime.datetime(2004,11,20)
print(c.strftime("%A"))