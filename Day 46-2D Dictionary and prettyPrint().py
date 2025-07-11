print("🌠  2D Dictionaries  🌠")

clue = {}

def prettyPrint():
  print()
  for key, value in clue.items():
    print(key, value)
  print()

while True:
  name = input("What's the name:\n>")
  location = input("State the location:\n>")
  weapon = input("What's the weapon called:\n>")
  clue[name] = {"location" : location, "weapon" : weapon}
  prettyPrint()