myStuff = []

try:
  f.open("Stuff.mine", "r")
  myStuff = eval(f.read())
  f.close()
# Try to find a file called 'Stuff.mine' and open it

except:
  print("ERROR: Unable to load")
# If the file can't be found, show the error instead of crashing the whole program

for row in myStuff:
  print(row)
