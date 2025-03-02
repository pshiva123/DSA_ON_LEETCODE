class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board=[['.' for i in range(n)]for j in range(n)]
        ans=[]
        solve(board,0,n,ans)
        return ans


def solve(board,col,n,ans):
    if col==n:
        temp=[]
        for row in board:
            s=''.join(row)
            temp.append(s)
        ans.append(temp.copy())
        return
    for i in range(n):
        if isSafe(board,n,i,col):
            board[i][col]='Q'
            solve(board,col+1,n,ans)
            board[i][col]="."
def isSafe(board,n,row,col):
    i=row
    j=col
    while(i>=0 and j>=0):
        if board[i][j]=='Q':
            return False
        i-=1
        j-=1
    i=row
    j=col
    while(j>=0):
        if board[i][j]=='Q':
            return False
        j-=1
    i=row
    j=col
    while(i<n and j>=0):
        if board[i][j]=='Q':
            return False
        j-=1
        i+=1
    return True

    
        
