def colorcoder(color, text):
  print("Super Subroutine")
  if color == "red":
    a = "\033[0;31m"
  elif color == "black":
    a = "\033[0;30m"
  elif color == "green":
    a = "\033[0;32m"
  elif color == "brown":
    a = "\033[0;33m"
  elif color == "blue":
    a = "\033[0;34m"
  elif color == "purple":
    a = "\033[0;35m"
  elif color == "cyan":
    a = "\033[0;36m"
  elif color == "yellow":
    a = "\033[1;33m"
  else:
    print("COLOR NOT FOUND")
  defcolor = "\033[0m"

  print("With my ", "\033[95m", "new program ", defcolor, "I can just call ", color,"('",text,"') ","and my subroutine will implement the changes like this >>> ", a, text, defcolor, "\n\nWith no \033[1;36m", "weird gaps", defcolor, "\n\n\033[7mEPIC", sep="")


colorcoder("green", "Mathematics is Fun")
