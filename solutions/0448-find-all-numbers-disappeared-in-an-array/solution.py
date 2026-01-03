class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ans=[]
        s=set(nums)
        n=len(nums)
        for i in range(1,n+1):
            if i not in s:
                ans.append(i)
        return ans
        
