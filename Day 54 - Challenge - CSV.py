import csv

with open("Day54Totals.csv") as file:
  reader = csv.DictReader(file)
  total = 0.0
  for row in reader:
    total += ((float(row["Cost"])) * (int(row["Quantity"])))
    
  print("🌟Shop $$ Tracker🌟")
  total = round(total, 2)
  print(f"Your shop took £{total} pounds today.")
    