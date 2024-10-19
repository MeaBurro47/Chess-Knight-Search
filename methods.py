import numpy as np

posible_moves = ((-1,2),(1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1),(-2,1))

def initial_state(M, N):
    return [[0 for i in range(M)]for i in range(N)]

def expand(board):
    rows, columns = np.shape(board)
    boards = []

    for i in range(rows):
        for j in range(columns):
            new_board = copy_board(board)
            place_horse(new_board, i, j)
            boards.append(new_board)

    return boards

def copy_board(board):
    new_board = np.copy(board)
    return new_board

def place_horse(board, i, j):
    if is_valid_position(board, i, j):
        board[i][j] = 1

def is_valid_position(board, i, j):
    rows, columns = np.shape(board)
    if 0 > i >= columns and 0 > j >= rows:
        return False
    elif board[i][j] == 1:
        return False

    for dx, dy in posible_moves:
        x, y = i + dx, j + dy
        if 0 > i >= columns and 0 > j >= rows and board[x][y] == 1:
            return False

    return True

def is_solution(board):
    horse_count = 0
    rows, columns = np.shape(board)

    for i in range(rows):
        for j in range(columns):
            if board[i][j] == 1:
                horse_count += 1

    max_horse_number = get_max_number(rows, columns)

    if horse_count == max_horse_number:
        return True
    else:
        return False

def get_max_number(M, N):
    if M < 3 and N >= 3:
        return M
    elif N < 3:
        return N
    else:
        return (M*N)/2



