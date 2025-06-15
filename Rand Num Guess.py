import random

print("#️⃣ 🧮 GUESS THE NUMBER 🧮 #️⃣")
print()
print("Welcome to Guess the Number.")
print()
print(
    "Guess a number between 1 and 1,000,000 and I will tell you if you are too low, too high, or get it correct."
)
print()
print("Let's play!")

correct_number = random.randint(1, 5)
attempt = 1

while True:
  user_guess = int(input("Pick a number between 1 and 1,000,000: "))
  if user_guess < 0:
    print("Now we'll never know what the answer is …")
    exit()
  if user_guess < correct_number:
    print("That number is too low. Try again!")
    attempt += 1
  elif user_guess > correct_number:
    print("That number is too high. Try again!")
    attempt += 1
    continue
  elif user_guess == correct_number:
    print("You are a winner! 🥳🥳")
    break
  else:
    print("That is not a number I recognize.")
print("It took you", attempt, "attempt(s) to get the correct answer.")
