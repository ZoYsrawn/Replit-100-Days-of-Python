from getpass import getpass as input

print("E P I C    🪨  📄 ✂️    B A T T L E ")
print()
print("Select your move (R, P or S)")
print()

p1score = 0
p2score = 0

while True:
  player1Move = input("Player 1 > ")
  print()
  player2Move = input("Player 2 > ")
  print()

  if player1Move == "R":
    if player2Move == "R":
      print("You both picked Rock, draw!")
    elif player2Move == "S":
      print("Player1 smashed Player2's Scissors into dust with their Rock!")
      p1score += 1
    elif player2Move == "P":
      print("Player1's Rock is smothered by Player2's Paper!")
      p2score += 1
    else:
      print("Invalid Move Player 2!")
  elif player1Move == "P":
    if player2Move == "R":
      print("Player2's Rock is smothered by Player1's Paper!")
      p1score += 1
    elif player2Move == "S":
      print("Player1's Paper is cut into tiny pieces by Player2's Scissors!")
      p2score += 1
    elif player2Move == "P":
      print("Two bits of paper flap at each other. Dissapointing. Draw.")
    else:
      print("Invalid Move Player 2!")
  elif player1Move == "S":
    if player2Move == "R":
      print("Player 2's Rock makes metal-dust out of Player1's Scissors")
      p2score += 1
    elif player2Move == "S":
      print(
          "Ka-Shing! Scissors bounce off each other like a dodgy sword fight! Draw."
      )
    elif player2Move == "P":
      print("Player1's Scissors make confetti out of Player2's paper!")
      p1score += 1
    else:
      print("Invalid Move Player 2!")
  else:
    print("Invalid Move Player 1!")

  print("Player 1 has", p1score, "points")
  print("Player 2 has", p2score, "points")
  print()

  if p1score == 3 or p2score == 3:
    print("Game Over! Thanks for playing!")
    exit()
  else:
    continue
