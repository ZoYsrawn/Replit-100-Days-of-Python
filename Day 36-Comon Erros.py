#Common Errors

#Order matters

myList = []


def printList():
  print()
  for i in myList:
    print(i)
  print()


while True:
  addItem = input("Item > ").capitalize().strip()
  if addItem not in myList:
    myList.append(addItem)
  printList()

#VERSUS

# while True:
#   addItem = input("Item > ").strip().capitalize()
#   if addItem not in myList:
#     myList.append(addItem)
#   printList()
