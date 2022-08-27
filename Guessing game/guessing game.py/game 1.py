import random
def guess_number():
    random_number=random.randint(1,20)
    player_name=input("enter your name:")
    confirm_play=input("would you like to start the game?(enter yes/no):")
    attempts=0
    while confirm_play.lower()=="yes":
        guess=int(input("guess any number between 1 and 20:"))
        if guess<1 or guess>20:
            print("please guess any number in the range.")
        elif guess==random_number:
            print("congratulations",player_name,"you won!")
            attempts=attempts+1
            print("it took",attempts,"attempts to win this game")
            break
        elif guess>random_number:
            print("HINT:try smaller number")
            attempts=attempts+1
        elif guess<random_number:
            print("HINT:try larger number")
            attempts=attempts+1
    else:
        print("thanks",player_name,"for your time.")
guess_number()