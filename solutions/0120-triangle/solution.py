class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n=len(triangle)
        for i in range(1,n):
            triangle[i][0]+=triangle[i-1][0]
            for j in range(1,len(triangle[i])):
                a=triangle[i-1][j-1]
                b=float('inf')
                if len(triangle[i-1])>j:
                    b=triangle[i-1][j]
                triangle[i][j]+=min(a,b)
        return min(triangle[-1])




        
