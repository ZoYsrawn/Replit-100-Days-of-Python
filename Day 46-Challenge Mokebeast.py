print("🌠  🌟 MokeBeast Generator 🌟  🌠")
print()

mokebeast = {}

def prettyPrint():
  for key, value in mokebeast.items():
    print("name: ",key, end="  |  ")
    for subkey, subvalue in value.items():
      print(subkey, subvalue, end="  |  ")
    print()


while True:
  name = input("Input the beast name >")
  print()
  element = input("Input the beast element >")
  print()
  move = input("Input the beast special move >")
  print()
  hp = input("Input the beast starting HP >")
  print()
  mp =input("Input the beast starting MP >")
  print()
  again = input("Again y/n >")

  mokebeast[name] = {"element":element, "move":move, "HP":hp, "MP":mp}
  prettyPrint()

  if again.strip().lower() == "n":
    break
  else:
    continue
  
