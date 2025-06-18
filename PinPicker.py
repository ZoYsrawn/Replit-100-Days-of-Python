print("This is a pin picker")
print("---------------------")

def pinPicker(number):
  import random
  pin = ""
  for i in range(number):
    pin += str(random.randint(0,9))
  return pin

are = pinPicker(3)
print(are)