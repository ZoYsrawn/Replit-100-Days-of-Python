import time, os

inventory = []

def viewItem():
  time.sleep(1)
  os.system("clear")
  seen = set(inventory)
  for item in seen:
    print(f"{item} {inventory.count(item)}")

def addItem():
  time.sleep(1)
  os.system("clear")
  item = input("Input what needs to be added:").capitalize()
  inventory.append(item)

while True:
  time.sleep(1)
  os.system("clear")
  print("SET TESTER")
  print()
  print("----------")
  menu = input("1: Add\n2: View\n>")
  if menu == "1":
    addItem()
  else:
    viewItem()
    


