class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n=len(matrix)
        for i in range(n):
            for j in range(0,i+1):
                matrix[j][i],matrix[i][j]=matrix[i][j],matrix[j][i]
        for i in range(n):
            for j in range(math.ceil(n/2)):
                matrix[i][j],matrix[i][n-j-1]=matrix[i][n-j-1],matrix[i][j]



        
        
