print("NO DUPLICATES")

myList = []


def printList():
  for item in myList:
    print(item)
  print()


while True:
  additem = input("What do you want to add > ").capitalize().strip()
  if additem not in myList:
    myList.append(additem)
  printList()
