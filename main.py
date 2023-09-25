# Tictactoe

print('Welcome to the Game')

# Blank Board
board = [['-'] * 3] + [['-'] * 3] + [['-'] * 3]
# Board row and column labels
columnIndices = [' A', 'B', 'C']
rowIndices = ['1', '2', '3']


# Function to display current board
def drawBoard():
    start = " "
    for column in columnIndices:
        if start == " ":
            print(start + " " + column, end="")
            start += "1"
        else:
            print(" " + column, end="")
    print()
    row_index = 1
    for row in board:
        row_print = ''.join(str(row).split(','))
        row_print1 = ''.join(str(row_print).split("'"))
        print(f'{row_index} {row_print1}')
        row_index += 1


# Function to ask player to make their row/column choices, and switch player turns
def makeChoice():
    global turn
    if turn % 2 == 0:
        player = 'X'
    else:
        player = 'O'
    print(f"Your turn {player}")
    selection_row_choices = [0, 1, 2]
    # Makes sure player inputs a valid input
    while True:
        try:
            selection_row = int(input('Make row selection: ')) - 1
            if selection_row in selection_row_choices:
                print('good row choice')
                break
            else:
                print("Enter a valid selection")
        except ValueError:
            print("Enter a valid selection")

    selection_column_choices = ['A', 'B', 'C']
    # Makes sure player inputs a valid input
    while True:
        selection_column = input('Make column selection: ').upper()
        if selection_column in selection_column_choices:
            print('good column choice')
            break
        else:
            print("Enter a valid column selection")
    if selection_column == 'A':
        selection_column = int(0)
    if selection_column == 'B':
        selection_column = int(1)
    if selection_column == 'C':
        selection_column = int(2)

    grid_selection = f"{selection_row}{selection_column}"
    print(grid_selection)

    if board[selection_row][selection_column] == 'O' or board[selection_row][selection_column] == 'X':
        print('Spot taken, select another spot')
    else:
        board[selection_row][selection_column] = player
        turn += 1

# Defining game ending conditions with functions
def diagonal_win():
    if board[0][0] == board[2][2] and board[1][1] == board[0][0] and board[1][1] != '-' \
            or board[0][2] == board[2][0] and board[1][1] == board[2][0] and board[1][1] != '-':
        print(f"Diagonal win! {board[1][1]} wins the game!")
        return True


def horizontal_win():
    for x in range(3):
        if board[x][0] == board[x][1] == board[x][2] and board[x][1] != '-':
            print(f"Horizontal win! {board[x][1]} wins the game!")
            return True


def vertical_win():
    for column in range(3):
        if board[0][column] == board[1][column] and board[1][column] == board[2][column] and board[0][column] != '-':
            print(f"Vertical win! {board[0][column]} wins the game!")
            return True


def draw():
    blank = '-'
    if blank not in board[0] and blank not in board[1] and blank not in board[2]:
        print("Game is draw")
        return True

# Function to prompt if player would like to play again and make a valid input
def rematch():
    while True:
        global game
        ask = input("Would you like to play again? Y/N : ")
        if ask.upper() == "Y":
            drawBoard()
            break
        elif ask.upper() == "N":
            game = False
            return game
        else:
            print("Enter either Y/N")


#Initializing the game
drawBoard()
turn = 0
game = True
while game:
    makeChoice()
    drawBoard()
    if diagonal_win():
        board = [['-'] * 3] + [['-'] * 3] + [['-'] * 3]
        rematch()
    if horizontal_win():
        board = [['-'] * 3] + [['-'] * 3] + [['-'] * 3]
        rematch()
    if vertical_win():
        board = [['-'] * 3] + [['-'] * 3] + [['-'] * 3]
        rematch()
    if draw():
        board = [['-'] * 3] + [['-'] * 3] + [['-'] * 3]
        rematch()
