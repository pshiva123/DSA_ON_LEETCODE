class Solution:
    def countOppositeParity(self, nums: list[int]) -> list[int]:
        ans=[]
        n=len(nums)
        for i in range(n):
            c=0
            for j in range(i+1,n):
                if nums[i]%2!=nums[j]%2:
                    c+=1
            ans.append(c)
        return ans
                
        
