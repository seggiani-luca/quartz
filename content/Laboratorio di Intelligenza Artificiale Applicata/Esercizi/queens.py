# Implement the 8-queens problem solver using the backtracking approach

SIZE = 8
NUM  = 8

board = [[0 for _ in range(SIZE)] for _ in range(SIZE)] 
i = 0

def print_piece(piece):
    match piece:
        case 0:
            print(".", end="")
        case 1:
            print("Q", end="")
    print(" ", end="")

def print_board():
    for row in board:
        for piece in row:
            print_piece(piece)
        print()

def check(row, col):
    for r in range(1, row + 1):
        # straight north
        if board[row - r][col] == 1:
            return False

        # diagonal northwest
        if col - r >= 0 and board[row - r][col - r] == 1:
            return False
        
        # diagonal northeast 
        if col + r < SIZE and board[row - r][col + r] == 1:
            return False

    return True

def place(row):
    global i

    if row == SIZE:
        # increase solution count
        i += 1

        # print solution
        print(f"Found solution {i}")
        print_board()
        print()

        return

    for col in range(SIZE):
        # check if valid
        if not check(row, col):
            continue

        # place queen
        board[row][col] = 1

        # try next row 
        place(row + 1)
        
        # backtrack
        board[row][col] = 0 

    return

place(0)
