import random

def roll(sides):
 a=random.randint(1,sides)
 print(a)

print("!Welcome to Roll a dice!")
print()
print("Choose how many sides you want your dice to have")
sides=int(input(">:"))
while True:
  print("You rolled the dice:")
  roll(sides)
  print("Do you want to roll again?(Y/N)")
  b=input(">:").lower()
  if b=="y":
    roll(sides)
    continue
  else:
    break
print(f"Thanks for playing!")
