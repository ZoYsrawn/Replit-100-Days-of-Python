print("🌠  2D Dictionaries  🌠")

clue = {}

while True:
  name = input("What's the name:\n>")
  location = input("State the location:\n>")
  weapon = input("What's the weapon called:\n>")
  clue[name] = {"location" : location, "weapon" : weapon}
  print(clue)