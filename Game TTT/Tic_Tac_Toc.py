import random
import os
theBoard =[' '] * 10
availabe = [str(item) for item in range(0,10)]
players =[0,'A','N']

def clearBoard():
    os.system('cls')

def space_check(board,position):
    return board[position]==' '

def random_player():
    return random.choice((-1,1))

def display_board(availabe,theBoard):
    print('Sample Grid \t \t  Move Game')
    print(availabe[7] +' | ' + availabe[8] + ' | ' + availabe[9]+    '\t \t' + theBoard[7] +' | ' + theBoard[8] + ' | ' + theBoard[9] )
    print('---------\t\t---------')
    print(availabe[4] +' | ' + availabe[5] + ' | ' + availabe[6]+    '\t \t' + theBoard[4] +' | ' + theBoard[5] + ' | ' + theBoard[6])
    print('---------\t\t---------')
    print(availabe[1] +' | ' + availabe[2] + ' | ' + availabe[3]+    '\t \t' + theBoard[1] +' | ' + theBoard[2] + ' | ' + theBoard[3])

def win_check(board,mark):
    return ((board[7] ==  board[8] ==  board[9] == mark) or 
    (board[4] ==  board[5] ==  board[6] == mark) or 
    (board[1] ==  board[2] ==  board[3] == mark) or 
    (board[7] ==  board[4] ==  board[1] == mark) or 
    (board[8] ==  board[5] ==  board[2] == mark) or 
    (board[9] ==  board[6] ==  board[3] == mark) or 
    (board[7] ==  board[5] ==  board[3] == mark) or 
    (board[9] ==  board[5] ==  board[1] == mark)) 

def player_choice(board,player):
    position=0
    while position not in [1,2,3,4,5,6,7,8,9] and space_check(board,position):
        try:
            position=int(input('Player %s, choose the next position: (1-9) ' %(player)))
        except:
            print("I'm sorry, plaese try again")
    return position

def place_marker(avail,board,marker,position):
    board[position] = marker
    avail[position] = ' '

def full_board_check(board):
    return ' ' not in board[1:]

def replay():
    return input('Do you want to paly again? Enter Yes or No: ').lower().startswith('y')

while True:
     clearBoard()
     print('Welcome to Tic Tac Toc!!!')
     toggle =random_player()
     player =players[toggle]
     print('For this round, Player %s will go first' %(player))

     game_on = True
     input('Hit Enter to continue')
     while game_on:
         display_board(availabe,theBoard)
         position= player_choice(theBoard,player)
         place_marker(availabe,theBoard,player,position)

         if win_check(theBoard,player):
             display_board(availabe,theBoard)
             print('Congratulations! Player '+str(player)+' wins!')
             game_on = False
         else:
            if full_board_check(theBoard):
                display_board(availabe,theBoard)
                print('The game is a draw!')
                break
            else:
                toggle *= -1
                player = players[toggle]
                clearBoard()  

     #reset the board y and available moves list
     theBoard = [' '] * 10
     available = [str(num) for num in range(0,10)]
    
     if not replay():
        break            








