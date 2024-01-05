n = 5
board = [[" " for _ in range(n)] for __ in range(n)]

player1_sign = "X"
player2_sign = "Y"

player1_1 = [0, 1]
player1_2 = [0, 2]
player1_3 = [0, 3]

player2_1 = [1, 0]
player2_2 = [2, 0]
player2_3 = [3, 0]


move1 = [True, True, True]
move2 = [True, True, True]

def initializeBoard():
    global board

    board[0][0] = "@"
    board[0][4] = "@"
    board[4][0] = "@"
    board[4][4] = "@"

    board[0][1] = player1_sign
    board[0][2] = player1_sign
    board[0][3] = player1_sign

    board[1][0] = player2_sign
    board[2][0] = player2_sign
    board[3][0] = player2_sign

def printBoard():
    print()
    for i in range(5):
        for j in range(5):
            if j != 4:
                print(" " + board[i][j], end=' | ')
            else:
                print(board[i][j], end='')
        print()
        if i != 4:
            print("----------------------")
    print()

def checkWinner():
    if player1_1[0] == n - 1 and player1_2[0] == n - 1 and player1_3[0] == n - 1:
        return 1
    elif player2_1[1] == n - 1 and player2_2[1] == n - 1 and player2_3[1] == n - 1:
        return 2
    else:
        return 0

def isValidMove(x, y, turn):
    if x <= 4 and y <= 4 and turn == 1:
        if board[x][y] == " ":
            return 1
        elif board[x][y] != " " and board[x + 1][y] == " ":
            return 0
        elif board[x][y] != " " and board[x + 1][y] != " ":
            return -1
        else:
            return -2
        
    elif x <= 4 and y <= 4 and turn == 2:
        if board[x][y] == " ":
            return 1
        elif board[x][y] !=  " " and board[x][y + 1] == " ":
            return 0
        elif board[x][y] != " " and board[x][y + 1] != " ":
            return -1
        else:
            return -2

def play(turn):
    global board, player1_1, player1_2, player1_3, player2_1, player2_2, player2_3

    if checkWinner() == 1:
        print("Player1 won!")
        exit()
    elif checkWinner() == 2:
        print("Player2 won!")
        exit()

    if turn == 1:
        print("Player X turn...")
        input_number = int(input("Please enter 1 or 2 or 3: "))
        while input_number != 1 and input_number != 2 and input_number != 3:
            print("Invalid move!")
            input_number = int(input("Please enter 1 or 2 or 3: "))

        if input_number == 1 and isValidMove(player1_1[0] + 1, player1_1[1], 1) == 1:
            board[player1_1[0]][player1_1[1]] = " "
            player1_1[0] += 1
            board[player1_1[0]][player1_1[1]] = player1_sign
        elif input_number == 2 and isValidMove(player1_2[0] + 1, player1_2[1], 1) == 1:
            board[player1_2[0]][player1_2[1]] = " "
            player1_2[0] += 1
            board[player1_2[0]][player1_2[1]] = player1_sign
        elif input_number == 3 and isValidMove(player1_3[0] + 1, player1_3[1], 1) == 1:
            board[player1_3[0]][player1_3[1]] = " "
            player1_3[0] += 1
            board[player1_3[0]][player1_3[1]] = player1_sign

        elif input_number == 1 and isValidMove(player1_1[0] + 1, player1_1[1], 1) == 0:
            board[player1_1[0]][player1_1[1]] = " "
            player1_1[0] += 2
            board[player1_1[0]][player1_1[1]] = player1_sign
        elif input_number == 2 and isValidMove(player1_2[0] + 1, player1_2[1], 1) == 0:
            board[player1_2[0]][player1_2[1]] = " "
            player1_2[0] += 2
            board[player1_2[0]][player1_2[1]] = player1_sign
        elif input_number == 3 and isValidMove(player1_3[0] + 1, player1_3[1], 1) == 0:
            board[player1_3[0]][player1_3[1]] = " "
            player1_3[0] += 2
            board[player1_3[0]][player1_3[1]] = player1_sign


        elif input_number == 1 and isValidMove(player1_1[0] + 1, player1_1[1], 1) == -1:
            play(1)
        elif input_number == 2 and isValidMove(player1_2[0] + 1, player1_2[1], 1) == -1:
            play(1)
        elif input_number == 3 and isValidMove(player1_3[0] + 1, player1_3[1], 1) == -1:
            play(1)

        else:
            print("Player X can not move!")
            play(2)
        
    else:
        print("Player Y turn...")
        input_number = int(input("Please enter 1 or 2 or 3: "))
        while input_number != 1 and input_number != 2 and input_number != 3:
            print("Invalid move!")
            input_number = int(input("Please enter 1 or 2 or 3: "))

        if input_number == 1 and isValidMove(player2_1[0], player2_1[1] + 1, 2) == 1:
            board[player2_1[0]][player2_1[1]] = " "
            player2_1[1] += 1
            board[player2_1[0]][player2_1[1]] = player2_sign
        elif input_number == 2 and isValidMove(player2_2[0], player2_2[1] + 1, 2) == 1:
            board[player2_2[0]][player2_2[1]] = " "
            player2_2[1] += 1
            board[player2_2[0]][player2_2[1]] = player2_sign
        elif input_number == 3 and isValidMove(player2_3[0], player2_3[1] + 1, 2) == 1:
            board[player2_3[0]][player2_3[1]] = " "
            player2_3[1] += 1
            board[player2_3[0]][player2_3[1]] = player2_sign
        
        elif input_number == 1 and isValidMove(player2_1[0], player2_1[1] + 1, 2) == 0:
            board[player2_1[0]][player2_1[1]] = " "
            player2_1[1] += 2
            board[player2_1[0]][player2_1[1]] = player2_sign
        elif input_number == 2 and isValidMove(player2_2[0], player2_2[1] + 1, 2) == 0:
            board[player2_2[0]][player2_2[1]] = " "
            player2_2[1] += 2
            board[player2_2[0]][player2_2[1]] = player2_sign
        elif input_number == 3 and isValidMove(player2_3[0], player2_3[1] + 1, 2) == 0:
            board[player2_3[0]][player2_3[1]] = " "
            player2_3[1] += 2
            board[player2_3[0]][player2_3[1]] = player2_sign


        elif input_number == 1 and isValidMove(player2_1[0], player2_1[1] + 1, 2) == -1:
            play(2)
        elif input_number == 2 and isValidMove(player2_2[0], player2_2[1] + 1, 2) == -1:
            play(2)
        elif input_number == 3 and isValidMove(player2_3[0], player2_3[1] + 1, 2) == -1:
            play(2)
        
        else:
            print("Player Y can not move!")
            play(1)
        

    printBoard()

print("Welcome to the game!")
initializeBoard()
printBoard()

while checkWinner() == 0:
    play(1)
    play(2)
