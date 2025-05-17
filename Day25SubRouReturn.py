import random

def rollDice(sides):
  result = random.randint(1,sides)
  return result

def roll_6_and_8():
  roll_6_sided_dice = rollDice(6)
  roll_8_sided_dice = rollDice(8)
  health = roll_6_sided_dice * roll_8_sided_dice
  return health

print("⚔️Character stats generator⚔️")


haveACharacter = "y"

while haveACharacter == "y":
  character = input("Name your warrior: ")
  print()
  health = str(roll_6_and_8())
  print("Their health is ", health,"hp")
  print()
  haveACharacter = input("Want to create another character?(Y/N)").lower()
