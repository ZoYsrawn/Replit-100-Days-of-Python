import os, time
listofEmail = []

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
  time.sleep(1)
  os.system("clear")
  