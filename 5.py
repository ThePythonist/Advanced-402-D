from persiantools.jdatetime import JalaliDateTime
import pytz
import jdatetime

now = jdatetime.datetime.now()
day = now.day
month = now.month
year = now.year

today = JalaliDateTime(year, month, day, 0, 0, 0, 0, pytz.utc).strftime("%A")
print(today)
