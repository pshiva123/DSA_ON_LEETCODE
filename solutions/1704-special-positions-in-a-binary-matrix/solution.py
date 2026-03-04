class Solution:
    def numSpecial(self, matrix: List[List[int]]) -> int:
        n=len(matrix[0])
        m=len(matrix)
        ans=0
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==1:
                    #move up
                    flag=True
                    for k in range(i-1,-1,-1):
                        if matrix[k][j]==1:
                            flag=False
                            break
                    
                    #move down
                    for k in range(i+1,m):
                        if matrix[k][j]==1:
                            flag=False
                            break
                 
                    #move left
                    for k in range(j-1,-1,-1):
                        if matrix[i][k]==1:
                            flag=False
                            break
                   
                    for k in range(j+1,n):
                        if matrix[i][k]==1:
                            flag=False
                            break
                    if flag is True:
                        #print(i,j)
                        ans+=1
                    
        return ans
                    

        
