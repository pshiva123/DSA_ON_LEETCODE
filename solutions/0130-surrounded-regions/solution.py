class Solution:
    def solve(self, board: List[List[str]]) -> None:
        n=len(board)
        m=len(board[0])
        vis=[[False]*m for _ in range(n)]
        for j in range(m):
            if board[0][j]=="O" and vis[0][j]==False:
                print("0",j)
                dfs(board,n,m,0,j,vis)
        for i in range(n):
            if board[i][0]=="O" and vis[i][0]==False:
                print(i,"0")
                dfs(board,n,m,i,0,vis)
        for j in range(m):
            if board[-1][j]=="O" and vis[-1][j]==False:
                print(n-1,j)
                dfs(board,n,m,n-1,j,vis)
        for i in range(n):
            if board[i][-1]=="O" and vis[i][-1]==False:
                print(i,m-1)
                dfs(board,n,m,i,m-1,vis)
        for i in range(n):
            for j in range(m):
                if board[i][j]=="O" and vis[i][j]==False:
                    board[i][j]="X"
        
        return board

        


def dfs(board,n,m,i,j,vis):
    vis[i][j]=True
    di=[(-1,0),(1,0),(0,1),(0,-1)]
    for d in di:
        nr,nc=d[0]+i,d[1]+j
        if 0<=nr<n and 0<=nc<m and vis[nr][nc]==False and board[nr][nc]=="O":
            dfs(board,n,m,nr,nc,vis)
        
            
        
