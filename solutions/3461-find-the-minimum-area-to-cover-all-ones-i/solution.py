class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        firstrow=-1
        lastrow=-1
        for i in range(len(grid)):
            if 1 in grid[i]:
                firstrow=i
                break
        for i in range(len(grid)-1,-1,-1):
            if 1 in grid[i]:
                lastrow=i
                break
        min_col=len(grid[0])
        for i in grid:
            for j in range(len(i)):
                if i[j]==1:
                    if(j<min_col):
                        min_col=j
                        break
        max_col=-1
        for i in grid:
            for j in range(len(grid[0])-1,-1,-1):
                if(i[j]==1):
                    if(j>max_col):
                        max_col=j
                        break
        print(firstrow,lastrow,min_col,max_col)
        """"if(firstrow==min_col and lastrow==max_col):
            return 1
        elif(firstrow==lastrow):
            return max_col-min_col+1
        elif(min_col==max_col):
            return lastrow-firstrow+1"""
        
        k=max_col-min_col+1
        l=lastrow-firstrow+1
        return k*l
            
                
                
                
        
