import random, os, time

def add():
  os.system("clear")
  giveidea = input("Idea: > ")
  f = open("my.ideas", "a+")
  f.write(f"{giveidea}\n")
  f.close()
  time.sleep(1)
  os.system("clear")

def show():
  os.system("clear")
  f = open("my.ideas", "r")
  ideas = f.read().split("\n")
  f.close()
  ideas.remove("")
  idea = random.choice(ideas)
  print(idea)
  time.sleep(2)
  os.system("clear")

while True:
  print("IDEAS")
  print()
  print()
  print("1: Add an idea\n2: Load up a random idea")
  print()
  menu = input("> ")
  if menu == "1":
    add()
  elif menu == "2":
    show()
  else:
    print("Wrong Input")
  