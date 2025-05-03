class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n=len(matrix)
        m=len(matrix[0])
        for i in range(1,n):
            for j in range(m):
                left=float('inf') if j==0 else matrix[i-1][j-1]
                right=float('inf') if j==m-1 else matrix[i-1][j+1]
                up=matrix[i-1][j]
                matrix[i][j]+=min(left,right,up)

        return min(matrix[-1])
        
