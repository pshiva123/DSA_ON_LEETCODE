class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ct=0
        ele=-1
        for i in range(len(nums)):
            if ct==0:
                ct=1
                ele=nums[i]
            elif nums[i]==ele:
                ct+=1
            else:
                ct-=1
        ans=0
        for i in nums:
            if i==ele:
                ans+=1
        if ans>len(nums)//2:
            return ele
        return -1
        
