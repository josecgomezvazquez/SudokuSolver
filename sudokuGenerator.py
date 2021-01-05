
# Used for randomizing
from random import sample

# Sudoku Generator
"""
Begin the creation of the board
"""

base = 3            # Size of the base of a 3x3 square
side = base * base  # Size of the side of a sudoku board

# Pattern for a baseline solution
# r = rows
# c = columns
def pattern(r, c):
    return (base * (r % base) + r // base + c) % side

# Randomize rows and columns (of valid base return)
def shuffle(s):
    return sample(s, len(s))


rBase = range(base)     # Row base
rows = [g * base + r for g in shuffle(rBase) for r in shuffle(rBase)]
cols = [g * base + c for g in shuffle(rBase) for c in shuffle(rBase)]
nums = shuffle(range(1, base * base + 1))

# Produce sudoku board using randomized baseline pattern
board = [[nums[pattern(r, c)] for c in cols] for r in rows]

# Testing the first print looks good
for line in board:
    print(line)
    
print('\n') # Just to separate the randomzied boards

"""
End of creation of the baord
"""

"""
Begin the removal of random pieces of the board
"""
    
# Removing numbers to make things look like a sudoku puzzle
squares = side * side
empties = squares * 3 // 4
for p in sample(range(squares), empties):
    board[p // side][p % side] = 0

numSize = len(str(side))
for line in board: 
    print("["+"  ".join(f"{n or '.':{numSize}}" for n in line)+"]")

print('\n')

"""
End of the removal of random pieces of the board
"""

def printBoard(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")
        for j in range(len(board)):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
                
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")
                

def findEmpty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)  # row, col

    return None

def valid(bo, num, pos):
    # Check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False

    return True


def solveBoard(board):
    find = findEmpty(board)
    if not find:
        return True
    else:
        row, col = find
        
    for i in range(1, 10):
        if valid(board, i, (row, col)):
            board[row][col] = i
            
            if solveBoard(board):
                return True
            
            board[row][col] = 0
    return False
            

printBoard(board)
solveBoard(board)

print('\n\n')

printBoard(board)



























