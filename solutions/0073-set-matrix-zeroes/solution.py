class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        clo=1
        m=len(matrix)
        n=len(matrix[0])
        for i in range(0,m):
            for j in range(0,n):
                if matrix[i][j]==0:
                    if j==0:
                        clo=0
                        matrix[i][0]=0
                    else:
                        matrix[0][j]=0
                        matrix[i][0]=0
        for i in range(m-1,0,-1):
            for j in range(n-1,0,-1):
                if matrix[i][0]==0 or matrix[0][j]==0:
                    matrix[i][j]=0
        for j in range(1,n):
            if matrix[0][0]==0:
                matrix[0][j]=0
        for i in range(m):
            if clo==0:
                matrix[i][0]=0


        
