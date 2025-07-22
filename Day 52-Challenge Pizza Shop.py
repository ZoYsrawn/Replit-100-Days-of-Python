import time, os

myOrder = []

try:
  f = open("pizza.txt", "r")  # Only need read permissions here
  myOrder = eval(f.read())
  f.close()
except:
  print("Unable to Load")


def prettyPrint():
  for row in myOrder:
    print(f"{row[0] :^10}  {row[1] :^10}  {row[2] :^10}  {row[3] :^10}")
  print()


while True:
  print()
  print("🌟Sominoe's Dodgy Pizzas🌟")
  print()
  print()
  print("1: Add Pizza\n2: View Pizza")
  menu = input("> ")
  if menu == "1":
    os.system("clear")
    name = input("Name of the patron: ")
    toppings = input("Toppings: ")
    size = input("Size (s/m/l): ")
    row = [name, toppings, size]
    print(row)
    while True:
      try:
        quantity = int(input("Quantity: "))
        row.append(str(quantity))
        print()
      except:
        print("You must input a numerical character, try again.")
        continue
      else:
        myOrder.append(row)
        break
    if size == "s":
      prize = quantity * 9.99
      print(f"\nThanks {name} your pizzas will cost {prize}")
    elif size == "m":
      prize = quantity * 14.99
      print(f"\nThanks {name} your pizzas will cost {prize}")
    else:
      prize = quantity * 19.99
      print(f"\nThanks {name} your pizzas will cost {prize}")
    prettyPrint()
    time.sleep(2)
    os.system("clear")

    f = open("pizza.txt", "w")
    f.write(str(myOrder))
    f.close()

  elif menu == "2":
    prettyPrint()
    time.sleep(1)
    os.system("clear")
