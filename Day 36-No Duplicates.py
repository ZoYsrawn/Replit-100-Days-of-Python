myList = []


def printList():
  print()
  for i in myList:
    print(i)
  print()


while True:
  addItem = input("Item > ")
  if addItem not in myList:
    myList.append(addItem)
  printList()

#VERSUS

# myList = []

# def printList():
#   print()
#   for i in myList:
#     print(i)
#   print()

# while True:
#   addItem = input("Item > ").capitalize().strip()
#   if addItem not in myList:
#     myList.append(addItem)
#   printList()
