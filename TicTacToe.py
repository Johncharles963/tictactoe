import random

gameActive = True
firstTurn = random.randint(1,2)
board = [' ']*10

def print_board():
    boardStr = f'\n   | {board[1]} | {board[2]} | {board[3]} |\n' \
               f'   | {board[4]} | {board[5]} | {board[6]} |\n' \
               f'   | {board[7]} | {board[8]} | {board[9]} |'
    print(boardStr)

def is_winner(bo, le):
    return (bo[1] == le and bo[2] == le and bo[3] == le) or\
        (bo[4] == le and bo[5] == le and bo[6] == le) or\
        (bo[7] == le and bo[8] == le and bo[9] == le) or\
        (bo[1] == le and bo[4] == le and bo[7] == le) or\
        (bo[2] == le and bo[5] == le and bo[8] == le) or\
        (bo[3] == le and bo[6] == le and bo[9] == le) or\
        (bo[1] == le and bo[5] == le and bo[9] == le) or\
        (bo[3] == le and bo[5] == le and bo[7] == le)

def is_board_full():
    if board.count(" ") > 1:
        return False
    else:
        return True

def get_user_input():
    cont = True
    while cont:
        try:
            userInput = int(input("Which space would you like to take (1-9): "))
            if userInput < 1 or userInput > 9:
                print("Please enter a vaild number! (1-9)")
            elif is_space_free(userInput):
                board[userInput] = "x"
                print_board()
                cont = False
            else:
                print("That space is taken!")
                print_board()
        except:
            print("Please enter a vaild number! (1-9)")
            print_board()

def get_comp_input():
    possibleMoves = []
    for i in range(1,10):
        if board[i] == " ":
            possibleMoves.append(i)
    compcheck = check_for_winning_move(possibleMoves, "o")
    playerCheck = check_for_winning_move(possibleMoves, "x")
    if compcheck != 0:
        board[compcheck] = "o"
    elif playerCheck != 0:
        board[playerCheck] = "o"
        preventWinningWords = random.choice(['Computer: "Nope"','Computer: "Blocked"', 'Computer: "Nice Try"','Computer: "Rejected"','Computer: "NOPE"', 'Computer: "Defense"','Computer: "Not Today"'])
        print(preventWinningWords)
    else:
        chosenMove = comp_choose_space(possibleMoves)
        board[chosenMove] = "o"


def check_for_winning_move(moves, le):
    for item in moves:
        newBoard = board.copy()
        newBoard[item] = le
        if is_winner(newBoard, le):
            return item
    return 0
def is_space_free(space):
    return board[space] == " "

def comp_choose_space(moves):
    newBoard = board.copy()
    if newBoard.count(" ") == 10:
        return random.choice([1,3,7,9,5])
    if newBoard[5] == " " and 5 in moves:
        return 5
    else:
        corners = list(filter(lambda x: x in [1, 3, 7, 9], moves))
        if len(corners) > 1 :
            return random.choice(corners)
    if board[1] != 'x' and board[2] != 'x' and board[3] != 'x':
        spaces = list(filter(lambda x: x in [1, 2, 3], moves))
        return random.choice(spaces)
    elif  board[4] != 'x' and board[5] != 'x' and board[6] != 'x':
        spaces = list(filter(lambda x: x in [4, 5, 6], moves))
        return random.choice(spaces)
    elif  board[7] != 'x' and board[8] != 'x' and board[9] != 'x':
        spaces = list(filter(lambda x: x in [7, 8, 9], moves))
        return random.choice(spaces)
    elif  board[1] != 'x' and board[4] != 'x' and board[7] != 'x':
        spaces = list(filter(lambda x: x in [1, 4, 7], moves))
        return random.choice(spaces)
    elif  board[2] != 'x' and board[5] != 'x' and board[8] != 'x':
        spaces = list(filter(lambda x: x in [2, 5, 8], moves))
        return random.choice(spaces)
    elif  board[3] != 'x' and board[6] != 'x' and board[9] != 'x':
        spaces = list(filter(lambda x: x in [3, 6, 9], moves))
        return random.choice(spaces)
    else:
        return random.choice(moves)

def board_full():
    whiteSpace = list(filter(lambda x: x == " ",board))
    if len(whiteSpace) == 1:
        return True
    else:
        return False
def check_if_game_over():
    if is_board_full():
        print("The game is Tied!")
        playAgain()
        return True
    if is_winner(board, "x"):
        print("You won!")
        playAgain()
        return True
    elif is_winner(board, "o"):
        print("You lost!")
        winningWords = random.choice(['Computer: "Get Wrecked"','Computer: "Beep Boop"','Computer: "Get Wrecked"' ])
        print(winningWords)
        print_board()
        playAgain()
        return True
    else:
        return False
def playAgain():
    cont = True
    global board
    global firstTurn
    while cont:
        answer = input('Do you want to keep playing?:')
        if answer.lower().startswith("y"):
            print("Lets Play again!")
            board = [" "] * 10
            firstTurn = random.randint(1,2)
            cont = False
        elif answer.lower().startswith("n"):
            print("GoodBye!")
            exit()

def play_game():
    print("Welcome to Tic-Tac-Toe!\n Select a board space to place your x! (1-9)")
    while(gameActive):
        if firstTurn == 1:
                print_board()
                get_user_input()
                if not check_if_game_over():
                    get_comp_input()
                    check_if_game_over()
        else:
                get_comp_input()
                print_board()
                if not check_if_game_over():
                    get_user_input()
                    check_if_game_over()

