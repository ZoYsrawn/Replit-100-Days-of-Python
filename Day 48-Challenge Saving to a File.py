print("🌟HIGH SCORE TABLE🌟")
print()
print()
file = open("high.score", "a+")
while True:
  inputname = input("Input your initials (all cap) > ").upper()
  inputscore = input("Input your score > ")
  file.write(f"{inputname}  {inputscore}\n")
  print("\nAdded!")
  print()
  menu = input("Add another? y/n")
  if menu.strip().lower() == "n":
    file.close()
    break
  else:
    continue
  
