class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        c=0
        an=max(nums)
        res=1
        for num in nums:
            if num==an:
                c+=1
            else:
                c=0
            res=max(c,res)
        return res
        




        
