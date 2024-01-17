seconds = 1
minutes = seconds *60
hours = minutes *60

days = hours *24
weeks = days *7
leapYear = input("Is it a leap year?")
if leapYear == "yes" or leapYear == "Yes":
  year = (weeks*52) + (days)
else:
  year = (weeks*52)
print("Seconds: ", year)