#FINAL PROJECT
# Author   : Kaden Keane
# Email    : kkeane@umass.edu
# Spire ID : 34835608

instructions = [
"Welcome to the instructions! I'll try and keep this quick but thorough.\nI will assume that You already know how to play standard tic-tac-toe, so we will simply focus on the new rules and how to control the game",
"The first thing to note is the fact that whenever you make your 4th move, the oldest move deletes.\nThis way the board is constantly changing as you get farther into the game.\nIt becomes pretty clear how this works once you start playing",
"A tile that is about to disappear will be marked a with ~ symbols.\nFor example, ~X~ would be an X tile that will dissapear after the X player's next turn",
"Here is an example of a board:\n\n3 :    [' O ', '   ', '~O~']\n2 :    ['   ', ' X ', ' X ']\n1 :    ['   ', '~X~', ' O ']\n          1      2      3\n\nHere it is the O player's turn.",
"You can see that there are 3 tiles for each player on the board and each player has 1 tile marked with ~ symbols.\nThose are the oldest move by that player.\nWhen the O player makes a move, that will be their 4th tile on the board and so the tile marked by ~ will disappear so that they continue having only 3 tiles on the board at a time.\nThen their next oldest tile will be marked and that will delete after the next turn",
"Two slightly advanced rules that are worth noting are:\n1. You can replace a tile which is about to disappear.\nFor example, O could place a tile in the top right corner and it would replace the disappearing tile.\nO could NOT place a tile in the bottom middle because despite it being marked, that tile is not disappearing until the X player's next turn, NOT this turn",
"2. If the O player places a tile in the top middle spot they will win the game.\nThis may not seem right because the top right tile is disappearing, but wins are calculated BEFORE tiles are deleted.\nThis is required in order for gameplay to run smoothly.\nWinning like this is the only situation where you can have 4 tiles on the board.",
"That covers all you need to know about game rules.\nnext we will discuss how you make a move.\nHere is a marked board for reference:\n\n3 :    [' A ', ' B ', ' C ']\n2 :    [' D ', ' E ', ' F ']\n1 :    [' G ', ' H ', ' I ']\n          1      2      3\n",
"Moves are inputted as 2 digit numbers.\nThe first digit represents the horizontal position, or you can think of it as which column it is in, and the second number represents the vertical position, or the row.\n(Think of it as (x,y) coordinates. Over then up)\n For example, in the reference board position A would be 13, E would be 22, and F would be 32",
"Here is a list of how to access every tile, just to make things abundantly clear.\nA:13\nB:23\nC:33\nD:12\nE:22\nF:32\nG:11\nH:21\nI:31\n",
"That should be everything you need to play the game! Of course, the goal is to get 3 of your tiles in a row first.\nGood luck!"
]
greeting = "Welcome to my version of Tic-Tac-Toe! In this version of the game, things are slightly different and more strategic, and also there are no more games ending in ties!"
