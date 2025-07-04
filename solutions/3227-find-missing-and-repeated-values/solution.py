class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n=len(grid)
        numsxor=0
        gridxor=0
        for row in grid:
            for i in row:
                gridxor=gridxor^i
        for i in range(1,n*n+1):
            numsxor=numsxor^i
        bitnumber=0
        gridx=-1
        numsx=-1
        for i in range(31,-1,-1):
            a=(numsxor>>i)&1
            b=(gridxor>>i)&1
            if a==b:
                bitnumber+=1
            else:
                gridx=b
                numsx=a
                break
        bitnumber=31-bitnumber
        zeros,ones=0,0
        for i in range(1,n*n+1):
            x=(i>>bitnumber)&1
            if x==1:
                ones=ones^i
            else:
                zeros=zeros^i
        for row in grid:
            for i in row:
                x=(i>>bitnumber)&1
                if x==1:
                    ones=ones^i
                else:
                    zeros=zeros^i
        cnt=0
        for row in grid:
            for i in row:
                if i==zeros:
                    cnt+=1
        if cnt==2:
            return [zeros,ones]
        return [ones,zeros]


        
