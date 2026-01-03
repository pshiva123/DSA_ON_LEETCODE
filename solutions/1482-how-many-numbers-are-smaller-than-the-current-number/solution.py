class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans=[]
        n=len(nums)
        for i in range(n):
            cnt=0
            for j in range(n):
                if i!=j and nums[j]<nums[i]:
                    cnt+=1
            ans.append(cnt)
        return ans        
