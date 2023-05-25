import random

def random_board():
    #a sudoku board has to have very little squares filled, ergo I only have  a max of 4 that are filled
    board = [[0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],]
    num = random.randint(1,4)
    for i in range(num):
      x = random.randint(0,9)
      y = random.randint(0,9)
      board[x][y] = random.randint(1,9)
    return board


def print_board(board):
    for i in range(len(board)):
        if i%3 == 0 and i !=0:
            print("- - - - - - - - - - - - -")
        for j in range(len(board[i])):
            if j%3==0 and j !=0:
                print(" | ", end="")
            if j ==8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end ="")

def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)
    return None

def valid(board, num, pos):
    #check row
    for i in range(0,len(board)): #can be any number from 1-9, just chose 0
        if board[pos[0]][i]== num and pos[1] != i: #will ignore postion that was just inputted
            return False
    # check columns
    for i in range(0,len(board)):
        if board[i][pos[1]]== num and pos[0] != i: 
            return False
    
    #check sector
    sector_x = pos[1]//3
    sector_y =pos[0] //3

    for i in range(sector_y *3, sector_y *3 +3):
        for j in range (sector_x *3, sector_x *3 +3):
            if board[i][j] == num and (i,j) != pos:
                return False        
    return True

def solve(board):
    find = find_empty(board)
    if not find:
        return True
    else:
        row, col = find
    
    for i in range(1,10):
        if valid(board, i, (row,col)):
            board[row][col] =i
            #use recursion to solve the rest of the board
            if solve(board):
                return True
            board[row][col] =0
    return False



ask = (input("Would you like to play sudoku?[Y/N]")).upper()
while ask == "Y":
    board = random_board()
    print_board(board)
    print("---------------------")
    solved = (input("Would you like to see the solved board? [Y/N]")).upper()
    if solved == "Y":
        solve(board)
        print_board(board)
        ask = (input("Would you like to play sudoku?[Y/N]")).upper()
    else:
        asking = (input("Type 'done' when you are finished?")).upper()
        if asking == "DONE":
            solve(board)
            print_board(board)
        else:
            print("Was not in the instructions")
        ask = (input("Would you like to play sudoku?[Y/N]")).upper()
