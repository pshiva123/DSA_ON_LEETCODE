class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n=len(nums)
        s=nums[::-1]
        ans=[]
        for i in range(n-1,-1,-1):
            while s and s[-1]<=nums[i]:
                s.pop()
            if s:
                ans.append(s[-1])
            else:
                ans.append(-1)
            s.append(nums[i])
        return ans[::-1]

        
