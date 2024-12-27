import numpy as np
if __name__=='__main__':
    while True:
        s=input("Roll the dice (y/n) : ")
        if s.lower()=='n':
            print("Thanks for playing!")
            break
        elif  s.lower()=='y':
            print(np.random.randint(1,6))
        else:
            print("Invalid Choice")

