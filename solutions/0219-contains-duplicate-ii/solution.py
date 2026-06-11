class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n,d=len(nums),{}
        for i in range(n):
            if nums[i] in d:
                d[nums[i]].append(i)
            else:
                d[nums[i]]=[i,]
        for li in d:
            if len(d[li])>1:
                for i in range(1,len(d[li])):
                    if abs(d[li][i]-d[li][i-1])<=k:
                        return True
        return False        
