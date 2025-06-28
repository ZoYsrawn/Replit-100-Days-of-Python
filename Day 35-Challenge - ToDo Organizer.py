import os, time

toDoList = []


def printList():
  print()
  for index in range(len(toDoList)):
    print(f"{index+1}:  {toDoList[index]}")
  print()


while True:
  menu = input(
      "\033[34mTo-DoList Manager\033[0m\n\nDo you want to view, add, edit, delete, or remove the todo list?\n> "
  )
  if menu == "view":
    printList()
    time.sleep(1)
    os.system("clear")
  elif menu == "add":
    print()
    item = input("What do you want to add?\n").title()
    if item in toDoList:
      print("ITEM ALREADY IN THERE")
    else:
      toDoList.append(item)
  elif menu == "remove":
    print()
    item = input("What do you want to remove?\n").title()
    if item in toDoList:
      print(f"Is this the item they really want to remove? '{item}'")
      yesno = input("> ")
      if yesno == "yes":
        toDoList.remove(item)
      else:
        print("SURE!")
  elif menu == "edit":
    print()
    a = input("What do you want to edit to change? > ").title()
    if a in toDoList:
      b = input("What do you want to change it to? > ").title()
      position = toDoList.index(a)
      toDoList[position] = b
    else:
      print("NO SUCH ITEM IN THERE")
  elif menu == "delete":
    toDoList.clear()
  time.sleep(1)
  os.system("clear")
