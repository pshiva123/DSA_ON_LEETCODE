class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        def f(nums,target,dp):
            if target==0:
                return 1
            if target<0:
                return 0
            if (target in dp):
                return dp[target]
            total=0
            for num in nums:
                total+=f(nums,target-num,dp)
            dp[target]=total
            return total
        return f(nums,target,{})
        
