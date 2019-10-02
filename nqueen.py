def issafe(n,i,j,board):
    for p in range(i):
        if board[j][p]==1:
            return False
    x=j
    y=i
    while x>=0 and y>=0:
        if board[x][y]==1:
            return False
        x-=1
        y-=1
    while x>=0 and y<n:
        if board[x][y]==1:
            return False
        x-=1
        y+=1
    return True

def solve(board,row,n):
    if row==n-1:
        for i in range(n):
            for j in range(n):
                if board[i][j]==1:
                    print("Q",end="")
                else:
                    print("_",end="")
            print()
    for i in range(n):
        if issafe(n,i,row,board):
            board[row][i]=1
            nex=solve(board,row+1,n)
            if nex:
                return True
            board[row][i]=0
    return False

n=int(input())
board=[[0]*n]*n
solve(board,0,n)

