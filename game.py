board = [
    ['-', '-', '-'],
    ['-', '-', '-'],
    ['-', '-', '-']
]

current_player = 'X'

game_over = False

while not game_over:
    print("  0",  '1', '2' )
    print("0" + " ".join(board[0]))
    print("1" + " ".join(board[1]))
    print("2" + " ".join(board[2]))

    print(f"Ход игрока {current_player}")
    row = int(input("Введите номер строки (0-2): "))
    col = int(input("Введите номер столбца (0-2): "))

    if board[row][col] == '-':
        board[row][col] = current_player
    else:
        print("Клетка занята, попробуйте снова")
        continue

    if (board[0][0] == current_player and board[0][1] == current_player and board[0][2] == current_player or
        board[1][0] == current_player and board[1][1] == current_player and board[1][2] == current_player or
        board[2][0] == current_player and board[2][1] == current_player and board[2][2] == current_player or
        board[0][0] == current_player and board[1][0] == current_player and board[2][0] == current_player or
        board[0][1] == current_player and board[1][1] == current_player and board[2][1] == current_player or
        board[0][2] == current_player and board[1][2] == current_player and board[2][2] == current_player or
        board[0][0] == current_player and board[1][1] == current_player and board[2][2] == current_player or
        board[0][2] == current_player and board[1][1] == current_player and board[2][0] == current_player):
        print(f"Игрок {current_player} победил!")
        game_over = True

    draw = True
    for row in board:
        if '-' in row:
            draw = False
            break

    if draw and not game_over:
        print("Ничья!")
        game_over = True

    if current_player == 'X':
        current_player = 'O'
    else:
        current_player = 'X'
