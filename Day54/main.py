import csv # Imports the csv library

print("Shop $$ Tracker")

total = 0.0
with open("Day54Totals.csv") as file: 
  reader = csv.DictReader(file) 

  for row in reader: 
    total += float(row['Cost'])*int(row['Quantity'])
print (f"Total: ${int(total)}")
