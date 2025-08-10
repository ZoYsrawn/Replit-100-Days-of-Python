import csv # Imports the csv library

with open("January.csv") as file: 
  reader = csv.DictReader(file) # Treats the file as a dictionary 
  line = 0
  for row in reader: 
    print (row["Net Total"])