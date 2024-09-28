class Solution:
    def ss(self,n):
        s=0
        while(n>0):
            s+=n%10
            n=n//10
        return s

    def minElement(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            s=self.ss(nums[i])
            nums[i]=s
        return min(nums)
        
