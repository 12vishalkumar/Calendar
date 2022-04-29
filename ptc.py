# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar
import datetime
d, m, y = map(int, input().split())
D = datetime.date(y, d, m)
print(calendar.day_name[D.weekday()].upper()) 