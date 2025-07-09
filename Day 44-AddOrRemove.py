listOfShame = [] 
# Creates an empty list.

def prettyPrint():
  print()
  for row in listOfShame:
    for item in row:
      print(f"{item: ^10}", end="  |  ")
    print()
  print()

while True:
  menu = input("Add or Remove?")
  if menu.strip().lower() == "a":
    # Starts a never ending loop (until we end it)
    name = input("What is your name? ")
    age = input("What is your age? ")
    pref = input("What is your computer platform? ")
    # Get the user input.
  
    row = [name, age, pref] 
    # Assigns the 3 variables into a single row.
  
    listOfShame.append(row) 
    # Adds the contents of the row variable at the end of the list

  else:
    name = input("What is the name of the record you want to delete? >")
    for row in listOfShame:
      if name in row:
        listOfShame.remove(row)
        
  prettyPrint() 