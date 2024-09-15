class Solution:
    def maxScore(self, a: List[int], b: List[int]) -> int:
        n=len(b)
        d1,d2,d3,d4=[-float('inf')]*n,[-float('inf')]*n,[-float('inf')]*n,[-float('inf')]*n
        d1[0]=a[0]*b[0]
        for i in range(1,n):
            d1[i]=max(d1[i-1],a[0]*b[i])
        for i in range(1,n):
            if i==1:
                d2[i]=d1[i-1]+a[1]*b[i]
            else:
                d2[i]=max(d2[i-1],d1[i-1]+a[1]*b[i])
        for i in range(2,n):
            if i==2:
                d3[i]=d2[i-1]+a[2]*b[i]
            else:
                d3[i]=max(d3[i-1],d2[i-1]+a[2]*b[i])
        for i in range(3,n):
            if i==3:
                d4[i]=d3[i-1]+a[3]*b[i]
            else:
                d4[i]=max(d4[i-1],d3[i-1]+a[3]*b[i])
        return max(d4)



        
