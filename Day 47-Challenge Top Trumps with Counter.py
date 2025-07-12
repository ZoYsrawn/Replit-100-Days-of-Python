import os, time, random

trumps = {}
trumps["David"] = {
    "Intelligence": 178,
    "Speed": 4,
    "Guile": 80,
    "Baldness Level": 99
}
trumps["Mr Spock"] = {
    "Intelligence": 200,
    "Speed": 50,
    "Guile": 50,
    "Baldness Level": 0
}
trumps["Moica from Friends"] = {
    "Intelligence": 150,
    "Speed": 50,
    "Guile": 50,
    "Baldness Level": 0
}
trumps["Professor X"] = {
    "Intelligence": 250,
    "Speed": 1,
    "Guile": 200,
    "Baldness Level": 101
}
trumps["Megan"] = {
    "Intelligence": 220,
    "Speed": 122,
    "Guile": 220,
    "Baldness Level": 121
}

while True:
  print("TOP TRUMPS")
  print("----------")
  print()
  print("Characters")
  for key in trumps:
    print(key)
  print()

  user = input("Pick your player\n>")
  computer = random.choice(list(trumps.keys()))
  print(f"\nThe computer picked {computer}")
  print("Choose your stat: Intelligence, Speed, Guile, and Baldness Level")

  myc = 0
  cc = 0

  answer = input("> ")
  if trumps[user][answer] > trumps[computer][answer]:
    print("YOU WON !!!")
    myc +=1
  elif trumps[user][answer] < trumps[computer][answer]:
    print("The computer won!")
    cc +=1
  else:
    print("It is a big fat draw. Oops. BLNT")

  menu = input("Again? (y/n) > ")
  if menu.strip().lower() == "y":
    time.sleep(2)
    os.system("clear")
    continue
  else:
    break


if myc < cc:
  print(f"The computer won {cc} times!")
elif myc > cc:
  print(f"You won {myc} times!")
else:
  print("DRAW")

