N = int(input('Board size: '))
# decraring and initializing the array with 0
# this array will have N square col
board = [[0]*N for x in range(N)]

# this function checks for the safe place
def is_attacked(row,col):

    # checking row & col
    for i in range(0,N):
        if board[row][i] == 1 or board[i][col] == 1:
            return True

    # checking digonal     
    for i in range(0,N):
        for j in range(0,N):
            if((row+col)==(i+j)) or ((row-col)==(i-j)):
                if board[i][j] == 1:
                    return True
    return False

# this function places the queen on board
def n_queen(n):

    if n==0:
        return True
    # these nested loops are to traverse through the board column by column
    here
    # (like:- 0,0 0,1 0,2 0,3) 
    for i in range(0,N):
        for j in range(0,N):

            # checking for safe column
            if (not is_attacked(i,j)) and (board[i][j]!=1):

                # if safe column found than Queen will be placed on column
                board[i][j] = 1
                if n_queen(n-1)==True:
                    return True
                board[i][j] = 0
    return False
 
 
if n_queen(N) == False:
    print("Not possible")
else:
    # prints the board when queens are placed
    for i in range(N):
            for j in range(N):
                print (board[i][j], end = " ") 
            print()
        