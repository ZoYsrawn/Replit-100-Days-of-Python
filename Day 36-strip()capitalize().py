print("NO DUPLICATES")

myList = []


def printList():
  for item in myList:
    print(item)
  print()


while True:
  additem = input("What do you want to add > ").strip().capitalize()
  if additem not in myList:
    myList.append(additem)
  printList()
