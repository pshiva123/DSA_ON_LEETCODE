class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        arr=[]
        for i in range(m):
            li=["#"]*n
            if i==0:
                li=["."]*n
            else:
                li[n-1]="."
            arr.append(''.join(li))
        
        return arr

        
