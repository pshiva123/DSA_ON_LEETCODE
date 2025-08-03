class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        pfound,qfound=False,False
        i,n=0,len(nums)
        while(i+1<n and nums[i]<nums[i+1]):
            i+=1
            pfound=True
        if i==n-1:
            return False
        while(i+1<n and nums[i]>nums[i+1]):
            i+=1
            qfound=True
        if i==n-1:
            return False
        while(i+1<n and nums[i]<nums[i+1]):
            i+=1
        return (i==n-1 and pfound and qfound)
            
        
