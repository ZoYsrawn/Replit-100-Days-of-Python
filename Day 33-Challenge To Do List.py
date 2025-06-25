import time, os

myList = []

def printList():
  print()
  for item in myList:
    print("\033[34m",item, "\033[0m")
  print()
  

while True:
  message = "\033[1m \033[31m To Do List Manager \033[0m: "
  print(f"{message: ^100}")
  print()
  menu = input("Do you want to view, add, or edit your to do list? >  ")
  if menu == "view":
    printList()
    time.sleep(2)
    os.system("clear")
  elif menu == "add":
    item = input("What do you want to add? >  ")
    myList.append(item)
    printList()
    time.sleep(1)
    os.system("clear")
  elif menu == "edit":
    item = input("What have you completed and seek to edit out? >  ")
    if item in myList:
      myList.remove(item)
      printList()
      time.sleep(1)
      os.system("clear")
    else:
      print(f"🚨 {item} is not present in your List! 🚨")