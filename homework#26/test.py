import time
import datetime

s = "11-12-1986"
d = datetime.datetime.strptime(s, "%d-%m-%Y")
f = datetime.date.today()
print(f, d)

#datetime.date.year()
tt = d.timetuple()
tp = f.timetuple()
print(tt[0], tt[1], tt[3])