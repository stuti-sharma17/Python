import random
x=random.randint(1,100)
while True:
    user_input=int(input("Guess a number between 1 and 100:"))
    if x==user_input:
        print("You guessed it! The number was indeed",x)
        break
    else:
        if x > user_input:
            print("TOO LOW !!")
        else:
            print("TOO HIGH !!")


