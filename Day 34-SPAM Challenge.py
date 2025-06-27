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

def spam():
  os.system("clear")
  n = len(listofEmail[0:10])
  for index in range(n):
    print(f"\033[31mDear {listofEmail[index]},\033[0m\n")
    print("It has come to our attention that you're missing out on the\n")
    print("amazing \033[34mReplit 100 days of code\033[0m. We insist you do it right\n")
    print("away. If you don't we will pass on your email address to every\n")
    print("spammer we've ever encountered and also sign you up to the My\n")
    print("Little Pony newsletter, because that's neat. We might just do\n")
    print("that anyway.\n")
    print()
    print("\033[33mLove and hugs,\n")
    print("Ian Spammington III\033[0m")
    time.sleep(3)
    os.system("clear")
    

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
  elif menu == "4":
    spam()
  time.sleep(1)
  os.system("clear")
  