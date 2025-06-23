class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n=len(nums)
        left=[-1]*n
        right=[-1]*n
        mini=nums[0]
        for i in range(1,n):
            if nums[i]<=mini:
                mini=nums[i]
            else:
                left[i]=1
        maxi=nums[-1]
        for i in range(n-2,-1,-1):
            if nums[i]>=maxi:
                maxi=nums[i]
            else:
                right[i]=1
        for i in range(n):
            if left[i]==1 and right[i]==1:
                return True
        print(left)
        print(right)
        return False


        
