import random
if __name__=='__main__':
    # windows +; for using emojis in windows
    emojis={'r':'🪨','s':'✂️','p':'📃'}
    while True:
        user_input=input("Rock/Paper/Scissors ?? (r/p/s)").lower()
        if user_input not in ['r','p','s']:
            print("Invalid input. Please enter r for Rock, p for Paper or s for Scissors")
            continue
        comp_choice=random.choice(['r','p','s'])
        print(f'User Choice : {emojis[user_input]}')
        print(f'Computer Choice : {emojis[comp_choice]}')
        if user_input==comp_choice:
            print(f"Both players selected {emojis[user_input]}. It's a tie!")
            temp=input("Want to play again : (y/n) ")
            if temp=='n':
                break
        elif user_input=='r':
            if comp_choice=='s':
                print(f"Rock smashes scissors! User wins!")
                temp=input("Want to play again : (y/n) ")
                if temp=='n':
                    break
            if comp_choice=='p':
                print(f"Paper covers rock! Computer wins!")
                temp=input("Want to play again : (y/n) ")
                if temp=='n':
                    break
        elif user_input=='p':
            if comp_choice=='r':
                print(f"Paper covers rock! User wins!")
                temp=input("Want to play again : (y/n) ")
                if temp=='n':
                    break
            if comp_choice=='s':
                print(f"Scissors cuts paper! Computer wins!")
                temp=input("Want to play again : (y/n) ")
                if temp=='n':
                    break
        elif user_input=='s':
            if comp_choice=='p':
                print(f"Scissors cuts paper! User wins!")
                temp=input("Want to play again : (y/n) ")
                if temp=='n':
                    break
            if comp_choice=='r':
                print(f"Rock smashes scissors! Computer wins!")
                temp=input("Want to play again : (y/n) ")
                if temp=='n':
                    break
        


