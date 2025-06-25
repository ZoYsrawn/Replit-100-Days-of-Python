import os, time

myAgenda = []

def printList():
  print()
  for item in myAgenda:
    print(item)
  print()
  time.sleep(1)
  os.system("clear")

while True:
  menu = input("What do you want to do: add or remove? > ")
  if menu == "add":
    item = input("What's next on the Agenda? > ")
    myAgenda.append(item)
  elif menu == "remove":
    item = input("What is it that you seek to remove? > ")
    myAgenda.remove(item)

  printList()
  
