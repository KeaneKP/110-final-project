#FINAL PROJECT FUNCTIONS
# Author   : Kaden Keane
# Email    : kkeane@umass.edu
# Spire ID : 34835608


import random as rand
import text
#new input functions
def ninput(*args):
    print(*args)
    inp = input("\nYour input: ")
    if(len(inp)<1):
        return ninput("Please enter a valid input")
    #allows player to exit game
    if (inp=="exit" or inp=="x"):
        print("EXITING GAME...")
        exit()
    return inp
def intInput(*args, move=False):
    inp = ninput(*args)
    if(move):
        if len(inp) < 2:
            return intInput("enter a valid input")

    try:
        int(inp)
        return inp
    except:
        return intInput("Please enter a valid input")
#probably a better way to check win that doesn't just check every possible line but whatever
#the board is small so I do this
#plus I feel like I did each one in a pretty smart way
def checkWin(board, player):
    if player == 1:
        p = (" X ", "~X~")
    else:
        p = (" O ", "~O~")
    # check each row
    for row in board:
        check = True
        for i in row:
            if not i in p:
                check = False
        if(check):
            #print("Row check. row:", row, "i:", i)
            return True
    #check each column
    for i in range(3):
        check = True
        for row in board:
            if not row[i] in p:
                check = False
        if(check):
            #print("Column check. row:", row, "i:", i)
            return True
    #check diagonals
    #top left diagonal
    check = True
    for i in range(3):
        if not board[i][i] in p:
            check = False
    if(check):
        #print("tl diagonal. i:", i)
        return True
    #bottom left diagonal
    check = True
    for i in range(3):
        if not board[2-i][i] in p:
            check = False
    if(check):
        #print("bl diagonal. i:", i)
        return True
        
    #if we made it this far then there is no winner yet
    return False

def printBoard(board):
    print("\n")
    for i in range(len(board)):
        print(3-i, ":   ", board[2-i])
    print("          1      2      3")

def validateMove(board, move, player):
    if (player==1):
        return (board[int(move[1])-1][int(move[0])-1] == "   " or board[int(move[1])-1][int(move[0])-1] == "~X~")
    else:
        return (board[int(move[1])-1][int(move[0])-1] == "   " or board[int(move[1])-1][int(move[0])-1] == "~O~")

def copyBoard(board):
    #I'm so mad that this is a function that I need.
    #I should just be able to say newBoard=board
    # or at least newboard = board.copy()
    out = []
    for row in board:
        out.append(row.copy())
    return out

def markOldMoves(board, player, list):
    i = 0
    if len(list[1+player]) >= 3:
        oldestMove = list[1+player][0]
        #need this check because otherwise if a player replaces their dissappearing piece then it will still dissappear
        if (board[int(oldestMove[1])-1][int(oldestMove[0])-1][0]=="~"):
            board[int(oldestMove[1])-1][int(oldestMove[0])-1] = "   "
        i = 1
    if(len(list[1+player]) >= 2):
        oldestMove = list[1+player][i]
        if (player==1):
            board[int(oldestMove[1])-1][int(oldestMove[0])-1] = "~X~"
        else:
            board[int(oldestMove[1])-1][int(oldestMove[0])-1] = "~O~"
    return board

def managePastMoves(player, list, lastMove):
    list[1+player].append(lastMove)
    if len(list[1+player]) >= 4:
        list[1+player].pop(0)
    return list

def restart(aiPlayer, ai):
    inp = ninput("do you want to play again?:  ")
    #it just checks the first letter of the response so "y", "yes", "Yeah", "yes please", etc. would all work
    if inp[0].lower()=="y":
        startGame(ai, True, aiPlayer)
    else:
        print("ok bye.")
        exit()

def greet():
    print(text.greeting)
    inp = ninput("Would you like instructions on how to play the game??")
    if (inp[0].lower()=="y"):
        for txt in text.instructions:
            print("\n"+txt)
            input("Press enter to continue: ")
    ninput("Are you ready to begin?")

def startGame(ai, restart=False, aiPlayer=0):
    board = [["   ", "   ", "   "],["   ", "   ", "   "],["   ", "   ", "   "]]
    if not restart:
        #print instructions and introduction
        greet()
        aiPlayer = int(intInput("Do you want an AI player? enter one of the following:\n1. No AI Player\n2. Human Vs. AI\n3. AI vs AI (you just watch)"))-1
    if abs(aiPlayer) == 1:
        aiPlayer *= (-1)**rand.randrange(0,5)
    printBoard(board)
    move(board, 1, [[],[],[]], ai, aiPlayer)
    

def move(board, player, lastMoves, ai, aiPlayer=0):
    print("====================================================")
    if(player==aiPlayer or aiPlayer==2):
        inp = ai.decideMove(board, player, lastMoves)
        print("enter a move: ", inp)
    else:
        inp = intInput("enter a move: ", move=True)
    
    #checks if requested space is empty
    if validateMove(board, inp, player):
        if (player == 1):
            board[int(inp[1])-1][int(inp[0])-1] = " X "
        else: 
            board[int(inp[1])-1][int(inp[0])-1] = " O "
        if checkWin(board, player): 
            printBoard(board)
            if(player==1):
                print("PLAYER 1 HAS WON")
                restart(aiPlayer, ai)
            else:
                print("PLAYER 2 HAS WON")
                restart(aiPlayer, ai)
        else:
            newBoard = markOldMoves(board, player, lastMoves)
            printBoard(newBoard)
            move(newBoard, player*(-1), managePastMoves(player, lastMoves, inp), ai, aiPlayer)
    else:
        print("That space is not empty, try again")
        move(board, player, lastMoves, aiPlayer)
