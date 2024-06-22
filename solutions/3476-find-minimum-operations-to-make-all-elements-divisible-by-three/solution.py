class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        c=0
        for i in nums:
            if(i%3==0):
                continue
            else:
                c+=1
        return c
                
        
