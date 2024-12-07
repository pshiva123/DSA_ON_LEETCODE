class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        if min(nums)<k:
            return -1
        di={}
        for i in nums:
            if i in di:
                di[i]+=1
            else:
                di[i]=1
        c=0
        for i in di:
            if i>k:
                c+=1
        return c
            
        
        
