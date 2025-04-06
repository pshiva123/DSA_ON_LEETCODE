class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        c=0
        while True:
            mini=float('inf')
            idx=-1
            if list(sorted(nums))==nums:
                break
            for i in range(len(nums)-1):
                s=nums[i]+nums[i+1]
                if s<mini:
                    mini=s
                    idx=i
            nums=nums[:idx]+[mini]+nums[idx+2:]
            c+=1
        return c

        
