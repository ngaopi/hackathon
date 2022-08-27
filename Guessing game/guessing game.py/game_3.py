guess=3
i=5
chance=5
while i>=1:
    n=int(input("enter the number:"))
    if n==guess:
        print("congratulations!you have guessed the correct answer")
        break
    elif n<guess or n >guess:
        print("sorry!your guessed is wrong","you have",chance,"chance to guess")
        chance=chance-1
        i=i-1
    
    
    

  
