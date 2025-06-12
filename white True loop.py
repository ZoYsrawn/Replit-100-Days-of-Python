counter = 0
while True:
  numb = int(input("Enter a number: "))
  print("ADDING IT UP!")
  counter += numb
  print("The current total is: ", counter)
  addAnother = input("Would you like to add another number? ")
  if addAnother == "no":
    break
print("The final sum is,", counter)