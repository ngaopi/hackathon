import random
x=random.randint(1,10)
guess=int(input("guess a number between 1 and 10:"))
while guess!=x:
    print("sorry.you guessed incorrectly.try again.")
    guess=int(input("guess a number between 1 and 10:"))
print("congratulations!you guessed the number correctly!")

