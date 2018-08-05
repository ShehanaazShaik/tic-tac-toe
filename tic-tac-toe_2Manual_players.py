"""
Tic-tac-toe
Inspired by blogpost: http://thebillington.co.uk/blog/posts/writing-a-tic-tac-toe-game-in-python
Improvised by Shaik Shehanaaz
"""

board = list(range(1,10))#stores the board composition

playerOneTurn = True #whose turn is it?Player1 or Player2

def printBoard() :
    #Prints board onto the screen 
    print('')
    for i in range(0,9):
        print( '|' + str(board[i]),end='')
        if((i+1)%3==0):print('|')
    print('')

def winner():
    #Checks if any of the player has won
    for x in range (0, 3) :
        #Checking for horizontal condition; 0,1,2 - 3,4,5 - 6,7,8
        y = x * 3
        if (board[y] == board[y + 1] and board[y] == board[y + 2]) :return True
        #Checking for vertical condition; 0,3,6 - 1,4,7 - 2,5,8
        if (board[x] == board[(x + 3)] and board[x] == board[(x + 6)]) :return True
    #Checking diagonal condition
    if((board[0] == board[4] and board[0] == board[8]) or 
       (board[2] == board[4] and board[4] == board[6])) :return True

print("LET's play!!!")
printBoard()
print("Choose your position number:")
#Executing a loop until there is a winner
while not winner() :
    #if playerOneTurn :print( "Player 1:",end='')
    #else :print( "Player 2:",end='')
    print( "Player 1:",end='') if playerOneTurn else print( "Player 2:",end='')
    try:
        choice = int(input())
        if board[choice - 1] in ['X','O']:print("illegal move, plase try again")
        board[choice-1]='X' if playerOneTurn else 'O'
    except:print("please enter a valid field")
    playerOneTurn = not playerOneTurn
    printBoard()
    
print ("DRUM ROLLS")
print ("Player " + str(int(playerOneTurn + 1)) + " WINS!!!!")
printBoard()