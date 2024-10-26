from datetime import datetime

#current date and time
now = datetime.now()
print(now)

#Date: Jan 12, 2032 Time: 14:03
formatteddate = now.strftime("%b %d, %Y Time:%I:%M")
print(formatteddate)