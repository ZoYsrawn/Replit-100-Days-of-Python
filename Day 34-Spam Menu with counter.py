import os
import time
listofEmail = []

def prettyPrint():
  os.system("clear")
  print("listofEmail")
  print()
  counter = 1
  for email in listofEmail:
    print(f"{counter}: {email}")
    counter += 1
  time.sleep(1)
    

while True:
  print("SPAMMER Inc.")
  menu = input("1: Add email\n2: Remove email\n3: Show emails\n4: Get SPAMMING\n> ")
  if menu == "1":
    email = input("Add email: ")
    listofEmail.append(email)
  elif menu == "2":
    email = input("Email to remove: ")
    if email in listofEmail:
      listofEmail.remove(email)
  elif menu == "3":
    prettyPrint()
  time.sleep(1)
  os.system("clear")
  