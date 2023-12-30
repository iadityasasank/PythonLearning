print ("Are you a superfan of 'The Big Bang Theory' or a fake fan?")
print()
print("Answer these questions to find out.")

Glasses = input("Does someone wear glasses?")
if Glasses == "yes" or Glasses=="Yes" or Glasses=="YES":
  print("Correct!")
  Number =input("In which year did Big Bang Theory aired there final season?")
  if Number=="2020":
    print("Correct!")
    print("You are a superfan!")
  else:
    print("Incorrect!")
else:
  print("Wrong!")
  WhoGlasses = input("Check who wears glasses and enter the characters name: ")
  if WhoGlasses == "Leonard" or WhoGlasses =="leonard" or WhoGlasses=="LEONARD":
    print("You got it")
  else:
    print("Try again!")
    Number =input("In which year did Big Bang Theory aired there final season?")
    if Number=="2020":
      print("Correct!")
      print("You are a superfan!")
    else:
      print("Incorrect!")
      print("You are a fake fan!")
