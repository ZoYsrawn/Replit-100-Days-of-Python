import random, os, time

idea = [] #create a separate container for loading up random stuff
while True:
  print("IDEAS")
  print()
  print()
  print("1: Add an Idea\n2: Load up a random idea")
  print()
  menu = input("> ").strip()
  if menu == "1":
    os.system("clear")
    giveidea = input("Idea: > ")
    idea.append(giveidea)
    f = open("my.idea", "a")
    f.write(giveidea)
    f.close()
  elif menu == "2":
    os.system("clear")
    f = random.choice(idea)
    print(f)
    print(idea)
  time.sleep(1)
  os.system("clear")