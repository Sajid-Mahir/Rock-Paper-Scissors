import random

while True:
    
    print("Rock, Paper or, Scissors?")
    move=input().lower()
    choices=['rock','paper','scissors']
    bot=random.choice(choices)
    print(f"\nYou Chose {move}, Computer Chose {bot}.\n")
   
    if move==bot:
        print("Wooo!! It's a Tie!")
        
    elif move=='rock':
        if bot=='scissors':
            print("Great! you smashed the Bot's Scissors :D")
        else:
            print("Well that was underwhelming, you lose. ;(")
    
    elif move=='scissors':
        if bot=='rock':
            print('You got brutally crushed by the Bot so, you lose. ;(')
        else:
            print("Sharp scissors you got there ;D Obviously! you win.")
            
    elif move=='paper':
        if bot=='rock':
            print("Damn... you covered that rock real good, you win.")
        else:
            print("This is not a paper-cut game, you lose. ;(")
            
    else:
        print("Try that in another game, here we have some rules!!")
    
    print("Wanna Play Again? (yes/y/no/n)")
    play=input().lower()
    if play =='no' or play =='n':
        break