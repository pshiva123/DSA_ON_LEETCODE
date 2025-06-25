class Solution:
    def numEnclaves(self,  board: List[List[int]]) -> int:
        n=len(board)
        m=len(board[0])
        cnt=0
        vis=[[False]*m for _ in range(n)]
        for j in range(m):
            if board[0][j]==1 and vis[0][j]==False:
                dfs(board,n,m,0,j,vis)
        for i in range(n):
            if board[i][0]==1 and vis[i][0]==False:
                dfs(board,n,m,i,0,vis)
        for j in range(m):
            if board[-1][j]==1 and vis[-1][j]==False:
                dfs(board,n,m,n-1,j,vis)
        for i in range(n):
            if board[i][-1]==1 and vis[i][-1]==False:
                dfs(board,n,m,i,m-1,vis)
        for i in range(n):
            for j in range(m):
                if board[i][j]==1 and vis[i][j]==False:
                    cnt+=1
        
        return cnt

        


def dfs(board,n,m,i,j,vis):
    vis[i][j]=True
    di=[(-1,0),(1,0),(0,1),(0,-1)]
    for d in di:
        nr,nc=d[0]+i,d[1]+j
        if 0<=nr<n and 0<=nc<m and vis[nr][nc]==False and board[nr][nc]==1:
            dfs(board,n,m,nr,nc,vis)

        
