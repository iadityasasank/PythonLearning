from getpass import getpass as input

print("E P I C    🪨  📄 ✂️    B A T T L E ")
print()

P1_S = 0
P2_S = 0

while True:
  print("Select your move (R, P or S)")
  print()

  player1Move = input("Player 1 > ").lower()
  print()
  player2Move = input("Player 2 > ").lower()
  print()

  if player1Move == "r":
    if player2Move == "r":
      print("You both picked Rock, draw!")
    elif player2Move == "s":
      print("Player1 smashed Player2's Scissors into dust with their Rock!")
      P1_S += 1
    elif player2Move == "p":
      print("Player1's Rock is smothered by Player2's Paper!")
      P2_S += 1
    else:
      print("Invalid Move Player 2!")

  elif player1Move == "p":
    if player2Move == "r":
      print("Player2's Rock is smothered by Player1's Paper!")
      P1_S += 1
    elif player2Move == "s":
      print("Player1's Paper is cut into tiny pieces by Player2's Scissors!")
      P2_S += 1
    elif player2Move == "p":
      print("Two bits of paper flap at each other. Dissapointing. Draw.")
    else:
      print("Invalid Move Player 2!")

  elif player1Move == "s":
    if player2Move == "r":
      print("Player 2's Rock makes metal-dust out of Player1's Scissors")
      P2_S += 1
    elif player2Move == "s":
      print("Ka-Shing! Scissors bounce off each other like a dodgy sword fight! Draw.")
    elif player2Move == "p":
      print("Player1's Scissors make confetti out of Player2's paper!")
      P1_S += 1
    else:
      print("Invalid Move Player 2!")

  else:
    print("Invalid Move Player 1!")

  # Check for win conditions after all other logic
  if P1_S >= 3:
    print("Player 1 wins with", P1_S, "points")
    break
  elif P2_S >= 3:
    print("Player 2 wins with", P2_S, "points")
    break
  else: 
    continue # Skip to the next round if neither player won
