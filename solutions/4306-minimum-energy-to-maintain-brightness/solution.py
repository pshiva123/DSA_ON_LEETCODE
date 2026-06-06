import math
class Solution:
    def minEnergy(self, n: int, brightness: int, intervals: list[list[int]]) -> int:
        intervals.sort()
        merge=[]
        for start, end in intervals:
            if not merge or merge[-1][1]<start:
                merge.append([start,end])
            else:
                merge[-1][1]=max(merge[-1][1],end)
            
        ans=0
        for l,r in merge:
            ans+=(r-l+1)
        req=(brightness+2)//3
        return ans*req
            
        
