import time
import os


def prettyPrint():
  for row in toDo:
    for item in row:
      print(f"{item: ^10}", end="  |  ")
    print()
  print()

toDo = []

while True:
  print("ToDO List Management System")
  print()
  print()
  menu = input("1:  Add\n2:  View\n3:  Remove\n4:  Edit\n>")
  if menu.strip().lower() == "add" or menu.strip().lower() =="1":
    what = input("What the to-do is >")
    when = input("When it is due >")
    priority = input("What's the priority (high, medium, or low) >")
    row = [what, when, priority]
    toDo.append(row)
  elif menu.strip().lower() == "view" or menu.strip().lower() =="2":
    view1 = input("1:  View all\n2:  View priority\n>")
    if view1.strip().lower() == "1" or view1.strip().lower() == "view all":
      prettyPrint()
    else:
      view2 = input("What's the priority >")
      if view2.strip().lower() == "high":
        for row in range(len(toDo)):
          for item in range(len(toDo[row])):
            if toDo[row][item] == "high":
              print(toDo[row])
      elif view2.strip().lower() == "medium":
        for row in range(len(toDo)):
          for item in range(len(toDo[row])):
            if toDo[row][item] == "medium":
              print(toDo[row])
      elif view2.strip().lower() == "low":
        for row in range(len(toDo)):
          for item in range(len(toDo[row])):
            if toDo[row][item] == "low":
              print(toDo[row])
  
  elif menu.strip().lower() == "edit" or menu.strip().lower() =="4":
    ask = input("What do you want to edit >")
    ask2 = input ("What to do you want to edit it with >")
    for row in range(len(toDo)):
      for item in range(len(toDo[row])):
        if ask in toDo[row][item]:
          toDo[row][item] = ask2
        else:
          print("Such an item does not exit in the list!")
  
  elif menu.strip().lower() == "remove" or menu.strip().lower() =="3":
    ask = input("Are you sure?")
    if ask.strip().lower() == "y":
      toDo.clear()
    else:
      prettyPrint()


  time.sleep(1)
  os.system("clear")






