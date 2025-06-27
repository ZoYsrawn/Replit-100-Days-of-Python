import os
import time
listofEmail = []

def prettyPrint():
  os.system("clear")
  print("listofEmail")
  print()
  for index in range(len(listofEmail)):
    print(f"\033[31m{index+1}:\033[0m \033[34m{listofEmail[index]}\033[0m")
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
  