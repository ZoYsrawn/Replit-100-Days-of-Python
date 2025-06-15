print("MATH GAME!")
print("-----------")
print()
print("Let's play a game and test your math skills!")
print()

score = 0
mul = int(input("Name your multiples: "))
for i in range(1, 11):
  print(i, "x", mul, "= ")
  x = int(input(""))
  if x == i * mul:
    print("Greak Work!")
    score += 1
  else:
    print("Nope. The answer was", i * mul)

if score == 10:
  print("🥳 🥳 🥳 You got all of them right! 🎉 🎉 🎉 🥳 🥳 🥳")
  print("That was a perfect score. You scored", score, "out of 10.")
else:
  print("You scored", score, "out of 10.")
