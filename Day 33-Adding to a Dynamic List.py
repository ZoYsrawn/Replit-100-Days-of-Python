import os, time

myAgenda = []

def printList():
  print()
  for item in myAgenda:
    print(item)
  print()
  time.sleep(1)
  
    

while True:
  item = input("What's next on our agenda? > ")
  myAgenda.append(item)
  printList()
  os.system("clear")
  
