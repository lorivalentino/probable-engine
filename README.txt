This is a 2-player game on a chessboard:
•	The game starts with k coins located at one or more (x, y) coordinates on the board (a single cell may contain more than one coin). The coordinate of the upper left cell is (1, 1) and the coordinate of the lower right cell is (15,15).
•	In each move, a player can move a single coin from some cell (x, y) to one of four possible tiles:
    # move1: 1 tile right 2 tiles up
    # move2: 1 tile left 2 tiles up
    # move3: 2 tiles left 1 tile up
    # move4: 2 tiles left 1 tile down

•	The players move in alternating turns. The first player who is unable to make a move loses the game.
•	Constraints:
o	1 <= k <= 1000
o	1 <= (x, y) coordinates <= 15
o	k and the (x, y) coordinates are randomly selected
•	Provide the players with an option to save the game. Saving a game outputs the current field the save_SURNAME.txt file and exits the program.
•	Provide the players with an option to restart the game. Restarting a game resets the board.
•	For better user experience, clear the screen every time you display the board. HINT: import os
