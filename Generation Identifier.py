print("GENERATION IDENTIFIER")
print("WELCOME to you very own generation identifier!")
print("---------------------------------------------------------------")
print("This program will tell you what generation you are based on the year you were born.")
print()
print()
print("Let's do this!")
print()
print()


year = int(input("What year were you born? "))
print()
if year < 1925:
  print("Sorry. We don't have a generation for you yet.")
  exit()
else:
  if year >= 1925 and year <= 1946:
      print("You are a Traditionalist 💀")
      print("Wow, you guys still exist?!. Welcome to the world of the internet!")
  elif year >= 1947 and year <= 1964:
      print("You are a Baby Boomer 👵")
      print("Generally less familiar with emojis and their nuances!")
  elif year >= 1965 and year <= 1980:
      print("You are a Generation X 👦")
      print("You are the first generation to grow up with computers and the internet!")
  elif year >= 1981 and year <= 1996:
      print("You are a Millenial ✨ · 🌱")
      print("Ah, the avocado toast 🥑 and starbucks generation! Expensive Coffee Is Their Caviar.")
  elif year >= 1997 and year <= 2012:
      print("You are a Generation Z 👦")
      print("Weirdly Short Attention Span, Always Connected, and Always Online")
      print("You are the first generation to grow up with smartphones and social media!")
  else:
      print("You are a Generation Alpha 👶")
      print("Weirdly obsessed with looks and TikTok")
    
