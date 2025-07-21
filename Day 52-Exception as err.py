myStuff = []

try:
  f.open("Stuff.mine", "r")
  myStuff = eval(f.read())
  f.close()
# Try to find a file called 'Stuff.mine' and open it

except Exception as err:
  print("ERROR: Unable to load")
  print(err)

for row in myStuff:
  print(row)
