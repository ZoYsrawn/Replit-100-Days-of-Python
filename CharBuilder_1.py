import os
import random
import time

print(" CHARACTER BUILDER ")
print()


def legend():
  character = input("Name Your Legend: >> ")
  print("Ah!", character)

  chartype = input("Character Type (Human, Elf, Wiard, Orc): >> ")
  print(chartype)
  print("A", chartype, "!")


def rollDice(sides):
  result = random.randint(1, sides)
  return result


def health():
  a = rollDice(6)
  b = rollDice(8)
  result = ((a * b) / 2) + 10
  return result


def strength():
  x = rollDice(6)
  y = rollDice(8)
  result = ((x * y) / 2) + 12
  return result


havechar = "yes"

while havechar == "yes":
  legend()
  print("HEALTH:", health())
  print("STRENGTH:", strength())
  print()
  print("MAY YOUR NAME GO INTO THE LEGEND FOREVER!")
  print()
  time.sleep(5)
  os.system('clear')
  havechar = input("Do you want to create another character? (yes/no): >> ")
  if havechar == "no":
    print("Goodbye, traveler!")
  else:
    continue
