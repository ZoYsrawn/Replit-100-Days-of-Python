import time
import os

print("🌠  2D Dictionaries  🌠")

clue = {}

def prettyPrint():
  print()
  for key, value in clue.items():
    print(key, end=": ")
    for subkey, subvalue in value.items():
      print(subkey, subvalue, end=" | ")
    print()
    

while True:
  name = input("What's the name:\n>")
  location = input("State the location:\n>")
  weapon = input("What's the weapon called:\n>")
  clue[name] = {"location" : location, "weapon" : weapon}
  prettyPrint()
  time.sleep(1)
  os.system("clear")