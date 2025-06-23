class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n=len(nums)
        dp=[1]*n
        prev=[]
        nums.sort()
        for i in range(n):
            prev.append(i)
        for i in range(1,n):
            for j in range(i):
                if (nums[i]%nums[j]==0 or nums[j]%nums[i]==0) and dp[i]<dp[j]+1:
                    dp[i]=dp[j]+1
                    prev[i]=j
        ans=-1
        lastindex=-1
        for i in range(n):
            if dp[i]>ans:
                ans=dp[i]
                lastindex=i
        li=[nums[lastindex]]
        while(prev[lastindex]!=lastindex):
            lastindex=prev[lastindex]
            li.append(nums[lastindex])
        return li[::-1]

