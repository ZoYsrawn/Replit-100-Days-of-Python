sentence = input("\033[33mWhat sentence do you want rainbow-ising? >\033[0m\n")
print(f"\033[32m{sentence: <5}\033[0m")
print()

def printColor(text):
  if text == "r":
    print("\033[31m", end="")
  elif text == "b":
    print("\033[34m", end="")
  elif text == "g":
    print("\033[32m", end="")
  elif text == "p":
    print("\033[95m", end="")
  elif text == "y":
    print("\033[33m", end="")
  elif text == " ":
    print("\033[0m", end="")


for letter in sentence:
  printColor(letter.lower())
  print(letter, end="")
print()
  


