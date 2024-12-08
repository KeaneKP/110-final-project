#FINAL PROJECT GAME AI
# Author   : Kaden Keane
# Email    : kkeane@umass.edu
# Spire ID : 34835608

import random as rand
import functions as f
#import FINAL_PROJECT as main

possibleMoves = ["11", "12", "13", "21", "22", "23", "31", "32", "33"]
def generateValidMoves(board, player, possible):
    validMoves = []
    for move in possible:
        if f.validateMove(board, move, player):
            validMoves.append(move)
    return validMoves

def decideMove(board, player, last, r=True, r2=True):
    validMoves = generateValidMoves(board, player, possibleMoves)
    winningMove = findWinningMove(board, validMoves, player)
    if (winningMove!="no"):
        if (r):
            #print("win")
            pass
        return winningMove
    opponentWin = stopOpponentWinning(board, validMoves, player, last)
    if (opponentWin!="no"):
        if (r):
            #print("stop")
            pass
        return opponentWin
    if(r2):
        winIn2 = advancedMove(board, validMoves, player, last)
        if (winIn2!="no"):
            #print("win in 2")
            pass
            return winIn2
    if(r):
        oppBlock = blockingMove(board, validMoves, player, last)
        if (oppBlock!="no"):
            #print("opp block")
            pass
            return oppBlock
    if (r):
        #print("random")
        pass
        return generateRandomMove(validMoves)
    else:
        return "no"
    

def generateRandomMove(moves):
    move = moves[rand.randrange(0, len(moves))]
    return move

def findWinningMove(board, moves, player):
    for move in moves:
        modifiedBoard = f.copyBoard(board)
        if (player==1):
            modifiedBoard[int(move[1])-1][int(move[0])-1] = " X "
        else:
            modifiedBoard[int(move[1])-1][int(move[0])-1] = " O "
        if f.checkWin(modifiedBoard, player):
            return move
    return "no"
def stopOpponentWinning(board, moves, player, last):
    for move in moves:
        modifiedBoard = f.copyBoard(board)
        modifiedBoard = f.markOldMoves(modifiedBoard, player, last)
        if (player==-1):
            modifiedBoard[int(move[1])-1][int(move[0])-1] = " X "
        else:
            modifiedBoard[int(move[1])-1][int(move[0])-1] = " O "
        if f.checkWin(modifiedBoard, player*(-1)):
            return move
    return "no"
def advancedMove(board, moves, player, last):
    '''
    This is where things get crazy
    Basically the AI is going to look at a move and then say "If I was playing against this move what would I do" then see if they can win from that position
    this could run into an issue if it runs into a loop of repeatedly generating future moves and never decides on one
    I think in general there will be an issue if the response move also runs advancedMove() so I might just make it unable to do so
    essentially this will only pick a move if there exists a move that will result in a win in 2 turns even if the opponent plays an optimal move to stop it
    '''
    for move in moves:
        modifiedBoard = f.copyBoard(board)
        modLast = f.copyBoard(last)
        if (player==1):
            modifiedBoard[int(move[1])-1][int(move[0])-1] = " X "
        else:
            modifiedBoard[int(move[1])-1][int(move[0])-1] = " O "
        modifiedBoard = f.markOldMoves(modifiedBoard, player, last)
        modLast = f.managePastMoves(player, modLast, move)
        #the modified board now shows what it would look like after the move
        response = decideMove(modifiedBoard, player*(-1), modLast, False, False)
        if (response!="no"):
            #it re runs decide move as the opponent to create the "optimal" (assuming the ai picks the optimal response) response move 
            if (player==-1):
                modifiedBoard[int(response[1])-1][int(response[0])-1] = " X "
            else:
                modifiedBoard[int(response[1])-1][int(response[0])-1] = " O "
            modifiedBoard = f.markOldMoves(modifiedBoard, player*(-1), modLast)
            modLast = f.managePastMoves(-player, modLast, response)
            #hopefully now we should have a board that reflects two moves having been made.
            if(not f.checkWin(modifiedBoard, player*(-1))):
                newValidMoves = generateValidMoves(modifiedBoard, player, possibleMoves)
                for newMove in newValidMoves:
                    newModifiedBoard = f.copyBoard(modifiedBoard)
                    if (player==1):
                        newModifiedBoard[int(newMove[1])-1][int(newMove[0])-1] = " X "
                    else:
                        newModifiedBoard[int(newMove[1])-1][int(newMove[0])-1] = " O " 
                    if f.checkWin(newModifiedBoard, player):
                        return move
    return "no"
    #I wrote this entire function without testing it and somehow it worked perfectly first try. This is awesome


def blockingMove(board, moves, player, last):
    #this one just looks at what the best move for the opponent is and then blocks them
    modifiedBoard = f.copyBoard(board)
    modifiedBoard = f.markOldMoves(modifiedBoard, player, last)
    bestOpp = decideMove(modifiedBoard, -player, last, False)
    if (bestOpp in moves):
        return bestOpp
    return "no"
        


