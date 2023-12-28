print("Hello, Welcome to world of", "\033[35m","Avatar!!","\033[0m")
print()
print("As we know Fire, Water, Earth & Air are the elements of the nature, What do you like the most?")
print("Press 1 for Fire, 2 for Water, 3 for Earth & 4 for Air")
Bender = input("What do you like the most? ")
if Bender == "1":
  print("Wow! You are a","\033[31m","Fire bender!")
elif Bender == "2":
  print("Wow! You are a","\033[34m","Water bender!")
elif Bender == "3":
  print("Wow! You are a","\033[38;2;165;42;42m","Earth bender!")
elif Bender == "4":
  print("Wow! You are a","\033[37m","Earth bender!")
else:
  print("\033[0m","You did not choose any of the option, try again!")
