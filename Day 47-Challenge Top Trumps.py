import random
import time
import os

print("🌟  T O P   T R U M P S  🌟")
print("------------------------------")
print()
print()

simpson = {"Intelligence": 45, "Speed": 55, "Guile": 33, "Might": 61}
monica = {"Intelligence": 56, "Speed": 30, "Guile": 78, "Might": 20}
professor = {"Intelligence": 98, "Speed": 32, "Guile": 91, "Might": 41}
superman = {"Intelligence": 80, "Speed": 93, "Guile": 85, "Might": 98}
batman = {"Intelligence": 98, "Speed": 71, "Guile": 83, "Might": 77}
thor = {"Intelligence": 59, "Speed": 92, "Guile": 58, "Might": 99}
blackwidow = {"Intelligence": 55, "Speed": 67, "Guile": 77, "Might": 69}
ironman = {"Intelligence": 90, "Speed": 55, "Guile": 88, "Might": 80}

Characters = {"Mr. Simpson":simpson, "Monica from Friends":monica, "Professor X":professor,
             "Superman":superman, "Batman":batman, "Thor, Son of Odin":thor, "Black Widow":blackwidow,
             "Iron Man": ironman}

while True:
  print("Characters\n\n")
  for key in Characters:
    print(key)
  
  # Define ANSI color codes
  COLOR_RED = "\033[31m"
  COLOR_GREEN = "\033[32m"
  COLOR_RESET = "\033[0m"

  your_selection = input(f"\nPick your character\n> {COLOR_GREEN}")
  print()
  random_select = random.choice(list(Characters.keys()))
  print()
  while random_select == your_selection:
    random_select = random.choice(list(Characters.keys()))
  
  print(f"You picked: {your_selection}{COLOR_RESET}")
  print()
  print(f"Computer has picked {random_select}")
  print()



  
  
  cc = 0
  myc = 0
  stats = input("Choose your stat:\n1:  Intelligence\n2:  Speed\n3:  Guile\n4: Might\n>")
  if stats.strip() == "1":
    print(f'{your_selection}: has an Intelligence stat of {Characters[your_selection]["Intelligence"]}')
    print(f'{random_select}: {Characters[random_select]["Intelligence"]}')
    if Characters[random_select]["Intelligence"] > Characters[your_selection]["Intelligence"]:
      print("\nComputer wins!")
      cc +=1
    elif Characters[random_select]["Intelligence"] == Characters[your_selection]["Intelligence"]:
      print("\nIt is a big fat tie!")
    else:
      print(f"\n{your_selection} wins!")
      myc +=1

  elif stats.strip() == "2":
    print(f'{your_selection}: has a Speed stat of {Characters[your_selection]["Speed"]}')
    print(f'{random_select}: {Characters[random_select]["Speed"]}')
    if Characters[random_select]["Speed"] > Characters[your_selection]["Speed"]:
      print("\nComputer wins!")
      cc +=1
    elif Characters[random_select]["Speed"] == Characters[your_selection]["Speed"]:
      print("\nIt is a big fat tie!")
    else:
      print(f"\n{your_selection} wins!")
      myc +=1

  elif stats.strip() == "3":
    print(f'{your_selection}: has a Guile stat of {Characters[your_selection]["Guile"]}')
    print(f'{random_select}: {Characters[random_select]["Guile"]}')
    if Characters[random_select]["Guile"] > Characters[your_selection]["Guile"]:
      print("\nComputer wins!")
      cc +=1
    elif Characters[random_select]["Guile"] == Characters[your_selection]["Guile"]:
      print("\nIt is a big fat tie!")
    else:
      print(f"\n{your_selection} wins!")
      myc +=1

  elif stats.strip() == "4":
    print(f'{your_selection}: has a Might stat of {Characters[your_selection]["Might"]}')
    print(f'{random_select}: {Characters[random_select]["Might"]}')
    if Characters[random_select]["Might"] > Characters[your_selection]["Might"]:
      print("\nComputer wins!")
      cc +=1
    elif Characters[random_select]["Might"] == Characters[your_selection]["Might"]:
      print("\nIt is a big fat tie!")
    else:
      print(f"\n{your_selection} wins!")
      myc +=1

  else:
    print("Woefully wrong selection, try again")

  time.sleep(3)
  os.system("clear")
  menu = input("AGAIN? (y/n) > ")
  if menu.strip().lower() == "y":
    os.system("clear")
    continue
  else:
    break

if myc > cc:
  print(f"You won {myc} times!")
elif myc == cc:
  print("WOW, this is a tie!!!")
elif myc < cc:
  print(f"The computer won {cc} times!")
else:
  print("DO NOT KNOW WHAT's HAPPENING")