import random


def rollDice(number):
  while True:
    x = random.randint(1, number)
    print("You rolled ", x)
    print()
    rollagain = input("Roll again? (yes/no): ")
    if rollagain.lower() == "no":
      exit()
    elif rollagain.lower() == "yes":
      continue
    else:
      print("Invalid input. Please enter 'yes' or 'no'.")
    




print("Infinity Dice 🎲")
print("-----------------")
print()
number = int(input("How many sides?: "))

rollDice(number)

  