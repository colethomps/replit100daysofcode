import datetime

print("Event Countdown Timer")

event = input("Input the event > ")
print()
year = int(input("Input the year > "))
print()
month = int(input("Input the month > "))
print()
day = int(input("Input the day > "))
print()
today = datetime.date.today()
event_date = datetime.date(year=year, month=month, day=day)

if today == event_date:
  print(f"{event} is today!")
elif today > event_date:
  print(f"{event} was {today - event_date} ago")
else:
  print(f"{event} is in {event_date - today}")