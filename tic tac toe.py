row1 = [" ", " ", " "]
row2 = [" ", " ", " "]
row3 = [" ", " ", " "]
# this defines the initial state of the board
movecount = 0
# this counts the number of moves for a draw


def board():
    print(row1)
    print(row2)
    print(row3)
# this prints the board


def movex():
    print("Player X's turn to move.")
    column = int(input("Choose a column (1, 2, or 3): "))
    rowx = int(input("Choose a row (1, 2, or 3): "))
    columnx = column - 1
    if rowx == 1:
        row1[columnx] = "X"
    elif rowx == 2:
        row2[columnx] = "X"
    elif rowx == 3:
        row3[columnx] = "X"
# this defines the move of the player using X


def moveo():
    print("Player O's turn to move.")
    column = int(input("Choose a column (1, 2, or 3): "))
    rowo = int(input("Choose a row (1, 2, or 3): "))
    columno = column - 1
    if rowo == 1:
        row1[columno] = "O"
    elif rowo == 2:
        row2[columno] = "O"
    elif rowo == 3:
        row3[columno] = "O"
# this defines the move of the player using O


def end():
    if row1[0] == row1[1] == row1[2] and row1[0] != " ":
        if row1[0] == "X":
            print("Player X wins.")
            quit()
        elif row1[0] == "O":
            print("Player O wins.")
            quit()
    elif row2[0] == row2[1] == row2[2] and row2[0] != " ":
        if row2[0] == "X":
            print("Player X wins.")
            quit()
        elif row2[0] == "O":
            print("Player O wins.")
            quit()
    elif row3[0] == row3[1] == row3[2] and row3[0] != " ":
        if row3[0] == "X":
            print("Player X wins.")
            quit()
        elif row3[0] == "O":
            print("Player O wins.")
            quit()
    elif row1[0] == row2[0] == row3[0] and row1[0] != " ":
        if row1[0] == "X":
            print("Player X wins.")
            quit()
        elif row1[0] == "O":
            print("Player O wins.")
            quit()
    elif row1[1] == row2[1] == row3[1] and row1[1] != " ":
        if row1[1] == "X":
            print("Player X wins.")
            quit()
        elif row1[1] == "O":
            print("Player O wins.")
            quit()
    elif row1[2] == row2[2] == row3[2] and row1[2] != " ":
        if row1[2] == "X":
            print("Player X wins.")
            quit()
        elif row1[2] == "O":
            print("Player O wins.")
            quit()
    elif row1[0] == row2[1] == row3[2] and row1[0] != " ":
        if row1[0] == "X":
            print("Player X wins.")
            quit()
        elif row1[0] == "O":
            print("Player O wins.")
            quit()
    elif row1[2] == row2[1] == row3[0] and row1[2] != " ":
        if row1[2] == "X":
            print("Player X wins.")
            quit()
        elif row1[2] == "O":
            print("Player O wins.")
            quit()
    elif movecount == 9:
        print("The game is a draw.")
        quit()
    else:
        pass
# define the conditions for a win, draw, and to continue if none of those conditions are met


def game():
    global movecount
    board()
    end()
    movex()
    movecount += 1
    board()
    end()
    moveo()
    movecount += 1
# this is the sequence of code used for the game


while True:
    game()
# loops the game so that it continues until stopped by a quit process
