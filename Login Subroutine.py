def login():
  while True:
    username = input("What is your username?: ")
    password = input("What is your password?: ")
    print()
    if username != "david" and password != "golslayer":
      print("Whoops! I don't recognize that username or password. Try again!")
      continue
    else:
      print("Welcome to Replit!")
      break


print("Replit Login System")
print()
login()
