from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c=Counter(nums)
        k=len(nums)//3
        ans=[]
        for i in c:
            if c[i]>k:
                ans.append(i)
        return ans
        
