import heapq
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        n=len(heights)
        m=len(heights[0])
        heap=[]
        diff=[[float('inf')]*m for _ in range(n)]
        diff[0][0]=0
        heapq.heappush(heap,(0,0,0))
        di=[(-1,0),(1,0),(0,1),(0,-1)]
        while heap:
            difference,i,j=heapq.heappop(heap)
            if i==n-1 and j==m-1:
                break
            for d in di:
                nr,nc=d[0]+i,d[1]+j
                if 0<=nr<n and 0<=nc<m:
                    curdif=abs(heights[nr][nc]-heights[i][j])
                    newcost=max(difference,curdif)
                    if newcost<diff[nr][nc]:
                        diff[nr][nc]=newcost
                        heapq.heappush(heap,(newcost,nr,nc))
        
        return diff[-1][-1]




        
