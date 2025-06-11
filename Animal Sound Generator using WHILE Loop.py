print("Alexa! PLAY SOME ANIMAL SOUNDS!")
print()

exit = ""
while exit != "yes":
  a = input("Which animal sound do you want to hear?  ")
  if a == "Cow" or a == "cow":
    print("A", a, "goes moo!")
    print("Cute, isn't it?")
    exit = input("Do you want to exit?  ")
  elif a == "Dog" or a == "dog":
    print("Ummm.......a", a, "goes woof!")
    print("Looks like he want to play!")
    exit = input("Do you want to exit?  ")
  elif a == "Cat" or a == "cat":
    print("A", a, "goes meow!")
    print("He is such a fun cutie!")
    exit = input("Do you want to exit?  ")
  elif a == "Sheep" or a == "sheep":
    print("A", a, "goes baa!")
    print("He is a sport!")
    exit = input("Do you want to exit?  ")
  elif a == "Chicken" or a == "chicken":
    print("A", a, "goes cluck!")
    print("Want some eggs?")
    exit = input("Do you want to exit?  ")
  elif a == "Duck" or a == "duck":
    print("A", a, "goes quack!")
    print("Hahahahahaha")
    exit = input("Do you want to exit?  ")
  elif a == "Goat" or a == "goat":
    print("A", a, "goes baa!")
    print("He is such a fun cutie!")
    exit = input("Do you want to exit?  ")
  else:
    print("Sorry, I don't know that animal sound.")
    exit = input("Do you want to exit?  ")
  