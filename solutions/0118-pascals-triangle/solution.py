class Solution:
    def generate(self, n: int) -> List[List[int]]:
        li=[[1]]
        for i in range(1,n):
            x=[1]
            for j in range(1,i+1):
                up=0 if j>i-1 else li[i-1][j]
                upleft=0 if j-1<0 else li[i-1][j-1]
                x.append(up+upleft)
            #x.append(1)
            li.append(x)
        return li


        
