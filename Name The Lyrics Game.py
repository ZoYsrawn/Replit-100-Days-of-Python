print("N A M E   T H E   L Y R I C S")
print()
print("Fill in the blank lyrics!")
print("Type in the blank lyrics and see if you are as cool as me.")
print()
print()

counter = 1
while True:
  print("Every night in my dreams I ________ you.")
  answer = input(" > ")
  if answer != "see":
    print("Nope, try again.")
    counter += 1
  else:
    print("You got it!")
    break
print("Well done! It only took you",counter, "attempts.")
if counter == 1:
  print("Congratulations! You got it on your first try!")