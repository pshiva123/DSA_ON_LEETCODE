class Solution:
    def minOperations(self, nums: List[int]) -> int:
        c=0
        s=0
        k=len(nums)
        for i in range(k-2):
            if nums[i]==0:
                nums[i]=1
                nums[i+1]^=1
                nums[i+2]^=1
                c+=1
            s+=nums[i]
        s+=nums[-1]+nums[-2]
        return c if s==k else -1

        
