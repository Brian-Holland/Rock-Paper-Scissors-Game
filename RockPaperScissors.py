import random

print('Welcome to Rock, Paper, Scissors.')
userscore = 0
compscore = 0

print('Would you like to play? Y/N?')
playstatus = input()
if playstatus == 'Y' or playstatus == 'y':
    while True:
   
        print('Rock, Paper, or Scissors?')
        userpick = input()
        if userpick == 'Rock' or userpick == 'rock':
            userfinal = 1
        elif userpick == 'Paper' or userpick == 'paper':
            userfinal = 2
        elif userpick == 'Scissors' or userpick == 'scissors':
            userfinal = 3
        else:
            userpick = ('Invalid Selection')
            print('Please make a valid selection')
            continue
        print('You have selected: ' + userpick)


        comprand = random.randint(1,3)
        if comprand == 1:
            comppick = 'Rock'
            compfinal = 1
        elif comprand == 2:
            comppick = 'Paper'
            compfinal = 2
        else:
            comppick = 'Scissors'
            compfinal = 3
        print('The computer has chosen...')
        print(comppick)


        if userfinal == compfinal:
            print('Draw. No points given this round. Current score:' + ' User:'+ str(userscore) + ' Computer:' + str(compscore))
        elif userfinal == 1 and compfinal == 3:
            userscore = userscore+1
            print('Rock beats Scissors. You win this round. Current score:' + ' User:'+ str(userscore) + ' Computer:' + str(compscore))
        elif userfinal == 1 and compfinal == 2:
            compscore = compscore+1
            print('Paper beats Rock. You lose this round. Current score:' + ' User:'+ str(userscore) + ' Computer:' + str(compscore))
        elif userfinal == 2 and compfinal == 1:
            userscore = userscore+1
            print('Paper beats Rock. You win this round. Current score:' + ' User:'+ str(userscore) + ' Computer:' + str(compscore))
        elif userfinal == 2 and compfinal == 3:
            compscore = compscore+1
            print('Scissors beats Paper. You lose this round. Current score:' + ' User:'+ str(userscore) + ' Computer:' + str(compscore))
        elif userfinal == 3 and compfinal == 1:
            compscore = compscore+1
            print('Rock beats Scissors. You lose this round. Current score:' + ' User:'+ str(userscore) + ' Computer:' + str(compscore))
        elif userfinal == 3 and compfinal == 2:
            userscore = userscore+1
            print('Scissors beats Paper. You win this round. Current score:' + ' User:'+ str(userscore) + ' Computer:' + str(compscore))

        print('Would you like to play again?(Y/N)')      
        playstatus = input()
        if playstatus == 'n' or playstatus == 'N':
            break
        else:
            continue
            
   
print('Thank you for playing. Final score:' + ' User:'+ str(userscore) + ' Computer:' + str(compscore))
