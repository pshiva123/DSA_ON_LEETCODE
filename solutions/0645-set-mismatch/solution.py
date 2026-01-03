class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        s=set()
        rep=-1
        n=len(nums)
        for i in nums:
            if i in s:
                rep=i
                break
            s.add(i)
        s=set(nums)
        for i in range(1,n+1):
            if i not in s:
                return [rep,i]
        
        
        
        


        
