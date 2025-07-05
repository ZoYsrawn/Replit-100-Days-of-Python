print("👾 MokéBeast - The Non-Copyright Generic Beast Battle Game 👾")

mokedex = {"name" : None, "type" : None, "special move" : None, "HP" : None, "MP" : None}

for name, value in mokedex.items():
  mokedex[name] = input(f"{name} :\t").strip().title()
print()
print()


if mokedex["type"] == "Fire":
  print("\033[31m", end="")
elif mokedex["type"] == "Water":
  print("\033[95m", end="")
elif mokedex["type"] == "Air":
  print("\033[34m", end="")
elif mokedex["type"] == "Spirit":
  print("\033[32m", end="")
elif mokedex["type"] == "Earth":
  print("\033[33m", end="")

for name, value in mokedex.items():
  print(f"{name}: {mokedex[name]}")