import random
import sys
import numpy
import csv
import os

# global state variables
from scipy.signal.filter_design import cheb1ap

is_finished = False
ActivePlayer = 1

chessboard = [[0 for x in range(15)] for y in range(15)]


def reset_board():
    board = [[0 for x in range(15)] for y in range(15)]
    return board


def draw():
    # numbers represent the number of coins on the tile

    #TODO: Add system call to clear screen

    # os.clear()
    for ycoord in range(0, 15):
        sys.stdout.write("|")
        for xcoord in range(0, 15):
            # if chessboard[xcoord][ycoord] is 0:
            #     print "  |",
            # else:
            print '{:2}'.format(chessboard[xcoord][ycoord]),
            sys.stdout.write("|")
        print ""


def randomize_coin(k):
    for ctr in range(k):
        chessboard[random.randint(0, 14)][random.randint(0, 14)] += 1


def move(source_x, source_y, destination_x, destination_y):
    if source_x < 1 or source_x > 15:
        raise Exception("Invalid source x-coordinates")
    if source_y < 1 or source_y > 15:
        raise Exception("Invalid source y-coordinates")
    coins = chessboard[source_x - 1][source_y - 1]
    if coins < 1:
        raise Exception("There is no coin on that tile, please try again.")
    # if destination_x < 0 or destination_x > 15:
    #     raise Exception("Invalid destination x-coordinates")
    # if destination_y < 0 or destination_y > 15:
    #     raise Exception("Invalid destination y-coordinates")
    # TODO: Add valid move checking
    # Populate array of valid moves
    # move1: 1 tile right 2 tiles up
    # move2: 1 tile left 2 tiles up
    # move3: 2 tiles left 1 tile up
    # move4: 2 tiles left 1 tile down
    move_set = [(+1, -2), (-1, -2), (-2, -1), (-2, +1)]
    valid_moves = [(source_x + x, source_y + y) for (x, y) in move_set]
    print valid_moves
    if (destination_x, destination_y) in valid_moves:
        chessboard[source_x - 1][source_y - 1] -= 1
        if destination_x < 1 or destination_x > 15:
            print "Coin is removed"
            return
        if destination_y < 1 or destination_y > 15:
            print "Coin is removed"
            return
        chessboard[destination_x - 1][destination_y - 1] += 1
    else:
        raise Exception("Invalid destination choose only among the 4 possible moves")


def move2(source_x, source_y, destination_x, destination_y):
    if source_x < 1 or source_x > 15:
        raise Exception("Invalid source x-coordinates")
    if source_y < 1 or source_y > 15:
        raise Exception("Invalid source y-coordinates")
    coins = chessboard[source_x - 1][source_y - 1]
    if coins == 0:
        raise Exception("There is no coin on that tile, please try again.")
    if coins == 1:
        raise Exception("You cannot move that coin.")

    # if destination_x < 0 or destination_x > 15:
    #     raise Exception("Invalid destination x-coordinates")
    # if destination_y < 0 or destination_y > 15:
    #     raise Exception("Invalid destination y-coordinates")
    # Populate array of valid moves
    # move1: 1 tile right 2 tiles up
    # move2: 1 tile left 2 tiles up
    # move3: 2 tiles left 1 tile up
    # move4: 2 tiles left 1 tile down
    move_set = [(+1, -2), (-1, -2), (-2, -1), (-2, +1)]
    valid_moves = [(source_x + x, source_y + y) for (x, y) in move_set]
    print valid_moves
    if (destination_x, destination_y) in valid_moves:
        chessboard[source_x - 1][source_y - 1] -= 1
        if destination_x < 1 or destination_x > 15:
            print "Coin is removed"
            return
        if destination_y < 1 or destination_y > 15:
            print "Coin is removed"
            return
        if chessboard[destination_x - 1][destination_y - 1] == 0:
            chessboard[destination_x - 1][destination_y - 1] += 1
    else:
        raise Exception("Invalid destination choose only among the 4 possible moves")


def count_coins():
    return sum(map(sum, chessboard))


def check_finished():
    for ycoord in range(0, 15):
        for xcoord in range(0, 15):
            if chessboard[xcoord][ycoord] > 1:
                return False
    return True


def save_state(file_name):
    print "Saving array"
    print chessboard
    state = numpy.asarray(chessboard)
    numpy.savetxt(file_name, state, delimiter=',', fmt='%i')


def load_state(file_name):
    print "load array"
    with open(file_name, 'r') as f:
        reader = csv.reader(f)
        data = list(list(rec) for rec in csv.reader(f, delimiter=','))
    data = [ [int(x) for x in row] for row in data ]
    print data
    return data


def saving_and_loading_test(chessboard_state):
    draw()
    backup = chessboard_state
    save_state('VALENTINO.txt')
    chessboard_state = load_state('VALENTINO.txt')
    if chessboard_state == backup:
        print "load success"
    else:
        print "load failed"


def input_k_coins():
    # test for randomization
    print "Please input number of coins:"
    try:
        k = int(raw_input())
        if 1 < k < 1000:
            randomize_coin(int(k))
            draw()
        else:
            print "Number of coins must be an integer from 1 to 1000"
            input_k_coins()
    except ValueError as ve:
        print "Number of coins must be an integer from 1 to 1000"
        input_k_coins()


def random_k_coins():
    k = random.randint(1, 1000)
    print "Random k value is:", k
    randomize_coin(int(k))
    draw()


def switch_player(active_player):
    if active_player == 1:
        active_player = 2
    else:
        active_player = 1
    return active_player


# setup the board
print "Do you want to input the number of coins (1 to 1000) or randomize the number of coins? [random or input]?"
while True:
    choice = raw_input()
    if choice.lower() == "random":
        random_k_coins()
        break
    elif choice.lower() == "input":
        input_k_coins()
        break
    print "[random or input]"

while check_finished():
    print "Game Over! Do you want to generate a new board? [Y/N]"
    choice_made = False
    while not choice_made:
        choice = raw_input()
        if choice.lower() == "n":
            exit(0)
        elif choice.lower() == "y":
            chessboard = reset_board()
            print "Do you want to input the number of coins [1 to 1000] or randomize the number of coins? [random or input]?"
            while True:
                choice = raw_input()
                if choice.lower() == "random":
                    random_k_coins()
                    choice_made = True
                    break
                elif choice.lower() == "input":
                    input_k_coins()
                    choice_made = True
                    break
                print "random or input"
        else:
            print "[Y/N]"

# Game Instructions
# Win the game by being the last player to move a coin
print "Input your move in the ff format: \"source_x source_y destination_x destination_y\""
print "Example: 1 1 3 2"
print "Input \"save SURNAME.txt\" to save your game as SURNAME.txt"
print "Input \"load SURNAME.txt\" to load your game from SURNAME.txt"
print "Input quit to exit the game"
# main event loop
while not is_finished:
    try:
        print "Player", ActivePlayer, "'s Turn:"
        player_input = raw_input()
        if player_input.split()[0].lower() == "save":
            save_state(player_input.split()[1])
            continue
        if player_input.split()[0].lower() == "load":
            load_state(player_input.split()[1])
            draw()
            continue
        if player_input.lower() == "quit":
            exit()
        source_x, source_y, dest_x, dest_y = player_input.split()
        move2(int(source_x), int(source_y), int(dest_x), int(dest_y))
    except Exception as ex:
        print ex.message
    else:
        print "Remaining coins", count_coins()
        if not check_finished():
            ActivePlayer = switch_player(ActivePlayer)
            draw()
        else:
            print "Player", ActivePlayer, "has won!"
            draw()
            is_finished = True
