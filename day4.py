print("Welcome to your Adventure Story Simulator.")
print ()
print("I am going to ask you a bunch of questions and then create an epic story with you as the star.")

print()
name = input("What is your name? ")
print()
enemyName = input("What is your enemy's name? ")
print()
superPower = input("What is your super power? ")
print()
live = input("Where do you live?")
print()
food = input("What is your favorite food?")

"""
Color	Value
Default	0
Black	30
Red	31
Green	32
Yellow	33
Blue	34
Purple	35
Cyan	36
White	37

print("\033[text color number m") Eg: for red color print("\033[31m")
"""

print()
print("Hello", name, "Your ability to",  "\033[35m", superPower, "\033[0m", "will make sure you never have to look at",  "\033[31m", enemyName,  "\033[0m","again." "Go eat",  "\033[32m", food,  "\033[0m","as you walk down the streets of",  "\033[36m", live,  "\033[0m", "and use",  "\033[35m", superPower,  "\033[0m","for good and not evil!")
