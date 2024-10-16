#FINAL PROJECT
# Author   : Kaden Keane
# Email    : kkeane@umass.edu
# Spire ID : 34835608


#Instructions:
#like tic tac toe but your oldest move gets deleted. Makes it so that the game can never end in a tie, only in a win for someone. More strategic

#TODO:
# Make a basic AI to play against
# Make instructions for the game
# make a start menu where the user can select whether they need instructions or not and also if its 1v1 or 1vCPU
# make it so the game doesn't explode when you type in an invalid move

import game_ai as ai
#aiEnabled = True

initialBoard = [["   ", "   ", "   "],["   ", "   ", "   "],["   ", "   ", "   "]]

def printBoard(board):
    print("\n")
    for i in range(len(board)):
        print(3-i, ":   ", board[2-i])
    print("          1      2      3")
printBoard(initialBoard)


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
        
#this is stupid but I want to be able to do lastMoves[player] to get the list of past moves for a specifc player
#so my solution is to do lastMoves[1+player] to get either lastMoves[0] or [2] but thats annoying because lastMoves[1] is blank and thats stupid
lastmoves = [[],[],[]]
def manageLastMoves(board, player, lastMove):
    #print("ran lastMoves", player, lastMove)
    lastmoves[1+player].append(lastMove)
    if len(lastmoves[1+player]) >= 4:
        #print("removed a move", player, lastMove)
        oldestMove = lastmoves[1+player][0]
        board[int(oldestMove[1])-1][int(oldestMove[0])-1] = "   "
        lastmoves[1+player].pop(0)
    if(len(lastmoves[1+player]) >= 3):
        #print("marked an old move", player, lastMove)
        oldestMove = lastmoves[1+player][0]
        if (player==1):
            board[int(oldestMove[1])-1][int(oldestMove[0])-1] = "~X~"
        else:
            board[int(oldestMove[1])-1][int(oldestMove[0])-1] = "~O~"
    #print(lastmoves)
    return board

def move(board, player):
    #if(aiEnabled and player==-1):
    #    inp = ai.generateRandomMove()
    #    print("enter a move: ", inp)
    #else:
    inp = input("enter a move: ")

    #allows player to exit game
    if (inp=="exit" or inp=="x"):
        exit()
    
    #checks if requested space is empty
    if board[int(inp[1])-1][int(inp[0])-1] == "   ":
        if (player == 1):
            board[int(inp[1])-1][int(inp[0])-1] = " X "
        else: 
            board[int(inp[1])-1][int(inp[0])-1] = " O "
        if checkWin(board, player): 
            printBoard(board)
            if(player==1):
                print("PLAYER 1 HAS WON")
            else:
                print("PLAYER 2 HAS WON")
            exit()
        else:
            newBoard = manageLastMoves(board, player, inp)
            printBoard(newBoard)
            move(newBoard, player*(-1))
    else:
        print("That space is not empty, try again")
        move(board, player)





#game start
move(initialBoard, 1)
