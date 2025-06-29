print(" R O L O D E X   N A M E   L I S T ")
print()

myRolodex = []


def printList():
  for item in myRolodex:
    print(item)
  print()


while True:
  firstname = input("Enter the first name > ").strip().title()
  surname = input("Enter the surname > ").strip().title()
  name = f"{firstname} {surname}"
  print("THE NAME IS ", name)
  if name not in myRolodex:
    myRolodex.append(name)
  else:
    print("ERROR : Duplicate Name")
  printList()
