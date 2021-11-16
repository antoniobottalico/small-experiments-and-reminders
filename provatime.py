import datetime

def currentTime():
  print("Current date and time : ")
  today = datetime.datetime.strftime(datetime.datetime.today() , '%d/%m/%Y-%Hh/%Mm')
  print(today)

oneDayLater = datetime.datetime.today() + datetime.timedelta(days = 1)
currentTime()
print("Time after one day : ")
print(datetime.datetime.strftime(oneDayLater , '%d/%m/%Y-%Hh/%Mm'))


fourWeeksLater = datetime.datetime.today() + datetime.timedelta(weeks = 4)
print("")
currentTime()
print("Time after four weeks : ")
print(datetime.datetime.strftime(fourWeeksLater , '%d/%m/%Y-%Hh/%Mm'))


oneHourLater = datetime.datetime.today() + datetime.timedelta(hours = 72)
print("")
currentTime()
print("Time after 72 hour : ")
print(datetime.datetime.strftime(oneHourLater , '%d/%m/%Y-%Hh/%Mm'))


minutesLater = datetime.datetime.today() + datetime.timedelta(minutes = 15)
print("")
currentTime()
print("Time after 15 minutes : ")
print(datetime.datetime.strftime(minutesLater , '%d/%m/%Y-%Hh/%Mm'))


imposta_data = datetime.datetime(2021,10,5,20,40)
print(imposta_data)
data=imposta_data - datetime.timedelta(hours = 72)
print(data)

