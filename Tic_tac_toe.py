# ---global var---

# board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
# if game is still going
game_still_going = True

# if tie, win
winner = None

# Whose turn it is
current_player = "X"


# display board
def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


# to check if display_board() is able to call.
# display_board()


# play tic-tac-toe
def play_game():
    # display initial board
    display_board()

    # while game is in progress
    while game_still_going:
        # handles turn for single player

        handle_turn(current_player)

        # checks if game is over

        check_if_game_over()

        # flip to the next player

        flip_player()

    # game ended

    if winner == "X" or winner == "O":
        print(winner + " won.")
    elif winner == None:
        print("its tie.")


# handles turn for single player
def handle_turn(player):
    print(player + "'s turn  ")

    position = input("choose a position to enter 1-9: ")

    valid = False
    while not valid:

        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Invalid input, choose something between 1-9: ")

        position = int(position) - 1

        if board[position] == "-":
            valid = True
        else:
            print("you are strictly not allowed, its an order, don't try to break my code, its roboust :p ")

    board[position] = player
    display_board()


def check_if_game_over():
    check_if_win()
    check_if_tie()


def check_if_win():
    # setup global variables so that we can write to it.
    global winner
    # check rows
    row_winner = check_rows()

    # check columns
    column_winner = check_columns()

    # check diagonals
    diagonal_winner = check_diagonals()

    if row_winner:
        # there was a win
        winner = row_winner
    elif column_winner:
        # there was a win
        winner = column_winner
    elif diagonal_winner:
        # there was a win
        winner = diagonal_winner
    else:
        # there was no win
        winner = None
    return


def check_rows():
    # set up global variable
    global game_still_going
    # check if any of the rows have same values
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    # if rows are match
    if row_1 or row_2 or row_3:
        game_still_going = False
    # return the winner Mr. X or Mr. O
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return


def check_columns():
    # set up global variable
    global game_still_going
    # check if any of the columns have same values
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"
    # if columns are match
    if column_1 or column_2 or column_3:
        game_still_going = False
    # return the winner Mr. X or Mr. O
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    return


def check_diagonals():
    # set up global variable
    global game_still_going
    # check if any of the diagonals have same values
    diagonals_1 = board[0] == board[4] == board[8] != "-"
    diagonals_2 = board[6] == board[4] == board[2] != "-"

    # if diagonals are match
    if diagonals_1 or diagonals_2:
        game_still_going = False
    # return the winner Mr. X or Mr. O
    if diagonals_1:
        return board[0]
    elif diagonals_2:
        return board[6]
    return


def check_if_tie():
    global game_still_going
    if "-" not in board:
        game_still_going = False
    return


def flip_player():
    # global variable
    global current_player
    # if current player was X, change to O
    if current_player == "X":
        current_player = "O"
    # if current player was O, change to X
    elif current_player == "O":
        current_player = "X"
    return


play_game()

# Board
# display board
# handles a turn
# play game
# check win
# check rows
# check columns
# check diagonals
# check tie
# flip player
